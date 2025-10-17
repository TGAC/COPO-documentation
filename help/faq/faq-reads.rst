.. _faq-reads:

Reads
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

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

     .. figure:: /assets/images/reads/ui/reads_manifest_paired.png
        :alt: Reads manifest for paired reads
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/ui/reads_manifest_paired.png
        :class: with-shadow with-border

        **Reads manifest for paired reads**

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

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link