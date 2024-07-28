# myapp/views.py
from django.shortcuts import render
from django.views import View
from .models import TitleButton
import pandas as pd
from .utils import get_resolver

class TitleButtonView(View):
    def get(self, request):
        my_models = TitleButton.objects.all()
        return render(request, 'myapp/index.html', {'title_button_def': my_models})
class BrokerVisuals:
    def __init__(self, **kwargs):
        self.param_dict = kwargs
        self.component = self.param_dict.get("component", str())
        self.profile_id = self.param_dict.get("profile_id", str())
        self.user_id = self.param_dict.get("user_id", str())
        self.context = self.param_dict.get("context", dict())
        self.request_dict = self.param_dict.get("request_dict", dict())
        self.da_object = self.param_dict.get("da_object", DAComponent(self.profile_id, self.component))

    def do_server_side_table_data(self):
        self.context["component"] = self.component
        request_dict = self.param_dict.get("request_dict", dict())

        data = generate_server_side_table_records(self.profile_id, component=self.component, request=request_dict)
        self.context["draw"] = data["draw"]
        self.context["records_total"] = data["records_total"]
        self.context["records_filtered"] = data["records_filtered"]
        self.context["data_set"] = data["data_set"]

        return self.context

class DAComponent:
    def __init__(self, profile_id=None, component=str()):
        self.profile_id = profile_id
        self.component = component
def visualize(request):
    context = dict()

    task = request.POST.get("task", str())
    profile_id = request.session.get("profile_id", str())

    component = request.POST.get("component", str())
    da_object = DAComponent(profile_id=profile_id, component=request.POST.get("component", str()))

    if component in da_dict:
        da_object = da_dict[component](profile_id=profile_id)

    target_id = request.POST.get("target_id", None)

    if component == "read" and target_id:
        target_id = target_id.split("_")[0]

    broker_visuals = BrokerVisuals(context=context,
                                   profile_id=profile_id,
                                   request=request,
                                   user_id=request.user.id,
                                   component=request.POST.get("component", str()),
                                   target_id=target_id,
                                   da_object=da_object)

    task_dict = dict(server_side_table_data=broker_visuals.do_server_side_table_data)

    if task in task_dict:
        context = task_dict[task]()

    out = jsonpickle.encode(context, unpicklable=False)
    return HttpResponse(out, content_type='application/json')

def get_not_deleted_flag():
    """
    provides a consistent way of setting records as not deleted
    :return:
    """
    return "0"

def resolve_control_output_apply(data, args):
    if args.get("type", str()) == "array":  # resolve array data types
        resolved_value = list()
        for d in data:
            resolved_value.append(get_resolver(d, args))
    else:  # non-array types
        resolved_value = get_resolver(data, args)

    return resolved_value

def generate_server_side_table_records(profile_id=str(), da_object=None, request=dict()):
    # function generates component records for building an UI table using server-side processing
    # - please note that for effective data display,
    # all array and object-type fields (e.g., characteristics) are deferred to sub-table display.
    # please define such in the schema as "show_in_table": false and "show_as_attribute": true

    data_set = list()

    # assumes 10 records per page if length not set
    n_size = int(request.get("length", 10))
    draw = int(request.get("draw", 1))
    start = int(request.get("start", 0))

    return_dict = dict()

    records_total = da_object.get_collection_handle().count_documents(
        {'profile_id': profile_id, 'deleted': get_not_deleted_flag()})

    # retrieve and process records
    filter_by = dict()

    # get and filter schema elements based on displayable columns
    schema = [x for x in da_object.get_schema().get(
        "schema_dict") if x.get("show_in_table", True)]

    # build db column projection
    projection = [(x["id"].split(".")[-1], 1) for x in schema]

    # order by
    sort_by = request.get('order[0][column]', '0')
    sort_by = request.get('columns[' + sort_by + '][data]', '')
    sort_direction = request.get('order[0][dir]', 'asc')

    sort_by = '_id' if not sort_by else sort_by
    sort_direction = 1 if sort_direction == 'asc' else -1

    # search
    search_term = request.get('search[value]', '').strip()

    records = da_object.get_all_records_columns_server(sort_by=sort_by,
                                                       sort_direction=sort_direction,
                                                       search_term=search_term,
                                                       projection=dict(projection),
                                                       limit=n_size,
                                                       skip=start,
                                                       filter_by=filter_by)
    records_filtered = records_total

    if search_term:
        records_filtered = da_object.get_collection_handle().count_documents(
            {'profile_id': profile_id, 'deleted': get_not_deleted_flag(),
             'name': {'$regex': search_term, "$options": 'i'}})

    if records:
        df = pd.DataFrame(records)

        df['record_id'] = df._id.astype(str)
        df["DT_RowId"] = df.record_id
        df.DT_RowId = 'row_' + df.DT_RowId
        df = df.drop('_id', axis='columns')

        for x in schema:
            x["id"] = x["id"].split(".")[-1]
            df[x["id"]] = df[x["id"]].apply(
                resolve_control_output_apply, args=(x,)).astype(str)

        data_set = df.to_dict('records')

    return_dict["records_total"] = records_total
    return_dict["records_filtered"] = records_filtered
    return_dict["data_set"] = data_set
    return_dict["draw"] = draw

    return return_dict