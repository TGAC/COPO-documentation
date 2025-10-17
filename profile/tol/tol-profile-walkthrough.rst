.. _tol-profile-walkthrough:

=======================
Tree of Life Profile
=======================

In COPO, a Tree of Life (ToL) [#f1]_ work profile [#f2]_  is required to submit research objects [#f3]_ such as
samples, barcoding manifests, sequence annotations, reads, assemblies and files.

A :abbr:`ToL (Tree of Life)` profile can be used to create one of the following biodiversity projects:

* Aquatic Symbiosis Genomics (ASG)
* Darwin Tree of Life (DTOL)
* Darwin Tree of Life Environmental (DTOL_ENV)
* European Reference Genome Atlas (ERGA)

.. raw:: html

   <br>

.. seealso::

  * :ref:`How to Update Profiles <profile-update>`
  * :ref:`How to Delete Profiles <profile_deletion>`
  * :ref:`How to Make Profiles (also known as Projects) Public <releasing-profiles>`
  * :ref:`Sharing Profiles <sharing-profiles>`
  * :ref:`Releasing Profiles (Studies) <releasing-profiles>`
  * :ref:`Sorting Profiles <sorting-profiles>`
  * :ref:`Profile Types Legend <profile-types-legend>`

.. raw:: html

   <hr>

.. _tol-profile-steps:

Steps to Create a Tree of Life Profile
---------------------------------------

1. Choose Profile Type
~~~~~~~~~~~~~~~~~~~~~~

.. _tol-profile-steps-choose-profile-type-important-note:

.. important::

   The profile type dropdown menu is displayed beside the **Work Profiles** page title. By default, it will only
   display the **Genomics** profile option.

   If your desired profile type is not displayed in the dropdown menu, please
   :email:`contact the COPO team <ei.copo@earlham.ac.uk>` indicating the type of profile group that you would
   like to be granted access to. Thereafter, the desired profile type option will be displayed in the dropdown menu
   (along with the default **Genomics** profile type).

   Please ensure that you select the correct profile type from the dropdown menu when creating a new profile record.

.. hint::

   Please see the :ref:`Projects brokered through COPO <copo-project-affiliations>` section for an overview of the
   projects i.e. profile types that are brokered through COPO.

Choose the desired profile type from the dropdown menu.

See the following screenshot for possible **Tree of Life (ToL)** profile type options.

Please refer to the :ref:`important note <tol-profile-steps-choose-profile-type-important-note>` above if the desired
profile type is not displayed in the dropdown menu.

.. figure:: /assets/images/profiles/ui/profile_add_profile_with_profile_types_dropdown_menu_displayed.png
   :alt: Profile types dropdown menu when adding a new profile record
   :align: center
   :target: https://github.com/TGAC/COPO-documentation/blob/main/assets/images/profiles/ui/profile_add_profile_with_profile_types_dropdown_menu_displayed?raw=true
   :class: with-shadow with-border

   **ToL Profile: Dropdown menu showing all profile types; including the default option, ‘Genomics’**

After you have chosen a profile type option, click the |add-profile-button| **Add new profile record** button to view
the **Add Profile** form for the desired profile type

.. figure:: /assets/images/profiles/ui/profile_add_record_button_web_page.png
   :alt: Add new profile record button
   :align: center
   :target: https://github.com/TGAC/COPO-documentation/blob/main/assets/images/profiles/ui/profile_add_record_button_web_page.png?raw=true
   :class: with-shadow with-border

   **ToL Profile: Add new profile record button**

.. _tol-profile-steps-details:

2. Provide Profile Details in the Add Profile Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the **Add Profile** form dialog, provide details for the new profile.

See the following sections for more information:

   * :ref:`Title & Description <tol-profile-steps-details-title-description>`
   * :ref:`Choose Associated Profile Type (if applicable) <tol-profile-steps-details-associated-profile-type>`
   * :ref:`Choose Sequencing Centre (if applicable) <tol-profile-steps-details-sequencing-centre>`
   * :ref:`Input Locus Tag <tol-profile-steps-details-locus-tag>`
   * :ref:`Save Profile Details <tol-profile-steps-details-save-profile-form>`

.. _tol-profile-steps-details-title-description:

Title & Description
^^^^^^^^^^^^^^^^^^^

   .. hint::

      Both profile **Title** and profile **Description** are mandatory form fields.

      Meaningful field values are recommended in the form boxes because the information will appear
      in submissions of the research objects associated with the profile, in public remote repositories.

   .. figure:: /assets/images/profiles/ui/profile_add_profile_form_title_description.png
      :alt: Provide profile title and description on add profile form
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_add_profile_form_title_description.png
      :class: with-shadow with-border
      :height: 300px

      **ToL Profile Form: Provide profile title and description**

   .. raw:: html

      <br>

.. _tol-profile-steps-details-associated-profile-type:

Select Associated Profile Type (if applicable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. note::

         The **Associated Profile Type** [#f7]_ dropdown menu will only display if the
         **European Reference Genome Atlas (ERGA)** profile type is selected.

         It is mandatory to choose an associated profile type when creating an
         :abbr:`ERGA (European Reference Genome Atlas)` profile. Associated profile types are also known as subprojects
         or child projects.

      * More than one associated type can be selected.

       .. figure:: /assets/images/profiles/ui/profile_add_profile_form_associated_type_for_erga_profile_type.png
          :alt: Choose associated profile type or subproject on add profile form for ERGA profile type
          :align: center
          :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_add_profile_form_associated_type_for_erga_profile_type.png
          :class: with-shadow with-border
          :height: 500px

          **ERGA Profile Type Form: Choose associated profile type or a subproject** [#f5]_

       .. raw:: html

          <br>

.. _tol-profile-steps-details-sequencing-centre:

Select Sequencing Centre (if applicable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      .. note::

         The **Sequencing Centre** dropdown menu will only display if the
         **European Reference Genome Atlas (ERGA)** profile type is selected.

         It is mandatory to choose a sequencing centre when creating an :abbr:`ERGA (European Reference Genome Atlas)`
         profile.

        If **Sanger Institute** is selected as the sequencing centre, the **Associated Profile Type** field will
        automatically be set to **Sanger Institute Approval Needed (SANGER)**.

         See the :ref:`Sequencing Centres that utilise COPO <faq-profiles-sequencing-centres-list>`
         :abbr:`FAQ (Frequently Asked Question)` for additional information.

      .. figure:: /assets/images/profiles/ui/profile_add_profile_form_sequencing_centre.png
         :alt: Choose sequencing centre on 'Add Profile' form
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_add_profile_form_sequencing_centre.png
         :class: with-shadow with-border
         :height: 500px

         **ERGA Profile Type: Choose sequencing centre**

      .. raw:: html

         <br>

.. _tol-profile-steps-details-locus-tag:

Input Locus Tag (if applicable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: /assets/images/profiles/ui/profile_add_profile_form_locus_tag.png
      :alt: Choose locus tag on add profile form
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_add_profile_form_locus_tag.png
      :class: with-shadow with-border
      :height: 250px

      **ToL Profile form: Input locus tag**

   .. raw:: html

      <br>

   If applicable, input the :abbr:`ENA (European Nucleotide Archive)` [#f4]_ **Locus Tag** [#f6]_ in the form box.
   Please refer to the :ref:`How can I assign a locus tag to assemblies <faq-assemblies-submission-locus-tag-assignment>`
   :abbr:`FAQ (Frequently Asked Question)` for guidelines.

   .. raw:: html

      <br>

.. _tol-profile-steps-details-save-profile-form:

3. Save Profile Form
~~~~~~~~~~~~~~~~~~~~~

Click the **Save** button to save the profile details entered in the **Add Profile** form.


4. Profile created
~~~~~~~~~~~~~~~~~~~

The new profile will be displayed in the **Profile** list

    .. figure:: /assets/images/profiles/ui/profile_tol_profile_created.png
      :alt: Tree of Life profile created
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_tol_profile_created.png
      :class: with-shadow with-border

      **ToL Profile: 'Work Profiles' web page displaying the created profile**

    .. raw:: html

       <br>

    .. hint::

      The list of profiles or profile records on the **Work Profiles** web page can be sorted by date created, profile title or
      profile type.

      Choose the desired sort type from the **Sort by** dropdown menu (at the top-right of the profile record).

      See more information in the :ref:`Sorting Profiles <sorting-profiles>` section.

.. raw:: html

   <br>

.. seealso::

   * See :ref:`Steps to create Genomics profile <genomics-profile-walkthrough>` if you would like to make other
     submissions

.. raw:: html

   <hr>

.. _tol-profile-components:

Tree of Life Profile Components
----------------------------------

A COPO profile [#f2]_ defines a set of component types from which instances of research objects can be created.

The following component types are currently defined:

#. :ref:`Accessions <accessions-component>`
#. :ref:`Assembly <assemblies>`
#. :doc:`Barcoding manifests <barcoding-manifest-component>`
#. :ref:`Files <files>`
#. :ref:`Reads <reads>`
#. :ref:`Samples <samples-component-tol>`
#. :ref:`Sequence Annotations <sequence-annotations>`

.. figure:: /assets/images/profiles/buttons/profile_component_buttons_tol.png
   :alt: Tree of Life profile components
   :align: center
   :height: 200px
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/buttons/profile_component_buttons_tol.png
   :class: with-shadow with-border

   **Tree of Life Profile Components**

* Component instances defined within a profile will only be visible within that profile.

* To access a component within a profile, click the component button displayed within the popup after the
  |profile-components-button| button was clicked (see the screenshot above).

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`.
.. [#f2] Also known as COPO profile. See term: :term:`COPO profile`.
.. [#f3] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, samples,
         barcodes (also known as targeted sequences in European Nucleotide Archive (ENA)) and sequence annotations.

         A Tree of Life (ToL) profile is considered as a *project* or *study* research object.
.. [#f4] See term: :term:`ENA`.
.. [#f5] See term: :term:`ERGA`.
.. [#f6] See term: :term:`Locus tag`.
.. [#f7] See :ref:`copo-project-associated-projects` for available subprojects.

   The associated project type refers to the subproject a sample is part of (e.g. a sample may be in the
   :abbr:`ERGA (European Reference Genome Atlas)` project but associated with the
   :abbr:`BGE (Biodiversity Genomics Europe)` subproject). In sample records, this is recorded as
   **associated_tol_project**; in profile records, as **associated_type**.

..
    Images declaration
..
.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/profiles/buttons/components_button.png
   :height: 4ex
   :class: no-scaled-link