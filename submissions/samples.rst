.. _samples-submission:

==============================
Samples Submission
==============================

The **Samples** web page facilitates the submission of sample metadata through a manifest [#f1]_.

Various types of sample manifests can be submitted depending on the project profile in use. Each manifest type has
its own specific requirements and fields.

The following sections provide detailed guidance on the submission of each manifest type:

.. toctree::
   :titlesonly:

   tol/tol-samples-submission
   genomics/genomics-samples-submission

.. raw:: html

   <br>

.. seealso::

   * :ref:`Accessing the Samples web page for Tree of Life profiles <accessing-samples-web-page-tol>`
   * :ref:`Accessing the Samples web page for Genomics profiles <accessing-samples-web-page-genomics>`
   * :ref:`How to submit Assemblies <assemblies>`
   * :ref:`How to upload Files <files>`
   * :ref:`How to submit Reads <reads>`
   * :ref:`How to submit Sequence Annotations <sequence-annotations>`
   * :ref:`accessions-dashboard`

.. raw:: html

   <hr>

.. _downloading-submitted-sample-manifest:

How to Download Submitted Sample Manifest
----------------------------------------------

.. hint::

   This is useful if you would like to update sample metadata for a manifest or retrieve the actual manifest that was
   submitted.

   Samples can be updated by resubmitting the manifest with the updated metadata. See :ref:`samples-update` section
   for more information about which fields can be updated.

.. note::

   * At least one sample record (in a manifest) must be submitted before a manifest can be downloaded.

     See the :ref:`Download sample manifest FAQ <faq-samples-download-sample-manifest-incorrect-sample-metadata>`
     section for more information.

   * The colour of the |add-manifest-button| button is based on the type of profile that you are making a submission to.

     See the :ref:`profile-types-legend` section regarding the colour code for the various types of project
     profiles on COPO.

The following steps describe how to download a submitted sample manifest:

#. Navigate to the **Samples** web page.

   To do this, please refer to the relevant section below, depending on the type of profile that you are working on.

   * :ref:`Accessing the Samples web page for Tree of Life profiles <accessing-samples-web-page-tol>`
   * :ref:`Accessing the Samples web page for Genomics profiles <accessing-samples-web-page-genomics>`

#. On the **Samples** web page, select **only one** sample record from the sample record table displayed.

   Then, click the |download-sample-manifest-button| button to download the manifest.

   **Note**: The record that you click the |download-sample-manifest-button| on is associated with a particular
   manifest ID so all samples associated with that manifest ID will be downloaded. The manifest ID value can be viewed
   in the **Manifest Identifier** column in the data table.

   See the :ref:`Download sample manifest FAQ <faq-samples-download-sample-manifest-incorrect-sample-metadata>` section
   for more information.

   .. raw:: html

      <br>

   .. hint::

      The manifest will be automatically downloaded as a ``.xlsx`` file

   .. figure:: /assets/images/samples/ui/samples_pointer_to_download_sample_manifest_button.png
      :alt: Samples web page with one sample record selected and a pointer to the 'Download sample manifest' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/ui/samples_pointer_to_download_sample_manifest_button.png
      :class: with-shadow with-border

      **Samples web page: Pointer to 'Download sample manifest' button**

   .. raw:: html

      <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] A manifest is a spreadsheet that contains information about the samples you want to submit. The manifest can
   include various fields such as sample identifiers, descriptions, collection locations, and other relevant metadata.

..
    Images declaration
..

.. |add-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/samples/buttons/samples_download_manifest_button.png
   :height: 4ex
   :class: no-scaled-link
