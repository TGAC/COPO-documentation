.. _faq-general:

General
-------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

What is COPO?
~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   COPO standards for Collaborative OPen Omics. It is a web-based platform that helps the scientific
   community describe their research data using :abbr:`FAIR (Findable, Accessible, Interoperable, and Reusable)`
   community standards and share it with appropriate public repositories. It is an open-source project based at the
   `Earlham Institute (EI) <https://www.earlham.ac.uk>`__ formerly known as :abbr:`TGAC (The Genome Analysis Centre)`
   in Norwich, United Kingdom.

   COPO simplifies the process of preparing, validating and submitting research metadata, making it easier for
   persons to comply with data sharing requirements and promote open science.

    COPO supports a variety of data types, including genomic sequences, phenotypic data, and ecological observations.
    It provides tools for metadata annotation, data validation, and submission to repositories such as the
    European Nucleotide Archive (ENA), the Open Science Framework (OSF), and Dataverse among others.

.. raw:: html

   <br>


What type of data can be submitted using COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   The Collaborative OPen Omics (COPO) project supports the following types of omics data:

    * :ref:`Assemblies <assemblies>` (e.g. FASTA)
    * :ref:`Barcoding <barcoding-manifest-submissions>` (e.g. 10x Genomics, PacBio)
    * :ref:`Images <image-submission>` (e.g. :abbr:`REMBI (Recommended Metadata for Biological Images)`,
      :abbr:`ST-FISH (Spatial Transcriptomics Fluorescence In Situ Hybridisation)`)
    * :ref:`Reads <reads>` (e.g. Illumina, Oxford Nanopore Technologies, PacBio)
    * :ref:`Samples <samples-submission>` (e.g. Tree of Life, :abbr:`DwC (Darwin Core)`,
      :abbr:`MIxS (Minimum Information about any, (x) Sequence)`,
      :abbr:`FAANG (Functional Annotation of Animal Genomes)`)
    * :ref:`Sequence Annotations <sequence-annotations>` (e.g., GFF3, VCF)
    * :ref:`Single-cell <single-cell-submissions>` (e.g. 10x Genomics, Smart-seq)

   In addition, COPO supports the submission of associated data files. See :ref:`files` for more information.

   .. seealso::

      :ref:`Public Repositories for COPO Data Submissions <faq-public-repositories>`

.. raw:: html

   <br>

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

     * :download:`Download a seminar presentation </assets/files/presentations/EI_Seminar_23042024_Advancing_Biodiversity_Research_The_Evolution_of_COPO.pptx>`
       which gives an overview of the evolution of the COPO project since its inception in 2014 to the present day

.. raw:: html

   <br>


Who are the developers of the COPO project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Please see `COPO team <https://copo-project.org/about/#project-team-section-current>`__ section on the **About** web
   page of the COPO's website for current software developers of the project.

.. raw:: html

   <br>

How can I contact the COPO team?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   You can contact the COPO team by sending an email to :email:`ei.copo@earlham.ac.uk` or by using the contact form on
   the `Contact <https://copo-project.org/contact/>`__ page of the COPO's website.

.. raw:: html

   <br>

Is there an API for COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Yes, COPO provides a :abbr:`RESTful (REpresentational State Transfer ful)` :term:`API` that allows programmatic
   access to its features and functionalities.

   For more information, please refer to the :ref:`Using COPO API documentation <copo-api>`.

.. raw:: html

   <br>

Does COPO have a testing website?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   Yes, COPO has a testing website that users can explore features and functionalities before performing actual
   submissions. It can be accessed at `<https://demo.copo-project.org>`__.

   Any data submitted via this testing site is not submitted to any public repositories and is deleted after 24 hours.

.. raw:: html

   <br>

.. _faq-public-repositories:

Which public repositories does COPO submit data to?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   COPO submits data to the following public repositories:

   * `Biostudies <https://www.ebi.ac.uk/biostudies/>`__ in care of
     `BioImage Archive (BIA) <https://www.ebi.ac.uk/bioimage-archive/>`__
   * `European Nucleotide Archive (ENA) <https://www.ebi.ac.uk/ena/browser/home>`__
   * `Zenodo <https://zenodo.org/>`__

   .. list-table:: Data Submission Types and Repositories
      :width: 100%
      :align: center
      :header-rows: 1

      * - Submission type
        - Public repository
      * - Assemblies
        - ENA
      * - Barcoding (also known as Tagged sequences)
        - ENA
      * - Images
        - Zenodo (for :abbr:`REMBI (Recommended Metadata for Biological Images)` images,
          :abbr:`ST-FISH (Spatial Transcriptomics Fluorescence In Situ Hybridisation)`),
          :abbr:`BIA (BioImage Archive)` (for samples images, REMBI images (forthcoming))
      * - Reads
        - ENA
      * - Samples
        - ENA
      * - Sequence Annotations
        - ENA
      * - Single-cell
        - ENA


.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link