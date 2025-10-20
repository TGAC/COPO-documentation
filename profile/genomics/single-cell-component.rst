:orphan:

.. _single-cell-component:

============
Single-cell
============

Single-cell [#f1]_ experiments provide insights into cellular heterogeneity, enabling researchers to study
individual cell types, states and functions within complex biological systems. In COPO, the single-cell component
object captures metadata associated with single-cell experiments, facilitating data submission to public repositories.

Refer to the :ref:`single-cell-submissions` section for guidance on how to upload and submit single-cell metadata.

In addition, the Single-cell website entails

.. seealso::

    * `Single-cell website <https://dwc.tdwg.org/list>`__
    * :ref:`Samples <samples-component-genomics>`
    * :ref:`Files <files>`
    * :ref:`Accessions <accessions-component>`
    * :ref:`Reads <reads>`
    * :ref:`Assemblies <assemblies>`
    * :ref:`Sequence annotations <sequence-annotations>`
    * :ref:`Images <images-component>`

.. raw:: html

   <hr>

.. _accessing-single-cell-web-page:

Accessing the Single-cell Web Page
----------------------------------

The Single-cell web page can be accessed via the **Components** button or via the components icon navigation pane when
viewing another component's web page associated with a Genomics profile.

Using the Components Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _accessing-single-cell-web-page-components-button:

Click the |profile-components-button| button associated with a profile. Then, click the  |single-cell-component-button|
button in the popup menu as shown below:

.. figure:: /assets/images/single_cell/ui/single_cell_button_pointer_genomics.png
   :alt: Single-cell profile component button
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/single_cell/ui/single_cell_button_pointer_genomics.png
   :class: with-shadow with-border
   :height: 300px

   **Genomics Profile Components: Single-cell button**

.. raw:: html

   <br>

Using the Components Icon Navigation Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The component icon navigation pane provides a quick access to other components associated with the same profile. It
appears on the inner right pane of the screen when you are viewing a component’s web page. The icons displayed in the
navigation pane correspond to the components associated with the profile.

If you are unsure what each icon represents, you can perform any of the following:

* Hover the mouse over the icon in the component icon navigation pane to see a tooltip with the component's name
* Refer to the :ref:`Component buttons <accessing-single-cell-web-page-components-button>` in the section above
* Refer to the :ref:`What are profile components? FAQ <faq-profiles-explain-components>`

.. note::

   * The navigation pane will not display the icon associated with the page that is currently being viewed.

   * If a component has subcomponents, a dropdown menu is shown when at least two items are available. However, if you
     are viewing a subcomponent’s web page and only one item remains, that item is displayed directly in the navigation
     pane.

.. figure:: /assets/images/single_cell/icons/single_cell_icon_pointer_genomics.png
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/single_cell/icons/single_cell_icon_pointer_genomics.png
   :class: with-shadow with-border
   :height: 120px

   **Genomics Profile: Navigation pane showing the Single-cell component icon**

.. raw:: html

   <hr>

.. _single-cell-submission-types:

Types of Single-cell Submissions
----------------------------------

COPO supports Single-cell Ribonucleic Acid Sequencing (scRNA-Seq) data submissions. The schema name for single-cell is
*COPO_SINGLE_CELL* and the supported standards include:

* `Darwin Core (DwC) <https://dwc.tdwg.org/list>`__
* `Functional Annotation of Animal Genomes (FAANG) <https://www.animalgenome.org/community/FAANG>`__
* `Minimum Information about any (x) Sequence (MIxS) <https://genomicsstandardsconsortium.github.io/mixs>`__
* Tree of Life (ToL)

.. list-table:: Types of Single-cell submissions
   :widths: 45 25 30
   :width: 100%
   :align: center
   :header-rows: 1

   * - Type
     - Abbreviation
     - COPO Identifier
   * - Single-cell Ribonucleic Acid Sequencing Darwin Core
     - scRNA-Seq DwC
     - version_dwc_sc_rnaseq
   * - Single-cell Ribonucleic Acid Sequencing Functional Annotation of Animal Genomes
     - scRNA-Seq FAANG
     - version_faang_sc_rnaseq
   * - Single-cell Ribonucleic Acid Sequencing Minimum Information about any (x) Sequence
     - scRNA-Seq MIxS
     - version_mixs_sc_rnaseq
   * - Single-cell Ribonucleic Acid Sequencing Tree of Life
     - scRNA-Seq ToL
     - version_tol_sc_rnaseq

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Single-cell`

..
    Images declaration
..

.. |profile-components-button| image:: /assets/images/profiles/buttons/components_button.png
   :height: 4ex
   :class: no-scaled-link

.. |single-cell-component-button| image:: /assets/images/single_cell/buttons/components_single_cell_button.png
   :height: 4ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310