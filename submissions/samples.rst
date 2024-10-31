.. _samples-submission:

==============================
Samples Submission
==============================

The following are the types of sample manifests that can be submitted.

Click the links below to learn more about each type of manifest submission:

* :doc:`Aquatic Symbiosis Genomics (ASG) manifests<tol-asg-manifest-submissions>`
* :doc:`Darwin Tree of Life (DToL) manifests <tol-dtol-manifest-submissions>`
* :doc:`Darwin Tree of Life Environmental (DToL_ENV) manifests <dtol-env-manifest-submissions>`
* :doc:`European Reference Genome Atlas (ERGA) manifests <tol-erga-manifest-submissions>`

.. raw:: html

   <br>

.. image:: /assets/files/presentations/copo_sample_submission_process_illustration.gif
   :alt: Samples submission and validation process in COPO
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/files/presentations/copo_sample_submission_process_illustration.gif
   :class: with-shadow with-border
   :scale: 60%

.. centered:: **Samples submission and validation process in COPO**

.. raw:: html

   <br>

.. seealso::

    * :ref:`How to access Samples web page <accessing-samples-web-page>`
    * :ref:`How to submit Assemblies <assemblies>`
    * :ref:`Barcoding manifest submissions <barcoding-manifest-submissions>`
    * :ref:`How to upload Files <files>`
    * :ref:`How to submit Reads <reads>`
    * :ref:`How to submit Sequence Annotations <sequence-annotations>`

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

   See :ref:`How to access Samples web page <accessing-samples-web-page>` section for guidance.

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

   .. figure:: /assets/images/samples/samples_pointer_to_download_sample_manifest_button.png
      :alt: Samples web page with one sample record selected and a pointer to the 'Download sample manifest' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_pointer_to_download_sample_manifest_button.png
      :class: with-shadow with-border

      **Samples web page: Pointer to 'Download sample manifest' button**

   .. raw:: html

      <br>

..
    Images declaration
..

.. |add-manifest-button| image:: /assets/images/buttons/add_manifest_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-sample-manifest-button| image:: /assets/images/buttons/samples_download_manifest_button.png
   :height: 4ex
   :class: no-scaled-link
