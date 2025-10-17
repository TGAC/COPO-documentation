.. _samples-submission-genomics:

========================================
Sample Submission for Genomics Profiles
========================================

.. _samples-submission-genomics-note:

---------------------
Prerequisites & Notes
---------------------

.. important::

   Create a **Genomics** profile to make sample submissions. Please see:
   :ref:`Steps to Create a Genomics Profile <genomics-profile-walkthrough>` for guidance.

   If you have already created a Genomics profile, please skip this step.

   If this section does not apply to your use case and you are working with a :abbr:`ToL (Tree of Life)` [#f1]_
   profile [#f2]_, please refer to the :ref:`samples-submission-tol` section.

.. note::

   Samples cannot be deleted after they have been submitted.

.. raw:: html

   <hr>

.. _accessing-samples-web-page-genomics:

--------------------------------
Accessing the Samples Web Page
--------------------------------

The Samples web page can be accessed via the **Components** button or via the components icon navigation pane when
viewing another component's web page associated with a Genomics profile.

.. _accessing-samples-web-page-via-components-button:

Using the Components Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the |profile-components-button| button associated with a profile. Then, click the  |samples-component-button| from
the popup menu displayed as shown below:

.. figure:: /assets/images/samples/ui/samples_button_pointer_genomics.png
   :alt: Samples' profile component
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/ui/samples_button_pointer_genomics.png
   :class: with-shadow with-border
   :height: 300px

   **Genomics Profile Components: Samples component button**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /profile/profile-component-navigation-pane-overview.rst

.. figure:: /assets/images/samples/icons/samples_icon_pointer_genomics.png
   :alt: Samples profile component icon
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/samples/icons/samples_icon_pointer_genomics.png
   :class: with-shadow with-border
   :height: 120px

   **Genomics Profile: Navigation pane showing the Samples component icon**

.. raw:: html

   <hr>

.. _submit-genomics-sample-manifest:

----------------
Upload Samples
----------------

.. hint::

  To download a blank **sample** manifest template, click the |blank-manifest-download-button| button.

#. On the **Samples** web page, click the dropdown menu to view available sample checklists as shown below.

    .. figure:: /assets/images/samples/genomics/ui/samples_pointer_to_dropdown_menu.png
      :alt: Pointer to Samples checklist dropdown menu
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/genomics/ui/samples_pointer_to_dropdown_menu.png
      :class: with-shadow with-border

      **Samples web page: Pointer to Samples checklist dropdown menu**

    .. figure:: /assets/images/samples/genomics/ui/samples_with_checklist_dropdown_list.png
      :alt: Available sample checklist options within a Genomics profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/genomics/ui/samples_with_checklist_dropdown_list.png
      :class: with-shadow with-border

      **Samples web page: Checklist dropdown menu options**

    .. raw:: html

       <br>

    .. tip::

       Hover over a checklist dropdown menu option to view its description. Alternatively, an overview of each option
       is provided in the :ref:`Sample manifest checklist section <sample-manifest-checklists>`.

   .. raw:: html

      <br>

#. Choose an option from the dropdown menu.

#. Click |add-sample-manifest-button| button to add **Samples** from a spreadsheet for the chosen checklist as shown below:

   .. note::

      The option you select in the dropdown menu determines the type of manifest to be uploaded. If you
      upload a manifest that does not match this selection, the system will return an error.

   .. figure:: /assets/images/samples/genomics/ui/samples_pointer_to_add_samples_manifest_button.png
      :alt: Pointer to 'Add/Update Sample(s) from Sample Spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/genomics/ui/samples_pointer_to_add_samples_manifest_button.png
      :class: with-shadow with-border

      **Samples upload: Click 'Add/Update Sample(s) from Sample Spreadsheet' button**

   .. raw:: html

      <br>

#. An **Upload Sample Manifest** dialog is displayed. Click the |upload-sample-manifest-button| button to choose a file from
   your local system.

    .. figure:: /assets/images/samples/genomics/modals/samples_upload_samples_manifest_dialog.png
      :alt: Upload Sample Manifest dialog
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/genomics/modals/samples_upload_samples_manifest_dialog.png
      :class: with-shadow with-border

      **Samples upload: 'Upload Sample Manifest' dialog**

   .. raw:: html

      <br>

#. The uploaded manifest is shown in a table in the **Upload Sample Manifest** dialog as shown below. Click the
   |samples-finish-button| button to submit the sample manifest.

    .. figure:: /assets/images/reads/modals/reads_upload_reads_manifest_dialog_with_uploaded_manifest_displayed.png
      :alt: Upload Read Manifest dialog
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/modals/reads_upload_reads_manifest_dialog_with_uploaded_manifest_displayed.png
      :class: with-shadow with-border
      :height: 600px

      **Reads' upload: 'Upload Read Manifest' dialog with uploaded manifest**

   .. raw:: html

      <br>

#. The new read(s) will be displayed on the **Reads** web page after a successful submission.

    .. hint::

       Reads records that are highlighted **yellow** indicate that the records are pending submission. The records will
       be highlighted **green** after a successful submission.

    .. figure:: /assets/images/reads/ui/reads_uploaded.png
      :alt: Read(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/ui/reads_uploaded.png
      :class: with-shadow with-border

      **Reads' upload: Reads' web page displaying the uploaded read(s)**

    .. raw:: html

       <br>

.. raw:: html

  <hr>

Submit Images
~~~~~~~~~~~~~

Follow the steps indicated :ref:`here <image-submission>` for image submission.

.. raw:: html

  <hr>

#. The new sample(s) will be displayed on the **Samples** web page after a successful submission.

    .. figure:: /assets/images/samples/asg/ui/asg_samples_submitted.png
      :alt: Sample(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/asg/ui/asg_samples_submitted.png
      :class: with-shadow with-border

      **ASG manifest submission: Samples web page displaying the uploaded sample(s)**

    .. raw:: html

       <br><br>

.. raw:: html

    <hr>

---------------
Related Topics
---------------

.. seealso::

   * :ref:`How to Update Samples <samples-update>`
   * :ref:`downloading-submitted-sample-manifest`
   * :ref:`Accessions profile component <accessions-component>`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`.
.. [#f2] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.


.. raw:: html

   <br><br>

..
    Images declaration
..
.. |add-sample-manifest-button| image:: /assets/images/buttons/add_manifest_button_for_genomics_profile.png
   :height: 4ex
   :class: no-scaled-link

.. |blank-manifest-download-button| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/samples/buttons/components_samples_button.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-finish-button| image:: /assets/images/buttons/finish_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-sample-manifest-button| image:: /assets/images/samples/genomics/buttons/samples_upload_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/profiles/buttons/components_button.png
   :height: 4ex
   :class: no-scaled-link