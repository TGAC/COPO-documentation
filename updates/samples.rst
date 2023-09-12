.. _samples_update:

==============================
Updating Samples
==============================

Samples can be updated by reuploading/resubmitting the manifest that was used to create them with the amended changes
**before** or **after** the samples have been accepted by a sample manager and submitted to
:abbr:`ENA (European Nucleotide Archive)` [#f1]_.

Please note that not all field values of existing samples can be updated via the manifest resubmission update method.
The fields that can be updated with that method are listed below.

.. hint::

   Collapse the list of fields that can be updated by for instance, clicking the **List of ASG project fields that
   can be updated** item below.

.. note::

   * The manifest must be uploaded again with the amendments included for the change or update to occur.

   * You **cannot** reupload a manifest with some of the existing samples removed. The removed samples
     (from the reuploaded manifest) will not be automatically removed from the manifest sample record. If you would
     like existing samples to be removed or deleted from the manifest record, please contact
     :email:`COPO team <ei.copo@earlham.ac.uk>` for assistance detailing the profile title and reason for the
     removal.

   * Fields are also referred to as columns in the manifest.

.. collapse:: List of ASG project fields that can be updated

   .. hlist::
      :columns: 2

      * BARCODE_HUB
      * BARCODE_PLATE_PRESERVATIVE
      * COLLECTOR_SAMPLE_ID
      * CULTURE_OR_STRAIN_ID
      * DATE_OF_PRESERVATION
      * DEPTH
      * DIFFICULT_OR_HIGH_PRIORITY_SAMPLE
      * ELEVATION
      * HAZARD_GROUP
      * IDENTIFIED_BY
      * IDENTIFIED_HOW
      * IDENTIFIER_AFFILIATION
      * INFRASPECIFIC_EPITHET
      * LIFESTAGE
      * PARTNER_SAMPLE_ID
      * PLATE_ID_FOR_BARCODING
      * PRESERVED_BY
      * PRESERVER_AFFILIATION
      * PURPOSE_OF_SPECIMEN
      * RELATIONSHIP
      * SEX
      * SIZE_OF_TISSUE_IN_TUBE
      * SPECIMEN_ID_RISK
      * TIME_ELAPSED_FROM_COLLECTION_TO_PRESERVATION
      * TIME_OF_COLLECTION
      * TISSUE_FOR_BARCODING
      * TISSUE_REMOVED_FOR_BARCODING
      * TUBE_OR_WELL_ID_FOR_BARCODING
      * VOUCHER_ID

.. raw:: html

   <br>

.. collapse:: List of DTOL project fields that can be updated

   .. hlist::
      :columns: 2

      * BARCODE_HUB
      * BARCODE_PLATE_PRESERVATIVE
      * COLLECTOR_SAMPLE_ID
      * CULTURE_OR_STRAIN_ID
      * DATE_OF_PRESERVATION
      * DEPTH
      * DIFFICULT_OR_HIGH_PRIORITY_SAMPLE
      * ELEVATION
      * GAL_SAMPLE_ID
      * HAZARD_GROUP
      * IDENTIFIED_BY
      * IDENTIFIED_HOW
      * IDENTIFIER_AFFILIATION
      * INFRASPECIFIC_EPITHET
      * LIFESTAGE
      * PLATE_ID_FOR_BARCODING
      * PRESERVED_BY
      * PRESERVER_AFFILIATION
      * PURPOSE_OF_SPECIMEN
      * RELATIONSHIP
      * SEX
      * SIZE_OF_TISSUE_IN_TUBE
      * SPECIMEN_IDENTITY_RISK
      * TIME_ELAPSED_FROM_COLLECTION_TO_PRESERVATION
      * TIME_OF_COLLECTION
      * TISSUE_FOR_BARCODING
      * TISSUE_REMOVED_FOR_BARCODING
      * TUBE_OR_WELL_ID_FOR_BARCODING
      * VOUCHER_ID

.. raw:: html

   <br>

.. collapse:: List of ERGA project fields that can be updated

   .. hlist::
      :columns: 1

      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_CONTACT
      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_OR_BIOCULTURAL_PROJECT_ID
      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_OR_BIOCULTURAL_RIGHTS_APPLICABLE
      * BARCODE_HUB
      * BARCODE_PLATE_PRESERVATIVE
      * COLLECTED_BY
      * COLLECTION_LOCATION
      * COLLECTOR_AFFILIATION
      * COLLECTOR_SAMPLE_ID
      * COMMON_NAME
      * CULTURE_OR_STRAIN_ID
      * DATE_OF_COLLECTION
      * DATE_OF_PRESERVATION
      * DECIMAL_LATITUDE
      * DECIMAL_LONGITUDE
      * DEPTH
      * DESCRIPTION_OF_COLLECTION_METHOD
      * DIFFICULT_OR_HIGH_PRIORITY_SAMPLE
      * DNA_REMOVED_FOR_BIOBANKING
      * DNA_VOUCHER_FOR_BIOBANKING
      * ELEVATION
      * ETHICS_PERMITS_DEF
      * ETHICS_PERMITS_FILENAME
      * ETHICS_PERMITS_REQUIRED
      * FAMILY
      * GAL
      * GAL_SAMPLE_ID
      * GENUS
      * GRID_REFERENCE
      * HABITAT
      * HAZARD_GROUP
      * IDENTIFIED_BY
      * IDENTIFIED_HOW
      * IDENTIFIER_AFFILIATION
      * IDENTIFIER_AFFILIATION
      * INDIGENOUS_RIGHTS_APPLICABLE
      * INDIGENOUS_RIGHTS_DEF
      * INDIGENOUS_RIGHTS_DEF
      * INFRASPECIFIC_EPITHET
      * LIFESTAGE
      * NAGOYA_PERMITS_DEF
      * NAGOYA_PERMITS_FILENAME
      * NAGOYA_PERMITS_REQUIRED
      * ORDER_OR_GROUP
      * ORGANISM_PART
      * ORIGINAL_COLLECTION_DATE
      * ORIGINAL_GEOGRAPHIC_LOCATION
      * OTHER_INFORMATION
      * PRESERVATION_APPROACH
      * PRESERVATIVE_SOLUTION
      * PRESERVED_BY
      * PRESERVER_AFFILIATION
      * PURPOSE_OF_SPECIMEN
      * REGULATORY_COMPLIANCE
      * RELATIONSHIP
      * SAMPLE_COORDINATOR
      * SAMPLE_COORDINATOR_AFFILIATION
      * SAMPLE_COORDINATOR_ORCID_ID
      * SAMPLING_PERMITS_FILENAME
      * SAMPLING_PERMITS_REQUIRED
      * SCIENTIFIC_NAME
      * SEX
      * SIZE_OF_TISSUE_IN_TUBE
      * SPECIMEN_IDENTITY_RISK
      * TAXON_ID
      * TAXON_REMARKS
      * TIME_ELAPSED_FROM_COLLECTION_TO_PRESERVATION
      * TIME_OF_COLLECTION
      * TISSUE_FOR_BARCODING
      * TISSUE_FOR_BIOBANKING
      * TISSUE_REMOVED_FOR_BARCODING
      * TISSUE_REMOVED_FOR_BIOBANKING
      * TISSUE_REMOVED_FROM_BARCODING
      * TISSUE_VOUCHER_ID_FOR_BIOBANKING
      * TUBE_OR_WELL_ID_FOR_BARCODING
      * VOUCHER_ID

.. raw:: html

   <br>
   <hr>

Updating Taxonomy
---------------------------

To update the scientific name for a sample, please make an email request to the
:email:`COPO team <ei.copo@earlham.ac.uk>` providing the **biosampleAccession** and the new **SCIENTIFIC_NAME** to be
updated.

.. note::

   * The new value for the **SCIENTIFIC_NAME** field must be a valid scientific name and must be present in the NCBI
     [#f2]_ Taxonomy database.
   * ``<biosampleAccession>`` is the unique identifier for the sample in ENA.
   * ``<SCIENTIFIC_NAME>`` is the new scientific name for the sample.

Please make the request in the following format:

.. code-block:: none
   :caption: Format to make scientific name update

   <biosampleAccession>:<SCIENTIFIC_NAME>


.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`ENA`.
.. [#f2] See term: :term:`NCBI`.
.. [#f3] See term: :term:`ASG`.
.. [#f4] See term: :term:`DTOL`.
.. [#f5] See term: :term:`ERGA`.