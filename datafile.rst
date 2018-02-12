####################
Datafiles
####################

Datafile is one of the core components of a COPO profile. Within this page, the user can perform the following tasks:

1. **Upload** datafiles to COPO
2. **Inspect** or view the uploaded files
#. **Describe** or attribute metadata to the uploaded files

.. image:: images/datafile-page.jpg

The screenshot shows the datafile page, with tabs to represent the key tasks mentioned (i.e., upload, inspect, and describe). Clicking a tab reveals the underlying view and controls to carry out actual work.


Upload
----------

Follow these steps to upload datafiles to COPO:

1. Click the **Upload** tab to reveal the file upload view (see screenshot above).
2. Within the upload pane, click the **Select files...** button. This should open a file browser.
#. Select one or more files to upload.

The selected files are uploaded to COPO. The upload process might involve compressing the datafiles (for large files), and `hashing` (for subsequent integrity verifications).

The process is demonstrated using the screenshots below. Two files were selected for upload; each approximately :code:`2GB` in size. The files are uploaded, compressed, and hashed. 

.. image:: images/datafile-zipped.jpg


.. image:: images/datafile-hashing.jpg

.. warning::
   In order to speed up the upload process, and for general user experience, it is advised that large files (e.g., size >=1GB) be compressed (using gzip) before  uploading them to COPO.



In the screenshot below, the displayed files have successfully been through the upload process. For each file, the name, extension (:code:`.gz` added if compressed), size (which now reflects the modified size after compression), and the hash value are displayed.

.. image:: images/datafile-upload-finish.jpg


Inspect
----------
.. image:: images/datafile-inspect.jpg

The inspect pane provides a view to the datafiles within a profile. 

