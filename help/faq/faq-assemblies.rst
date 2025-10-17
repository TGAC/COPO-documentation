.. _faq-assemblies:

Assemblies
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

.. _faq-assemblies-submission-file-types:

What are the types of files that are required for assembly submissions in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

  .. figure:: /assets/images/profiles/ui/profile_add_form_profile_form_locus_tag.png
     :alt: Adding locus tag to a profile
     :align: center
     :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profiles/ui/profile_add_form_profile_form_locus_tag.png
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

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link