.. _permits-submission:

=====================
Permits Submission
=====================

How to Submit Permits
------------------------------

.. note::

   * Permits can only be submitted after  :abbr:`ERGA (European Reference Genome Atlas)` [#f1]_ samples have been uploaded in the **Upload Sample Spreadsheet** dialog.

   * Permits can only be submitted via a :abbr:`ToL (Tree of Life)` [#f2]_ profile [#f3]_. Please see:
     :ref:`Steps to Create a Tree of Life Profile <tol-profile-walkthrough>` for guidance.

   * If you are using a Windows operating system (OS) to upload permits, the file name of the permits should exclude
     the extension  ``.pdf`` or ``.PDF``. This is because Windows OS by default, hides file extensions which results in
     it not being visible to you.

     If you would like to see the file extension, you can enable it by following these
     `guidelines <https://support.microsoft.com/en-gb/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01>`__.

     Ultimately, the permit file name should be in the format: ``permit_name.pdf`` **not** ``permit_name.pdf.pdf``.

   * COPO automatically appends the permit file name with the date of the submission during the permit submission
     process. This is to ensure that the permit file name is unique.

     For example, if a permit with the file name ``permit_name.pdf`` is uploaded, COPO will append the date to the file
     name as follows: ``permit_name_yyyymmdd.pdf`` where ``yyyymmdd`` is the date when the submission was made.

.. warning::
    * If you have more than one permit ﬁle to upload, they **must** be uploaded at the
      same time i.e. after you have clicked the |upload-permits-button| button, navigate
      to the directory where the permits are stored and ``CTRL + click`` all of the
      permits so that all the permits are highlighted and uploaded at the same time.

.. seealso::

   * :ref:`Downloading Submitted Permits <permits-submission-download-permits>`
   * :ref:`Images Submission <images-submission>`
   * :ref:`How to Submit ERGA Manifests <tol-erga-manifest-submissions>`
   * :ref:`How to Submit Barcoding Manifests <barcoding-manifest-submissions>`

#. The uploaded samples are shown in a table in the **Upload Sample Spreadsheet** dialog as shown below. Click the
   |upload-permits-button| button to browse your local (computer) system for ``.pdf`` permits for the samples.

    .. figure:: /assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_uploaded_samples_permits_required.png
      :alt: Upload Sample Spreadsheet dialog with uploaded samples
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_uploaded_samples_permits_required.png
      :class: with-shadow with-border

      **ERGA manifest submission: 'Upload Sample Spreadsheet' dialog with uploaded samples**

#. The permits table is empty under the **Sample Permits** tab in the **Upload Sample Spreadsheet** dialog.

    .. figure:: /assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_no_permits_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with no permits uploaded
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_no_permits_uploaded.png
      :class: with-shadow with-border

      **ERGA manifest submission: 'Upload Sample Spreadsheet' dialog with no permits uploaded**

#. The permits table is populated with the permits uploaded under the **Sample Permits** tab in the
   **Upload Sample Spreadsheet** dialog

    .. figure:: /assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_permits_uploaded.png
      :alt: Upload Sample Spreadsheet dialog with permits uploaded
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/erga/samples_erga_upload_spreadsheet_dialog_with_permits_uploaded.png
      :class: with-shadow with-border

      **ERGA manifest submission: 'Upload Sample Spreadsheet' dialog with permits uploaded**

#. Click the |finish-button| button to submit the permits and samples.

   A **Submit Samples** confirmation dialog is displayed. If you decide to confirm the samples submission, click
   the **Confirm** button.

   .. figure:: /assets/images/samples/samples_submit_samples_dialog.png
     :alt: 'Submit Samples' confirmation dialog
     :align: center
     :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_submit_samples_dialog.png
     :class: with-shadow with-border

     **ERGA manifest submission: 'Submit Samples' confirmation dialog**

.. raw:: html

   <hr>

.. _permits-submission-download-permits:

Download Submitted Permits
------------------------------

.. note::

   *  Permits can only be downloaded **after** they have been submitted.
   *  Permits **cannot** be deleted or modified after they have been submitted.
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

#. Select the sample record(s) that you would like to download permits for.

   Then, click the |download-permits-button1| button to download permit(s) submitted for the selected sample record(s).

   .. figure:: /assets/images/samples/samples_pointer_to_download_permits_button.png
      :alt: Samples web page with sample record(s) selected and a pointer to the 'Download permits' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_pointer_to_download_permits_button.png
      :class: with-shadow with-border

      **Samples web page: Pointer to 'Download permits' button**

   .. raw:: html

      <br>

#. If any permit submission(s) exist for the selected sample record(s), the permits will be automatically downloaded for
   the selected sample record(s) as shown below:

   .. hint::

      Permits will be downloaded as a ``.zip`` file

   If no permits were submitted for the selected sample record(s), a message is displayed in the popup
   dialog indicating such as shown below:

   .. figure:: /assets/images/samples/samples_download_permits_dialog_with_no_permits_exist_message.png
      :alt: No permits exists message in popup dialog for selected sample record(s)
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/samples/samples_download_permits_dialog_with_no_permits_exist_message.png
      :class: with-shadow with-border

      **Samples web page: Popup dialog displaying message, 'No permits exist for selected sample record(s)'**

.. raw:: html

   <hr>

On Accept or Reject Samples web page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have been assigned as a **sample manager**, see
`Download submitted permits section for sample managers <permits-submission-download-permits-sample-managers>` for more
information.

.. raw:: html

   <br>

.. raw:: html

   <hr>

.. rubric:: Footnotes
.. [#f1] See term: :term:`ERGA`.
.. [#f2] See term: :term:`Tree of Life (ToL) <ToL>`.
.. [#f3] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.


..
    Images declaration
..
.. |accept-reject-samples-navigation-button| image:: /assets/images/buttons/samples_accept_reject_navigation_button.png
   :height: 4ex
   :class: no-scaled-link

.. |clear-selection-button| image:: /assets/images/buttons/clear_selection_button.png
   :height: 4ex
   :class: no-scaled-link

.. |download-permits-button1| image:: /assets/images/buttons/permits_download_button1.png
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

.. |upload-permits-button| image:: /assets/images/buttons/permits_upload_button.png
   :height: 4ex
   :class: no-scaled-link
