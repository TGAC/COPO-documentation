.. _standalone-profile-walkthrough:

====================
Stand-alone Profile
====================

In COPO, a Stand-alone work profile [#f1]_ is required to submit research objects [#f2]_ such as files, reads,
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

Steps to Create a Stand-alone Profile
---------------------------------------------

#. Click the |add-profile-button| **Add new record** icon to view the **Add Profile** form

    .. figure:: /assets/images/profile/profile_add_record_button_web_page.png
      :alt: Add new profile record button
      :align: center
      :target: https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/profile/profile_add_record_button_web_page.png
      :class: with-shadow with-border

      **Stand-alone Profile: Add new profile record icon**

#. **Contact COPO via email** dialogue is displayed indicating that the user is not a member of any manifest group
   and that the user must make a request to be added to a manifest group to make :abbr:`ToL (Tree of Life)` manifest
   submissions if the user would like to do so.

   Click **Okay** to close the dialogue.

    .. figure:: /assets/images/profile/profile_contact_copo_prompt_for_group_access.png
      :alt: Contact COPO dialogue
      :align: center
      :target: https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/profile/profile_contact_copo_prompt_for_group_access.png
      :class: with-shadow with-border
      :height: 400px

      **Stand-alone Profile: Contact COPO dialogue is displayed regarding getting access to make Tree of Life (ToL)
      manifest submissions**

#. Provide details for the new profile then, click **Save**

    .. figure:: /assets/images/profile/profile_add_profile_form_web_page_standalone.png
      :alt: Add profile form
      :align: center
      :target: https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/profile/profile_add_profile_form_web_page_standalone.png
      :class: with-shadow with-border
      :height: 400px

      **Stand-alone Profile: Add profile form dialogue**

    .. raw:: html

       <br>

    .. hint::

      Both profile **Title** and profile **Description** are mandatory form fields.

      Meaningful field values are recommended in the form boxes because the information will appear
      in submissions of the research objects associated with the profile, in public remote repositories.

#. The new profile will be displayed in the **Profile** list

    .. figure:: /assets/images/profile/profile_standalone_profile_created.png
      :alt: Stand-alone profile created
      :align: center
      :target: https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/profile/profile_standalone_profile_created.png
      :class: with-shadow with-border

      **Stand-alone Profile: Work profiles' web page displaying the created profile**

    .. raw:: html

       <br>

    .. hint::

      The **Work Profiles**' list can be sorted by date created, profile title or profile type.

      Choose the desired sort type from the **Sort by** dropdown menu (at the top-right of the profile record).

.. raw:: html

   <hr>

.. _standalone-profile-components:

Stand-alone Profile Components
-----------------------------------

A COPO profile defines a set of component types from which instances of research objects [#f2]_ can be created.

The following component types are currently defined:

   #. :ref:`Accessions <accessions-component>`
   #. :ref:`Assembly <assemblies>`
   #. :ref:`Files <files>`
   #. :ref:`Reads <reads>`
   #. :ref:`Sequence Annotations <sequence-annotations>`

   .. figure:: /assets/images/profile/profile_standalone_profile_components.png
      :alt: Stand-alone profile components
      :align: center
      :target: https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/profile/profile_standalone_profile_components.png
      :class: with-shadow with-border
      :height: 650px

      **Stand-alone Profile Components**

* Component instances defined within a profile will only be visible within that profile [#f1]_. 

* To access a component within a profile, click the component button displayed within the popup after the
  |profile-components-button| button was clicked (see the screenshot above).

* Profile actions [#f4]_ can be accessed via the |profile-actions-button| button. The actions describe the process of each
  component within a profile.

.. raw:: html

   <hr>

.. _standalone-profile-virtual-sample-submissions:

Submitting Virtual Samples
-----------------------------------

Please follow the steps below to submit virtual samples [#f5]_:

#. Create a Stand-alone profile or select an existing one.
   See :ref:`Steps to create a Stand-alone profile <standalone-profile-walkthrough>`.

#. Submit reads to the Stand-alone profile. See :ref:`Submitting Reads <reads>` section.

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

.. [#f1] Also known as COPO profile. See: :term:`COPO profile  or work profile<COPO profile>`.
.. [#f2] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, files and sequence annotations.

         A Stand-alone profile is considered as a *project* research object.
.. [#f3] See term: :term:`ENA`.
.. [#f4] See term: :term:`Profile action`.
.. [#f5] See term: :term:`Virtual sample`.

..
    Images declaration
..
.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-actions-button| image:: /assets/images/buttons/profile_actions_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-view-more-button| image:: /assets/images/buttons/profile_view_more_button.png
   :height: 4ex
   :class: no-scaled-link




   



