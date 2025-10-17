.. _faq-permits:

Permits
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

Can I view or download permits that I have uploaded in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

  Yes, permits can be retrieved and downloaded by selecting the desired sample record(s) on the **Samples** web page

  Then, clicking the |download-permits-button1| button on the web page.

.. raw:: html

  <br>

.. _faq-permits-error-uploading-multiple-permits-separately:

Why am I unable to upload permit one after the other?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   .. warning::

        * If you have more than one permit ﬁle to upload, they **must** be uploaded at the
          same time i.e. after you have clicked the |upload-permits-button| button, navigate
          to the directory where the permits are stored and ``CTRL + click`` all of the
          permits so that all the permits are highlighted and uploaded at the same time.

   * All permit ﬁles have to be selected/opened from the directory and uploaded
     together not one after the other.

.. raw:: html

   <br>

How can I resolve 'Conflicting data...' error when uploading permits in COPO after having uploaded a manifest?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   The error message ``Conflicting data`` is displayed when at least one of the following occurs:

   * The permit file name provided in the manifest does not end with the extension ``.pdf`` or ``.PDF``

     **Resolution**: Rename the name of the permit file so that it ends with the extension, ``.pdf`` or ``.PDF`` then,
     reupload the manifest

   * In the uploaded manifest, different permit file names are associated with the same **SPECIMEN_ID**

     **Resolution**: Provide a unique permit file name for each **SPECIMEN_ID** or provide the same file name for
     permit files that are associated with the same **SPECIMEN_ID** in the manifest. Then, reupload the manifest.

.. raw:: html

   <br>

Why do I encounter the error 'No xx permit found for xx 'SPECIMEN_ID'...Filename of permit must be named xx' after having uploading the permit files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::   Click to view answer

   .. raw:: html

      <br>

   This error message occurs when at least one of the following occurs:

   * The manifest uploaded requires multiple permit files but they were uploaded separately i.e. one after the other.

     **Resolution**: Please refer to :ref:`faq-permits-error-uploading-multiple-permits-separately`
     :abbr:`FAQ (Frequently Asked Question)` for more information.

   * The permit file name uploaded from your local system actually ends with ``.pdf.pdf`` (or ``.PDF.PDF``) and not
     ``.pdf`` (or ``.PDF``)

     **Resolution**: Ensure that the name of the permit file ends with the ``.pdf`` or ``.PDF`` extension only.

     If you are using a Windows operating system (OS) to upload permits, Windows OS by default, hides file extensions
     which results in it not being visible to you.

     If you would like to see the file extension, you can enable it by following these
     `guidelines <https://support.microsoft.com/en-gb/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01>`__.

   Reupload the manifest as well as the permit files after the resolutions have been made.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |download-permits-button1| image:: /assets/images/buttons/permits_download_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |upload-permits-button| image:: /assets/images/buttons/permits_upload_button.png
   :height: 4ex
   :class: no-scaled-link