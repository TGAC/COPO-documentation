.. _images-submission:

=====================
Images Submission
=====================

How to Submit Images
------------------------------

.. note::

   * Images can only be submitted after samples have been uploaded in the **Upload Sample Spreadsheet** dialog. The max
     total image size should be no more than 2GB.

   * Images can only be submitted via a ToL [#f1]_ profile. Please see:
     :ref:`Steps to Create a Tree of Life Profile <tol-profile-walkthrough>` for guidance.

   * The file name of sample images must be named as ``{Specimen_ID}-{n}.[jpg|png]`` where ``{n}`` is the image number,
     ``{Specimen_ID}`` is the specimen ID of the sample in the manifest and ``jpg`` or ``png`` is the extension of the
     file.

.. important::

   The |upload-images-button| button will only be enabled after you upload a manifest in the
   **Upload Sample Spreadsheet** dialog. This process must be completed in one go; you cannot close the dialog and
   return later to upload images. The images rely on metadata from the sample manifest, so the |upload-images-button|
   button becomes active immediately after the manifest is uploaded, allowing you to add images in the same session.

.. seealso::

  * :ref:`Viewing Submitted Images <images-submission-view-images>`
  * :ref:`Images Submission FAQ <faq-images>`
  * :ref:`Permits Submission <permits-submission>`
  * :ref:`How to Submit ASG Manifests <tol-asg-manifest-submissions>`
  * :ref:`How to Submit DToL Manifests <tol-dtol-manifest-submissions>`
  * :ref:`How to Submit ERGA Manifests <tol-erga-manifest-submissions>`
  * :ref:`How to Submit Barcoding Manifests <barcoding-manifest-submissions>`

#. The images table is empty under the **Sample Images** tab in the **Upload Sample Spreadsheet** dialog.

    .. figure:: /assets/images/samples/samples_upload_spreadsheet_dialog_with_no_images_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with no image uploaded
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_erga_upload_spreadsheet_dialog_with_no_images_uploaded.png
      :class: with-shadow with-border

      **Manifest submission: 'Upload Sample Spreadsheet' dialog with no images uploaded**

#. The images table is populated with the images uploaded under the **Sample Images** tab in the
   **Upload Sample Spreadsheet** dialog.

    .. figure:: /assets/images/samples/samples_upload_spreadsheet_dialog_with_images_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with image(s) uploaded
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_upload_spreadsheet_dialog_with_images_uploaded.png
      :class: with-shadow with-border

      **Manifest submission: 'Upload Sample Spreadsheet' dialog with image(s) uploaded**

#. Click the |finish-button| button to submit the images and samples.

   A **Submit Samples** confirmation dialog is displayed. If you decide to confirm the samples submission, click
   the **Confirm** button.

   .. figure:: /assets/images/samples/samples_submit_samples_dialog.png
     :alt: 'Submit Samples' confirmation dialog
     :align: center
     :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_submit_samples_dialog.png
     :class: with-shadow with-border

     **Manifest submission: 'Submit Samples' confirmation dialog**

.. raw:: html

   <hr>

.. _images-submission-view-images:

View Submitted Images
------------------------------

.. note::

   *  Images can only be viewed **after** they have been submitted.
   *  Images **cannot** be deleted or modified after they have been submitted.
   *  The |accept-reject-samples-navigation-button| button will only appear on the web page if you
      are assigned as a sample manager.

.. hint::

   * To **select multiple** sample records, hold down the ``Ctrl`` key on your keyboard and click the sample records
     that you would like to select.
   * To **select a range** of sample records, hold down the ``Shift`` key on your keyboard and click the first and
     last sample records that you would like to select.
   * To **select all** sample records, click |select-all-button|
   * To **select filtered** sample records, click |select-filtered-button|
   * To **clear selection** of sample records, click |clear-selection-button|

.. raw:: html

  <br>

On Samples web page
~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the **Samples** web page.

   See :ref:`How to access Samples web page <accessing-samples-web-page>` section for guidance.

#. Select the sample record(s) that you would like to view images for.

   Then, click the |view-images-button1| button to view the image(s) submitted for the selected sample record(s).

   .. figure:: /assets/images/samples/samples_pointer_to_view_images_button.png
      :alt: Samples web page with sample record(s) selected and a pointer to the 'View images' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_pointer_to_view_images_button.png
      :class: with-shadow with-border

      **Samples web page: Pointer to 'View images' button**

   .. raw:: html

      <br>

#. If any image submission(s) exist for the selected sample record(s), a popup dialog will be displayed with the
   image(s) submitted for the selected sample record(s) as shown below:

   .. hint::

      Click the image to view a larger version.

   .. figure:: /assets/images/samples/samples_view_images_dialog_with_images_displayed.png
      :alt: View images popup dialog with images displayed for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_view_images_button.png
      :class: with-shadow with-border

      **Samples web page: Popup dialog displaying submitted image(s) for selected sample record(s)**

   .. raw:: html

      <br>

   .. centered:: **OR**

   If no images were submitted for the selected sample record(s), a message is displayed in the popup
   dialog indicating such as shown below:

   .. figure:: /assets/images/samples/samples_view_images_dialog_with_no_images_exist_message.png
      :alt: No images exists message in popup dialog for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_view_images_button.png
      :class: with-shadow with-border

      **Samples web page: Popup dialog displaying message, 'No images exist for selected sample record(s)'**

.. raw:: html

   <hr>

On Accept or Reject Samples web page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have been assigned as a **sample manager**, see
:ref:`View submitted images section for sample managers <images-submission-view-images-sample-managers>` for more
information.

.. raw:: html

   <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Tree of Life (ToL) <ToL>`.

..
    Images declaration
..
.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |clear-selection-button| image:: /assets/images/buttons/clear_selection_button.png
   :height: 4ex
   :class: no-scaled-link

.. |finish-button| image:: /assets/images/buttons/finish_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |select-all-button| image:: /assets/images/buttons/select_all_button.png
   :height: 4ex
   :class: no-scaled-link

.. |select-filtered-button| image:: /assets/images/buttons/select_filtered_button.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-images-button| image:: /assets/images/buttons/images_upload_button.png
   :height: 4ex
   :class: no-scaled-link

.. |view-images-button1| image:: /assets/images/buttons/images_view_button1.png
   :height: 4ex
   :class: no-scaled-link