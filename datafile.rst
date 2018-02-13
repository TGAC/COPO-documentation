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
The inspect pane provides a view to the datafiles within a profile.

.. image:: images/datafile-inspect.jpg

The presented view (see screenshot above) displays the two files uploaded to COPO. The file type has been identified as `fastq`. In general, the inspect view is consistent [#consistency_in_view]_ with the view discussed under the :ref:`sample detail view <sample-detail-view>` section. The user can reference that section for a description of overlapping controls. 

.. note::
   COPO tries to determine, and display accordingly, the type of an uploaded datafile. Where this is not possible, the type will be displayed as `unknown`. However, this does not disrupt the actions the user can perform on such files.
   

Tasks can be performed on a single datafile or a group (or bundle) of datafiles. Some of the relevant tasks defined for datafiles are:

Describe
	Click this button to describe selected datafiles. This would activate the description wizard, enabling the process of metadata attribution for the target files. 
	
	As mentioned, the user can either describe a single file or a bundle of files. This process will be discussed subsequently in more detail.  
	
Discard Metadata
	 Click this button to remove associated metadata on selected datafiles. 
	 
	 .. hint::
	    A **metadata indicator** is a visual cue beside a datafile record with information about its metadata level. In the screenshot above, the metadata indicator is represented by the red square beside a datafile record, and this indicates the absence of metadata. The user can hover over the indicator for state information. 



Datafile Description
---------------------
COPO supports, and provides description templates suitable for, a number of repositories (e.g., `ENA <https://www.ebi.ac.uk/ena/>`_, `Figshare <https://figshare.com>`_). Before embarking on datafile description, the user might want to give some thought about the description end-point (i.e., the intended repository) of the target datafiles. For instance, certain file types might only be suitable for submission to specific repositories.

We will endeavour to cover the different description routes currently implemented in COPO. Irrespective of the description template used or the intended repository, the general process of datafile description remains similar.


Selecting the target files
-------------------------------







.. rubric:: Footnotes

.. [#consistency_in_view] A certain level of UI consistency will be maintained, were possible, across profile components.

