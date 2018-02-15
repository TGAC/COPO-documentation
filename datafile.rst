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

.. note::
   While COPO is positioned to broker the submission of data to remote repositories, it is not equipped to serve as a `silo` for datafiles. Uploaded datafiles are held only for a short period of time, pending deposition of such to remote repositories.


Inspect
----------
The inspect pane provides a view to the datafiles within a profile.

.. image:: images/datafile-inspect.jpg

The presented view (see screenshot above) displays the two files uploaded to COPO. The file type has been identified as `fastq`. In general, the inspect view is consistent [#consistency_in_view]_ with the view discussed under the :ref:`sample detail view <sample-detail-view>` section. The user can reference that section for a description of overlapping controls. 

.. note::
   COPO tries to determine, and display accordingly, the type of an uploaded datafile. Where this is not possible, the type will be displayed as `unknown`. However, this does not disrupt the actions the user can perform on such files.
   

Tasks can be performed on a single datafile or a group of datafiles (bundle). Some of the relevant tasks defined for datafiles are:

Describe
	Click this button to describe selected datafiles. This would activate the description wizard, enabling the process of metadata attribution for the target files. 
	
	As mentioned, the user can either describe a single file or a bundle of files. This process will be discussed subsequently in more detail.  
	
Discard Metadata
	 Click this button to remove associated metadata on selected datafiles. 
	 
	 .. hint::
	    A **metadata indicator** is a visual cue beside a datafile record with information about its metadata level. In the screenshot above, the metadata indicator is represented by the red square beside a datafile record, and this indicates the absence of metadata. The user can hover over the indicator for state information. 



Datafile Description
---------------------
COPO supports, and provides relevant description templates for, submission of datafiles to a number of repositories (e.g., `ENA <https://www.ebi.ac.uk/ena/>`_, `Figshare <https://figshare.com>`_). 

Before embarking on datafile description, the user might want to give some thought about the end-point (i.e., the intended repository) of the target datafiles. For instance, certain file types might only be suitable for submission to specific repositories.

Irrespective of the description template used or the intended repository, the general process of datafile description is relatively similar. Any discrepancy in using any particular template will be highlighted where relevant.


Select the target files
--------------------------
The first step involves selecting the files to be described or the **description bundle**. The user can select a single file or multiple files. 

.. note::
	Multiple file description is useful (and possible) in situations where the files to be described would have similar metadata, and be potentially submitted to the same repository.
	
1.	Select the files to be described
2.	Click the **Describe** button

.. image:: images/datafile-select-files.jpg

The datafiles are validated for suitability of being described together, and the user would be expected to confirm the `bundling` action (see the screenshot below).

.. note::
	The confirmation dialog `might` not be displayed in a single file description.

.. image:: images/datafile-bundling-confirm.jpg

3. Click **Continue** to confirm the bundling

The view should switch to display the description wizard.


.. _datafile-wizard-label:

Datafile description wizard
-------------------------

.. image:: images/datafile-description-wizard.jpg
.. image:: images/datafile-description-wizard-2.jpg

The screenshots above provide an illustration of the datafile description wizard. The wizard, as observed in the screenshot, is laid out into different logical work sections, which include:

1. Action buttons
2. Stage transition buttons
#. Stage label
#. Description metadata or stage form
#. Description bundle
#. Info/Help panes


Action buttons
----------------

These are the group of buttons located to the top left hand corner (:ref:`highlighted in red, top left hand side <datafile-wizard-label>`).

Discard Description
   Clicking this action button will discard the description and associated metadata to the description bundles. The view will switch back to the **Inspect** pane.
   
   .. warning::
   	The discard description action deletes every description metadata associated with datafiles in the description bundle. Given the implication of this action, the user will be required to confirm the action before proceeding.
	
Exit Description
   Clicking this button terminates the description (and the wizard). The view will switch back to the **Inspect** pane.
   
   .. note::
    The exit description action, unlike the discard description action, preserves the metadata attributed to the description bundle. Description metadata, up to but not including the current stage, is saved and the user can continue from this `breakpoint` at a later stage.

Stage Info
   Clicking this displays relevant information to the current stage (e.g., metadata input required in the stage). Same information can be found on the **Info** panel (:ref:`right side hand side <datafile-wizard-label>`).
   
   
Stage transition buttons
--------------------------

The stage transition buttons (:ref:`highlighted in green, right hand side <datafile-wizard-label>`) are the **Prev** and **Next** buttons that enable the user to go back and forth through the stages of the wizard. 

By clicking **Next**, the user-supplied input in a current stage is saved, and the wizard transitions to next stage. The user can also go back through the stages, to update or view previous entries, by clicking the **Prev** button.

Stage label
---------------

The stage label is situated on the same level (:ref:`left hand side, below the action buttons <datafile-wizard-label>`) as the stage transition buttons. It provides a sensible labelling for the wizard stages. 

The current stage takes the focus, and is blue in colour. Visited stages are grey in colour. Each stage label also has an associated serial number for ease of reference.

In the :ref:`screenshot <datafile-wizard-label>` above, the current stage has the label `Target Repo` and an associated serial number of `1`, that indicates the first stage of the wizard.

.. note::
 New stages are presented to the user based on inputs in previous stages. Different inputs might therefore lead to entirely different paths or sequence of stages in the wizard.
   

.. Info panel (right side corner of the page)
..    This panel displays information about user interaction within a component page (e.g., feedback after record creation). In the wizard description context, it displays stage information as a user goes through different stages of a description.










.. rubric:: Footnotes

.. [#consistency_in_view] Some level of UI consistency is maintained, were possible, across all profile components.

