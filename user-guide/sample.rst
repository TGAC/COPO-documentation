===========
Samples
===========

The samples page enables users to describe and manage their biological samples. 

Samples within a profile can be linked to, or form part of, other components within a profile. For instance, a sample may be linked to a datafile as a metadata. The screenshot below shows the sample page before any record has been added.

.. image:: /images/sample1.jpg

COPO provides a wizard to aid in the process of entering samples. 

Initiate the sample wizard
----------------------------

To initiate the sample wizard, click the **Describe samples** icon (see the highlighted blue icon in the screenshot above).

.. hint:: 
   The sample description wizard is a sequence of steps that guides the user through the process of describing samples.
   
Number of samples 
------------------

Enter the number of samples to describe in the first stage of the wizard. 

.. hint:: 
   Multiple sample having a common set of attributes can be described in a batch.

.. image:: /images/sample-no-of-samples.jpg


Before proceeding through wizard stages, there are a few controls worth pointing out on the page. The screenshot above will be used as a point of reference.

Discard Description (left side of the wizard)
   Click this to discard and exit the current description. Please not that this action is irreversible.

Stage Info (next to the discard description button)
   Click this at any stage of the description to display information relevant to the stage.
   
Prev & Next (right side of the wizard)
   Use this to go forward and backward through the description stages
   
Info panel (right side corner of the page)
   This panel displays information about user interaction within a component page (e.g., feedback after record creation). In the wizard description context, it displays stage information as a user goes through different stages of a description.
   
Help panel (right side corner of the page)
   Click this tab to access context-based help about the samples page. This panel is also available to other components (e.g., Datafile)

Sample cloning
------------------
When describing new samples, the user can choose to inherit metadata from an existing sample. This may be useful in situations where the samples to be described have similar attributes to some reference sample. This functionality is set to **No** by default. Set the option to **Yes** if sample cloning is desired. In this guide, the clone option is selected to explore this functionality.

.. image:: /images/sample-clone.jpg


.. _sample-type-label:

Sample type
---------------
COPO provides a number of templates for describing samples defined by sample types. By selecting a particular sample type, the user can tailor the sample metadata towards a specific work process (e.g., submission to a particular repository).
   
The default sample type is **COPO Standard**. In the screenshot below, **Sample type** is set to **Biosample Standard**. However, this guide will highlight results from both types when relevant.

.. image:: /images/sample-type-biosample.jpg

.. hint:: 
   The **Biosample Standard** sample type is useful for describing repository agnostic samples. **COPO Standard** is the recommended type to use for submissions to the `European Nucleotide Archive <https://www.ebi.ac.uk/ena>`_.


Cloning method
---------------
The cloning method stage is presented if sample clone was selected in a previous stage. The user can select, either from a local sample collection or by resolving an accession to a remote database, the reference sample to clone.

.. image:: /images/sample-clone-2.png

.. note:: 
   The **Existing Sample** option is only active if there are available samples in the current profile. Samples from other profiles are not available to be cloned in this view. **Resolve Accession** is the default option when there are no existing samples in a profile.
   
Results from both options will be provided in this guide where relevant. Also, for demonstration purposes, the accession - :code:`SAMN05282547` (valid at the time of writing) is selected to be resolved.

.. note:: 
   COPO currently supports resolving sample accessions to the `BioSamples <https://www.ebi.ac.uk/biosamples/>`_  database. 
   

  
Enter an accession and press the **Resolve!** button, located to the right of the accession input box.
  
.. image:: /images/sample-resolve.jpg

The screenshot above shows the result of resolving the accession, :code:`SAMN05282547`, the metadata of which is displayed to the right. Also, the highlighted (in red circle) icon next to the **Accession** label, when hovered over also reveals the resolved sample metadata. 

The resolved attributes from this sample will form the basis of the current description. This will be demonstrated at a later stage.


.. warning:: 
   If an accession can't be resolved, an error will be displayed to inform the user. In that case, the user can either select a sample locally to clone (if there are any in the profile) or simply move on to the next stage.
   

If there are existing samples, this option can also be explored to clone a sample. 

.. image:: /images/sample-clone-existing.jpg

Select the **Existing Sample** option. The input control should change accordingly to enable the user to select from a list of samples. The user can either type into the input box to filter the samples, or simply scroll through the list of available samples. 

The use can hover over a sample, in the displayed list, to reveal information about the sample (see the screenshot above). 

Select the sample to clone, and hit **Next** to proceed with the description.

.. warning:: 
   The **Existing Sample** option is active only if there are samples defined in the current profile.

   
Proposed sample name
---------------------
The proposed sample name stage provides the user the opportunity to name the prospective samples. Two options are available to the user, each of which fits a specific naming use-case:

1. Predefined Names (default option)
2. Bundle Name

.. image:: /images/sample-naming.jpg

.. hint:: 
   Clicking an input control presents a help tip relevant to the selected control. 
   

The **Predefined Names** option is relevant in cases where the user has existing sample names. The sample names can come from a column in a spreadsheet,  or from a comma/tab separated list of names. To use this option, copy the sample names and paste in the **Predefined Names** input box and click the **Next** button to proceed. The screenshot above points to an example with comma separated list of sample names.

The  **Bundle Name** option will come in handy for users with no predefined sample names. If selected, the user will be required to enter a **bundle name**.

.. note::
   A **bundle name** is a prefix from which similar sample names may be derived. For example, if a user enters *sample* as a bundle name, COPO would use this entry to generate sample names of the form: *sample_1, sample_2, sample_3*, etc.


Assigned sample name
---------------------

.. image:: /images/sample-assigned-name.jpg

In this stage, the sample names for the prospective samples are generated. Sample names are unique in COPO, and the validation to satisfy this constraint is done before generating the names. The user can modify any of the generated names by simply entering a new name in a desired name field. Click the **Next** button to proceed.


.. warning::
   The validation for unique sample names may result in the rejection of certain proposed names. To work around this, the user will be required to supply alternative values for the affected sample name fields.
   
Sample attributes
---------------------
So far, we have specified the number of samples to describe; chosen a description template (or sample type) on which to base the sample description; and cloned a sample, the metadata of which would be used to bootstrap the  description. In the current stage - the sample attributes stage - the user can define common attributes that will apply to all the samples. 


.. note::
   The sample attributes stage acts as a template, that enables the user define common features that will be shared by all  samples in a description.  All entries made here will be assigned to all the prospective samples in the current description.
 

.. image:: /images/sample-attribute-biosample.jpg

The screenshot shows the result of cloning a sample from a remote repository, and selecting to use the **Biosample** sample type. The fields have been pre-populated with the resolved metadata from the clone target. The following components are available on the form.

Organism
   The Organism input control is used to capture the taxonomic information associated to the source biological material e.g., specie, genus, strain. This is an :term:`ontology field<Ontology field>`.  

.. note::
	When manually entering value in an ontology field, an auto-complete list of matched entries will be presented to select from. In some cases, the same matched term appear can be displayed multiple times, but from different ontology sources. 
 

Characteristics
	The Characteristics input control is used to enter information about the characteristics of the samples e.g., length, colour. 
	
	Any number of characteristics can be entered by clicking the **Add Characteristics** button (highlighted in the screenshot). To delete a characteristic, click the **Delete**  (highlighted in the screenshot) button next to an entry. 

.. note::
   A characteristic input control is a *composite control* made up of 3 input fields: **Category**, **Value**, and **Unit**. Each of these fields is an ontology field. Numeric values are not necessarily mapped to an ontology, and can be entered as free text.

An example characteristic entry would look like: Category (Height), Value (50), Unit (Centimeter). When referring to a sample, the example characteristic can be read as the sample having a **height** of **50** **centimetres**. 


Comments
	The Comments control is a key/value or **Title**/**Value** input field pair, which can be used to further add context to described samples. The Comments control, unlike the Characteristics, is free text and therefore can't be used to link ontologies. 
	
	Any number of comments can be entered by clicking the **Add Comments** button (similar to Characteristics). To delete a comment, click the **Delete** button next to an entry.

	
The Sample attributes form is slightly different when describing samples based on the **COPO Standard** template (see: :ref:`sample-type-label`).

.. image:: /images/sample-attribute-copo.jpg

The **Source** and **Factors** fields are defined under the **COPO Standard** attributes template, and the **Organism** and **Comments** fields are no longer featured (see the screenshot above).

Source
	This specifies the source of the sample. The user can either select from the list of sources, or create a new source to associate with the sample.
	
	.. warning::
		The source selection input will need to be populated with source records created by the user within the same profile.
	
	To create a new source, click the **Create & Assign Source** button. A source form will be presented as shown in the screenshot below. Enter information about the source and click **Save**. This will automatically associate the created source with the sample.
	
	.. image:: /images/sample-create-source.jpg
	
Factors
	Factors express treatment on the sample, e.g., dose, duration. The factor control is similar to the characteristic control, and the user can refer to the characteristic control above for more information on how to use this control.
	


Sample generation
---------------------
The prospective samples are set to be generated when the user clicks the **Next** button in the **Sample attributes** stage. As mentioned, the features entered in the Sample attributes stage of the wizard will be used as defaults for all the samples in the bundle. 

.. image:: /images/sample-generation.jpg

The user will be required to confirm the action to be taken.

Review 
	Selecting this option keeps the user in the current (Sample attributes) stage. The user can then go on and make any modifications to the common attributes of the samples.
	
Continue
	Selecting this option will cause the wizard to go ahead with the actual generation of the samples. The defined attributes are copied across to all the samples generated, and the wizard transitions to the next stage.

.. warning::
   Once the samples have been generated, stepping back to the **Sample attributes** stage to update an entry would no longer have an effect on the *common* features assigned to the samples. 
   
   
Review stage
-------------
The review stage is the final stage of the wizard. In this stage, the user is able to modify specific attribute values for the generated samples. Samples information is presented in a tabular format. To modify an attribute value, highlight the required cell and press the **Enter** key on your keyboard. When done modifying the value in a cell, press the **Enter** key again to save your changes. Click the **Finish!** button to end the description session.

.. image:: /images/sample-review.jpg

In the screenshot above, features defined in the **Sample attributes** stage form the column headers of the review table. The sample name takes the second column. 

Each sample in the bundle starts off with the same value, and the user can modify each cell (or attribute for a sample) as required. The **Category** of a characteristic is kept fixed as a column header, and the user can only modify the **Value** and **Unit** (where applicable) for individual or group of samples. Also, the **Title** of a comment is kept fixed as a column header. The user can only modify the **Value** of a comment.


The review stage provides the following functionality.

Multi-sample editing
	A feature value can be modified for a single or multiple samples at once: 
	
	* Highlight the target cell (by clicking on it)
	* Press the **Enter** key to activate cell edit 
	* Modify the feature value (make sure not to press **Enter** after this)
	* Click to select the rows to apply the update
	* Click **Apply to selected** to apply to selected rows; **Apply to all** to apply to all the samples; **Apply to current** to apply only to the sample for which the edit form is triggered
	
	.. image:: /images/sample-multi-edit.jpg
	
Sequential editing
	The wizard automatically highlights the next sample (one position down, same feature or column), after the Enter key is pressed to commit an edit. In this way, the user can conveniently enter feature values sequentially for all the samples.
	
Arrow keys
	Arrows keys (top, left, down, and right), as well as TAB, can be used to navigate the sample review table. 
   

Completing a description
-------------------------
.. image:: /images/sample-description-finish.jpg

Click the **Finish!** button (see the highlight in the screenshot above) when done editing the samples to complete the description. This will terminate the wizard and the page refreshed to display the sample detail view with the generated samples.

.. _sample-detail-view:

Sample detail view
---------------------

.. image:: /images/sample-detail-view.jpg

The screenshot above is an illustration of the sample detail view. We will take a look at the following controls provided by the user interface (UI). 

Some of these controls will serve the same purpose, when presented within the same UI context (page placement, etc.), in other profile components page.

Quick tour
	The quick tour control (orange icon, highlighted in red) can be found at top left corner of the page. Click this to activate a quick tour of page components. 
	
Profile components
	The profile components control (group of icons, highlighted in orange) can be found at the top right corner of the page. This provides a shortcut navigation to other components within the same profile.
	
	
The next set of controls act directly on (tabular) records listed on the page. These controls have been highlighted in the screenshot above (see buttons highlighted in blue).

Select all
	Click this button to select all records listed in the table. 
	
Select filtered
	This will normally make sense if used within the context of record filtering, as it selects only those records in the table that have been filtered. This makes it easy to perform an action on a group of filtered records. If no (explicit) filtering has been applied to the table, clicking this button will select all records in the table.
	
Select none
	Click this button to clear previously selected records.
	
Describe
	Click this button to activate the description wizard for a new description session. This will switch the current `Inspect` view to reveal the `Describe` view. 
	
	.. warning::
	   Only one description session can be activated. To initiate a new description session, a current description must first be discarded by clicking the **Discard Description** button in the `Describe` view.
	   
Edit
	Click this button to trigger a record update on the selected record. Only one record can be selected for this action.
	
Search 
	This table control (highlighted in green in the screenshot) allows for the filtering of records based on supplied search criteria. 
	
Details
	This is the green plus icon beside a record. Click this to display additional information about the record.
	











