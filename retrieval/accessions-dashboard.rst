.. _accessions-dashboard:

=======================
Retrieving Accessions
=======================

Accepted submissions result in accessions being created for Tree of Life (ToL) [#f1]_ profiles while submissions under
Genomics profiles, undergo the same process.

Accessions can be explored via the following:

   * Within the data table on the web page after submissions are made. View the list of accession types below to see
     the types of accessions created. Each type corresponds to a column in the data table where the accessions are
     displayed.

   * Accessions web page for the desired profile (accessible via the :ref:`Accessions component <accessions-component>`
     attached to the profile in COPO)

   * `Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__

   The accessions can be viewed immediately after submissions are accepted under :abbr:`ToL(Tree of Life)` profiles
   and immediately after profiles are released under Genomics profiles via the following:

      * `ENA browser <https://www.ebi.ac.uk/ena/browser/home>`__  [#f2]_

      * `NCBI BioSample <https://www.ncbi.nlm.nih.gov/biosample>`__  [#f3]_

The types of accessions that are created are:

* Genomics submissions
   * Assembly accessions
   * Experiment accessions
   * Run accessions
   * Sample accessions
   * Sequence annotation accessions
   * Study accessions

* :abbr:`ToL (Tree of Life)` [#f1]_ submissions
   * Biosample accessions
   * SRA accessions
   * Submission accessions

.. figure:: /assets/images/accessions/accessions_genomics_profile_in_table_after_submission.png
      :alt: Accessions in data table after submission
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/accessions/accessions_genomics_profile_in_table_after_submission.png
      :class: with-shadow with-border

      **Genomics profile: Reads webpage displaying accessions in the data table after submission**

.. raw:: html

       <br>

.. figure:: /assets/images/dashboard/dashboard_accessions_other_accessions.png
      :alt: Other accessions
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/dashboard/dashboard_accessions_other_accessions.png
      :class: with-shadow with-border

      **Accessions Dashboard: Other accessions**

.. raw:: html

       <br>

.. figure:: /assets/images/dashboard/dashboard_accessions_sample_accessions.png
      :alt: Genomics projects' accessions
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/dashboard/dashboard_accessions_sample_accessions.png
      :class: with-shadow with-border

      **Accessions Dashboard: Sample accessions**

.. raw:: html

       <br>

.. note::

    * The |accept-reject-samples-navigation-button| button will only appear on the web page if you
      are granted permission to be a sample manager.

.. seealso::

  * :ref:`Genomics profile components <genomics-profile-components>`
  * :ref:`ToL profile components <tol-profile-components>`
  * :ref:`Accessions profile component <accessions-component>`


.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`
.. [#f2] See term: :term:`ENA`
.. [#f3] See term: :term:`NCBI`



..
    Images declaration
..
.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link