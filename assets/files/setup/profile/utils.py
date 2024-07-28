# Detailed code can be found on COPO GitHub repository
# in the directory: common/utils/html_tags_utils.py
from bson import ObjectId
from common.dal.copo_da import DAComponent, DataSchemas
from common.dal import utils as d_utils
from common.dal.mongo_util import get_collection_ref
from common.lookup import lookup
from common.lookup.resolver import RESOLVER
import time
import pandas as pd

Lookups = get_collection_ref("Lookups")


class COPOLookup:
    def __init__(self, **kwargs):
        self.param_dict = kwargs
        self.search_term = self.param_dict.get("search_term", str()).lower()
        self.accession = self.param_dict.get("accession", dict())
        self.data_source = self.param_dict.get("data_source", str())
        self.profile_id = self.param_dict.get("profile_id", str())
        self.referenced_field = self.param_dict.get("referenced_field", str())
        self.drop_downs_pth = RESOLVER['copo_drop_downs']

    def broker_component_search(self):
        dispatcher = {
            'agrovoclabels': self.get_lookup_type,
            'countrieslist': self.get_lookup_type,
            'mediatypelabels': self.get_lookup_type,
            'fundingbodies': self.get_lookup_type,
            'cg_dependency_lookup': self.cg_dependency_lookup,
            'isa_samples_lookup': self.get_isasamples,
            'sample_source_lookup': self.get_samplesource,
            'all_samples_lookup': self.get_allsamples,
            'run_lookup': self.get_runs,
            'study_lookup': self.get_studies,
            'experiment_lookup': self.get_experiments,
            'sample_lookup': self.get_samples
        }

        result = []
        message = 'error'

        if self.data_source in dispatcher:
            try:
                result = dispatcher[self.data_source]()
                message = 'success'
            except Exception as e:
                exception_message = "Error brokering component search. " + str(e)
                print(exception_message)
                lg.exception(e)
                raise

        return dict(result=result, message=message)

    def broker_data_source(self):
        """
        function resolves dropdown list given a data source handle
        :return:
        """
        pths_map = lookup.DROP_DOWNS_SOURCE

        data = pths_map.get(self.data_source, str())

        if isinstance(data, str) and data:  # it's only a path, resolve to get actual data
            data = helpers.json_to_pytype(data)

        return data

    def get_lookup_type(self):
        projection = dict(label=1, accession=1, description=1)
        filter_by = dict(type=self.data_source)

        records = list()

        if self.accession or self.search_term:
            if self.accession:
                bn = list()
                bn.append(self.accession) if isinstance(self.accession, str) else bn.extend(self.accession)
                filter_by["accession"] = {'$in': bn}
            elif self.search_term:
                filter_by["label"] = {'$regex': self.search_term, "$options": 'i'}

            records = cursor_to_list(Lookups.find(filter_by, projection))

            if not records and self.search_term:
                del filter_by["label"]
                records = cursor_to_list(Lookups.find(filter_by, projection))

        return records

    def get_samplesource(self):
        """
        lookup sources related to a sample
        :return:
        """
        import common.utils.html_tags_utils as htags
        from common.dal.sample_da import Source

        df = pd.DataFrame()

        if self.accession:
            if isinstance(self.accession, str):
                self.accession = self.accession.split(",")

            object_ids = [ObjectId(x) for x in self.accession if x.strip()]
            records = cursor_to_list(Source().get_collection_handle().find({"_id": {"$in": object_ids}}))

            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['desc'] = df['accession'].apply(lambda x: htags.generate_attributes(Source(), x))
                df['description'] = df['desc'].apply(lambda x: self.format_description(x))
                df['server-side'] = True  # ...to request callback to server for resolving item description
        elif self.search_term:
            projection = dict(name=1)
            filter_by = dict()
            filter_by["name"] = {'$regex': self.search_term, "$options": 'i'}

            sort_by = 'name'
            sort_direction = -1

            records = Source(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                 projection=projection,
                                                                                 sort_by=sort_by,
                                                                                 sort_direction=sort_direction)

            if not records:
                # try getting all records
                del filter_by["name"]
                records = Source(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                     projection=projection,
                                                                                     sort_by=sort_by,
                                                                                     sort_direction=sort_direction)

            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['description'] = ''
                df['server-side'] = True  # ...to request callback to server for resolving item description

        result = list()

        if not df.empty:
            df = df[['accession', 'label', 'description', 'server-side']]
            result = df.to_dict('records')

        return result

    def cg_dependency_lookup(self):
        """
        lookup for cgcore dependent components
        :return:
        """
        import html_tags_utils as htags
        from common.dal.copo_da import CGCore

        result = list()
        df = pd.DataFrame()
        dependent_record_label = 'copo_name'

        if self.accession:
            if isinstance(self.accession, str):
                self.accession = self.accession.split(",")

            object_ids = [ObjectId(x) for x in self.accession if x.strip()]
            records = cursor_to_list(CGCore().get_collection_handle().find({"_id": {"$in": object_ids}}))
            result = list()

            if records:
                for record in records:
                    referenced_field = record.get("dependency_id", str())
                    kwargs = dict()
                    kwargs["referenced_field"] = referenced_field
                    schema = CGCore().get_component_schema(**kwargs)

                    label = record.get(dependent_record_label, str())

                    # modify schema before generating description
                    schema = [x for x in schema if
                              'dependency' in x and x['dependency'] == referenced_field and x.get("show_in_table",
                                                                                                  True)]
                    resolved = htags.resolve_display_data(schema, record)
                    description = self.format_description(resolved)

                    item_dict = dict(accession=str(record["_id"]),
                                     label=label,
                                     description=description)
                    item_dict['server-side'] = True  # ...to request callback to server for resolving item description

                    result.append(item_dict)
        elif self.search_term:
            referenced_field = self.referenced_field
            filter_name = dependent_record_label
            projection = {filter_name: 1}
            filter_by = dict(dependency_id=referenced_field)
            filter_by[filter_name] = {'$regex': self.search_term, "$options": 'i'}

            sort_by = filter_name
            sort_direction = -1

            records = CGCore(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                 projection=projection,
                                                                                 sort_by=sort_by,
                                                                                 sort_direction=sort_direction)

            if not records:
                # try getting all records
                del filter_by[filter_name]
                records = CGCore(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                     projection=projection,
                                                                                     sort_by=sort_by,
                                                                                     sort_direction=sort_direction)
            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df[filter_name]
                df['description'] = ''
                df['server-side'] = True  # ...to request callback to server for resolving item description

        if not df.empty:
            df = df[['accession', 'label', 'description', 'server-side']]
            result = df.to_dict('records')

        return result

    def get_isasamples(self):
        """
        lookup for ISA-based (COPO standard) samples
        :return:
        """

        import html_tags_utils as htags
        from common.dal.sample_da import Sample

        df = pd.DataFrame()

        if self.accession:
            if isinstance(self.accession, str):
                self.accession = self.accession.split(",")

            object_ids = [ObjectId(x) for x in self.accession if x.strip()]
            records = cursor_to_list(Sample().get_collection_handle().find({"_id": {"$in": object_ids}}))

            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['desc'] = df['accession'].apply(lambda x: htags.generate_attributes("sample", x))
                df['description'] = df['desc'].apply(lambda x: self.format_description(x))
                df['server-side'] = True  # ...to request callback to server for resolving item description

        elif self.search_term:
            projection = dict(name=1)
            filter_by = dict(sample_type="isasample")
            filter_by["name"] = {'$regex': self.search_term, "$options": 'i'}

            sort_by = 'name'
            sort_direction = -1

            records = Sample(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                 projection=projection,
                                                                                 sort_by=sort_by,
                                                                                 sort_direction=sort_direction)
            if not records:
                # try getting all records
                del filter_by['name']
                records = Sample(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                     projection=projection,
                                                                                     sort_by=sort_by,
                                                                                     sort_direction=sort_direction)
            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['description'] = ''
                df['server-side'] = True  # ...to request callback to server for resolving item description

        result = list()

        if not df.empty:
            df = df[['accession', 'label', 'description', 'server-side']]
            result = df.to_dict('records')

        return result

    def get_allsamples(self):
        """
        lookup for all samples irrespective of sample type
        :return:
        """

        import html_tags_utils as htags
        from common.dal.sample_da import Sample

        df = pd.DataFrame()

        if self.accession:
            if isinstance(self.accession, str):
                self.accession = self.accession.split(",")

            object_ids = [ObjectId(x) for x in self.accession if x.strip()]
            records = cursor_to_list(Sample().get_collection_handle().find({"_id": {"$in": object_ids}}))

            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['desc'] = df['accession'].apply(lambda x: htags.generate_attributes("sample", x))
                df['description'] = df['desc'].apply(lambda x: self.format_description(x))
                df['server-side'] = True  # ...to request callback to server for resolving item description
        elif self.search_term:
            projection = dict(name=1)
            filter_by = dict()
            filter_by["name"] = {'$regex': self.search_term, "$options": 'i'}

            sort_by = 'name'
            sort_direction = -1

            records = Sample(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                 projection=projection,
                                                                                 sort_by=sort_by,
                                                                                 sort_direction=sort_direction)
            if not records:
                # try getting all records
                del filter_by['name']
                records = Sample(profile_id=self.profile_id).get_all_records_columns(filter_by=filter_by,
                                                                                     projection=projection,
                                                                                     sort_by=sort_by,
                                                                                     sort_direction=sort_direction)

            if records:
                df = pd.DataFrame(records)
                df['accession'] = df._id.astype(str)
                df['label'] = df['name']
                df['description'] = ''
                df['server-side'] = True  # ...to request callback to server for resolving item description

        result = list()

        if not df.empty:
            df = df[['accession', 'label', 'description', 'server-side']]
            result = df.to_dict('records')

        return result

    def format_description(self, desc):
        html = """<table style="width:100%">"""
        for col in desc['columns']:
            html += "<tr><td>{}</td>".format(col['title'])
            html += "<td>{}</td>".format(desc['data_set'][col['data']])
            html += "</tr>"
        html += "</table>"

        return html

    def get_runs(self):
        from common.dal.submission_da import Submission
        existing_sub = Submission().get_records_by_field("profile_id", self.profile_id)
        df = pd.DataFrame()

        existing_accessions = ""
        accession_set = []
        if existing_sub:
            existing_accessions = existing_sub[0].get("accessions", "")
        if existing_accessions:
            runs = existing_accessions.get("run", "")
            if runs:
                for run in runs:
                    if run.get("accession", ""):
                        accession_set.append(run.get("accession", ""))

        if accession_set:
            df = pd.DataFrame(accession_set)
            df['accession'] = accession_set
            df['label'] = accession_set
            df['description'] = ''
            df['server-side'] = False  # ...to request callback to server for resolving item description

        result = df.to_dict('records')
        return result

    def get_studies(self):
        from common.dal.submission_da import Submission
        existing_sub = Submission().get_records_by_field("profile_id", self.profile_id)
        df = pd.DataFrame()

        existing_accessions = ""
        accession_set = []
        study_accession = ""
        if existing_sub:
            existing_accessions = existing_sub[0].get("accessions", "")
        if existing_accessions:
            study = existing_accessions.get("project", "")
            if study:
                if isinstance(study, dict):
                    study_accession = study.get("accession", "")
                elif isinstance(study, list):
                    study_accession = study[0].get("accession", "")
        accession_set.append(study_accession)
        if accession_set:
            df = pd.DataFrame(accession_set)
            df['label'] = df["accession"]
            df['description'] = ''
            df['server-side'] = False  # ...to request callback to server for resolving item description

        result = df.to_dict('records')
        return result

    def get_experiments(self):
        from common.dal.submission_da import Submission
        existing_sub = Submission().get_records_by_field("profile_id", self.profile_id)
        df = pd.DataFrame()
        existing_accessions = ""
        accession_set = []
        if existing_sub:
            existing_accessions = existing_sub[0].get("accessions", "")
        if existing_accessions:
            experiments = existing_accessions.get("experiment", "")
            if experiments:
                for experiment in experiments:
                    if experiment.get("accession", ""):
                        accession_set.append(experiment.get("accession", ""))

        if accession_set:
            df = pd.DataFrame(accession_set)
            df['label'] = df["accession"]
            df['description'] = ''
            df['server-side'] = False  # ...to request callback to server for resolving item description

        result = df.to_dict('records')
        return result

    def get_samples(self):
        from common.dal.submission_da import Submission
        existing_sub = Submission().get_records_by_field("profile_id", self.profile_id)
        df = pd.DataFrame()

        existing_accessions = ""
        accession_set = []
        if existing_sub:
            samples = existing_accessions.get("sample", "")
            if samples:
                for sample in samples:
                    if sample.get("sample_accession", ""):
                        accession_set.append(sample.get("sample_accession", ""))

        if accession_set:
            df = pd.DataFrame(accession_set)
            df['label'] = df["accession"]
            df['description'] = ''
            df['server-side'] = False  # ...to request callback to server for resolving item description

        result = df.to_dict('records')
        return result


def get_resolver(data, elem):
    """
    function resolves data for UI display, by mapping control to a resolver function
    :param data:
    :param elem:
    :return:
    """
    if not data:
        return ""
    func_map = dict()
    func_map["copo-characteristics"] = resolve_copo_characteristics_data
    func_map["copo-environmental-characteristics"] = resolve_environmental_characteristics_data
    func_map["copo-phenotypic-characteristics"] = resolve_phenotypic_characteristics_data
    func_map["copo-comment"] = resolve_copo_comment_data
    func_map["copo-multi-select"] = resolve_copo_multi_select_data
    func_map["copo-multi-select2"] = resolve_copo_multi_select_data
    func_map["copo-general-ontoselect"] = resolve_copo_multi_select_data
    func_map["copo-single-select"] = resolve_copo_multi_select_data
    func_map["copo-multi-search"] = resolve_copo_multi_search_data
    func_map["copo-lookup"] = resolve_copo_lookup_data
    func_map["copo-lookup2"] = resolve_copo_lookup2_data
    func_map["select"] = resolve_select_data
    func_map["copo-button-list"] = resolve_select_data
    func_map["ontology term"] = resolve_ontology_term_data
    func_map["copo-select"] = resolve_copo_select_data
    func_map["datetime"] = resolve_datetime_data
    func_map["datafile-description"] = resolve_description_data
    func_map["date-picker"] = resolve_datepicker_data
    func_map["copo-duration"] = resolve_copo_duration_data
    func_map["copo-datafile-id"] = resolve_copo_datafile_id_data

    control = elem.get("control", "text").lower()
    if control in func_map:
        resolved_data = func_map[control](data, elem)
    else:
        resolved_data = resolve_default_data(data)

    return resolved_data


def get_control_options(f, profile_id=None):
    # option values are typically defined as a list,
    # or in some cases (e.g., 'copo-multi-search'),
    # as a dictionary. However, option values could also be resolved or generated dynamically
    # using callbacks. Callbacks, essentially, define functions that resolve options data

    option_values = list()

    if f.get("control", "text") in ["copo-lookup", "copo-lookup2"]:
        return COPOLookup(accession=f.get('data', str()),
                          data_source=f.get('data_source', str()), profile_id=profile_id).broker_component_search()[
            'result']

    if "option_values" not in f:  # you shouldn't be here
        return option_values

    # return existing option values
    if isinstance(f["option_values"], list) and f["option_values"]:
        return f["option_values"]

    # resolve option values from a data source
    if f.get("data_source", str()):
        return COPOLookup(data_source=f.get('data_source', str()), profile_id=profile_id).broker_data_source()

    if isinstance(f["option_values"], dict):
        if f.get("option_values", dict()).get("callback", dict()).get("function", str()):
            call_back_function = f.get("option_values", dict()).get(
                "callback", dict()).get("function", str())
            parameter = f.get("option_values", dict()).get(
                "callback", dict()).get("parameter", dict())
            provider = f.get("option_values", dict()).get(
                "callback", dict()).get("provider", str())
            if provider:
                obj = _get_class(provider)
                option_values = getattr(obj, call_back_function)(**parameter)
        else:
            # e.g., multi-search has this format
            option_values = f["option_values"]
    return option_values


def resolve_copo_characteristics_data(data, elem):
    schema = d_utils.get_copo_schema("material_attribute_value")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            a = dict()
            if f["id"].split(".")[-1] in data:
                a[f["id"].split(
                    ".")[-1]] = resolve_ontology_term_data(data[f["id"].split(".")[-1]], elem)
                resolved_data.append(a)

    return resolved_data


def resolve_environmental_characteristics_data(data, elem):
    schema = d_utils.get_copo_schema("environment_variables")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            a = dict()
            if f["id"].split(".")[-1] in data:
                a[f["id"].split(
                    ".")[-1]] = resolve_ontology_term_data(data[f["id"].split(".")[-1]], elem)
                resolved_data.append(a)

    return resolved_data  # turn this casting off after merge


def resolve_phenotypic_characteristics_data(data, elem):
    schema = d_utils.get_copo_schema("phenotypic_variables")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            a = dict()
            if f["id"].split(".")[-1] in data:
                a[f["id"].split(
                    ".")[-1]] = resolve_ontology_term_data(data[f["id"].split(".")[-1]], elem)
                resolved_data.append(a)

    return resolved_data  # turn this casting off after merge


def resolve_copo_comment_data(data, elem):
    schema = d_utils.get_copo_schema("comment")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            a = dict()
            if f["id"].split(".")[-1] in data:
                a[f["id"].split(".")[-1]] = data[f["id"].split(".")[-1]]
                resolved_data.append(a)

    if not resolved_data:
        resolved_data = str()
    elif len(resolved_data) == 1:
        resolved_data = resolved_data[0]
    return resolved_data


def resolve_copo_multi_select_data(data, elem):
    resolved_value = list()

    option_values = None

    if "option_values" in elem:
        option_values = get_control_options(elem)

    if data:
        if isinstance(data, str):
            data = data.split(",")

        data = [str(x) for x in data]

        if option_values:
            if isinstance(option_values[0], str):
                option_values = [dict(value=x, label=x) for x in option_values]

            o_df = pd.DataFrame(option_values)
            o_df.value = o_df.value.astype(str)
            resolved_value = list(o_df[o_df.value.isin(data)].label)

    return resolved_value


def resolve_copo_multi_search_data(data, elem):
    resolved_value = list()

    option_values = None

    if isinstance(data, list):
        data = ','.join(map(str, data))

    if "option_values" in elem:
        option_values = get_control_options(elem)

    if option_values and data:
        for d_v in data.split(","):
            resolved_value = resolved_value + [x[option_values["label_field"]] for x in option_values["options"] if
                                               d_v == x[option_values["value_field"]]]

    return resolved_value


def resolve_copo_lookup_data(data, elem):
    resolved_value = str()

    elem['data'] = data
    option_values = get_control_options(elem)

    if option_values:
        resolved_value = option_values[0]['label']

    return resolved_value


def resolve_copo_lookup2_data(data, elem):
    resolved_value = str()

    elem['data'] = data
    option_values = get_control_options(elem, profile_id=None)

    if option_values:
        resolved_value = [x[
                              'label'] + "<span class='copo-embedded' style='margin-left: 5px;' data-source='{"
                                         "data_source}' data-accession='{data_accession}' >"
                                         "<i title='click for related information' style='cursor: pointer;' class='fa "
                                         ""
                                         ""
                                         ""
                                         "fa-info-circle'></i></span>".format(
            data_source=elem['data_source'], data_accession=x['accession']) for x in option_values]

    return resolved_value


def resolve_select_data(data, elem):
    option_values = None
    resolved_value = str()

    if "option_values" in elem:
        option_values = get_control_options(elem)

    if option_values and data:
        for option in option_values:
            if isinstance(option, str):
                sv = option
                sl = option
            elif isinstance(option, dict):
                sv = option['value']
                sl = option['label']
            if str(sv) == str(data):
                resolved_value = sl

    return resolved_value


def resolve_ontology_term_data(data, elem):
    schema = DataSchemas("COPO").get_ui_template().get(
        "copo").get("ontology_annotation").get("fields")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            if f["id"].split(".")[-1] in data:
                resolved_data.append(data[f["id"].split(".")[-1]])

    if not resolved_data:
        resolved_data = str()
    elif len(resolved_data) == 1:
        resolved_data = resolved_data[0]
    return resolved_data


def resolve_copo_select_data(data, elem):
    return data


def resolve_datetime_data(data, elem):
    resolved_value = str()

    if data:
        if data.date:
            try:
                resolved_value = time.strftime(
                    '%a, %d %b %Y %H:%M', data.timetuple())
            except ValueError:
                pass
    return resolved_value


def resolve_datepicker_data(data, elem):
    resolved_value = str()
    if data:
        resolved_value = data
    return resolved_value


def resolve_copo_duration_data(data, elem):
    schema = d_utils.get_copo_schema("duration")

    resolved_data = list()

    for f in schema:
        if f.get("show_in_table", True):
            # a = dict()
            if f["id"].split(".")[-1] in data:
                # a[f["label"]] = data[f["id"].split(".")[-1]]
                resolved_data.append(
                    f["label"] + ": " + data[f["id"].split(".")[-1]])

    return resolved_data


def resolve_copo_datafile_id_data(data, elem):
    resolved_data = dict()

    da_object = DAComponent(component="datafile")

    if data:
        datafile = da_object.get_record(data)
        resolved_data["recordLabel"] = datafile.get("name", str())
        resolved_data["recordID"] = data

    return resolved_data
