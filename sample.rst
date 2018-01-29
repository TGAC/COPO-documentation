####################
Samples
####################

The samples page enables users to describe and manage biological samples. 

Samples within a profile can be linked to, or form part of, other components within a profile. For instance, a sample may be linked to a datafile as a metadata. The screenshot below shows the sample page before any record has been added.

.. image:: images/sample1.jpg

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

.. image:: images/sample-no-of-samples.jpg


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

.. image:: images/sample-clone.jpg


Sample type
---------------
COPO provides a number of templates for describing samples defined by sample types. By selecting a particular sample type, the user can tailor the sample metadata towards a specific work process (e.g., submission to a particular repository).
   
The default sample type is **COPO Standard**. In the screenshot below, **Sample type** is set to **Biosample Standard**. However, this guide will highlight results from both types when relevant.

.. image:: images/sample-type-biosample.jpg

.. hint:: 
   The **Biosample Standard** sample type is useful for describing repository agnostic samples. **COPO Standard** is the recommended type to use for submissions to the `European Nucleotide Archive <https://www.ebi.ac.uk/ena>`_.


Cloning method
---------------
The cloning method stage is presented if sample clone was selected in a previous stage. The user can select, either from a local sample collection or by resolving an accession to a remote database, the reference sample to clone.

.. image:: images/sample-clone-2.png

.. note:: 
   The **Existing Sample** option is only active if there are available samples in the current profile. Samples from other profiles are not available to be cloned in this view. **Resolve Accession** is the default option when there are no existing samples in a profile.
   
Results from both options will be provided in this guide where relevant. Also, for demonstration purposes, the accession - :code:`SAMN05282547` (valid at the time of writing) is selected to be resolved.

.. note:: 
   COPO currently supports resolving sample accessions to the `BioSamples <https://www.ebi.ac.uk/biosamples/>`_  database. 
   

  
Enter an accession and press the **Resolve!** button, located to the right of the accession input box.
  
.. image:: images/sample-resolve.jpg

The screenshot above shows the result of resolving the accession, :code:`SAMN05282547`, the metadata of which is displayed to the right. Also, the highlighted (in red circle) icon next to the **Accession** label, when hovered over also reveals the resolved sample metadata. 

The resolved attributes from this sample will form the basis of the current description. This will be demonstrated at a later stage.


.. warning:: 
   If an accession can't be resolved, an error will be displayed to inform the user. In that case, the user can either select a sample locally to clone (if there are any in the profile) or simply move on to the next stage.

   
Proposed sample name
---------------------
The proposed sample name stage provides the user the opportunity to name the prospective samples. Two options are available to the user, each of which fits a specific naming use-case:

1. Predefined Names (default option)
2. Bundle Name

.. image:: images/sample-naming.jpg

.. hint:: 
   Clicking an input control presents a help tip relevant to the selected control. 
   

The **Predefined Names** option is relevant in cases where the user has existing sample names. The sample names can come from a column in a spreadsheet,  or from a comma/tab separated list of names. To use this option, copy the sample names and paste in the **Predefined Names** input box and click the **Next** button to proceed. The screenshot above points to an example with comma separated list of sample names.

The  **Bundle Name** option will come in handy for users with no predefined sample names. If selected, the user will be required to enter a **bundle name**.

.. note::
   A **bundle name** is a prefix from which similar sample names may be derived. For example, if a user enters *sample-* as a bundle name, COPO would use this entry to generate sample names of the form: *sample-1, sample-2, sample-3*, etc.


Assigned sample name
---------------------

.. image:: images/sample-assigned-name.jpg

In this stage, the sample names for the prospective samples are generated. Sample names are unique in COPO, and the validation to satisfy this constraint is done before generating the names. The user can modify any of the generated names by simply entering a new name in a desired name field. Click the **Next** button to proceed.


.. warning::
   The validation for unique sample names can lead to errors and the rejection of a proposed name. To work around this, supply a new name in the affected field before proceeding to a next stage.
   
Sample attributes
---------------------
So far, we have specified the number of samples to describe; gone on to select the description template (or sample type) on which to base the sample description; and even selected to clone a sample, the metadata of which could be used to bootstrap the  description. In the current stage - the sample attributes stage - the user can define common attributes that will apply to all the samples. 


.. note::
   The sample attributes stage acts as a template, that enables the user define common features that will be shared by all  samples in a description.  All entries made here will be assigned to all the prospective samples in the current description.
 

.. image:: images/sample-attribute-biosample.jpg

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


Sample generation
---------------------
The prospective samples are set to be generated when the user clicks the **Next** button in the **Sample attributes** stage. As mentioned, the features entered in the Sample attributes stage of the wizard will be used as defaults for all the samples in the bundle. 

.. image:: images/sample-generation.jpg

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

.. image:: images/sample-review.jpg

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
	
	.. image:: images/sample-multi-edit.jpg
	
Sequential editing
	The wizard automatically highlights the next sample (one position down), after the Enter key is pressed to commit an edit. In this way, the user can conveniently enter feature values sequentially for all the samples.
	
Arrow keys
	Arrows keys (top, left, down, and right), as well as TAB, can be used to navigate the sample review table. 
   












