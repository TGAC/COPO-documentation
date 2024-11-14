.. _reads:

=====================
Reads Submission
=====================

How to Submit Reads
---------------------

.. note::

  * Once **reads** have been submitted, they cannot be deleted.

  * Files must be uploaded before a **reads** manifest can be submitted. See: :ref:`How to Submit Files <files>`.

.. seealso::

   * :ref:`How to Update Reads <reads-update>`
   * :ref:`Explore Various Types of Reads Checklist <sample-manifest-checklists>`
   * :ref:`How to Submit Files <files>`
   * :ref:`How to check if data files for reads submissions have been processed after upload to ENA <files-ena-file-processing-status>`
   * :ref:`Types of Files for Read Submissions <faq-reads-submission-file-types>`
   * :ref:`accessions-dashboard`

.. raw:: html

   <hr>

Accessing the Reads' Web Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Reads'** [#f1]_  web page can be accessed from the **Components** button associated with a profile [#f2]_.

.. raw:: html

   <hr>

Use Components' Button to Navigate to Reads' Web Page
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Click the |profile-components-button| button associated with a profile. Then, click the  |reads-component-button| from
the popup menu displayed as shown below:

.. figure:: /assets/images/profile/profile_genomics_profile_components_reads.png
  :alt: Genomics Reads' profile component
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_genomics_profile_components_reads.png
  :class: with-shadow with-border
  :height: 300px

  **Genomics Profile Components: Reads component button**

.. raw:: html

   <hr>

Upload Reads
~~~~~~~~~~~~~~

.. hint::

   * To download a blank **Reads'** manifest template, click the |reads-blank-manifest-download-button| button.

   * For guidance on how to fill in the **Reads** manifest to submit *paired* reads, please see the
     :ref:`Reads manifest for paired reads <faq-reads-manifest-paired-reads>` :abbr:`FAQ (Frequently Asked Question)`.

.. warning::

   If you are submitting a **Reads** manifest that includes the column, ``Sample``, please ensure that the sample alias
   (i.e. sample name or accession number) is accurate. Once submitted, the value **cannot** be changed. Reads
   uploaded to COPO will also be sent to :abbr:`ENA (European Nucleotide Archive)`.

   This is important because the ``Sample`` column serves as the key for each row in the **Reads** manifest. Each
   unique sample in the manifest corresponds to a different biosample.

.. note::

   The colour of the |add-reads-manifest-button| button is based on the type of profile that you are submitting a
   Reads for. See the :ref:`profile-types-legend` section regarding the colour code for the various types of project
   profiles on COPO.


#. On the **Reads** web page, click the checklist dropdown to view a list of available checklists that support **Reads'**
   submission as shown below.

   Please note that the checklist options may vary depending on the type of profile you are submitting reads for.

    .. figure:: /assets/images/reads/reads_with_checklist_dropdown_list.png
      :alt: Available checklist options
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_with_checklist_dropdown_list.png
      :class: with-shadow with-border

      **Reads' web page: Checklist dropdown menu with checklist options displayed**

    .. raw:: html

       <br>

    An overview of each **Reads** checklist option is explained in the :ref:`Reads' checklist section <sample-manifest-checklists>`.

   .. raw:: html

      <br>

#. Click |add-reads-manifest-button| button to add **Reads'** from a spreadsheet for the chosen checklist as shown below:

     .. note::

        The colour of the |add-reads-manifest-button| button is based on the type of profile that you are submitting a
        Reads for. See the :ref:`profile-types-legend` section regarding the colour code for the various types of
        project profiles on COPO.

    .. figure:: /assets/images/reads/reads_pointer_to_add_reads_manifest_button.png
      :alt: Pointer to 'Add Reads' from Spreadsheet' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_pointer_to_add_reads_manifest_button.png
      :class: with-shadow with-border

      **Reads' upload: Click 'Add Reads' from Spreadsheet' button**

   .. raw:: html

      <br>

#. An **Upload Read Manifest** dialog is displayed. Click the |reads-upload-button| button to choose a file from
   your local system.

    .. figure:: /assets/images/reads/reads_upload_reads_manifest_dialog.png
      :alt: Upload Read Manifest dialog
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_upload_reads_manifest_dialog.png
      :class: with-shadow with-border

      **Reads' upload: 'Upload Read Manifest' dialog**

   .. raw:: html

      <br>

#. The uploaded manifest is shown in a table in the **Upload Read Manifest** dialog as shown below. Click the
   |reads-finish-button| button to submit the reads manifest.

    .. figure:: /assets/images/reads/reads_upload_reads_manifest_dialog_with_uploaded_manifest_displayed.png
      :alt: Upload Read Manifest dialog
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_upload_reads_manifest_dialog_with_uploaded_manifest_displayed.png
      :class: with-shadow with-border
      :height: 600px

      **Reads' upload: 'Upload Read Manifest' dialog with uploaded manifest**

   .. raw:: html

      <br>

#. The new read(s) will be displayed on the **Reads** web page after a successful submission.

    .. hint::

       Reads records that are highlighted **yellow** indicate that the records are pending submission. The records will
       be highlighted **green** after a successful submission.

    .. figure:: /assets/images/reads/reads_uploaded.png
      :alt: Read(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_uploaded.png
      :class: with-shadow with-border

      **Reads' upload: Reads' web page displaying the uploaded read(s)**

    .. raw:: html

       <br>

.. raw:: html

   <hr>

.. _reads-submission-section:

Submit Reads
~~~~~~~~~~~~~~

.. hint::

   The submitted read record will be highlighted **green**.

Click the desired reads records from the list of reads displayed on the **Reads'** web page. Then, click the **Submit** button
(located in the top-right corner of the table) as shown below:

.. figure:: /assets/images/reads/reads_pointer_to_submit_reads_button.png
  :alt: Submit reads button
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_pointer_to_submit_reads_button.png
  :class: with-shadow with-border

  **Reads submission: Click the "Submit" button to submit the highlighted read from the profile**

.. figure:: /assets/images/reads/reads_submitted.png
  :alt: Reads submitted successfully
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_submitted.png
  :class: with-shadow with-border

  **Reads submission: The Read has been submitted**

.. hint::

   To view accessions associated with the submitted reads, click the **Accessions** button located in the top-right
   corner of the table.

.. seealso::

   * :ref:`accessions-dashboard`

.. raw:: html

   <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes
.. [#f1] See: :term:`Reads`.
.. [#f2] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.

.. raw:: html

   <br><br>

..
    Images declaration
..

.. |add-reads-manifest-button| image:: /assets/images/buttons/add_reads_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/buttons/components_reads_button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-finish-button| image:: /assets/images/buttons/finish_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-upload-button| image:: /assets/images/buttons/reads_upload_button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-blank-manifest-download-button| image:: /assets/images/buttons/download_button_blank_manifest.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link