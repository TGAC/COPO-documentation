.. _adding_children_projects:

============================================
Adding Children Projects to Parent Projects
============================================

In COPO
------------

See :ref:`Choose associated profile type(s) <tol-profile-steps-details>` section when creating a profile for more
details.

.. raw:: html

   <hr>

In Public Repositories
------------------------

Please contact the :email:`COPO team <ei.copo@earlham.ac.uk>` if you would like to link child projects (subprojects)
to parent projects (also referred to as main, umbrella, or primary projects) in public repositories such as ENA [#f1]_
or NCBI [#f2]_.

Please include both the parent project accession and the accession(s) of the child project(s) when making your request.

.. note::

   * Only projects that are publicly available (i.e., have public accessions) can be linked to parent projects in
     public repositories.

   * Once linked, child projects may take a few days to appear under the parent project in the public repository
     interfaces.

.. only:: Internal

    .. raw:: html

       <hr>

    Get Parent Project Records by Project Accession  on ENA Webin REST V2 service
    --------------------------------------------------------------------------------

    .. note::

       * Ensure that you authenticate with your Webin account before you can query the ENA Webin REST V2 service.

       * ``<parent-project-accession>`` is the project accession of the main project or parent project

    .. hint::
       Umbrella project is also known as parent project and primary project.
       Child project is also known as subproject and secondary project.

    Visit the `ENA Webin REST V2 service <https://www.ebi.ac.uk/ena/submit/webin-v2>`__
    then, query the ``/project/{id}`` ENA Webin API method using the parent project accession

    See `ENA (European Nucleotide Archive) documentation about adding child projects to umbrella projects here
    <https://ena-docs.readthedocs.io/en/latest/faq/umbrella.html#adding-children-to-an-umbrella>`__.

    .. centered:: **OR**

    In the browser, input the URL, ``https://www.ebi.ac.uk/ena/submit/webin-v2/project/<parent-project-accession>``

    .. centered:: **OR**

    In the terminal, query: $ ``curl -X 'GET' 'https://www.ebi.ac.uk/ena/submit/webin-v2/project/<parent-project-accession>' -H 'accept: */*'``

.. raw:: html

   <br>

.. rubric:: Footnotes

.. [#f1] See term: :term:`ENA`.
.. [#f2] See term: :term:`NCBI`.