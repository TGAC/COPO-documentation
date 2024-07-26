from django.core.management.base import BaseCommand
from .profile_type_model import ProfileType
from .component_model import Component
from.record_action_button_model import RecordActionButton
from .title_button_model import TitleButton

class Command(BaseCommand):
    help = "Add profile type definition to the database "

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        self.stdout.write("Removing Existing Profile Types ")
        ProfileType().remove_all_profile_types()
        self.stdout.write("Adding Profile Types")

        ProfileType().create_profile_type(type="erga", description="European Reference Genome Atlas (ERGA)",
                                          widget_colour="#E61A8D", is_dtol_profile=True, is_permission_required=True)
        ProfileType().create_profile_type(type="asg", description="Aquatic Symbiosis Genomics (ASG)",
                                          widget_colour="#5829bb", is_dtol_profile=True, is_permission_required=True)
        ProfileType().create_profile_type(type="dtolenv",
                                          description="Darwin Tree of Life Environmental Samples (DTOLENV)",
                                          widget_colour="#fb7d0d", is_dtol_profile=True, is_permission_required=True)
        ProfileType().create_profile_type(type="dtol", description="Darwin Tree of Life (DTOL)",
                                          widget_colour="#16ab39", is_dtol_profile=True, is_permission_required=True)
        ProfileType().create_profile_type(type="genomics", description="Stand-alone", widget_colour="#009c95",
                                          is_dtol_profile=False, is_permission_required=False)

        self.stdout.write("Profile Types Added")

        self.stdout.write("Removing Component ")
        Component().remove_all_components()
        self.stdout.write("Adding Component ")

        Component().create_component(name="assembly", title="Assembly", widget_icon="puzzle piece",
                                     widget_colour="violet", widget_icon_class="fa fa-puzzle-piece",
                                     table_id="assembly_table", reverse_url="copo_assembly_submission:copo_assembly",
                                     subtitle="")
        Component().create_component(name="taggedseq", title="Barcoding Manifests", widget_icon="barcode",
                                     widget_colour="red", widget_icon_class="fa fa-barcode",
                                     table_id="tagged_seq_table",
                                     reverse_url="copo_barcoding_submission:copo_taggedseq",
                                     subtitle="#component_subtitle")
        Component().create_component(name="files", title="Files", widget_icon="file", widget_colour="blue",
                                     widget_icon_class="fa fa-file", table_id="files_table",
                                     reverse_url="copo_file:copo_files", subtitle="")
        Component().create_component(name="seqannotation", title="Sequence Annotations", widget_icon="tag",
                                     widget_colour="yellow", widget_icon_class="fa fa-tag",
                                     table_id="seqannotation_table",
                                     reverse_url="copo_seq_annotation_submission:copo_seq_annotation", subtitle="")
        Component().create_component(name="read", title="Reads", widget_icon="dna", widget_colour="orange",
                                     widget_icon_class="fa fa-dna", table_id="read_table",
                                     reverse_url="copo_read_submission:copo_reads", subtitle="#component_subtitle")
        Component().create_component(name="sample", title="Samples", widget_icon="filter", widget_colour="olive",
                                     widget_icon_class="fa fa-filter", table_id="sample_table",
                                     reverse_url="copo_sample:copo_samples", subtitle="")
        Component().create_component(name="accessions", title="Accessions", widget_icon="sitemap", widget_colour="pink",
                                     widget_icon_class="fa fa-sitemap", table_id="accessions_table",
                                     reverse_url="copo_accession:copo_accessions", subtitle="")
        Component().create_component(name="profile", title="Work Profiles", widget_icon="", widget_colour="",
                                     widget_icon_class="", table_id="copo_profiles_table", reverse_url="",
                                     subtitle="#component_subtitle")

        self.stdout.write("Component Added")

        self.stdout.write("Removing Record Action Button ")
        RecordActionButton().remove_all_record_action_buttons()
        self.stdout.write("Adding Record Action Button ")

        RecordActionButton().create_record_action_button(name="add_terminal_all", title="Add new file by terminal",
                                                         label="Add", type="", error_message="",
                                                         icon_class="fa fa-terminal", action="add_files_by_terminal",
                                                         icon_colour="blue")
        RecordActionButton().create_record_action_button(name="download_sample_manifest_single",
                                                         title="Download Sample Manifest",
                                                         label="Download sample manifest", type="single",
                                                         error_message="Please select one of samples in the manifest to download",
                                                         icon_class="fa fa-download", action="download-sample-manifest",
                                                         icon_colour="blue")
        RecordActionButton().create_record_action_button(name="add_local_all",
                                                         title="Add new file by browsing local file system",
                                                         label="Add", type="",
                                                         error_message="Add new file by browsing local file system",
                                                         icon_class="fa fa-desktop", action="add_files_locally",
                                                         icon_colour="blue")
        RecordActionButton().create_record_action_button(name="edit_record_single", title="Edit record", label="Edit",
                                                         type="single", error_message="Please select a record to edit",
                                                         icon_class="fa fa-pencil-square-o", action="edit",
                                                         icon_colour="green")
        RecordActionButton().create_record_action_button(name="add_record_all", title="Add new record", label="Add",
                                                         type="", error_message="", icon_class="fa fa-plus",
                                                         action="add", icon_colour="blue")
        RecordActionButton().create_record_action_button(name="download_permits_multiple", title="Download Permits",
                                                         label="Download permits", type="multi",
                                                         error_message="Please select one or more sample records from the table shown to download permits for",
                                                         icon_class="fa fa-download", action="download-permits",
                                                         icon_colour="orange")
        RecordActionButton().create_record_action_button(name="view_images_multiple", title="View Images",
                                                         label="View images", type="multi",
                                                         error_message="Please select one or more sample records from the table shown to view images for",
                                                         icon_class="fa fa-eye", action="view-images",
                                                         icon_colour="teal")
        RecordActionButton().create_record_action_button(name="submit_tagged_seq_multi", title="Submit Tagged Sequence",
                                                         label="Submit", type="multi",
                                                         error_message="Please select one or more record to submit",
                                                         icon_class="fa fa-info", action="submit_tagged_seq",
                                                         icon_colour="teal")
        RecordActionButton().create_record_action_button(name="submit_read_multi", title="Submit Read", label="Submit",
                                                         type="multi",
                                                         error_message="Please select one or more record to submit",
                                                         icon_class="fa fa-info", action="submit_read",
                                                         icon_colour="teal")
        RecordActionButton().create_record_action_button(name="submit_annotation_multi", title="Submit Annotation",
                                                         label="Submit", type="multi",
                                                         error_message="Please select one or more record to submit",
                                                         icon_class="fa fa-info", action="submit_annotation",
                                                         icon_colour="teal")
        RecordActionButton().create_record_action_button(name="submit_assembly_multi", title="Submit Assembly",
                                                         label="Submit", type="multi",
                                                         error_message="Please select one or more record to submit",
                                                         icon_class="fa fa-info", action="submit_assembly",
                                                         icon_colour="")
        RecordActionButton().create_record_action_button(name="delete_record_multi", title="Delete records",
                                                         label="Delete", type="multi",
                                                         error_message="Please select one or more records to delete",
                                                         icon_class="fa fa-trash-can", action="validate_and_delete",
                                                         icon_colour="red")
        RecordActionButton().create_record_action_button(name="releasestudy", title="Release Study",
                                                         label="Release Study", type="single", error_message="",
                                                         icon_class="fa fa-globe", action="release_study",
                                                         icon_colour="blue")
        self.stdout.write("Record Action Button Added")

        self.stdout.write("Removing Title Button ")
        TitleButton().remove_all_title_buttons()
        self.stdout.write("Adding Title Button ")

        TitleButton().create_title_button(name="accept_reject_samples",
                                          template="<button style=\"display: none\" title=\"Accept/Reject TOL Samples\"             class=\"big circular ui icon teal button accept_reject_samples copo-tooltip\">         <i class=\"icon tasks sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="tol_inspect",
                                          template="<button style=\"display: none\" title=\"Inspect TOL\"             class=\"big circular ui icon yellow button tol_inspect copo-tooltip\">         <i class=\"icon clipboard list\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="tol_inspect_gal",
                                          template="<button class=\"big circular ui icon green button tol_inspect_gal copo-tooltip\" title=\"Inspect TOL by GAL\">         <i class=\"icon building\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="copo_accessions",
                                          template="<button style=\"display: none\" title=\"View Accessions Dashboard\"             class=\"big circular ui icon pink button copo_accessions copo-tooltip\">         <i class=\"icon sitemap\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_taggedseq_spreadsheet_template",
                                          template="<button style=\"display: inline\" title=\"Add Tagged Sequence (s) from Tagged Sequence Spreadsheet\"             class=\"big circular ui icon button new-taggedseq-spreadsheet-template copo-tooltip\">         <i class=\"icon table sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_terminal_file",
                                          template="<button title=\"Add new file by terminal\"             class=\"big circular ui icon primary button new-terminal-file copo-tooltip\">         <i class=\"icon terminal sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_local_file",
                                          template="<button title=\"Add new file by browsing local file system\"             class=\"big circular ui icon primary button new-local-file copo-tooltip\">         <i class=\"icon desktop sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_reads_spreadsheet_template",
                                          template="<button style=\"display: inline\" title=\"Add Read(s) from Read Spreadsheet\"             class=\"big circular ui icon button new-reads-spreadsheet-template copo-tooltip\">         <i class=\"icon table sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_samples_spreadsheet_template",
                                          template="<button   title=\"Add Sample(s) from Spreadsheet\"             class=\"big circular ui icon button new-samples-spreadsheet-template copo-tooltip\">         <i class=\"icon table sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="quick_tour_template",
                                          template="<button title=\"Quick tour\"             class=\"big circular ui icon orange button takeatour quick-tour-template copo-tooltip\">         <i class=\"icon lightbulb\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="new_component_template",
                                          template="<button title=\"Add new profile record\"             class=\"big circular ui icon primary button new-component-template copo-tooltip\">         <i class=\"icon add sign\"></i>     </button>",
                                          additional_attr="")
        TitleButton().create_title_button(name="download_sop",
                                          template="<a title=\"Download Standard Operating Procedure (SOP)\"         class=\"big circular ui icon yellow button download-sop copo-tooltip\" target=\"_blank\">         <i class=\"icon download sign\"></i>     </a>",
                                          additional_attr="href:#sop_url")
        TitleButton().create_title_button(name="download_blank_manifest_template",
                                          template="<a  title=\"Download Blank Manifest Template\"             class=\"big circular ui icon brown button download-blank-manifest-template copo-tooltip\" target=\"_blank\">         <i class=\"icon download sign\"></i>     </a>",
                                          additional_attr="href:#blank_manifest_url")

        self.stdout.write("Title Button Added")

        self.stdout.write("Setup Completed")