.. _endpoints-profile:

Profile Endpoints
~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |profile-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |profile-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of Life (ToL) standard. You do not need to
     specify these unless you want to override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already includes other parameters.

.. raw:: html

   <hr>

Create Profile Record
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an API key from the
         :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

      * **title** (required): The name of the profile to be created.
      * **description** (optional): A brief overview of what the created profile will be about.
      * **profile_type** (optional): The type of profile to be created. [#f1]_

   .. raw:: html

         <br>

   **Usage**

    Please include at least the ``title``, ``description`` and ``profile_type`` parameter values in the API URL to
    create a profile record for the authenticated user. Replace ``<title>``, ``<description>`` and ``<profile_type>``
    with the desired values.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/profile/make_profile

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X POST "https://copo-project.org/api/profile/make_profile" -H  "accept: */*" -d "title=<title>&description=<description>&profile_type=<profile_type>"

    **Example**

     .. hint::

        To view the additional filters available for this endpoint, click the |profile-collapsible-item-arrow|
        *Show API query parameters* button above.
    
     To create a profile record with the title ``Sample profile``, description ``A profile to record sample objects.``
     and profile type ``Genomics``, use the following URL:

     *Via the Terminal using curl (for command-line users)*

     .. code::

        $ curl -X POST "https://copo-project.org/api/profile/make_profile" -H  "accept: */*" -H  "Content-Type: application/x-www-form-urlencoded" -d "title=Sample%20profile&description=A%20profile%20to%20record%20sample%20objects.&profile_type=Genomics"

.. raw:: html

   <br>

Fetch Profile Records
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   This endpoint retrieves all profile records associated with the authenticated user.

   **Usage**

      .. note::

         Authentication is required in order to use this API method. Create an API key from the
         :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/profile/get_for_user

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X POST "https://copo-project.org/api/profile/get_for_user" -H  "accept: */*" -d ""

.. raw:: html

   <br>

Fetch Profile Titles & Associated Tube or Well IDs
"""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_type** (required): The type of profile to be created. [#f1]_
      * **associated_profile_type** (optional): The subproject or secondary profile type to filter the results. [#f2]_
      * **d_from** (optional): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **d_to** (optional): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

         <br>

   **Usage**

    To apply filters, append them to the API URL as follows:
    ``sample/taxon_id/{taxon_ids}?standard=<standard>&return_type=<return_type>``. Replace ``{taxon_ids}``,
    ``<standard>`` and ``<return_type>`` with the desired values. See the example below.


    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/profile/tube_or_well_ids

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X POST "https://copo-project.org/api/profile/tube_or_well_ids?profile_type=<profile_type>" -H  "accept: */*" -d ""


    Replace ``<profile_type>`` with the name of the profile type. This endpoint results in a list of profile titles and associated
    tube or well IDs for the given profile type. Optionally, provide a date range filter based on the first and last
    sample manifest upload dates and ``associated_profile_type`` to filter the results.

    **Example**

     .. hint::

        * To view the additional filters available for this endpoint, click the |profile-collapsible-item-arrow| *Show API query
          parameters* button above.

     To retrieve the profile titles and associated tube or well IDs for the ``ERGA`` profile type and ``ERGA_COMMUNITY``
     associated profile type between 1st January, 2025 and 1st May, 2025 in CSV format, use the following URL.

     The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or working
     in a terminal environment.

     .. code-block:: bash

        https://copo-project.org/api/?profile_type=ERGA&associated_profile_type=ERGA_COMMUNITY&d_from=2025-01-01T00:00:00+00:0&d_to=2025-05-01T00:00:00+00:0&return_type=csv

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information
.. [#f2] See :ref:`copo-project-associated-projects` for available subprojects.

   The associated project type refers to the subproject a sample is part of (e.g. a sample may be in the
   :abbr:`ERGA (European Reference Genome Atlas)` project but associated with the
   :abbr:`BGE (Biodiversity Genomics Europe)` subproject). In sample records, this is recorded as
   **associated_tol_project**; in profile records, as **associated_type**.

..
    Images declaration
..

.. |profile-collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link