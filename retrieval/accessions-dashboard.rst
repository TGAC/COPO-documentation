.. _accessions-dashboard:

=======================
Retrieving Accessions
=======================

Accepted and submitted items are assigned unique identifiers known as an accessions.

Submissions linked to accessions become publicly visible immediately after sample submission acceptance for Tree of
Life (ToL) [#f1]_ profiles and after profile release for Genomics profiles (see
:ref:`releasing-profiles` for more information). The submissions can then be viewed via the platforms -
`ENA browser <https://www.ebi.ac.uk/ena/browser/home>`__  [#f2]_ or
`NCBI BioSample <https://www.ncbi.nlm.nih.gov/biosample>`__  [#f3]_ using the assigned accessions.

The type of accession assigned depends on the type of submission made. The following are different kinds of
accessions that can be assigned after successful submissions:

* Assembly
* Biosample
* Experiment
* Run
* Sequence annotation
* Study
* SRA
* Submission

.. tip::

   For sample submissions within a Tree of Life profile, the **Approval Date** column in the sample data table indicates
   when the submission was approved and which project the approving sample manger belongs to.

   The **Status** column indicates the current status of the submission. Once the submission is approved and
   has been successful, the status will be marked as **accepted**.

Accessions can be explored through the following ways:

.. note::

   Please noe that the |accept-reject-samples-navigation-button| button will only appear on a web page if you
   are granted permission to be a sample manager.

Within the data table
---------------------

After submissions have been successfully made, the accessions can be found within the data table on the respective
submission web page. For example:

.. figure:: /assets/images/accessions/ui/accessions_genomics_profile_in_table_after_submission.png
   :alt: Accessions in data table after submission for a Genomics profile
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/accessions/ui/accessions_genomics_profile_in_table_after_submission.png
   :class: with-shadow with-border

   **Reads webpage displaying accessions in the data table after submission**

.. raw:: html

   <br>

.. figure:: /assets/images/accessions/ui/accessions_tol_profile_in_table_after_submission.png
   :alt: Accessions in data table after submission for a Tree of Life profile
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/accessions/ui/accessions_tol_profile_in_table_after_submission.png
   :class: with-shadow with-border

   **Samples (under a Tree of Life profile) webpage displaying accessions in the data table after submission**

On Profile's Accessions Web Page
--------------------------------

Navigate to the Accessions web page for a desired profile (accessible via the
:ref:`Accessions component <accessions-component>`) to view all accessions associated with the profile's submissions.

On Accessions Dashboard
-----------------------

`Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__

.. figure:: /assets/images/dashboard/ui/dashboard_accessions_other_accessions.png
   :alt: Other accessions
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/dashboard/ui/dashboard_accessions_other_accessions.png
   :class: with-shadow with-border

   **Accessions Dashboard: Other accessions**

.. raw:: html

   <br>

.. figure:: /assets/images/dashboard/ui/dashboard_accessions_sample_accessions.png
   :alt: Genomics projects' accessions
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/dashboard/ui/dashboard_accessions_sample_accessions.png
   :class: with-shadow with-border

   **Accessions Dashboard: Sample accessions**

.. raw:: html

   <hr>

Related Topics
---------------

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
.. |accept-reject-samples-navigation-button| image:: /assets/images/samples/accept_reject_samples/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link