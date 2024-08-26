.. _faq:

Frequently Asked Questions
==============================

.. hint::

   To view the entire answer to a question, collapse the answer by clicking the |collapsible-item-arrow| button below.

Assemblies
--------------------

.. _faq-assemblies-submission-file-types:

What are the types of files that are required for assembly submissions in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the `European Nucleotide Archive's (ENA's) documentation <https://ena-docs.readthedocs.io/en/latest/submit/assembly.html#files-for-genome-assembly-submissions>`__
   for details about the types of files that can be submitted for assembly submissions.

.. raw:: html

  <br>

.. _faq-assemblies-submission-locus-tag-assignment:

How can I assign my own locus tag to assemblies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

  .. hint::

     Each profile in COPO is known as a study or project in :abbr:`ENA (European Nucleotide Archive)` (after reads
     have been submitted).

  .. note::

     Reads submission **must** be done in order for a locus tag to be assigned to the project.

     This is because a project submission is done to European Nucleotide Archive (ENA) once reads submission has
     been completed.

  You can assign a custom locus tag when creating a profile in COPO. See the image below for guidance.

  .. figure:: /assets/images/profile/profile_add_form_profile_form_locus_tag.png
     :alt: Adding locus tag to a profile
     :align: center
     :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/profile/profile_add_form_profile_form_locus_tag.png
     :class: with-shadow with-border
     :height: 400px

     **Profile form: Adding locus tag**

  If a locus tag is not assigned, :abbr:`ENA (European Nucleotide Archive)` will automatically assign a locus
  tag to your assembly after it has been submitted in COPO and deposited to ENA.

  See `ENA's documentation <https://ena-docs.readthedocs.io/en/latest/faq/locus_tags.html#what-are-locus-tags>`_
  for more details. The documentation outlines rules that the locus tag prefix should conform to.

.. raw:: html

   <hr>

Dashboard
--------------------

How can I view accessions after I have submitted samples, reads, or experiments in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  .. hint::

     GenBank accession numbers follow the format ``GCA_XXXXXXXXX``. They are automatically assigned by
     :abbr:`ENA (European Nucleotide Archive)` and can be viewed on the
     `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__ website using the
     link:  ``https://www.ncbi.nlm.nih.gov/datasets/genome/?bioproject=<project-id>`` where ``<project-id>`` is the
     project :abbr:`ID (identifier)` (also known as study :abbr:`ID (identifier)` or profile :abbr:`ID (identifier)`)
     associated with the profile used to submit the files in COPO.

   * Click the |accessions-dashboard-button| button.

   * The accessions dashboard will be displayed.

   * Alternatively, navigate to the `Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__.

.. raw:: html

   <br>

Is there a way to analyse metadata submissions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Yes, the following are ways to analyse metadata submissions:

   .. raw:: html

      <br>

   #. `Tree of Life dashboard <https://copo-project.org/copo/tol_dashboard/tol>`__
       * Alternatively, click the |tol-dashboard-button| button.
   #. `Tree of Life inspection web page <https://copo-project.org/copo/tol_dashboard/tol_inspectt>`__
       * Alternatively, click the |tol-inspect-button| button.
   #. `Tree of Life inspection by Genome Acquisition Lab web page <https://copo-project.org/copo/tol_dashboard/tol_inspect/gal>`__
       * Alternatively, click the |tol-inspect-by-gal-button| button.
   #. `Statistics web page <https://copo-project.org/copo/tol_dashboard/stats>`__

.. raw:: html

   <hr>

Files
--------------------

How do I know when data files that have been uploaded to COPO are public at European Nucleotide Archive (ENA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`files-ena-upload-status-after-copo-metadata-submission` section for more information.

.. raw:: html

   <hr>

Other
-------

When was the COPO  project launched?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   In September 2014, the COPO project was launched under the Biotechnology and Biological Sciences Research Council
   (BBSRC) with the aim of improving open access to and management of data within plant research. It was known as
   Collaborative Open Plant Omics at that time and is based at the The Genome Analysis Centre (TGAC).

   Now, the project is known as Collaborative OPen Omics. It is based at the
   `Earlham Institute (EI) <https://www.earlham.ac.uk>`__ formerly known as :abbr:`TGAC (The Genome Analysis Centre)`.

   .. list-table:: COPO project's logos over the years
      :width: 100%
      :align: center
      :header-rows: 1

      * - 2014 - 2022
        - 2023 - PRESENT
      * - .. figure:: /assets/logos/copo_logo_old.png
             :height: 10ex
             :alt: COPO logo during the years 2014 - 2022
             :align: center
             :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/logos/copo_logo_old.png
             :class: with-shadow with-border
        - .. figure:: /assets/logos/copo_logo_new.png
             :height: 12ex
             :alt: COPO logo during the years 2023 - PRESENT
             :align: center
             :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/logos/copo_logo_new.png
             :class: with-shadow with-border

   .. seealso::

     * :download:`Download a seminar presentation <../assets/files/presentations/EI_Seminar_23042024_Advancing_Biodiversity_Research_The_Evolution_of_COPO.pptx>`
       which gives an overview of the evolution of the COPO project since its inception in 2014 to the present day

.. raw:: html

   <hr>


Who are the developers of the COPO project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Please see:

   * `COPO Team <https://copo-project.org/about/#project-team-section-current>`__ section on the **About** web page of
     the COPO's website for current software developers of the project

   * `Former Team Members and Contributors <https://copo-project.org/about/#project-team-section-former>`__ section on the
     **About** web page of the COPO's website for the previous developers and contributors of the project

.. raw:: html

   <hr>

Permits
--------------------

Can I view or download permits that I have uploaded in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

  Yes, permits can be retrieved and downloaded by selecting the desired sample record(s) on the **Samples** web page

  Then, clicking the |download-permits-button1| button on the web page.

.. raw:: html

  <br>

.. _faq-permits-error-uploading-multiple-permits-separately:

Why am I unable to upload permit one after the other?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   .. warning::

        * If you have more than one permit ﬁle to upload, they **must** be uploaded at the
          same time i.e. after you have clicked the |upload-permits-button| button, navigate
          to the directory where the permits are stored and ``CTRL + click`` all of the
          permits so that all the permits are highlighted and uploaded at the same time.

   * All permit ﬁles have to be selected/opened from the directory and uploaded
     together not one after the other.

.. raw:: html

   <br>

How can I resolve 'Conflicting data...' error when uploading permits in COPO after having uploaded a manifest?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   The error message ``Conflicting data`` is displayed when at least one of the following occurs:

   * The permit filename provided in the manifest does not end with the extension ``.pdf`` or ``.PDF``

     **Resolution**: Rename the name of the permit file so that it ends with the extension, ``.pdf`` or ``.PDF`` then, reupload the
     manifest

   * In the uploaded manifest, different permit filenames are associated with the same **SPECIMEN_ID**

     **Resolution**: Provide a unique permit filename for each **SPECIMEN_ID** or provide the same filename for
     permit files that are associated with the same **SPECIMEN_ID** in the manifest. Then, reupload the manifest.

.. raw:: html

   <br>

Why do I encounter the error 'No xx permit found for xx 'SPECIMEN_ID'...Filename of permit must be named xx' after having uploading the permit files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   This error message occurs when at least one of the following occurs:

   * The manifest uploaded requires multiple permit files but they were uploaded separately i.e. one after the other.

     **Resolution**: Please refer to :ref:`faq-permits-error-uploading-multiple-permits-separately`
     :abbr:`FAQ (Frequently Asked Question)` for more information.

   * The permit filename uploaded from your local system actually ends with ``.pdf.pdf`` (or ``.PDF.PDF``) and not
     ``.pdf`` (or ``.PDF``)

     **Resolution**: Ensure that the name of the permit file ends with the ``.pdf`` or ``.PDF`` extension only.

     If you are using a Windows operating system (OS) to upload permits, Windows OS by default, hides file extensions
     which results in it not being visible to you.

     If you would like to see the file extension, you can enable it by following these
     `guidelines <https://support.microsoft.com/en-gb/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01>`__.

   Reupload the manifest as well as the permit files after the resolutions have been made.

.. raw:: html

   <hr>

Profiles
--------------------

How can I be added to a profile group?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

    * Make a request to the :email:`COPO team <ei.copo@earlham.ac.uk>` indicating
      the type of profile group that you would like to be assigned to.

    * The desired profile type will be displayed in the **Profile Type**
      dropdown menu in the **Add Profile** form after the request has been approved.

.. raw:: html

   <br>

How can I create a profile on COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

    * Click the |add-profile-button| button then, fill in and save the form displayed.

     ..  figure:: /assets/images/profile/profile_add_form.png
         :alt: Profile types dropdown menu
         :align: center
         :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/profile/profile_add_form.png
         :class: with-shadow with-border
         :width: 400px
         :height: 400px

         **Add Profile form: Choosing a Profile Type**

   * View the following video to see how to create a profile.

      ..  youtube:: 7xiVTNw6pPc
          :width: 640
          :height: 480
          :align: center

.. raw:: html

   <br>


How can I upload/submit research objects to a profile owned by another user or how can I create a group or how can I share my profile with others?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`sharing-profiles` section for more information.

.. raw:: html

   <br>

How can I add a subproject to a profile on COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * In the **Add Profile** form, choose the desired subproject(s) from the list of
     associated projects as shown below.

   * See the :ref:`copo-project-associated-projects` section for information about the available subprojects.

   ..  figure:: /assets/images/profile/profile_form_associated_types.png
       :alt: Associated profile types dropdown menu
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/profile/profile_form_associated_types.png
       :class: with-shadow with-border
       :width: 400px
       :height: 400px

       **Add Profile form: Selecting Associated Profile Type dropdown menu**

.. raw:: html

   <br>

How can I add a subproject or secondary project to a primary project in ENA/Biosamples?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * Contact the :email:`COPO team <ei.copo@earlham.ac.uk>` with the request
     providing the project accession of the child/subproject and the project accession of
     the parent/primary project.

.. raw:: html

   <br>

How can I edit or delete a profile that I have created in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * Click the |vertical-ellipsis-icon| icon that is associated with the desired profile.

   * The option to edit or delete a profile record will be displayed once clicked.

   * The web page will refresh after the task has been completed successfully.

.. raw:: html

   <br>

How many profiles can I have in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: You can have as many profiles as needed to represent your research objects.

   .. raw:: html

      <br>

   * For instance, you can create a profile to represent work done as part of a grant,
     subproject within a project or a :abbr:`PhD (Doctorate of Philosophy)` project.

.. raw:: html

   <br>

How can I view more profiles that I have created in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Scroll downwards on the web page.

   .. raw:: html

      <br>

   * More profiles that you have created will be loaded.

.. raw:: html

   <br>

.. _faq-profiles-view-more-information:

How can I view more information about a profile that I have created in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. note::
      * The |profile-view-more-button| button will only be associated with a profile if the profile has at least one
        of the following information.

   * Click the |profile-view-more-button| button associated with the profile.

   * After the button is clicked, a popup dialog will show at least one of the following information if it is available:

      * **Release Status** (if applicable)
      * **Release Date** (if applicable)
      * **Associated Profile Type(s)**
      * **Sequencing Centre**

   ..  figure:: /assets/images/profile/profile_view_more_button_with_popup_displayed.png
       :alt: Profile view more information popup dialog
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/profile/profile_view_more_button_with_popup_displayed.png
       :class: with-shadow with-border
       :width: 400px
       :height: 400px

       **Profile: View more information popup dialog**


.. raw:: html

   <br>

How can I navigate to the top of the web page after having loaded several work profiles?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Scroll upwards on the web page.

   .. raw:: html

      <br>

   * Alternatively, click the |navigate-to-top-button| button which automatically navigates
     to the top of the web page.

.. raw:: html

   <br>

How can I create components for a profile?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   #. Navigate to the work profile web page
   #. Click the |add-profile-button| button
   #. Fill in then, save the form that is displayed
   #. Click the |profile-components-button| button associated with the profile record to view
      the component of the action that was performed

.. raw:: html

   <br>

How can I make profiles or projects public or visible in European Nucleotide Archive (ENA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See :ref:`releasing-profiles` section for more information.

.. raw:: html

   <hr>
.. raw:: html

   <br>

.. _faq-profiles-sequencing-centres-list:

What are the names of the sequencing centres whose samples are brokered through COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   Currently, there are 20 sequencing centres whose samples are brokered through COPO.

   Each COPO :abbr:`ERGA (European Reference Genome Atlas)` profile should be associated with a sequencing centre.

   The following are the names of the sequencing centres:

   .. hlist::
      :columns: 2

      * CENTRO NACIONAL DE ANÁLISIS GENÓMICO
      * DNA SEQUENCING AND GENOMICS LABORATORY, HELSINKI GENOMICS CORE FACILITY
      * EARLHAM INSTITUTE
      * FUNCTIONAL GENOMIC CENTER ZURICH
      * GENOSCOPE
      * HANSEN LAB, DENMARK
      * INDUSTRY PARTNER
      * LAUSANNE GENOMIC TECHNOLOGIES FACILITY
      * LEIBNIZ INSTITUTE FOR THE ANALYSIS OF BIODIVERSITY CHANGE, MUSEUM KOENIG, BONN
      * NEUROMICS SUPPORT FACILITY, UANTWERP, VIB
      * NGS BERN
      * NGS COMPETENCE CENTER TÜBINGEN
      * NORWEGIAN SEQUENCING CENTRE
      * Other_ERGA_Associated_GAL
      * SANGER INSTITUTE
      * SCILIFELAB
      * SVARDAL LAB, ANTWERP
      * UNIVERSITY OF BARI
      * UNIVERSITY OF FLORENCE
      * WEST GERMAN GENOME CENTRE

.. raw:: html

  <br>

What happens when a profile is updated in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   When a profile is successfully updated in COPO, the changes made to the profile will be reflected in the research
   objects such as samples, reads, assemblies or files associated with the profile.

   For example, if a profile is updated to include -

   * a new associated profile type, the new associated profile type will be displayed in the sample records associated
     with the profile.

   * a new :abbr:`ENA (European Nucleotide Archive)` :ref:`locus tag <faq-assemblies-submission-locus-tag-assignment>`,
     the new ENA locus tag will be associate displayed in the reads, sequencing annotations and/ assembles associated
     with the profile.

.. raw:: html

   <hr>

Reads
--------------------

.. _faq-reads-manifest-paired-reads:

How do I fill in the Reads manifest to submit paired reads?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * Ensure that the **Reads** manifest contains the following:

      * **PAIRED** as the value for the **Library layout** column
      *  File names in the **File name** column separated by a comma

     See below for a snapshot of a **Reads** manifest for paired reads:

     .. figure:: /assets/images/reads/reads_manifest_paired.png
        :alt: Reads manifest for paired reads
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/reads/reads_manifest_paired.png
        :class: with-shadow with-border

        **Reads' manifest for paired reads**

.. raw:: html

   <br>

.. _faq-reads-submission-file-types:

What are the types of files that are required for read submissions in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the `European Nucleotide Archive's (ENA's) documentation <https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#accepted-read-data-formats>`__
   for details about the types of files that can be submitted for read submissions.

.. raw:: html

   <hr>

Samples
--------------------

.. _faq-samples-update-successful-validation-but-no-finish-button:

Why is the 'Finish' button not visible in the 'Upload Spreadsheet' dialog even though the manifest has been successfully uploaded and validated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   This issue occurs because in the manifest uploaded, one or more of the permit required fields or columns is set
   to ``Y``. This means that permit files are required for the sample(s) within the manifest.

   **Resolution**: Upload the permit files using the |upload-permits-button| button first then, the **Finish** button
   will be displayed in the **Upload Spreadsheet** dialog (once there are no errors).

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

Can I delete samples that have submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   No, samples cannot be deleted after the manifest have been submitted.

.. raw:: html

   <br>

Can I retrieve samples or the manifest that have been submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   Yes, see the :ref:`downloading-submitted-sample-manifest` section for more information.

.. raw:: html

   <br>

How can I view images that have been uploaded?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   See the :ref:`images-submission-view-images` section for more information.

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

   *  Microsoft Excel Spreadsheet format (``.xlsx``)

      See the :ref:`Downloading manifest in spreadsheet format <downloading-submitted-sample-manifest>` section
      for more information.

   * Comma-separated values (csv) format (``.csv``)

     On the **Samples** web page, click the |export-manifest-to-csv-format-button| button to download a manifest
     in csv format.

     See :ref:`How to access Samples web page <accessing-samples-web-page>` section for guidance.

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

   <hr>

.. _faq-sample-managers:

Sample Managers
--------------------

How can I be assigned as a sample manager?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * Make a request to the :email:`COPO team <ei.copo@earlham.ac.uk>` indicating the type of profile group
     that you would like to be assigned as a sample manager.

   * The permission will be granted after the request has been approved.

.. raw:: html

   <br>

How can I know if I have been assigned as a sample manager?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   * The |accept-reject-samples-navigation-button| button will be displayed on the web page.

   * The **accept/reject samples** web page will be displayed once the button is clicked.

   * Alternatively, if you can navigate to the `Accept/Reject Samples' web page <https://copo-project.org/copo/dtol_submission/accept_reject_sample>`__
     with an **Unauthorisation** error web page being displayed then, you are a sample manager.

.. raw:: html

   <br>

How can I accept or reject samples that users have submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. note::

      See :ref:`accessing-accept-reject-samples-web-page` section for guidelines on accessing the
      **Accept or Reject Samples** web page.


   See :ref:`accept-reject-samples` section for more information.

.. raw:: html

   <br>

How can I download sample manifests that have been submitted by manifest providers or sample submitters?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

  See :ref:`Downloading submitted sample manifest <samples-submission-download-sample-manifest-sample-managers>` section for more
  information.

.. raw:: html

   <br>

Can I download permits that users have uploaded in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Yes, on the **Accept or Reject Samples** web page, permits can be downloaded by selecting the desired sample record(s)
   then, clicking the |download-permits-button2| button on the web page.

   See :ref:`Downloading permits <permits-submission-download-permits-sample-managers>` section for more information.

.. raw:: html

   <br>

Can I view images that users have uploaded in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Yes, on the **Accept or Reject Samples** web page, images can be viewed by selecting the desired sample record(s)
   then, clicking the |view-images-button2| button on the web page.

   See :ref:`Viewing images <images-submission-view-images-sample-managers>` section for more information.

.. raw:: html

  <br>

.. _faq-sample-managers-within-several-manifest-groups:

If I belong to more than one sample manager manifest group, how can I view or accept samples that belong to them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   .. note::

      * The manifest dropdown menu will only be displayed on the **Accept or Reject samples** web page if you as a
        sample manager, belongs to more than one sample manager manifest group.

      * If the *dtol* sample manager group dropdown menu option is selected, both Aquatic Symbiosis Genomics (ASG)
        profiles and  Darwin Tree of Life (DToL) profiles will be displayed in the **All profiles** tab and/or
        **Profiles for My Sequencing Centre** the **Accept or Reject samples** web page will be displayed
        (if any exists).

   * Choose desired sample manager group from the manifest group dropdown menu.

   * Click the |accept-reject-samples-navigation-button| button to accept or reject samples.

     .. figure:: /assets/images/profile/profile_new_user_add_email_address_dialogue.png
        :alt: Add email address dialogue
        :align: center
        :class: with-shadow with-border

        **Accept or Reject samples: Email address prompt shown when a user logs into COPO for the first time**


   See :ref:`Viewing images <images-submission-view-images-sample-managers>` section for more information.

.. raw:: html

  <br>

.. _faq-sample-managers-sample-accept-reject-stage:

How do I know if a sample is awaiting acceptance or rejection?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   * On the **Accept or Reject Samples** web page, samples that are awaiting acceptance will be displayed
     in the **Pending** tab and samples that have been rejected will be displayed in the **Rejected** tab.

   * Samples in the **Rejected** tab can be re-accepted by selecting the desired sample record(s) then, clicking the
     |samples_accept_reject_button_accept| button. The samples will be displayed in the **Pending** tab.

   * If samples require more than one sample manager to accept or reject them, the samples will be displayed in the
     **Pending** tab until **all** sample managers have accepted them. Once all sample managers have accepted the
     samples, the samples will be displayed in the **Accepted** tab.

     As shown in the image below, sample records that are awaiting another acceptance will be highlighted **amber**
     or **yellow** and the date when the records have been accepted will be displayed in the **approval date** column
     in the samples data table.

     .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance.png
        :alt: Sample record awaiting another acceptance
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance.png
        :class: with-shadow with-border

        **Sample record awaiting another acceptance**

.. raw:: html

  <br>


How can I get a better view of sample record information displayed on the Accept or Reject Samples web page?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Click the |show-profile-panel-button| button to toggle the profile panel visibility on the
   **Accept or Reject Samples** web page to either hide the profile panel and view more sample records or show the
   profile panel to view more profiles.


.. raw:: html

  <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Compliance field`


..
    Images declaration
..

.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |accessions-dashboard-button| image:: /assets/images/buttons/dashboard_accessions_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |download-permits-button1| image:: /assets/images/buttons/permits_download_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |download-permits-button2| image:: /assets/images/buttons/permits_download_button2.png
   :height: 4ex
   :class: no-scaled-link

.. |export-manifest-to-csv-format-button| image:: /assets/images/buttons/samples_export_to_csv_format_button.png
   :height: 4ex
   :class: no-scaled-link

.. |navigate-to-top-button| image:: /assets/images/buttons/navigate_to_top_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-view-more-button| image:: /assets/images/buttons/profile_view_more_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link

.. |samples_accept_reject_button_accept| image:: /assets/images/buttons/samples_accept_reject_button_accept.png
   :height: 4ex
   :class: no-scaled-link

.. |show-profile-panel-button| image:: /assets/images/buttons/show_profile_panel_button.png
   :height: 4ex
   :class: no-scaled-link

.. |tol-dashboard-button| image:: /assets/images/buttons/dashboard_tol_button.png
   :height: 4ex
   :class: no-scaled-link

.. |tol-inspect-button| image:: /assets/images/buttons/tol_inspect_button.png
   :height: 4ex
   :class: no-scaled-link

.. |tol-inspect-by-gal-button| image:: /assets/images/buttons/tol_inspect_by_gal_button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits_upload_button.png
   :height: 4ex
   :class: no-scaled-link

.. |vertical-ellipsis-icon| image:: /assets/images/buttons/profile_vertical_ellipsis_icon.png
   :height: 4ex
   :class: no-scaled-link

.. |view-images-button1| image:: /assets/images/buttons/images_view_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |view-images-button2| image:: /assets/images/buttons/images_view_button2.png
   :height: 4ex
   :class: no-scaled-link