.. _sequence-annotations:

===================================
Sequence Annotations Submission
===================================

.. note::

  * Reads must be uploaded before a **Sequence Annotation** can be submitted.

.. seealso::

   * :ref:`How to Update Sequence Annotations <sequence-annotations-update>`
   * :ref:`How to Delete Sequence Annotations <sequence-annotations-deletion>`
   * :ref:`How to check if data files for sequence annotation submissions have been processed after upload to ENA <files-ena-file-processing-status>`
   * :ref:`How to Submit Reads <reads>`
   * :ref:`accessions-dashboard`

.. raw:: html

   <hr>

How to Submit Sequence Annotations
------------------------------------

Accessing the Sequence Annotations' Web Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Sequence Annotations'** [#f1]_ web page can be accessed from the **Components** button associated with a
profile [#f2]_.

.. raw:: html

   <hr>

Use Components' Button to Navigate to Sequence Annotations' Web Page
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Click the |profile-components-button| button associated with a profile. Then, click the  |sequence-annotations-component-button| from
the popup menu displayed as shown below:

.. figure:: /assets/images/profile/profile_genomics_profile_components_sequence_annotations.png
  :alt: Genomics Sequence Annotations' profile component
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/profile/profile_genomics_profile_components_sequence_annotations.png
  :class: with-shadow with-border
  :height: 300px

  **Genomics Profile Components: Sequence Annotations' component button**

.. raw:: html

   <hr>

.. _sequence-annotations-submission-section:

Submit Sequence Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click |add-sequence-annotations-button| button to add **Sequence Annotations'** as shown below:

    .. figure:: /assets/images/sequence_annotations/sequence_annotations_pointer_to_add_annotations_button.png
       :alt: Pointer to 'Add Record' button
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_pointer_to_add_annotations_button.png
       :class: with-shadow with-border

       **Sequence Annotations' submission: Click 'Add Record' button**

   .. raw:: html

      <br>

#. An **Add Sequence Annotation** dialog is displayed. Provide the details then, click the **Submit Annotation**
   button.

   Select a sample accession from the **SAMPLE** dropdown field menu. The dropdown menu will display the reads that
   were previously uploaded.

    .. figure:: /assets/images/sequence_annotations/sequence_annotations_add_sequence_annotation_dialog1.png
       :alt: Add Sequence Annotation dialog with no sample accession chosen from SAMPLE dropdown menu
       :align: center
       :height: 70ex
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_add_sequence_annotation_dialog1.png
       :class: with-shadow with-border

       **Sequence Annotations' submission: 'Submit Annotation' dialog with no sample accession chosen from SAMPLE dropdown menu**

   .. raw:: html

      <br>

   .. figure:: /assets/images/sequence_annotations/sequence_annotations_add_sequence_annotation_dialog2.png
      :alt: Add Sequence Annotation dialog with sample accession chosen from SAMPLE dropdown menu
      :align: center
      :height: 70ex
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_add_sequence_annotation_dialog2.png
      :class: with-shadow with-border

      **Sequence Annotations' submission: 'Submit Annotation' dialog with sample accession chosen from SAMPLE dropdown menu**

   .. raw:: html

      <br>

#. The new sequence annotation(s) will be displayed on the **Sequence Annotations** web page after a successful submission.

    .. hint::

       Sequence annotation records that are highlighted **yellow** indicate that the records are pending submission. The
       records will be highlighted **green** after a successful automatic submission.

    .. figure:: /assets/images/sequence_annotations/sequence_annotations_uploaded1.png
       :alt: Sequence Annotation(s) pending submission
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_uploaded1.png
       :class: with-shadow with-border

       **Sequence Annotations' submission: Sequence Annotations' web page displaying the (pending) uploaded sequence annotation(s)**

    .. raw:: html

       <br>

    .. figure:: /assets/images/sequence_annotations/sequence_annotations_uploaded2.png
       :alt: Sequence Annotation(s) submitted
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_uploaded2.png
       :class: with-shadow with-border

    **Sequence Annotations' submission: Sequence Annotations' web page displaying the submitted sequence annotation(s)**

.. raw:: html

   <br>

.. seealso::

   * :ref:`accessions-dashboard`

.. raw:: html

   <hr>

.. _sequence-annotations-deletion:

How to Delete Sequence Annotations
-----------------------------------

.. note::

   Sequence annotations can only be deleted **before** they have been submitted.

Click the desired sequence annotation from the list of sequence annotations displayed on the **Sequence Annotations**
web page. Then, click the **Delete** button (located in the top-right corner of the table) as shown below:

.. figure:: /assets/images/sequence_annotations/sequence_annotations_pointer_to_delete_sequence_annotation_button.png
   :alt: Delete sequence annotations button
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_pointer_to_delete_sequence_annotation_button.png
   :class: with-shadow with-border

   **Sequence annotation deletion: Click the "Delete" button to remove the highlighted sequence annotation from the profile**

.. figure:: /assets/images/sequence_annotations/sequence_annotations_deleted.png
   :alt: Sequence annotations deleted successfully
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/sequence_annotations/sequence_annotations_deleted.png
   :class: with-shadow with-border

   **Sequence annotation deletion: Sequence annotation record has been deleted**

.. raw:: html

   <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes
.. [#f1] See: :term:`Sequence Annotation`.
.. [#f2] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.

.. raw:: html

   <br><br>

..
    Images declaration
..
.. |add-sequence-annotations-button| image:: /assets/images/buttons/add_button.png
   :height: 4ex
   :class: no-scaled-link

.. |sequence-annotations-component-button| image:: /assets/images/buttons/components_sequence_annotations_button.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link