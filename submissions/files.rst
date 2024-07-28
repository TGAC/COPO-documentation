.. _files:

=====================
Files Submission
=====================

How to Submit Files
------------------------------

.. hint::

   * See :abbr:`ENA (European Nucleotide Archive)` `assembly submission file types documentation <https://ena-docs.readthedocs.io/en/latest/submit/assembly.html#files-for-genome-assembly-submissions>`__
     for the types of files that can be submitted in COPO for assembly submissions.

   * See :abbr:`ENA (European Nucleotide Archive)` `read submission file types documentation <https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#accepted-read-data-formats>`__
     for the types of files that can be submitted in COPO for read submissions.

.. seealso::

  * :ref:`How to Delete Files <files-deletion>`
  * :ref:`How to check if data files associated with a metadata submission have been uploaded to ENA <files-ena-upload-status-after-copo-metadata-submission>`
  * :ref:`How to Submit Reads <reads>`
  * :ref:`How to Submit Assemblies <assemblies>`

.. raw:: html

   <hr>

Accessing the Files' Web Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Files' web page can be accessed from the **Components** button or **Actions** button associated with a
profile [#f1]_.

.. raw:: html

   <hr>

Use Components' Button to Navigate to Files' Web Page
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Click the |profile-components-button| button associated with a profile. Then, click the  |files-component-button| from
the popup menu displayed as shown below:

.. figure:: /assets/images/profile/profile_genomics_profile_components_files.png
  :alt: Genomics Files' profile component
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/profile/profile_genomics_profile_components_files.png
  :class: with-shadow with-border
  :height: 600px

  **Genomics Profile Components: Files component button**

.. raw:: html

   <hr>

.. _files-submission-via-browser:

Submit Files from your Local (Computer) System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The total **maximum** file size that can be uploaded from your local (computer) system is around **2 GB**. If you
   have a file larger than 2 GB or have multiple files whose combined total size exceeds 2 GB, please
   :ref:`submit the file(s) via the terminal <files-submission-via-terminal>`.

#. Click the |add-files-via-computer-button| button on the Files web page to add a new file by browsing your
   local file system

    .. figure:: /assets/images/files/files_pointer_to_add_files_via_computer_button.png
      :alt: 'Add new file by browsing local file system' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_pointer_to_add_files_via_computer_button.png
      :class: with-shadow with-border

      **Files web page: 'Add new file by browsing local file system' button**

   .. raw:: html

      <br>

#. An **Upload File** dialogue is displayed. Click the **Upload** button to choose a file from your local system.

    .. figure:: /assets/images/files/files_upload_file_dialogue.png
      :alt: Upload File dialogue
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_upload_file_dialogue.png
      :class: with-shadow with-border

      **Files submission: Upload File dialogue**

   .. raw:: html

      <br>

#. The new file(s) will be displayed on the **Files** web page after a successful submission.

    .. figure:: /assets/images/files/files_uploaded1.png
      :alt: File(s) submitted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_uploaded1.png
      :class: with-shadow with-border

      **Files submission: Files' web page displaying the uploaded file(s)**

    .. raw:: html

       <br><br>

    .. hint::

      To add more files from your local system, click the |add-files-via-computer-button1| button (once files have been
      submitted to the profile) as an alternative to clicking the |add-files-via-computer-button| button.

.. raw:: html

   <hr>

.. _files-submission-via-terminal:

Submit Files via the Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click the |add-files-via-terminal-button| button on the Files web page to add a new file from a cluster via the
   terminal.

    .. figure:: /assets/images/files/files_pointer_to_add_files_via_terminal_button.png
      :alt: 'Add new file via terminal' button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_pointer_to_add_files_via_terminal_button.png
      :class: with-shadow with-border

      **Files web page: 'Add new file via terminal' button**

   .. raw:: html

      <br>

#. A **Move Data** dialogue is displayed. Follow the instructions displayed then, click the **Process** button to submit
   the file(s) to the profile.

    .. figure:: /assets/images/files/files_move_data_dialogue.png
      :alt: Move Data dialogue
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_move_data_dialogue.png
      :class: with-shadow with-border
      :height: 400px

      **Files submission: Move Data dialogue**

   .. figure:: /assets/images/files/files_move_data_dialogue_terminal_input1.png
      :alt: Terminal with command inputted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_move_data_dialogue_terminal_input1.png
      :class: with-shadow with-border

      **Input** $ ``ls - F1`` **command in the terminal**

      .. raw:: html

         <br>

   .. figure:: /assets/images/files/files_move_data_dialogue_with_details1.png
      :alt: Move Data dialogue with details inputted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_move_data_dialogue_with_details1.png
      :class: with-shadow with-border
      :height: 400px

      **Move Data dialogue: Input the filename(s) returned after having ran the** $ ``ls - F1`` **command in the
      terminal. Then, click the** ``Process`` **button.**

      .. raw:: html

         <br>

   .. _files-submission-via-terminal-download-commands:

   .. figure:: /assets/images/files/files_move_data_dialogue_with_details2.png
      :alt: Move Data dialogue with result (a command) after having clicked the "Process" button
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_move_data_dialogue_with_details2.png
      :class: with-shadow with-border
      :height: 400px

      **Move Data dialogue: Command outputted after having clicked command in the** ``Process`` **button. Download the
      command displayed.**

      The downloaded file will have *unknown* or *download* as the file name depending on the browser you are using.

   .. raw:: html

      <br>

   .. figure:: /assets/images/files/files_move_data_dialogue_terminal_input2.png
      :alt: Terminal with command pasted
      :align: center
      :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_move_data_dialogue_terminal_input2.png
      :class: with-shadow with-border

      **Paste the copied command in the terminal**

      Alternatively, you can make the downloaded file executable then, run the file in the directory
      where the files are located:

      .. raw:: html

         <br>

   .. raw:: html

      <br>

#. The new file(s) will be displayed on the **Files** web page after a successful file submission via the terminal i.e.
   after the command has been executed successfully in the terminal.

    .. figure:: /assets/images/files/files_uploaded2.png
       :alt: Files submitted
       :align: center
       :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_uploaded2.png
       :class: with-shadow with-border

       **Files submission: Files' web page displaying the uploaded file(s)**

    .. raw:: html

       <br><br>

    .. hint::

       To add more files via the terminal, click the |add-files-via-terminal-button1| button (once files have been
       submitted to the profile) as an alternative to clicking the |add-files-via-terminal-button| button.

.. raw:: html

   <hr>

.. _files-deletion:

How to Delete Files
--------------------

Click the desired file from the list of files displayed on the Files' web page. Then, click the **Delete** button
(located in the top-right corner of the table) as shown below:

.. figure:: /assets/images/files/files_pointer_to_delete_file_button.png
  :alt: Delete files button
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_pointer_to_delete_file_button.png
  :class: with-shadow with-border

  **File deletion: Click the "Delete" button to remove the highlighted file from the profile**

.. figure:: /assets/images/files/files_deleted.png
  :alt: Files deleted successfully
  :align: center
  :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/files/files_deleted.png
  :class: with-shadow with-border

  **File deletion: File has been deleted**

.. raw:: html

   <hr>

.. _files-ena-upload-status-after-copo-metadata-submission:

Checking ENA File Upload Status
--------------------------------

.. note::

   A reads, annotations or assembly submission must be completed before the file(s) can be uploaded to
   ENA (European Nucleotide Archive).

After having completed a reads, annotations or assembly submission and associated a file(s) to it during the
submission process in COPO, the file(s) are submitted to ENA (European Nucleotide Archive).

The status of the file(s) uploaded to the :abbr:`ENA (European Nucleotide Archive)` can be checked in the column,
**ENA File Processing Status**, on the reads, annotations or assembly web page.

The **ENA File Processing Status** column is highlighted with a red rectangle border in the image below:

.. figure:: /assets/images/sequence_annotations/sequence_annotations_pointer_to_ena_file_processing_status_column.png
   :alt: ENA (European Nucleotide Archive) File Processing Status column on the reads, annotations or assembly web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/sequence_annotations/sequence_annotations_pointer_to_ena_file_processing_status_column.png
   :class: with-shadow with-border

   **ENA File Processing Status: The status of the file(s) uploaded to ENA (European Nucleotide Archive)**

.. raw:: html

   <br>

.. hint::

   * Rows with a status of **"File archived: PUBLIC"** or in a green colour indicate that the file(s) have been successfully
     submitted to :abbr:`ENA (European Nucleotide Archive)`.

   * Rows with a status of **"Invalid file integrity: PRIVATE"** or in a red colour indicate that the file(s) failed
     to be submitted to :abbr:`ENA (European Nucleotide Archive)`.

.. raw:: html

   <br> <hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.

.. raw:: html

   <br><br>

..
    Images declaration
..

.. |files-component-button| image:: /assets/images/buttons/components_files_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-computer-button| image:: /assets/images/buttons/add_files_via_computer_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-terminal-button| image:: /assets/images/buttons/add_files_via_terminal_button.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-computer-button1| image:: /assets/images/buttons/add_files_via_computer_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |add-files-via-terminal-button1| image:: /assets/images/buttons/add_files_via_terminal_button1.png
   :height: 4ex
   :class: no-scaled-link

.. |profile-components-button| image:: /assets/images/buttons/profile_components_button.png
   :height: 4ex
   :class: no-scaled-link
