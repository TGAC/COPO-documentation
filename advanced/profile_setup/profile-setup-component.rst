.. _profile-setup-component:

Component
~~~~~~~~~

Components [#f1]_ are individual elements or modules that make up the profile. These can include various functionalities or
data points that contribute to the profile's overall purpose.

.. seealso::

   * `ProfileType configuration <profile-setup-profile-type>`_
   * `RecordActionButton configuration <profile-setup-record-action-button>`_
   * `TitleButton configuration <profile-setup-title-button>`_

..
   * :ref:`Stand-alone profile components <standalone-profile-components>`
   * :ref:`ToL profile components <tol-profile-components>`
   * :ref:`Accessions profile component <accessions-component>`

.. raw:: html

   <hr>

Component Database Table Structure
-----------------------------------

Each component that make up a profile has specific settings and functionalities that contribute to the profile's
overall purpose.

The PostgreSQL table **Component** consists of the following fields:

* ``id`` (Integer): The unique identifier for the component
* ``name`` (String): The name of the component
* ``title`` (String): The display title of the component
* ``widget_icon`` (String): The icon associated with the component
* ``widget_colour`` (String): The colour associated with the component, used for UI elements
* ``widget_icon_class`` (String): The :abbr:`CSS (Cascading Style Sheets)` class for the icon
* ``table_id`` (String): The identifier for the associated table
* ``reverse_url`` (String): The URL used for reversing the component
* ``subtitle`` (String): The subtitle of the component, providing additional context

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: Component database fields

   .. code-block:: bash

       id |         name         |        title         | widget_icon  | widget_colour | widget_icon_class  |      table_id       |                    reverse_url                     |      subtitle
      ----+----------------------+----------------------+--------------+---------------+--------------------+---------------------+----------------------------------------------------+---------------------
        1 | profile              | Work Profiles        |              |               |                    | copo_profiles_table |                                                    | #component_subtitle
        2 | accessions           | Accessions           | sitemap      | pink          | fa fa-sitemap      | accessions_table    | copo_accession:copo_accessions                     |
        3 | accessions_dashboard | Accessions           | pink         |               | fa fa-sitemap      | accessions_table    | copo_accession:copo_accessions                     |
        4 | assembly             | Assembly             | puzzle piece | violet        | fa fa-puzzle-piece | assembly_table      | copo_assembly_submission:copo_assembly             |
        5 | taggedseq            | Barcoding Manifests  | barcode      | red           | fa fa-barcode      | tagged_seq_table    | copo_barcoding_submission:copo_taggedseq           | #component_subtitle
        6 | files                | Files                | file         | blue          | fa fa-file         | files_table         | copo_file:copo_files                               |
        7 | sample               | Samples              | filter       | olive         | fa fa-filter       | sample_table        | copo_sample:copo_samples                           |
        8 | read                 | Reads                | dna          | orange        | fa fa-dna          | read_table          | copo_read_submission:copo_reads                    | #component_subtitle
        9 | seqannotation        | Sequence Annotations | tag          | yellow        | fa fa-tag          | seqannotation_table | copo_seq_annotation_submission:copo_seq_annotation |

.. raw:: html

   <br><br>

.. collapse:: Description of each Component record

   .. raw:: html

      <br>

   * **profile**: Work Profiles component
   * **accessions**: Accessions component
   * **accessions_dashboard**: Accessions component
   * **assembly**: Assembly component
   * **taggedseq**: Barcoding Manifests component
   * **files**: Files component
   * **sample**: Samples component
   * **read**: Reads component
   * **seqannotation**: Sequence Annotations component

.. raw:: html

   <hr>

Usage of Component
---------------------

Please check back soon for more information on how to use the component in the project.

.. raw:: html

   <hr>

.. _visual-representation-component:

Visualisation of Component in Project
--------------------------------------

.. figure:: /assets/images/django_admin_interface/profile/component/visualisation_component_button_tol_profile_components.png
   :alt: Viewing components associated with a profile on the 'Work Profiles' web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/django_admin_interface/profile/component/visualisation_component_button_tol_profile_components.png
   :class: with-shadow with-border
   :height: 400px

   **Tree of Life Profile: Components**

* The following components make up a :abbr:`ToL (Tree of Life)` [#f2]_ profile:

  * |accessions-component-button|
  * |assembly-component-button|
  * |barcoding-manifest-component-button|
  * |files-component-button|
  * |reads-component-button|
  * |samples-component-button|
  * |sequence-annotations-component-button|

Each profile will have a set of components that are associated with it. These components will be displayed on a profile
on the **Work Profiles** web page.

Components will also appear to the top-right of web pages for easy navigation to them, depending on the component that
is being viewed. For example,the **Reads** component leads to the **Reads** web page and the other components are
displayed as indicated by the arrows in the image below:

.. figure:: /assets/images/django_admin_interface/profile/component/visualisation_component_button_on_specific_web_page.png
   :alt: Profile types web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/django_admin_interface/profile/component/vvisualisation_component_button_on_specific_web_page.png
   :class: with-shadow with-border
   :height: 300px

   **Reads web page: Other components**

If the current web page is not the **Reads** web page, the **Reads** component, |reads-icon|, will be displayed at the
top-right corner of the web page.

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, files samples,
         barcodes (also known as targeted sequences in European Nucleotide Archive (ENA)) and sequence annotations.

         A Tree of Life (ToL) profile is considered as a *project* research object.

.. [#f2] See term: :term:`Tree of Life (ToL) <ToL>`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |accessions-component-button| image:: /assets/images/buttons/components_accessions_button.png
   :height: 3ex
   :class: no-scaled-link

.. |assembly-component-button| image:: /assets/images/buttons/components_assembly_button.png
   :height: 3ex
   :class: no-scaled-link

.. |barcoding-manifest-component-button| image:: /assets/images/buttons/components_barcoding_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |files-component-button| image:: /assets/images/buttons/components_files_button.png
   :height: 3ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/buttons/components_reads_button.png
   :height: 3ex
   :class: no-scaled-link

.. |reads-icon| image:: /assets/images/buttons/reads-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/buttons/components_samples_button.png
   :height: 3ex
   :class: no-scaled-link

.. |sequence-annotations-component-button| image:: /assets/images/buttons/components_sequence_annotations_button.png
   :height: 3ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6