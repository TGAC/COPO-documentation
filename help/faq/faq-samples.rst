.. _faq-samples:

Samples
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

.. _faq-samples-update-successful-validation-but-no-finish-or-confirm-button:

Why is the ‘Finish’ or ‘Confirm’ button not visible in the ‘Upload Sample Spreadsheet’ dialog after the manifest is successfully uploaded and validated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   This issue occurs because in the manifest uploaded, one or more of the permit required fields or columns is set
   to ``Y``. This means that permit files are required for the sample(s) within the manifest.

   **Resolution**: Upload the permit files using the |upload-permits-button| button first then,

   * The **Finish** button will be displayed in the **Upload Sample Spreadsheet** dialog (once there are no errors) if
     uploading the manifest for the first time.

   * Alternatively, if the manifest is being updated, the **Confirm** button will be displayed in the
     **Upload Sample Spreadsheet** dialog (once there are no errors).

.. raw:: html

   <br>

How can I update values for samples that I have submitted in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Reupload the amended manifest.

   .. raw:: html

      <br>

   .. note::

      * The manifest **must** be reuploaded in the same profile that the samples were submitted in.

      * If the manifest requires permits, the permits **must** also be reuploaded so that the samples' updates can be
        processed.

   * The desired value(s) will be updated once the field value is not a compliance field [#f1]_.
   * See the :ref:`samples-update` section for information about which field values can be updated.

.. raw:: html

  <br>

How to check the status of samples that have been accepted or rejected as a sample submitter?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   **Option 1**: The **Status** column in the samples data table will display the status of the sample record on the
   **Samples** web page.

   **Option 2**: The **Error** column in the samples data table will display an error message if the sample record
   has been rejected or if there are any errors associated with the sample record.

.. raw:: html

   <br>

Can I delete samples that have submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   No, samples cannot be deleted after the manifest have been submitted.

.. raw:: html

   <br>

.. _faq-samples-download-sample-manifest:

Can I retrieve samples or the manifest that have been submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   Yes, see the :ref:`downloading-submitted-sample-manifest` section for more information.

.. raw:: html

   <br>

.. _faq-samples-manifest-upload-limit:

Is there a limit to the number of samples that can be included in a single manifest?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   Yes, there is a limit to the number of samples that can be included in a single manifest uploaded to COPO.

   A threshold of 1,000 samples is recommended with larger sets split across multiple manifests under the same profile
   or different profiles. This is because the validation process can be lengthy and resource-intensive, requiring
   significant memory, which may cause the webpage to crash or lag if there are too many rows to process.

.. raw:: html

   <br>

.. _faq-samples-download-sample-manifest-incorrect-sample-metadata:

Why doesn’t the downloaded sample manifest contain the correct samples or metadata?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   When you click the |download-sample-manifest-button| button, the samples downloaded are associated with a specific
   manifest ID, which can be found in the **Manifest Identifier** column of the data table.

   If multiple manifests are uploaded to the same profile, each will have a different manifest ID, so ensure you click
   the |download-sample-manifest-button| button for the record corresponding to the manifest ID you need.

   .. raw:: html

      <br>

   **Guidance**: Check the **Manifest Identifier** column to ensure the manifest ID is the same for all the samples you
   wish to download. If you identify records with different manifest IDs, click on each record with a different
   manifest ID and then click the |download-sample-manifest-button| button to download the samples associated with that
   specific ID.

   In summary, if there are records with varying manifest IDs, you will need to click each record one by one then,
   click the |download-sample-manifest-button| button for each to download the correct manifest.

.. raw:: html

   <br>

How can I view images that have been uploaded?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the :ref:`image-submission-view-images` section for more information.

.. raw:: html

   <br>

How can I download permits that have been uploaded?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the :ref:`permits-submission-download-permits` section for more information.

.. raw:: html

   <br>

What are the formats that I can download samples in?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   The following are the formats that samples can be downloaded in:

   *  Spreadsheet format (``.xlsx``)

      See the :ref:`Downloading manifest in spreadsheet format <downloading-submitted-sample-manifest>` section
      for more information.

   * Comma-separated values (csv) format (``.csv``)

     On the **Samples** web page, click the |export-manifest-to-csv-format-button| button to download a manifest
     in csv format.

     Refer to the relevant section below, depending on the type of profile that you are working on.

     * :ref:`Accessing the Samples web page for Tree of Life profiles <accessing-samples-web-page-tol>`
     * :ref:`Accessing the Samples web page for Genomics profiles <accessing-samples-web-page-genomics>`

.. raw:: html

   <br>

.. _faq-virtual-sample-submissions:

How can I submit virtual samples in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   Virtual samples are research objects that are submitted to COPO under a Genomics profile.

   See the :ref:`genomics-profile-virtual-sample-submissions` section for more information.

.. raw:: html

   <br>

.. _faq-genomic-metadata-submission-types:

What are the types of genomic metadata submissions that can be made in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. note::

      Data files related to your desired genomic metadata submission type must be uploaded via the Files web page before
      submission.

      See the :ref:`files` section for more information.

   The following are types of genomic metadata submissions that can be made in COPO. Please click the desired link to
   view more information about each submission type.

   * :ref:`Reads <reads>`
   * :ref:`Assemblies <assemblies>`
   * :ref:`Sequence annotations <sequence-annotations>`

   Genomic metadata submissions can be made via the following methods:

   * Under a :ref:`Genomics profile <genomics-profile-walkthrough>` -  this method is applicable if the genomic
     data to be submitted is not associated with any particular project brokered by COPO.

   * Under a :ref:`Tree of Life (ToL) profile <tol-profile-walkthrough>` - this approach is applicable if the genomic
     data to be submitted is associated with a project brokered by COPO and there are existing or submitted sample
     metadata.

   .. seealso::

      * :ref:`Projects brokered through COPO <copo-project-affiliations>`
      * :ref:`Samples submission <samples-submission>`
      * :ref:`image-submission`
      * :ref:`permits-submission`
      * :ref:`barcoding-manifest-submissions`
      * :ref:`faq-reads` :abbr:`FAQ (Frequently Asked Question)`
      * :ref:`faq-assemblies` :abbr:`FAQ (Frequently Asked Question)`
      * :ref:`faq-sequence-annotations` :abbr:`FAQ (Frequently Asked Question)`

.. raw:: html

   <br>

Why do I get a 'PROXY_TISSUE_VOUCHER_ID_FOR_BIOBANKING' error when uploading or updating a manifest?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   If you encounter the error, ``The ID should be in the format of institute unique name:collection code:id or institute
   unique name:id and separated by \"|\" and the ID should be registered already.``, when trying to upload or update
   the field, **PROXY_TISSUE_VOUCHER_ID_FOR_BIOBANKING**, in a manifest, please ensure that the format of the ID is
   ``institution_unique_name:collection_code:voucher_id institution_unique_name:voucher_Id``.

.. raw:: html

  <br>

.. _faq-samples-submission-accessions-assignment:

Are accessions assigned in sample submissions after sample manifests are uploaded?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after sample submissions have been accepted by a sample manager.

   The acceptance makes the submissions public and available for viewing on repositories such as the
   `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`__ and
   `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__.

   See the :ref:`accessions-dashboard` section for more information.

.. raw:: html

   <br>

.. _faq-samples-submission-public-availability:

What are the steps for submitting sample metadata in COPO and ensure it appears in public repositories?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   .. note::

      Click the |collapsible-item-arrow| button below to view its content.

      .. collapse:: Prerequisites

         .. raw:: html

            <br>

         * Request to be added to a manifest group associated with your desired project by sending an email to the COPO
           team at :email:`ei.copo@earlham.ac.uk <ei.copo@earlham.ac.uk>`

           .. hint::

              Visit the :ref:`copo-project-affiliations` section to see a list of COPO-brokered projects.

         * Complete a manifest which is a spreadsheet containing metadata for the desired project.

           If you do not have a blank manifest for the project, you can refer to the :ref:`manifest-templates` section
           for guidance on downloading one to record the metadata.

   #. Log into the COPO website then, you’ll be navigated to the **Work Profiles** web page

      * Refer to the :ref:`overview-accessing-copo-website` section for guidance.

      .. raw:: html

         <br>

   #. Create a profile.

      * For more information, check the :ref:`Steps to Create a Tree of Life Profile <tol-profile-walkthrough>` section
        or the

      .. raw:: html

         <br>

   #. Click the |profile-components-button| button attached to the created profile then, the
      |samples-component-button| in the popup dialog to navigate to the **Samples** web page.

      * For additional information, please see the relevant section below, depending on the type of profile that you
        are working on.

        * :ref:`Accessing the Samples web page for Tree of Life profiles <accessing-samples-web-page-tol>`
        * :ref:`Accessing the Samples web page for Genomics profiles <accessing-samples-web-page-genomics>`

      .. raw:: html

         <br>

   #. Upload the completed manifest.

      Visit the :ref:`samples-submission` section for guidance on submitting samples.

      .. note::

         Choose the desired type of submission listed in that section to be directed to the page for submitting
         the manifest of that type.

   #. COPO validates the uploaded manifest.

      * If there are errors and/or warnings during the validation process, our system will provide messages to
        help resolve them.

        If you encounter errors that you are unable resolve, we are happy to assist. Contact the :email:`COPO team
        <ei.copo@earlham.ac.uk>` detailing the issue(s) encountered.

        If you encounter warnings, they are just informational and will not prevent the upload process from proceeding,
        as long as there are  no errors. Once there are no errors related to the field and you are satisfied with the
        value, the upload process will continue when you click the |finish-button| button if it is the first time
        you are uploading the manifest or the |confirm-button| button if you are updating the manifest.

      .. raw:: html

         <br>

   #. If applicable, upload :ref:`permits <permits-submission>` and/or :ref:`images <image-submission>` after
      uploading the sample manifest in the same attempt. Use the appropriate button in the
      **Upload Sample Spreadsheet** dialog to complete this step.

      .. important::

         This process must be completed in one go; you cannot close the dialog and return later to upload the permits
         and/or images. The permits and/or images rely on metadata from the sample manifest, and as such they must be
         added in the same session.

      .. note::

         The **Upload Sample Spreadsheet** title of the dialog will change depending on the type of submission that
         you are making e.g. **Upload ERGA Sample Spreadsheet**.

   #. Sample managers will be notified of the submission and will review it to accept or reject the samples.

      .. raw:: html

         <br>

   #. The metadata of accepted samples is deposited to :abbr:`ENA (European Nucleotide Archive)`, where accession
      numbers are assigned and reflected in COPO. These samples can then be queried in public repositories like
      `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`_ and
      `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__ using the assigned
      accession numbers.

      The accession numbers are displayed in the columns – **Biosample Accession**, **SRA Accession**, and **Submission
      Accession** – in the data table on the **Samples** web page in COPO. While each accession uniquely identifies a
      sample record, the biosample accession is primarily used as the identifier.

      Additionally, each cell/value in the aforementioned accession columns contains a hyperlink to the metadata on
      :abbr:`ENA (European Nucleotide Archive)`, allowing you to directly access the data there.

      For more details on retrieving accession numbers, please refer to the
      :ref:`Retrieving Accessions <accessions-dashboard>` section.

   .. seealso::

      * :ref:`Are accessions assigned in sample submissions after sample manifests are uploaded? <faq-samples-submission-accessions-assignment>` :abbr:`FAQ (Frequently Asked Question)`

      * If you intend to submit other types of metadata in COPO such as :ref:`assemblies <assemblies>`,
        :ref:`sequence annotations <sequence-annotations>`, :ref:`barcoding manifests <barcoding-manifest-submissions>`
        and :ref:`reads <reads>` submissions and would like to make the submitted metadata available in public
        repositories, please refer to the :ref:`Releasing Profiles (Studies) <releasing-profiles>` section for more
        information.

   .. seealso::

      :ref:`How can genomic metadata be associated with submitted or existing sample metadata in COPO and ensure it appears in public repositories? <faq-samples-submission-and-genomic-metadata-association>` :abbr:`FAQ (Frequently Asked Question)`

.. raw:: html

  <br>

.. _faq-samples-submission-and-genomic-metadata-association:

How can genomic metadata be associated with submitted or existing sample metadata in COPO and ensure it appears in public repositories?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   .. note::

      Click the |collapsible-item-arrow| button below to view its content.

      .. collapse:: Prerequisites

         .. raw:: html

            <br>

         Please refer to the :ref:`What are the steps for submitting sample metadata in COPO and ensure it appears in public repositories? <faq-samples-submission-and-genomic-metadata-association>`
         :abbr:`FAQ (Frequently Asked Question)` for guidance on submitting sample metadata in COPO. The genomic
         metadata submission process depends on the sample metadata submission process.

   In COPO, genomic metadata can be associated with submitted or existing sample metadata through the steps below:

   #. Upload the data files associated with the type of genomic metadata to be submitted on the Files web page.

      * See the :ref:`files` section for guidance.

      .. raw:: html

          <br>

   #. Upload the genomic metadata to the same profile used for the sample manifest submission on the **Work Profiles**
      web page.

      Each genomic metadata submission type requires wither a form or manifest (spreadsheet). Some fields may be
      linked to previously submitted sample metadata.

      Click the |profile-components-button| button associated with the profile then, click the appropriate option -
      |assembly-component-button| button, |barcoding-manifest-component-button| button, |reads-component-button| button
      or |sequence-annotations-component-button| in the popup dialog to navigate to the relevant web page.

   .. seealso::

      * :ref:`What are the steps for submitting sample metadata in COPO and ensure it appears in public repositories? <faq-samples-submission-public-availability>` :abbr:`FAQ (Frequently Asked Question)`
      * :ref:`Releasing Profiles (Studies) <releasing-profiles>` i.e. making genomic metadata public after submission in COPO in public repositories
      * :ref:`faq-genomic-metadata-submission-types` :abbr:`FAQ (Frequently Asked Question)` for guidance on the types
        of genomic metadata

.. raw:: html

   <br>

Why do I receive so many errors after having uploaded a sample manifest?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  These *Invalid column* errors are likely due to the uploaded manifest not matching the desired sample type.

  * **Samples uploaded to a Genomics profile** - please ensure that the correct sample type is selected from the
    checklist dropdown menu on the Samples web page before uploading a manifest.

  * **Samples uploaded to a Tree of Life (ToL) profile** - the sample type is determined by the type of ToL
    profile that you are uploading to.

    Please make sure that the manifest you upload matches the sample type associated with that profile.

    Refer to :ref:`profile-types-legend` to identify the colour of the add
    manifest button (for example, |add-dtol-manifest-button|). The colour of this button changes depending on the
    profile type. For example, it may be |add-asg-manifest-button| for an :abbr:`ASG (Aquatic Symbiosis Genomics)`
    profile or |add-erga-manifest-button| for an :abbr:`ERGA (European Reference Genome Atlas)` profile.

.. raw:: html

   <br><hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Compliance field`


..
    Images declaration
..

.. |add-asg-manifest-button| image:: /assets/images/samples/asg/buttons/add_asg_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-dtol-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |add-erga-manifest-button| image:: /assets/images/samples/erga/buttons/add_erga_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |assembly-component-button| image:: /assets/images/assemblies/buttons/components_assembly_button.png
   :height: 4ex
   :class: no-scaled-link

.. |barcoding-manifest-component-button| image:: /assets/images/barcoding/buttons/components_barcoding_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |confirm-button| image:: /assets/images/buttons/confirm_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/samples/buttons/samples_download_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |export-manifest-to-csv-format-button| image:: /assets/images/samples/buttons/samples_export_to_csv_format_button.png
   :height: 4ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/profiles/buttons/components_button.png
   :height: 4ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/reads/buttons/components_reads_button.png
   :height: 4ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/samples/buttons/components_samples_button.png
   :height: 4ex
   :class: no-scaled-link

.. |sequence-annotations-component-button| image:: /assets/images/sequence_annotations/buttons/components_sequence_annotations_button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits_upload_button.png
   :height: 4ex
   :class: no-scaled-link