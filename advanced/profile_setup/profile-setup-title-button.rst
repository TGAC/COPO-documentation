.. _profile-setup-title-button:

TitleButton
~~~~~~~~~~~~

Title buttons are individual elements or modules that make up the profile. These can include various
functionalities or data points that contribute to the profile's overall purpose.

.. seealso::

   * :ref:`Defining TitleButton Django model <django-model-definition>`
   * `Component structure <profile-setup-component>`_
   * `ProfileType structure <profile-setup-profile-type>`_
   * `RecordActionButton structure <profile-setup-record-action-button>`_

.. raw:: html

   <hr>

TitleButton Database Table Structure
-------------------------------------

The **TitleButton** model represents interactive buttons that allow users to perform specific actions related to
records within the profile. These actions can include creating, downloading or accessing other functionalities.

The PostgreSQL table **TitleButton** consists of the following fields:

* ``id`` (Integer):
     The primary key and unique identifier for each title button

* ``name`` (String):
      The internal name of the title button used to identify the title button. It is often used in the
      code to refer to the button

* ``template`` (String):
      The HTML template string used to render the button. It includes various HTML attributes such
      as style, title, :abbr:`CSS (Cascading Style Sheets)` classes and icon elements

* ``additional_attr`` (String):
     Any additional attributes required for the button. It is often used to store URLs or
     other necessary data for the button's functionality

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: TitleButton database fields

   .. code-block:: bash

       id |                name                |                                                                                                                        template                                                                                                                         |     additional_attr
      ----+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------
        1 | new_component_template             | <button title="Add new profile record"             class="big circular ui icon primary button new-component-template copo-tooltip">         <i class="icon add sign"></i>     </button>                                                                 |
        2 | quick_tour_template                | <button title="Quick tour"             class="big circular ui icon orange button takeatour quick-tour-template copo-tooltip">         <i class="icon lightbulb"></i>     </button>                                                                      |
        3 | new_samples_spreadsheet_template   | <button   title="Add Sample(s) from Spreadsheet"             class="big circular ui icon button new-samples-spreadsheet-template copo-tooltip">         <i class="icon table sign"></i>     </button>                                                   |
        4 | new_reads_spreadsheet_template     | <button style="display: inline" title="Add Read(s) from Read Spreadsheet"             class="big circular ui icon button new-reads-spreadsheet-template copo-tooltip">         <i class="icon table sign"></i>     </button>                            |
        5 | new_local_file                     | <button title="Add new file by browsing local file system"             class="big circular ui icon primary button new-local-file copo-tooltip">         <i class="icon desktop sign"></i>     </button>                                                 |
        6 | new_terminal_file                  | <button title="Add new file by terminal"             class="big circular ui icon primary button new-terminal-file copo-tooltip">         <i class="icon terminal sign"></i>     </button>                                                               |
        7 | new_taggedseq_spreadsheet_template | <button style="display: inline" title="Add Tagged Sequence (s) from Tagged Sequence Spreadsheet"             class="big circular ui icon button new-taggedseq-spreadsheet-template copo-tooltip">         <i class="icon table sign"></i>     </button> |
        8 | download_blank_manifest_template   | <a  title="Download Blank Manifest Template"             class="big circular ui icon brown button download-blank-manifest-template copo-tooltip" target="_blank">         <i class="icon download sign"></i>     </a>                                   | href:#blank_manifest_url
        9 | download_sop                       | <a title="Download Standard Operating Procedure (SOP)"         class="big circular ui icon yellow button download-sop copo-tooltip" target="_blank">         <i class="icon download sign"></i>     </a>                                                | href:#sop_url
       10 | accept_reject_samples              | <button style="display: none" title="Accept/Reject TOL Samples"             class="big circular ui icon teal button accept_reject_samples copo-tooltip">         <i class="icon tasks sign"></i>     </button>                                          |
       11 | tol_inspect                        | <button style="display: none" title="Inspect TOL"             class="big circular ui icon yellow button tol_inspect copo-tooltip">         <i class="icon clipboard list"></i>     </button>                                                            |
       12 | tol_inspect_gal                    | <button class="big circular ui icon green button tol_inspect_gal copo-tooltip" title="Inspect TOL by GAL">         <i class="icon building"></i>     </button>                                                                                          |
       13 | copo_accessions                    | <button style="display: none" title="View Accessions Dashboard"             class="big circular ui icon pink button copo_accessions copo-tooltip">         <i class="icon sitemap"></i>     </button>                                                   |

.. raw:: html

   <br><br>

.. collapse:: Description of each TitleButton record

   .. raw:: html

      <br>

   * **new_component_template**: Button to add a new profile record. It is styled with a primary colour and an icon of
     an add sign

   * **quick_tour_template**: Button to start a quick tour. It is styled with an orange colour and an icon of a
     lightbulb

   * **new_samples_spreadsheet_template**: Button to add samples from a spreadsheet template. It is styled with a teal
     colour and an icon of a table sign

   * **new_reads_spreadsheet_template**: Button to add reads from a spreadsheet template. It is styled with a teal
     colour and an icon of a table sign

   * **new_local_file**: Button to add a new file by browsing the local file system. It is styled with a primary colour
     and an icon of a desktop sign

     |section| :ref:`Section on Button Usage in the Project <files-submission-via-browser>`

   * **new_terminal_file**: Button to add a new file by terminal. It is styled with a primary colour and an icon of a
     terminal sign

     |section| :ref:`Section on Button Usage in the Project <files-submission-via-terminal>`

   * **new_taggedseq_spreadsheet_template**: Button to add tagged sequences from a spreadsheet template. It is styled
     with a teal colour and an icon of a table sign

     |section| :ref:`Section on Button Usage in the Project <accessing-accept-reject-samples-web-page>`

     |globe| `Associated web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__

   * **download_blank_manifest_template**: Button to download a blank manifest template. It is styled with a brown
     colour and an icon of a download sign

   * **download_sop**: Button to download the :abbr:SOP (Standard Operating Procedure). It is styled with a yellow
     colour and an icon of a download sign

   * **accept_reject_samples**: Button to accept or reject :abbr:`ToL (Tree of Life)` samples. It is styled with a teal
     colour and an icon of tasks

     |section| :ref:`Section on Button Usage in the Project <accessing-accept-reject-samples-web-page>`

     |globe| `Associated web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__

     |globe| `Django Admin UI <https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/title_button/title_button_accept_reject_samples_django_admin_ui.png>`__

   * **tol_inspect**: Button to inspect the :abbr:`ToL (Tree of Life)` samples. It is styled with a yellow colour and an
     icon of a clipboard list

     |section| :ref:`Section on Button Usage in the Project <tol-inspection>`

     |globe| `Associated web page <https://copo-project.org/copo/tol_dashboard/tol_inspect>`__

   * **tol_inspect_gal**: Button to inspect the :abbr:`ToL (Tree of Life)` by Genome Acquisition Lab (GAL). It is
     styled with a green colour and an icon of a building

     |section| :ref:`Section on Button Usage in the Project <tol-inspection-by-gal>`

     |globe| `Associated web page <https://copo-project.org/copo/tol_dashboard/tol_inspect/gal>`__

   * **copo_accessions**: Button to access the Accessions Dashboard. It is styled with a pink colour and an icon of a
     sitemap

.. raw:: html

   <hr>

Referencing Created TitleButton in Project
-------------------------------------------

.. note::

   * Ensure that a Django app is created to manage the ``TitleButton`` Django model and render the buttons in the
     template.

     Refer to the :ref:`profile-setup-component-creation` section which explains how to create a Django app for
     a component

   * Ensure that static files like :abbr:`CSS (Cascading Style Sheets)` and :abbr:`JS (JavaScript)` files are correctly
     configured in the Django project ``settings.py`` file

     .. code-block:: python

        # settings.py
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [BASE_DIR / 'static']

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. seealso::

   :ref:`project-application-structure` section which explains the structure of a Django project.

.. code-block:: python
   :caption: Define views that render the template containing the buttons in views.py

   # myapp/views.py
   from django.shortcuts import render
   from django.views import View
   from .models import TitleButton

   class TitleButtonView(View):
       def get(self, request):
           my_models = TitleButton.objects.all()
           return render(request, 'myapp/myapp.html', {'title_button_def': my_models})

.. code-block:: python
   :caption: Configure URL routing to the view defined above in the urls.py

   # myapp/urls.py
   from django.urls import path
   from .views import TitleButtonView

   urlpatterns = [
       path('title-buttons/', TitleButtonView.as_view(), name='title_buttons'),
   ]

.. raw:: html

   <hr>

* In the template HTML file (``myapp.html``), reference each element from the TitleButton table.

.. collapse:: TitleButton example template

   .. literalinclude:: /assets/files/setup/profile/title_button.html
      :language: html

.. raw:: html

   <hr>

* Handle any JavaScript functionality needed for the buttons in the :abbr:`JS (JavaScript)` file (``myapp.js``)

.. collapse:: Title button example javascript

   .. literalinclude:: /assets/files/setup/profile/title_button.js
      :language: javascript

.. raw:: html

   <hr>

.. _visual-representation-title-button:

Visualisation of TitleButton in Project
----------------------------------------

.. figure:: /assets/images/django_admin_interface/profile/title_button/visualisation_title_button_work_profiles_web_page.png
   :alt: Visual representation of 'new component' title button on 'Work Profiles' web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/title_button/visualisation_title_button_work_profiles_web_page.png
   :class: with-shadow with-border

   **Work Profiles web page: Visual representation of 'new component' title button**

* **new_component_template** button is labelled ``Add new profile record``. It is the |add-profile-button| button
  indicated by the blue arrow in the image above.

.. raw:: html

   <hr>

.. figure:: /assets/images/django_admin_interface/profile/title_button/visualisation_title_button_samples_web_page.png
   :alt: Visual representation of 'quick tour', 'new samples spreadsheet', 'download blank manifest ', 'download SOP' and 'accept/reject' title buttons on Samples web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/title_button/visualisation_title_button_samples_web_page.png
   :class: with-shadow with-border

   **Samples web page: Visual representation of 'quick tour', 'new samples spreadsheet', 'download blank manifest', 'download SOP' and 'accept/reject' title buttons**

* **quick_tour_template** button is labelled ``Quick tour``. It is the |quick-tour-button| button indicated by
  the orange arrow in the image above.

* **new_samples_spreadsheet_template** button is labelled ``Add Sample(s) from Spreadsheet``. It is the
  |add-dtol-manifest-button| button indicated by the green arrow.

  The colour of this button may differ based on the profile type. For example, it can be |add-asg-manifest-button| for
  :abbr:`ASG (Aquatic Symbiosis Genomics)` profile, |add-erga-manifest-button| for
  :abbr:`ERGA (European Reference Genome Atlas)` profile or |add-reads-manifest-button| for Genomics profile.

* **download_blank_manifest_template** button is labelled ``Download Blank Manifest Template``. It is the
  |blank-manifest-download-button| button indicated by the brown arrow.

* **download_sop**: button is labelled ``Download Standard Operating Procedure (SOP)``. It is the
  |sop-download-button| button indicated by the yellow arrow.

* **accept_reject_samples** button is labelled ``Accept/Reject TOL Samples``. It is the
  |accept-reject-samples-navigation-button| button indicated by the teal arrow.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-asg-manifest-button| image:: /assets/images/buttons/add_asg_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-dtol-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-erga-manifest-button| image:: /assets/images/buttons/add_erga_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-reads-manifest-button| image:: /assets/images/buttons/add_reads_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |blank-manifest-download-button| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 3ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |quick-tour-button| image:: /assets/images/buttons/quick_tour_button.png
   :height: 3ex
   :class: no-scaled-link

.. |sop-download-button| image:: /assets/images/buttons/download_button_sop.png
   :height: 3ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6