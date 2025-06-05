.. _profile-management-on-django-admin-interface:

=====================================
Managing Profiles with Django Admin
=====================================

  .. hint::

   Click the |collapsible-item-arrow| button below to view the contents

The Django Admin interface provides a robust and user-friendly way to manage the **ProfileType**,
**Component**, **RecordActionButton** and **TitleButton** models which are used to define and manage profiles in COPO.

See the :ref:`profile-setup-index` section for more information on setting up profiles before proceeding with this
section.

By navigating to http://copo-project.org/admin and logging in with your superuser credentials, you can easily view,
add, edit and delete the models that you have created with the management commands in the section,
:ref:`creating-setup-profile-python-command`.

Utilising the search, filter, and custom actions features enhances the efficiency of managing your data. By customising
the admin interface, you can tailor it to your specific needs, making it an invaluable tool for Django development
and administration.

.. raw:: html

      <hr>

.. figure:: /assets/images/django_admin_interface/profile/django_admin_pointer_to_registered_models.png
   :alt: Registered Models on Django Admin Interface
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/django_admin_pointer_to_registered_models.png
   :class: with-shadow with-border

   **Django Admin Interface: Viewing Profile type, Components, Record action button and Title button registered models**

.. raw:: html

      <br>

Viewing data
------------------

   Click the **Profile types**, **Components**, **Record action buttons** or the **Title buttons** link in the admin
   dashboard shown in the image above. This will take you to a list view of the respective model.

   .. collapse:: Profile types list view

      .. raw:: html

         <br>

      .. figure:: /assets/images/django_admin_interface/profile/profile_type/profile_django_admin_ui_pointer_to_list_view_of_profile_types.png
         :alt: List view of Profile types on Django Admin Interface
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/profile_type/profile_django_admin_ui_pointer_to_list_view_of_profile_types.png
         :class: with-shadow with-border

   .. raw:: html

      <br>

   .. collapse:: Component list view

      .. raw:: html

         <br>

      .. figure:: /assets/images/django_admin_interface/profile/component/profile_django_admin_ui_pointer_to_list_view_of_components.png
         :alt: List view of Components on Django Admin Interface
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/component/profile_django_admin_ui_pointer_to_list_view_of_components.png
         :class: with-shadow with-border

   .. raw:: html

      <br>

   .. collapse:: Record action buttons list view

      .. raw:: html

         <br>

      .. figure:: /assets/images/django_admin_interface/profile/record_action_button/profile_django_admin_ui_pointer_to_list_view_of_record_action_buttons.png
         :alt: List view of Record action buttons on Django Admin Interface
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/record_action_button/profile_django_admin_ui_pointer_to_list_view_of_record_action_buttons.png
         :class: with-shadow with-border

   .. raw:: html

      <br>

   .. collapse:: Title buttons list view

      .. raw:: html

         <br>

      .. figure:: /assets/images/django_admin_interface/profile/title_button/profile_django_admin_ui_pointer_to_list_view_of_title_buttons.png
         :alt: List view of Title buttons on Django Admin Interface
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/title_button/profile_django_admin_ui_pointer_to_list_view_of_title_buttons.png
         :class: with-shadow with-border

.. raw:: html

      <hr>

Adding data
-----------------

* Click the ``Add`` button in the top right corner of the respective model
* Fill out the form fields as defined in the respective model.
* Click the ``Save`` button to create the new data.

.. raw:: html

      <hr>

Editing data
------------------

* In the list view, click on the name of the item that you would like to edit.
* Modify the fields as needed.
* Click the ``Save`` button to update the data

.. raw:: html

      <hr>

Deleting data
------------------

* In the list view, select the checkbox next to the item(s) that you would like to delete.
* Select ``Delete selected item`` from the action dropdown menu and click ``Go``.
* Confirm the deletion in the next screen.

.. raw:: html

   <hr>

Using the Search and Filters
-------------------------------

**Search**
   Use the search box at the top of the list view to search for profiles by name or email.
   This is useful for quickly finding specific profiles.

**Filters**
   Use the filters on the right side of the list view to filter profiles by specific criteria such as
   birth_date.

   This helps in narrowing down the list to profiles matching certain conditions.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link