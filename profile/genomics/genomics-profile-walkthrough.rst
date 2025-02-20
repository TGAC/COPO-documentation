.. _genomics-profile-walkthrough:

====================
Genomics Profile
====================

In COPO, a Genomics work profile [#f1]_ is required to submit research objects [#f2]_ such as files, reads,
assemblies and sequence annotations.

.. hint::

   COPO work profiles are regarded as *project* research objects. The projects are created in
   :abbr:`ENA (European Nucleotide Archive)` [#f3]_ after :ref:`reads have been submitted <reads>`. Thus, any
   modifications that you would like to be done to a project in :abbr:`ENA (European Nucleotide Archive)` must be done
   to the desired profile in COPO.

.. seealso::

   * See :ref:`Steps to create Tree of Life (ToL) profile <tol-profile-walkthrough>` if you would like to make ToL
     manifest submissions
   * :ref:`How to Update Profiles <profile-update>`
   * :ref:`How to Delete Profiles <profile_deletion>`
   * :ref:`How to Make Profiles (also known as Projects) Public <releasing-profiles>`
   * :ref:`Sharing Profiles <sharing-profiles>`
   * :ref:`Sorting Profiles <sorting-profiles>`
   * :ref:`Profile Types Legend <profile-types-legend>`

.. raw:: html

   <hr>

Steps to Create a Genomics Profile
---------------------------------------------

#. Click the |add-profile-button| **Add new record** icon to view the **Add Profile** form

    .. figure:: /assets/images/profile/profile_add_record_button_web_page.png
      :alt: Add new profile record button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_add_record_button_web_page.png
      :class: with-shadow with-border

      **Genomics Profile: Add new profile record icon**

#. Provide details for the new profile then, click **Save**

   If applicable, input the :abbr:`ENA (European Nucleotide Archive)` [#f3]_ **Locus Tag** in the form box.
   Please refer to the :ref:`How can I assign a locus tag to assemblies <faq-assemblies-submission-locus-tag-assignment>`
   :abbr:`FAQ (Frequently Asked Question)` for guidelines.

    .. raw:: html

       <br>

    .. figure:: /assets/images/profile/profile_add_profile_form_web_page_genomics.png
      :alt: Add profile form
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_add_profile_form_web_page_genomics.png
      :class: with-shadow with-border
      :height: 400px

      **Genomics Profile: Add profile form dialog**

    .. raw:: html

       <br>

    .. hint::

      Both profile **Title** and profile **Description** are mandatory form fields.

      Meaningful field values are recommended in the form boxes because the information will appear
      in submissions of the research objects associated with the profile, in public remote repositories.

#. The new profile will be displayed in the **Profile** list

    .. figure:: /assets/images/profile/profile_genomics_profile_created.png
      :alt: Genomics profile created
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_genomics_profile_created.png
      :class: with-shadow with-border

      **Genomics Profile: Work profiles' web page displaying the created profile**

    .. raw:: html

       <br>

    .. hint::

      The **Work Profiles**' list can be sorted by date created, profile title or profile type.

      Choose the desired sort type from the **Sort by** dropdown menu (at the top-right of the profile record).

.. raw:: html

   <hr>

.. _genomics-profile-components:

Genomics Profile Components
-----------------------------------

A COPO profile defines a set of component types from which instances of research objects [#f2]_ can be created.

The following component types are currently defined:

   #. :ref:`Accessions <accessions-component>`
   #. :ref:`Assembly <assemblies>`
   #. :ref:`Files <files>`
   #. :ref:`Reads <reads>`
   #. :ref:`Sequence Annotations <sequence-annotations>`

   .. figure:: /assets/images/profile/profile_genomics_profile_components.png
      :alt: Genomics profile components
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_genomics_profile_components.png
      :class: with-shadow with-border
      :height: 250px

      **Genomics Profile Components**

* Component instances defined within a profile will only be visible within that profile [#f1]_. 

* To access a component within a profile, click the component button displayed within the popup after the
  |profile-components-button| button was clicked (see the screenshot above).

.. raw:: html

   <hr>

.. _genomics-profile-virtual-sample-submissions:

Submitting Virtual Samples
-----------------------------------

Please follow the steps below to submit virtual samples [#f4]_:

#. Create a Genomics profile or select an existing one.
   See :ref:`Steps to create a Genomics profile <genomics-profile-walkthrough>`.

#. Submit reads to the Genomics profile. See :ref:`Submitting Reads <reads>` section.

   .. important::

        * Files **must** be uploaded before reads submission can be made.
        * Reads submission is required before making a virtual sample submission.

#. All virtual sample submissions require a description.

   Provide the virtual sample description to the :email:`COPO team <ei.copo@earlham.ac.uk>` as well as the
   (completed) reads manifest file. COPO will add the sample description in ENA [#f3]_.

.. hint::
    Accessions are available a few minutes after reads have been submitted.

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.
.. [#f2] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, files and sequence annotations.

         A Genomics profile is considered as a *project* or *study* research object.
.. [#f3] See term: :term:`ENA`.
.. [#f4] See term: :term:`Virtual sample`.

..
    Images declaration
..
.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-view-more-button| image:: /assets/images/buttons/profile_view_more_button.png
   :height: 4ex
   :class: no-scaled-link




   



