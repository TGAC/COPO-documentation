.. _profile-setup-profile-type:

ProfileType
~~~~~~~~~~~~~~

ProfileType is an individual element or module that make up the profile. Each profile type is uniquely identified and
characterised by various fields that determine its behaviour and appearance.

.. seealso::

   * :ref:`Defining ProfileType Django model <django-model-definition>`
   * `Component structure <profile-setup-component>`_
   * `RecordActionButton structure <profile-setup-record-action-button>`_
   * `TitleButton structure <profile-setup-title-button>`_

.. raw:: html

   <hr>

ProfileType Database Table Structure
-------------------------------------

**ProfileType** represents the overarching category or classification of a profile. It defines the primary
characteristics and settings that apply to the profile as a whole. Understanding the structure and purpose of each
field helps in efficiently configuring and managing profile types in the application.

The PostgreSQL table **ProfileType** consists of the following fields:

* ``id`` (Integer):
      The unique identifier for the profile type. It is used as the primary key to uniquely identify
      each profile type within the table.

      **Example**: ``1``, ``2``, ``3``, etc.

* ``type`` (String):
      The name or designation of the profile type. It serves as a label to easily identify the
      profile type. It is often used as the abbreviation or short form of the profile type.

      **Example**: ``genomics``, ``dtol``, ``dtolenv``, ``asg``, ``erga``, ``test``, etc.

* ``description`` (String):
     A detailed description of the profile type.  It provides a comprehensive understanding of
     what the profile type represents and its scope.

     **Example**:

        * ``Genomics``: A profile that operates independently.

        * ``Darwin Tree of Life (DTOL)``: A profile related to the :abbr:`DToL (Darwin Tree of Life)` project.

        * ``Darwin Tree of Life Environmental Samples (DTOLENV)``: A profile for environmental samples within the
          :abbr:`DTOLENV (Darwin Tree of Life Environmental Samples)` project.

        * ``Aquatic Symbiosis Genomics (ASG)``: A profile related to the :abbr:`ASG (Aquatic Symbiosis Genomics)`
          project.

        * ``European Reference Genome Atlas (ERGA)``: A profile related to the
          :abbr:`ERGA (European Reference Genome Atlas)` project.

        * ``Test New Profile``: A profile for testing purposes.

* ``widget_colour`` (String):
      The colour associated with the profile type, used for UI elements. It enhances the visual
      distinction and user interface by providing a specific colour for each profile type.

      **Example**:

        * ``#009c95`` (cyan)
        * ``#16ab39`` (green)
        * ``#fb7d0d`` (orange)
        * ``#5829bb`` (purple)
        * ``#E61A8D`` (magenta)
        * violet

* ``is_dtol_profile`` (Boolean):
      Indicates whether the profile type is related to the
      :abbr:`DToL (Darwin Tree of Life)` project. It helps in categorising and filtering profiles that are part of the
      :abbr:`DToL (Darwin Tree of Life)` project.

      **Example**:

        * ``t`` (true): The profile is part of the :abbr:`DToL (Darwin Tree of Life)` project.
        * ``f`` (false): The profile is not part of the :abbr:`DToL (Darwin Tree of Life)` project.

* ``is_permission_required`` (Boolean):
      Indicates whether permissions are required to access this profile type. It
      ensures that sensitive or restricted profiles are only accessible by authorised users.

      **Example**:

        * ``t`` (true): Permissions are required to access the profile
        * ``f`` (false): No special permissions are required to access the profile

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: ProfileType database fields and records

   .. code-block:: bash

       id |   type   |                     description                     | widget_colour | is_dtol_profile | is_permission_required
      ----+----------+-----------------------------------------------------+---------------+-----------------+------------------------
        1 | genomics | Stand-alone                                         | #009c95       | f               | f
        2 | dtol     | Darwin Tree of Life (DTOL)                          | #16ab39       | t               | t
        3 | dtolenv  | Darwin Tree of Life Environmental Samples (DTOLENV) | #fb7d0d       | t               | t
        4 | asg      | Aquatic Symbiosis Genomics (ASG)                    | #5829bb       | t               | t
        5 | erga     | European Reference Genome Atlas (ERGA)              | #E61A8D       | t               | t
        6 | test     | Test New Profile                                    | violet        | f               | t

.. raw:: html

   <hr>

Usage of ProfileType
---------------------

Please check back soon for more information on how to use the profile type in the project.

.. raw:: html

   <hr>

.. _visual-representation-profile-type:

Visualisation of ProfileType in Project
----------------------------------------

.. figure:: /assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_without_dropdown_menu.png
   :alt: Work Profiles web page where desired profile type can be chosen to be created from the dropdown menu
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_without_dropdown_menu.png
   :class: with-shadow with-border

   **Work Profiles web page: Dropdown menu where desired profile type can be chosen to be created**

.. figure:: /assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_with_dropdown_menu.png
   :alt: Profile types shown as dropdown menu options on the Work Profiles web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_with_dropdown_menu.png
   :class: with-shadow with-border

   **Work Profiles web page: Dropdown menu options of profile types that can be created**

.. figure:: /assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_created_profiles.png
   :alt: A grid of created profiles on the Work Profiles web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/django_admin_interface/profile/profile_type/visual_display_profile_types_created_profiles.png
   :class: with-shadow with-border

   **Work Profiles web page: A grid of created profiles**

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

..
    Unicode declaration
..
.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6