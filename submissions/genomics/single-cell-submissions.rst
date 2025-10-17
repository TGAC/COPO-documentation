.. _single-cell-submissions:

======================
Single-cell Submission
======================

The section describes how to use COPO to submit Single-cell Ribonucleic Acid Sequencing (scRNA-Seq) [#f1]_ data to public
repositories like :abbr:`ENA (European Nucleotide Archive)` [#f2]_ and Zenodo.

.. raw:: html

   <hr>

---------------
Prerequisites
---------------

.. note::

   * **Samples**: Submit samples first before uploading Single-cell manifests. See
     :ref:`Samples submission <samples-submission-genomics>` section for guidance.

   * **Data files**: Upload all required data files before submting Single-manifests. See:
     :ref:`How to Submit Files <files>`.

.. _submit-manifest-single-cell:

-----------------
Upload Manifest
-----------------

#. Create a **Genomics** profile to make Single-cell data submissions. Please see:
   :ref:`Steps to Create a Genomics Profile <genomics-profile-walkthrough>` for guidance.

   *If you have already created a Genomics profile, please skip this step.*

#. Access the Single-cell web page for the created profile (see
   :ref:`Accessing the Single-cell web page <accessing-single-cell-web-page>`) for more information.

   .. hint::

      To download a manifest template, click the |blank-manifest-download-button| button on the Single-cell web page.

#. On the **Single-cell** web page, click the dropdown menu to view a list of available checklists that support
   **Single-cell** submissions as shown below.

    .. figure:: /assets/images/single_cell/ui/single_cell_with_checklist_dropdown_list.png
      :alt: Available sample checklist options within a Genomics profile
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/single_cell/ui/single_cell_with_checklist_dropdown_list.png
      :class: with-shadow with-border

      **Single-cell web page: Checklist dropdown menu options**

    .. raw:: html

       <br>

    .. tip::

       Hover over a checklist dropdown menu option to view its description. Alternatively, an overview of each
       checklist is explained in the section, :ref:`single-cell-submission-types`.

   .. raw:: html

      <br>

#. Click |add-single-cell-manifest-button| button to upload a Single-cell manifest from your local (computer) system.

    .. figure:: /assets/images/single_cell/ui/single_cell_pointer_to_add_manifest_button.png
      :alt: Pointer to 'Add Study from Spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/single_cell/ui/single_cell_pointer_to_add_manifest_button.png
      :class: with-shadow with-border

      **Single-cell manifest web page: Click 'Add Study from Spreadsheet' button**

   .. raw:: html

      <br>

#. A dialog is displayed. Click the |upload-single-cell-manifest-button| button in the dialog to choose a file from
   your local system.

    .. figure:: /assets/images/single_cell/modals/single_cell_upload_spreadsheet_dialog.png
      :alt: Upload Single-cell Spreadsheet dialog
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/single_cell/modals/single_cell_upload_spreadsheet_dialog.png
      :class: with-shadow with-border

      **Single-cell manifest submission: Upload Single-cell manifest dialog**

.. raw:: html

   <hr>

-----------------
Submit Manifest
-----------------

.. After uploading the manifest, click the |submit-single-cell-manifest-button| button to submit the Single-cell manifest
.. to the selected repository.

.. raw:: html

   <hr>

---------------
Related Topics
---------------

.. seealso::

    * :ref:`files`
    * :ref:`samples-submission`
    * :ref:`single-cell-submission-types`
    * :ref:`Single-cell Frequently Asked Questions <faq-single-cell>`

.. raw:: html

  <hr>

.. raw:: html

  <br>

.. rubric:: Footnotes

.. [#f1] See: :term:`Single-cell RNA Seq`.
.. [#f2] See term: :term:`ENA`.

..
    Images declaration
..
.. |add-single-cell-manifest-button| image:: /assets/images/buttons/add_manifest_button_for_genomics_profile.png
   :height: 4ex
   :class: no-scaled-link

.. |blank-manifest-download-button| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-single-cell-manifest-button| image:: /assets/images/single_cell/buttons/upload_single_cell_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

