.. _profile-setup-record-action-button:

RecordActionButton
~~~~~~~~~~~~~~~~~~~~~

Record action buttons are individual elements or modules that make up the profile and managed through a Django Admin
model. Each button in the profile serves a specific function, enabling users to perform various actions on records
within the profile.

.. seealso::

   * :ref:`Defining RecordActionButton Django model <django-model-definition>`
   * `Component structure <profile-setup-component>`_
   * `ProfileType structure <profile-setup-profile-type>`_
   * `TitleButton structure <profile-setup-title-button>`_

.. raw:: html

   <hr>

RecordActionButton Database Table Structure
--------------------------------------------

The **RecordActionButton** in Django Admin provides a structured way to manage and perform actions on profile
records. Each button is meticulously defined with attributes that ensure it functions correctly and provides clear
feedback to users.

These actions can include creating, updating, submitting or deleting records among other functions. Understanding the
fields and their purposes can significantly enhance the management and usability of profiles in a Django application

The PostgreSQL table **RecordActionButton** consists of the following fields:

* ``id`` (Integer):
      The unique identifier for the action button. It is auto-incremented by the database.

* ``name`` (String):
      The internal name of the action button, used in the back-end code to reference the button.

* ``title`` (String):
      The display title of the action button, shown to users in the :abbr:`UI (User Interface)`. It
      describes the action the button performs in a concise manner.

* ``label`` (String):
      The short label shown on the button, providing a brief indication was the button does.

* ``type`` (String):
      The type of action the button performs, such as single (acting on a single record) or multi
      (acting on multiple records).

* ``error_message`` (String):
      The error message displayed to users if the action cannot be completed. This helps in
      providing feedback to users about why an action failed.

* ``icon_class`` (String):
      The :abbr:`CSS (Cascading Style Sheets)` class for the icon associated with the button,
      providing a visual representation of the button's action and help improve user interface design.

* ``action`` (String):
      The specific action performed by the button, often mapped to a function or a :abbr:`URL (Uniform
      Resource Locator)` ndpoint that the action will call.

* ``icon_colour`` (String):
      The colour of the icon used for :abbr:`UI (User Interface)` consistency and visual cues
      thereby helping users to quickly identify the type of action.

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: Example records for the ProfileActionButton model, detailing the various actions available within a
              profile

   .. code-block:: bash

      id |              name               |                   title                    |          label           |  type  |                                     error_message                                     |      icon_class       |          action          | icon_colour
     ----+---------------------------------+--------------------------------------------+--------------------------+--------+---------------------------------------------------------------------------------------+-----------------------+--------------------------+-------------
       1 | add_record_all                  | Add new record                             | Add                      |        |                                                                                       | fa fa-plus            | add                      | blue
       2 | edit_record_single              | Edit record                                | Edit                     | single | Please select a record to edit                                                        | fa fa-pencil-square-o | edit                     | green
       3 | delete_record_multi             | Delete records                             | Delete                   | multi  | Please select one or more records to delete                                           | fa fa-trash-can       | validate_and_delete      | red
       4 | submit_assembly_multi           | Submit Assembly                            | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info            | submit_assembly          |
       5 | submit_annotation_multi         | Submit Annotation                          | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info            | submit_annotation        | teal
       6 | submit_read_multi               | Submit Read                                | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info            | submit_read              | teal
       7 | add_local_all                   | Add new file by browsing local file system | Add                      |        | Add new file by browsing local file system                                            | fa fa-desktop         | add_files_locally        | blue
       8 | add_terminal_all                | Add new file by terminal                   | Add                      |        |                                                                                       | fa fa-terminal        | add_files_by_terminal    | blue
       9 | submit_tagged_seq_multi         | Submit Tagged Sequence                     | Submit                   | multi  | Please select one or more record to submit                                            | fa fa-info            | submit_tagged_seq        | teal
      10 | download_sample_manifest_single | Download Sample Manifest                   | Download sample manifest | single | Please select one of samples in the manifest to download                              | fa fa-download        | download-sample-manifest | blue
      11 | view_images_multiple            | View Images                                | View images              | multi  | Please select one or more sample records from the table shown to view images for      | fa fa-eye             | view-images              | teal
      12 | download_permits_multiple       | Download Permits                           | Download permits         | multi  | Please select one or more sample records from the table shown to download permits for | fa fa-download        | download-permits         | orange
      13 | releasestudy                    | Release Study                              | Release Study            | single |                                                                                       | fa fa-globe           | release_study            | blue

.. raw:: html

   <br><br>

.. collapse:: Description of some RecordActionButton records

   .. raw:: html

      <br>

  * **add_record_all**: *Add new record* button (ID: 1)

       Allows users to add a new record to the profile. It is labelled *Add* and uses a blue ``fa fa-plus`` icon.

  * **edit_record_single**: *Edit record* button (ID: 2)

       Enables users to edit an existing record. This button is labeled *Edit* and it uses a green
       ``fa fa-pencil-square-o`` icon. It shows an error message, *Please select a record to edit*, if no record is
       selected.

  * **delete_record_multi**: *Delete records* button (ID: 3)

       Allows users to delete multiple records at once. This multi-action button uses a red ``fa fa-trash-can`` icon
       and prompts users to *Please select one or more records to delete* if no records are selected.

  * **submit_assembly_multi**: Submit Assembly

       |section| :ref:`Section on Button Usage in the Project <assemblies-submission-section>`

  * **submit_annotation_multi**: Submit Sequence Annotation

       |section| :ref:`Section on Button Usage in the Project <sequence-annotations-submission-section>`

  * **submit_read_multi**: Submit Reads

       |section| :ref:`Section on Button Usage in the Project <reads-submission-section>`

  * **add_local_all**: Add new file by browsing local file system

       |section| :ref:`Section on Button Usage in the Project <files-submission-via-browser>`

  * **add_terminal_all**: Add new file by terminal

       |section| :ref:`Section on Button Usage in the Project <files-submission-via-terminal>`

  * **submit_tagged_seq_multi**: Submit Tagged Sequence

       |section| :ref:`Section on Button Usage in the Project <barcoding-manifest-submissions-section>`

  * **download_sample_manifest_single**: Download Sample Manifest

       |section| :ref:`Section on Button Usage in the Project <downloading-submitted-sample-manifest>`

  * **view_images_multiple**: View Images

       |section| :ref:`Section on Button Usage in the Project <images-submission-view-images>`

  * **download_permits_multiple**: Download Permits

       |section| :ref:`Section on Button Usage in the Project <permits-submission-download-permits>`

  * **releasestudy**: Release Study

       |section| :ref:`Section on Button Usage in the Project <releasing-profiles>`

.. raw:: html

   <hr>

Referencing Created RecordActionButton in Project
-------------------------------------------------

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

* In the ``views.py``, define the views to render the template containing the buttons

.. collapse:: RecordActionButton example views.py

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record_action_button_views.py
      :language: python

* In the template HTML file (``myapp.html``), reference each element from the RecordActionButton table.

.. collapse:: RecordActionButton example template

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record_action_button.html
      :language: html

.. raw:: html

   <hr>

* Handle any JavaScript functionality needed for the buttons in the :abbr:`JS (JavaScript)` file (``myapp.js``)

.. collapse:: RecordActionButton example javascript

   .. raw:: html

      <br>

   .. literalinclude:: /assets/files/setup/profile/record_action_button.js
      :language: javascript

.. raw:: html

   <hr>

.. _visual-representation-record-action-button:

Visualisation of RecordActionButton in Project
-------------------------------------------------

.. figure:: /assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_assembly_web_page.png
   :alt:  Visualisation of the add, edit, delete and submit record action buttons on the Assembly web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_assembly_web_page.png
   :class: with-shadow with-border

   **Assembly web page: Visualisation of the add, edit, delete record and submit action buttons**

* **add_record_all** button is labelled ``Add`` and uses a |add-icon| icon. It is indicated by the blue arrow.

* **edit_record_single** button is labelled ``Edit`` and uses |edit-icon| icon. It is indicated by the green arrow.

* **delete_record_multi** button is labelled ``Delete`` and uses a |delete-icon| icon. It is indicated by the red
  arrow. The icon and colour of this button is used on multiple web pages with different actions.

* **submit_assembly_multi** button is labelled ``Submit`` and uses a |info-icon| icon. The icon and colour used in
  for this button, is also used for the **submit_annotation_multi**, **submit_read_multi** and
  **submit_tagged_seq_multi** buttons.

  The difference is in the label assigned and the action performed by the button. The button is indicated by the teal
  arrow in the image above.


.. raw:: html

   <hr>

.. figure:: /assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_files_web_page.png
   :alt:  Visualisation of the 'download sample manifest' button, 'view images' button and 'download permits' buttons on the Samples web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_files_web_page.png
   :class: with-shadow with-border

   **Samples web page:  Visualisation of the download sample manifest action button, view images action button and download permits action button**

* **add_local_all** button is labelled ``Add new file by browsing local file system`` and uses a |computer-icon| icon.
  It is indicated by the blue arrow on the right in the image above.

* **add_terminal_all** button is labelled ``Add new file by terminal`` and uses a |terminal-icon| icon. It is indicated
  by the blue arrow on the left in the image above.

.. raw:: html

   <hr>

.. figure:: /assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_samples_web_page.png
   :alt:  Visualisation of the 'add file by browser' record action button and 'add file via terminal' record action button on the Samples web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_samples_web_page.png
   :class: with-shadow with-border

   **Samples web page: Visualisation of the add file via browser record action button and add file via terminal record action button**

* **download_sample_manifest_single** button is labelled ``Download Sample Manifest`` and uses a |download-icon1| icon.
  It is indicated by the blue arrow in the image above.

* **view_images_multiple** button is labelled ``View Images`` and uses a |eye-icon| icon. It is indicated by the teal
  arrow.

* **download_permits_multiple** button is labelled ``Download Permits`` and uses a |download-icon2| icon. It is indicated
  by the orange arrow.

.. raw:: html

   <hr>

.. figure:: /assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_work_profiles_web_page.png
   :alt:  Visualisation of the release study record action button on the Work Profiles web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/record_action_button/visualisation_record_action_button_work_profiles_web_page.png
   :class: with-shadow with-border
   :height: 300px

   **Work Profiles web page: Visualisation of the release study record action button on a profile**

* **releasestudy** button is labelled ``Release Study`` and uses a |globe-icon| icon. It is indicated by the blue
  arrow in the image above.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |add-icon| image:: /assets/images/buttons/add_icon.png
   :height: 2.5ex
   :class: no-scaled-link

.. |computer-icon| image:: /assets/images/buttons/computer_icon.png
   :height: 2ex
   :class: no-scaled-link

.. |download-icon1| image:: /assets/images/buttons/download_icon1.png
   :height: 2ex
   :class: no-scaled-link

.. |download-icon2| image:: /assets/images/buttons/download_icon2.png
   :height: 2ex
   :class: no-scaled-link

.. |edit-icon| image:: /assets/images/buttons/edit_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |eye-icon| image:: /assets/images/buttons/eye_icon.png
   :height: 2ex
   :class: no-scaled-link

.. |delete-icon| image:: /assets/images/buttons/delete_icon.png
   :height: 3ex
   :class: no-scaled-link

.. |globe-icon| image:: /assets/images/buttons/globe_icon.png
   :height: 3ex
   :width: 2.6ex
   :class: no-scaled-link

.. |info-icon| image:: /assets/images/buttons/info_icon2.png
   :height: 3ex
   :class: no-scaled-link

.. |terminal-icon| image:: /assets/images/buttons/terminal_icon.png
   :height: 2ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6