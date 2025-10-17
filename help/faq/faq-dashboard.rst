.. _faq-dashboard:

Dashboard
--------------------

.. tip::

   To read the entire answer to a :abbr:`FAQ (Frequently Asked Question)`, click the arrow icon
   (|collapsible-item-arrow|) below any question to expand or collapse it.

.. raw:: html

  <hr>

.. _faq-dashboard-accessions-dashboard:

How can I view accessions after a metadata submission is made in COPO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Click to view answer

   .. raw:: html

      <br>

  .. hint::

     GenBank accession numbers follow the format ``GCA_XXXXXXXXX``. They are automatically assigned by
     :abbr:`ENA (European Nucleotide Archive)` and can be viewed on the
     `National Centre for Biotechnology Information (NCBI) <https://www.ncbi.nlm.nih.gov>`__ website using the
     link:  ``https://www.ncbi.nlm.nih.gov/datasets/genome/?bioproject=<project-id>`` where ``<project-id>`` is the
     project :abbr:`ID (identifier)` (also known as study :abbr:`ID (identifier)` or profile :abbr:`ID (identifier)`)
     associated with the profile used to submit the files in COPO.

  **Option 1**: View accessions in the data table
     Scroll to any column that ends with ``accession`` as depicted in the image below to view the accessions.

     .. note::

        The table row is highlighted in red in the image below because the files associated with the
        record are either still being processed or have encountered issues during processing.

     .. figure:: /assets/images/reads/ui/reads_table_showing_accessions.png
        :alt: Accessions column in the data table
        :align: center
        :target: https://raw.githubusercontent.com/TGAC/COPO-documentation/main/assets/images/reads/ui/reads_table_showing_accessions.png
        :class: with-shadow with-border
        :height: 300px

        **Accessions column in the data table**

  **Option 2**: Accessions web page
     * Click the |accessions-icon| button.

     * The accessions web page will be displayed.

  **Option 3**: Accessions dashboard
     Navigate to the `Accessions dashboard <https://copo-project.org/copo/copo_accessions/dashboard>`__ to view
     accessions

.. raw:: html

   <br>

Is there a way to analyse metadata submissions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. collapse::  Yes, the following are ways to analyse metadata submissions:

   .. raw:: html

      <br>

   #. `Tree of Life dashboard <https://copo-project.org/copo/tol_dashboard/tol>`__
       * Alternatively, click the |tol-dashboard-button| button.
   #. `Tree of Life inspection web page <https://copo-project.org/copo/tol_dashboard/tol_inspectt>`__
       * Alternatively, click the |tol-inspect-button| button.
   #. `Tree of Life inspection by Genome Acquisition Lab web page <https://copo-project.org/copo/tol_dashboard/tol_inspect/gal>`__
       * Alternatively, click the |tol-inspect-by-gal-button| button.
   #. `Statistics web page <https://copo-project.org/copo/tol_dashboard/stats>`__

.. raw:: html

   <hr>

..
    Images declaration
..

.. |accessions-icon| image:: /assets/images/accessions/icons/components_accessions_icon.png
   :height: 4ex
   :class: no-scaled-link

.. |collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |tol-dashboard-button| image:: /assets/images/dashboard/buttons/dashboard_tol_button.png
   :height: 4ex
   :class: no-scaled-link

.. |tol-inspect-button| image:: /assets/images/tol_inspection/buttons/tol_inspect_button.png
   :height: 4ex
   :class: no-scaled-link

.. |tol-inspect-by-gal-button| image:: /assets/images/tol_inspection/buttons/tol_inspect_by_gal_button.png
   :height: 4ex
   :class: no-scaled-link