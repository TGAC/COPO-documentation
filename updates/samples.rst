.. _samples-update:

=================
Updating Samples
=================

Samples can be updated by reuploading/resubmitting the manifest that was used to create them with the amended changes
**before** or **after** the samples have been accepted by a sample manager and submitted to
:abbr:`ENA (European Nucleotide Archive)` [#f1]_.

Please note that not all field values of existing samples can be updated via the manifest resubmission update method.
The fields that can be updated with that method are listed below. Those fields are known as *non-compliance fields*
while the fields that are not listed or cannot be updated are known as *compliance fields* [#f2]_.

See the :ref:`downloading-submitted-sample-manifest` section for guidelines about how to download a manifest that was
already submitted.

.. hint::

   To view a list of fields that can be updated for a particular project, collapse the list of fields by clicking the
   |collapsible-item-arrow| button below.

.. important::

   The amended manifest or updated spreadsheet file **must** be uploaded to the same profile that was initially used
   to upload the manifest (before any modifications were done).

   An error will occur if you perform one of the following actions:

   * Upload the amended manifest to a different profile [#f3]_ (other than the one used to upload the manifest to
     initially)
   * Upload the amended manifest to a new profile
   * Delete a profile that already has samples associated with it

   The |finish-button| button will **not appear** if a manifest requires permits and the permits have not been
   reuploaded. The permits **must** be reuploaded in order for the **Finish** button to appear when updating samples
   within a manifest. See the :ref:`No finish button displayed after manifest update and validation process
   <faq-samples-update-successful-validation-but-no-finish-button>` :abbr:`FAQ (Frequently Asked Question)` for
   insights.

.. note::

   * The manifest must be uploaded again with the amendments included for the change or update to occur.

   * If the manifest requires permits, the permits must be reuploaded before the manifest update can be completed. The
     **Finish** button will appear once the manifest validates successfully and the permits have been reuploaded.

   * You **cannot** reupload a manifest with some of the existing samples removed. The removed samples
     (from the reuploaded manifest) will not be automatically removed from the manifest sample record. If you would
     like existing samples to be removed or deleted from the manifest record, please contact
     :email:`COPO team <ei.copo@earlham.ac.uk>` for assistance detailing the profile title and reason for the
     removal.

   * Fields are also referred to as columns in the manifest.

.. raw:: html

   <br>

.. collapse:: List of Aquatic Symbiosis Genomics (ASG) project fields that can be updated

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

   <br><br>

.. collapse:: List of Darwin Tree of Life Samples (DToL) project fields that can be updated

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

   <br><br>

.. collapse:: List of European Reference Genome Atlas (ERGA) project fields that can be updated

   .. hlist::
      :columns: 1

      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_CONTACT
      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_OR_BIOCULTURAL_PROJECT_ID
      * ASSOCIATED_TRADITIONAL_KNOWLEDGE_OR_BIOCULTURAL_RIGHTS_APPLICABLE
      * BARCODE_HUB
      * BARCODING_STATUS
      * BARCODE_PLATE_PRESERVATIVE
      * BIOBANKED_TISSUE_PRESERVATIVE
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
      * DNA_VOUCHER_ID_FOR_BIOBANKING
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
      * PROXY_TISSUE_VOUCHER_ID_FOR_BIOBANKING
      * PROXY_VOUCHER_ID
      * PROXY_VOUCHER_LINK
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
      * VOUCHER_INSTITUTION
      * VOUCHER_LINK

.. raw:: html

   <br><hr>


.. rubric:: Footnotes

.. [#f1] See term: :term:`ENA`.
.. [#f2] See term: :term:`Compliance field`.
.. [#f3] Also known as COPO profile. See term: :term:`COPO profile`.

..
    Images declaration
..
.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/manifest_wizard_finish_button.png
   :height: 4ex
   :class: no-scaled-link