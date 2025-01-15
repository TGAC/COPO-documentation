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

How can I assign a locus tag to assemblies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_add_form_profile_form_locus_tag.png
     :class: with-shadow with-border
     :height: 400px

     **Profile form: Adding locus tag**

  If a locus tag is not assigned, :abbr:`ENA (European Nucleotide Archive)` will automatically assign a locus
  tag to your assembly after it has been submitted in COPO and deposited to ENA.

  See `ENA's documentation <https://ena-docs.readthedocs.io/en/latest/faq/locus_tags.html#what-are-locus-tags>`_
  for more details. The documentation outlines rules that the locus tag prefix should conform to.

.. raw:: html

  <br>

How do I determine which SAMPLE accession to choose from the SAMPLE dropdown menu in the ‘Add Assembly’ form for my project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  .. hint::

     When submitting assemblies, the sample accession, also known as **sraAccession**, follow the format,
     ``ERSXXXXXXXX``.

  * The **SAMPLE** dropdown menu in the **Add Assembly** form will display the sraAccession(s) that are associated
    with samples that have been submitted in COPO.

  * The sraAccession will be displayed in the **sraAccession** column in any data table that is associated with
    the profile and samples. In terms of assembly submission, the sraAccession will be displayed in the data table on
    the **Reads** web page (once reads have been submitted).

.. raw:: html

  <br>

.. _faq-assemblies-simultaneous-submission:

Are assemblies and sequence annotations submitted at the same time in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, assemblies and sequence annotations are submitted separately in COPO.

   It is possible that the notion of `simultaneous submission` arises from the use of the
   :abbr:`EMBL (and sequence annotations submitted at the)` flat file format, which combines both annotated assemblies
   and sequence annotations. This may lead to the impression of a simultaneous submission.

   If you are submitting sequence annotations directly to the :abbr:`ENA (European Nucleotide Archive)`, EMBL files
   must be used, as they include both assemblies and annotations together.

   On the other hand, sequence annotations can be submitted separately to ENA if your data files are in formats such as
   ``.gff`` or ``.fasta``.

   .. note::

     File submissions depend on how users prepare and generate their data. For instance, :abbr:`FASTA (Fast-All)` files
     are still essential for storing and sharing sequence data but, they are not sufficient for representing detailed
     genomic annotations.

     For annotation tasks, formats like :abbr:`GFF (General feature format)`, :abbr:`GTF (Gene transfer format)`
     and :abbr:`BED (Browser Extensible Data)` are more appropriate because they provide structured information
     about genomic features, gene structures and functional elements. Thus, while FASTA is not outdated, it is often
     used alongside more specialised formats for annotation purposes.

   Please refer to the following sections in ENA's documentation for more information:

    * `Analysis File Groups <https://ena-docs.readthedocs.io/en/latest/submit/analyses.html#analysis-file-groups>`__

    * `Files Required for Genome Assembly Submissions <https://ena-docs.readthedocs.io/en/latest/submit/assembly.html#files-for-genome-assembly-submissions>`__

.. raw:: html

  <br>


Are accessions assigned in assembly submissions after studies are released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after assembly submissions are done in COPO.

   The study release only makes the submissions public and available for viewing on repositories such as the
   `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`__ and
   `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__.

   See the :ref:`accessions-dashboard` section for more information.

.. raw:: html

  <br>

Dashboard
--------------------

.. _faq-dashboard-accessions-dashboard:

How can I view accessions after a metadata submission is made in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

  **Option 1**: View accessions in the data table
     Scroll to any column that ends with ``accession`` as depicted in the image below to view the accessions.

     .. note::

        The table row is highlighted in red in the image below because the files associated with the
        record are either still being processed or have encountered issues during processing.

     .. figure:: /assets/images/reads/reads_table_showing_accessions.png
        :alt: Accessions column in the data table
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_table_showing_accessions.png
        :class: with-shadow with-border
        :height: 300px

        **Accessions column in the data table**

  **Option 2**: Accessions web page
     * Click the |accessions-icon| button.

     * The accessions web page will be displayed.

  **Option 3**: Accessions dashboard
     Navigate to the `Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__ to view
     accessions

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

.. _faq-files:

Files
--------------------

How do I know when data files that have been uploaded to COPO are public at European Nucleotide Archive (ENA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`files-ena-file-processing-status` section for more information.

.. raw:: html

   <br>

Why can't I upload more data files in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   .. note::

      The total **maximum** file size that can be uploaded from your local (computer) system is around **2 GB**. If you
      have a file larger than 2 GB or have multiple files whose combined total size exceeds 2 GB, please
      :ref:`submit the file(s) via the terminal <files-submission-via-terminal>`.

   If you cannot upload new files to COPO on the **Files** web page, it is likely that you have reached the maximum
   number of data files that can be uploaded.

   Please delete some files to free up space for new files.

.. raw:: html

   <hr>

.. _faq-images:

Images
--------

How can I submit images in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Please see the :ref:`images-submission` section for guidance on how to submit images in COPO.

.. raw:: html

   <br

.. _faq-images-submission-errors:

What are the factors that can lead to errors during the image upload process in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. note::

      * Images can only be submitted after samples have been uploaded in the **Upload Sample Spreadsheet** dialog. The
        max total image size should be no more than 2GB.

      * Images can only be submitted via a ToL [#f1]_ profile. Please see:
        :ref:`Steps to Create a Tree of Life Profile <tol-profile-walkthrough>` for guidance.

      * The file name of sample images must be named as ``{Specimen_ID}-{n}.[jpg|png]`` where ``{n}`` is the image number,
        ``{Specimen_ID}`` is the specimen ID of the sample in the manifest and ``jpg`` or ``png`` is the extension of the file.

   .. important::

      The |upload-images-button| button will only be enabled after you upload a manifest in the
      **Upload Sample Spreadsheet** dialog. This process must be completed in one go; you cannot close the dialog and
      return later to upload images. The images rely on metadata from the sample manifest, so the |upload-images-button|
      button becomes active immediately after the manifest is uploaded, allowing you to add images in the same session.

   Errors occur due to several reasons. An error message will be displayed detailing the issue(s) encountered and
   potential resolution(s). If you are uncertain how to proceed, please contact the
   :email:`COPO team <ei.copo@earlham.ac.uk>`.

   Other potential reasons and solutions for errors include but are not limited to:

      * Uploading images where the total size of the images exceeds **2GB** (the maximum allowable file size) may
        result in errors.

        Common web browser error messages include ``Error 0: error`` though the specific message may vary by browser,
        as the error is browser-generated.

        **Workaround**: Upload smaller batches of images separately. You will need to first upload the manifest, any
        applicable permits, and then upload the images in batches, as images cannot be uploaded directly and all at
        once.

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
             :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/logos/copo_logo_old.png
             :class: with-shadow with-border
        - .. figure:: /assets/logos/copo_logo_new.png
             :height: 12ex
             :alt: COPO logo during the years 2023 - PRESENT
             :align: center
             :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/logos/copo_logo_new.png
             :class: with-shadow with-border

   .. seealso::

     * :download:`Download a seminar presentation <../assets/files/presentations/EI_Seminar_23042024_Advancing_Biodiversity_Research_The_Evolution_of_COPO.pptx>`
       which gives an overview of the evolution of the COPO project since its inception in 2014 to the present day

.. raw:: html

   <br>


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

   * The permit file name provided in the manifest does not end with the extension ``.pdf`` or ``.PDF``

     **Resolution**: Rename the name of the permit file so that it ends with the extension, ``.pdf`` or ``.PDF`` then,
     reupload the manifest

   * In the uploaded manifest, different permit file names are associated with the same **SPECIMEN_ID**

     **Resolution**: Provide a unique permit file name for each **SPECIMEN_ID** or provide the same file name for
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

   * The permit file name uploaded from your local system actually ends with ``.pdf.pdf`` (or ``.PDF.PDF``) and not
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
         :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_add_form.png
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
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_form_associated_types.png
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
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_view_more_button_with_popup_displayed.png
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

.. _faq-profiles-releasing-profiles:

How can I make profiles or projects public or visible in European Nucleotide Archive (ENA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      Profiles (in COPO) are referred to as projects or studies (in :abbr:`ENA (European Nucleotide Archive)`).

   See :ref:`releasing-profiles` section for more information.
.. raw:: html

   <br>

.. _faq-profiles-releasing-profiles-set-release-date:

How can I set the release date for public profiles or projects after having submitted reads?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      Profiles (in COPO) are referred to as projects or studies (in :abbr:`ENA (European Nucleotide Archive)`).

   It is not possible to set the release date for profiles or projects after reads have been submitted.

   By default, once reads are submitted, the project is private and the release date is set to two years from
   the submission date.

   You can, however, make the project public at any time before the release date by following the steps below or refer
   to the :ref:`releasing-profiles` section to make the profile public at any time after the submission.

.. raw:: html

   <br>

.. _faq-profiles-view-released-studies:

How can I view released studies on European Nucleotide Archive (ENA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      Profiles (in COPO) are referred to as projects or studies (in :abbr:`ENA (European Nucleotide Archive)`).

   If you know the project accession and/or profile title, you can find the corresponding project on the
   `Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__. By clicking the hyperlink
   associated with the project accession, you will be navigated to the associated study record on
   :abbr:`ENA (European Nucleotide Archive)`.

   .. seealso::

        :ref:`Retrieving accessions <accessions-dashboard>` section for more information.

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
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/reads_manifest_paired.png
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

   <br>


Which reads checklist from the dropdown menu on the Reads web page is associated with samples?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   The reads checklist associated with samples in the dropdown menu on the **Reads** web page is marked with an
   asterisk (*) and is selected by default when the page loads.

.. raw:: html

   <br>

.. _faq-reads-update-errors:

What are the factors that lead to errors during the reads update process in the COPO project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse:: Click to view answer

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They both refer to a spreadsheet.

   Errors occur due to several reasons. An error message will be displayed detailing the issue(s) encountered and
   potential resolution(s). If you are uncertain how to proceed, please contact the
   :email:`COPO team <ei.copo@earlham.ac.uk>`.

   Updates to reads can be made by uploading the amended manifest to the same checklist and profile initially used
   for the submission. Please note that this is possible if the values in the ``Sample``, ``File checksum``,
   ``File name`` and ``Library layout`` columns remain unchanged in the manifest. If any of these values change, errors
   will occur during the update process.

   This is because the value in the ``Sample`` column serves as the key for each row in the **Reads**
   manifest. Each unique sample in the manifest corresponds to a different biosample, which is linked to the values in
   the ``File checksum``, ``File name`` and ``Library layout`` columns.

   Other potential reasons for errors include but are not limited to:

      * Uploading null or empty files and associating them with rows in the manifest

      * Assigning files to samples that already have the same files attached will produce errors

.. raw:: html

  <br>

Are accessions assigned in reads submissions after studies are released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after reads submissions are done in COPO.

   The study release only makes the submissions public and available for viewing on repositories such as the
   `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`__ and
   `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__.

   See the :ref:`accessions-dashboard` section for more information.

.. raw:: html

   <hr>

Samples
--------------------

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

   <hr>

.. _faq-samples-submission-public-availability:

What are the steps for submitting metadata in COPO and ensuring it appears in public repositories?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

      * Refer to the :ref:`getting-started-accessing-copo-website` section for guidance.

      .. raw:: html

         <br>

   #. Create a profile.

      * For more information, check the :ref:`Steps to Create a Tree of Life Profile <tol-profile-walkthrough>` section.

      .. raw:: html

         <br>

   #. Click the **Components** button attached to the created profile

      * See the :ref:`accessing-samples-web-page` section for additional information.

      .. raw:: html

         <br>

   #. Upload the completed manifest

      Visit the :ref:`samples-submission` section for guidance on submitting samples.

      .. note::

         Choose the desired type of submission listed in that section to be directed to the page for submitting
         the manifest of that type.

   #. COPO will validate the uploaded manifest then, display any errors and/or warnings and provide messages to
      help resolve them.

      If you encounter errors that you are unable resolve, we are happy to assist. Contact the :email:`COPO team
      <ei.copo@earlham.ac.uk>` detailing the issue(s) encountered.

      .. raw:: html

         <br>

   #. If applicable, upload :ref:`permits <permits-submission>` and/or :ref:`images <images-submission>` after
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

How can I search for a particular profile or sample on the Accept or reject web page?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   See :ref:`accept-reject-samples-query-profiles-and-samples` section for guidelines on querying profiles and sample
   records on the **Accept or Reject Samples** web page.

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

     .. figure:: /assets/images/profile/profile_new_user_add_email_address_dialog.png
        :alt: Add email address dialog
        :align: center
        :class: with-shadow with-border

        **Accept or Reject samples: Email address prompt shown when a user logs into COPO for the first time**


   See :ref:`Viewing images <images-submission-view-images-sample-managers>` section for more information.

.. raw:: html

  <br>

.. _faq-sample-managers-samples-awaiting-another-review:

How can I tell if sample records are still awaiting review by another sample manager?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   * If samples require more than one sample manager to accept or reject them, the samples will be displayed in the
     **Pending Samples** tab until **all** sample managers have accepted them. Once all sample managers have accepted
     the samples, the samples will be displayed in the **Accepted Samples** tab.

     As shown in the image below, sample records that are awaiting another acceptance will be highlighted
     **yellow** or **amber** and the date when the records have been accepted will be displayed in the
     **Approval Date** column in the samples data table.

     Refer to the **Associated TOL (Tree of life) Project** column to view the associated project(s) that the sample
     record belongs to. See the image below for an illustration.

     .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance1.png
        :alt: Sample record awaiting another acceptance
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance1.png
        :class: with-shadow with-border

        **Sample record highlighted in yellow awaiting another acceptance**

     .. raw:: html

        <br>

     .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance2.png
        :alt: Sample record awaiting another acceptance
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_awaiting_another_acceptance2.png
        :class: with-shadow with-border

        **Approval date displayed in the 'Approval Date' column of the samples data table**

     In the example above, the sample record is associated with both :abbr:`BGE (Biodiversity Genomics Europe)` and
     SANGER (Sanger Institute) (associated) project types. A :abbr:`BGE (Biodiversity Genomics Europe)` sample manager
     has accepted the sample record, which is reflected in the **Approval Date** column in the data table. The record
     is highlighted in yellow to indicate that it is still awaiting acceptance from another sample manager.

     .. raw:: html

        <br>

     .. hint::

        * The **Approval Date** column displays the date when the sample record was accepted by the sample manager as
          well as the associated project that the sample manager belongs to.

        * The **Associated TOL (Tree of life) Project** column displays the associated project that the sample record
          belongs to.

     After the sample record has been accepted by all sample managers, the sample record will be displayed in the
     **Accepted Samples** tab as shown in the image below.

     .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_after_all_accepted1.png
        :alt: Sample record after all sample managers have accepted it
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_after_all_accepted1.png
        :class: with-shadow with-border

        **Sample record after all sample managers have accepted it**

     .. raw:: html

        <br>

     .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_after_all_accepted2.png
        :alt: Updated approval date in the 'Approval Date' column of the samples data table
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_after_all_accepted2.png
        :class: with-shadow with-border

        **Approval date updated in the 'Approval Date' column of the samples data table**

     In the example above, the sample record is associated with two projects:
     :abbr:`BGE (Biodiversity Genomics Europe)` and SANGER (Sanger Institute), as shown in the
     **Associated TOL (Tree of Life) Project** column. The sample managers assigned to both associated project types have
     approved the sample record and the **Approval Date** column has been updated in the samples data table.

.. raw:: html

  <br>

How to check the status of samples that have been accepted or rejected as a sample manager?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   **Option 1**: Accepted samples can be viewed in the **Accepted Samples** tab while rejected samples can be found in
   the **Rejected Samples** tab on the **Accept or Reject Samples** web page.

   **Option 2**: The **Status** column in the samples data table will display the status of the sample record.

   **Option 3**: The **Error** column in the samples data table will display an error message if the sample record
   has been rejected or if there are any errors associated with the sample record.

   **Option 4**: The **Status** log will display a chronological list of the status of the sample record as shown in the
   images below. It is located on the right of the **Accept or Reject Samples** web page below the top navigation bar.

   .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_status_log_collapsed.png
      :alt: Sample record status log collapsed
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_status_log_collapsed.png
      :class: with-shadow with-border
      :height: 200px

      **Sample record status log collapsed**

   .. raw:: html

      <br>

   .. figure:: /assets/images/samples_accept_reject/samples_accept_reject_status_log_expanded.png
      :alt: Sample record status log expanded
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples_accept_reject/samples_accept_reject_status_log_expanded.png
      :class: with-shadow with-border
      :height: 600px


      **Sample record status log expanded on hover**

   .. hint::

      If you hover over the **Status** log, it will expand to display more information about the status of the sample
      record.

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

   <hr>

Sequence Annotations
--------------------

How do I determine which SAMPLE accession to choose from the SAMPLE dropdown menu in the ‘Add Sequence Annotation’ form for my project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  .. hint::

     When submitting sequence annotations (also known as tagged sequences), the sample accession, also known as
     **sraAccession**, follow the format, ``ERSXXXXXXXX``.

  * The **SAMPLE** dropdown menu in the **Add Sequence Annotation** form will display the sraAccession(s) that are
    associated with samples that have been submitted in COPO.

  * The sraAccession can be found in the **sraAccession** column in any data table that is associated with
    the profile and samples. In terms of sequence annotation submission, the sraAccession will be displayed in the
    data table on the **Reads** web page (once reads have been submitted).

.. raw:: html

  <br>

Are sequence annotations and assemblies submitted at the same time in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See answer :ref:`here <faq-assemblies-simultaneous-submission>`

.. raw:: html

  <br>

Are accessions assigned in sequence annotation submissions after studies are released?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

   No, accessions are assigned after sequence annotation submissions are done in COPO.

   The study release only makes the submissions public and available for viewing on repositories such as the
   `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`__ and
   `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__.

   See the :ref:`accessions-dashboard` section for more information.

.. raw:: html

   <br><hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Compliance field`


..
    Images declaration
..

.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |accessions-icon| image:: /assets/images/buttons/components_accessions_icon.png
   :height: 4ex
   :class: no-scaled-link

.. |add-profile-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/buttons/samples_download_manifest_button.png
   :height: 4ex
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

.. |upload-images-button| image:: /assets/images/buttons/images_upload_button.png
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