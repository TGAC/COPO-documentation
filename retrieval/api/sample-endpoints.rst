.. _endpoints-sample:

Sample Endpoints
~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |sample-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |sample-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of Life (ToL) standard. You do not need to
     specify these unless you want to override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already includes other parameters.

.. raw:: html

   <hr>

Fetch Sample Records by Project
""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **project** (required): The name of the project [#f1]_. Multiple projects can be provided as a comma (,)
        separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded values in the API
        :abbr:`URL (Uniform Resource Locator)`.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    * Please include at least the ``project`` parameter value in the API URL to retrieve a list of ``copo_id`` [#f5]_
      values for sample records within that project. Replace ``{project}`` with the desired project name.

    * To apply filters, append them to the API URL as follows:
      ``sample/{project}?return_type=<return_type>``. Replace ``{project}`` and ``<return_type>`` with the desired
      values. See the example section below for full usage with optional filters.

    * After having retrieved the ``copo_id`` values, you can use them to retrieve full sample information using the
      :ref:`sample-api-endpoint-sample-by-copo-id` endpoint.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/{project}

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/{project}" -H  "accept: application/json"

   **Example**

    To retrieve a list of ``copo_id`` values for sample records in the ``ASG``, ``DTOL`` and ``ERGA`` projects in JSON
    format, use the following URL.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/asg%2Cdtol%2Cerga

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::


       $ curl -X GET "https://copo-project.org/api/sample/asg%2Cdtol%2Cerga" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records by Associated Project Type
""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **values** (required): The subproject or secondary project to filter the results. [#f4]_
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    * Please include at least the ``values`` parameter value in the API URL to retrieve sample records by associated
      project type.

    * To apply filters, append them to the API URL as follows:
      ``sample/associated_tol_project?values=<values>&standard=<standard>&return_type=<return_type>``.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/associated_tol_project

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/associated_tol_project" -H  "accept: application/json"

    This endpoint results in a list of all sample records of a given associated project type(s) in COPO.

   **Example**

     To retrieve the profile titles and associated tube or well IDs for the ``ASG`` profile type and ``ERGA_COMMUNITY``
     associated profile type between 1st January, 2025 and 1st May, 2025 in CSV format, use the following URL.

     The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or working
     in a terminal environment.

     *Via a Web Browser (simply paste the URL in the address bar)*

     .. code-block:: bash

        https://copo-project.org/api/?profile_type=ASG&associated_profile_type=ERGA_COMMUNITY&d_from=2025-01-01T00:00:00+00:0&d_to=2025-05-01T00:00:00+00:0&return_type=csv

.. raw:: html

   <br>

Fetch Sample Project Fields by Manifest Version
""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **manifest_type** (optional): The type of the manifest [#f1]_. If no type is provided, all manifest types
        are used.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/manifest/current_version

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/manifest/current_version" -H  "accept: application/json"

   **Example**

    To retrieve sample fields for the ``ASG`` project using the latest manifest version in CSV format, use the URL
    below.

    The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or
    working in a terminal environment.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/manifest/current_version?manifest_type=ASG&return_type=csv

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/manifest/current_version?manifest_type=ASG&return_type=csv" -H  "accept: */*"

.. raw:: html

   <br>

Fetch Sample Records between Dates
"""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **from** (required): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **to** (required): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``from`` and ``to`` parameter values in the API URL to retrieve sample records. Replace
    ``{from}`` and ``{to}`` with the desired start and end dates respectively.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/{from}/{to}

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/{from}/{to}" -H  "accept: application/json"

    **Example**

     To retrieve samples between 1st January, 2025 and 1st May, 2025 in the default JSON format, use the following URL.



.. raw:: html

   <br>

.. _sample-api-endpoint-updatable-fields:

Fetch Updatable Fields by Project
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **project** (required): The name of the project [#f1]_. Multiple projects can be provided as a comma (,)
        separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded values in the API
        :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

         <br>

   **Usage**

    * Please include at least the ``project`` parameter value in the API URL to retrieve list of fields that can be
      updated when a manifest is reuploaded/resubmitted in COPO based on that project. Replace ``<project>`` with the
      desired project name.

    * To apply filters, append them to the API URL as follows:
      ``sample/updatable_fields?project=<project>&standard=<standard>&return_type=<return_type>``. Replace
      ``<project>``, ``<standard>`` and ``<return_type>`` with the desired values. See the example section below for
      full usage with optional filters.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/updatable_fields?project=<project>

    .. centered:: OR

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/updatable_fields?project=<project>" -H  "accept: */*"

   **Example**

    To retrieve the updatable fields for the ``DTOL`` project using the ``dwc`` standard in CSV format, use the
    following URL.

    The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or
    working in a terminal environment.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/updatable_fields?project=DTOL&standard=dwc&return_type=csv

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/updatable_fields?project=DTOL&standard=dwc&return_type=csv" -H  "accept: */*"

.. raw:: html

   <br>

.. _sample-api-endpoint-sample-by-copo-id:

Fetch Sample Records by COPO ID
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **copo_ids** (required): The unique identifier of the sample record [#f5]_. Multiple copo IDs can be provided
        as a comma (,) separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded values in the
        API :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

         <br>

   **Usage**

    Please include the ``{copo_ids}`` parameter in the API URL to retrieve full sample information for the specified
    ``copo_id`` [#f5]_ values. Replace ``{copo_ids}`` with one or more sample IDs, separated by commas.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/copo_id/{copo_ids}

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/copo_id/{copo_ids}" -H  "accept: application/json"

   **Example**

    To retrieve sample metadata for sample records matching the ``copo_id`` values - ``67e14bbf5b9e8a38259f95eb``,
    ``67e14bbf5b9e8a38259f95ec``, ``67e14bbf5b9e8a38259f95ed``, ``67e14bbf5b9e8a38259f95ee``,
    ``67e14bbf5b9e8a38259f95ef``, ``67e14bbf5b9e8a38259f95f0`` and ``67e14bbf5b9e8a38259f95f1`` in the default JSON
    format, use the URL below.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/copo_id/67e14bbf5b9e8a38259f95eb%2C67e14bbf5b9e8a38259f95ec%2C67e14bbf5b9e8a38259f95ed%2C67e14bbf5b9e8a38259f95ee%2C67e14bbf5b9e8a38259f95ef%2C67e14bbf5b9e8a38259f95f0%2C67e14bbf5b9e8a38259f95f1

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/copo_id/67e14bbf5b9e8a38259f95eb%2C67e14bbf5b9e8a38259f95ec%2C67e14bbf5b9e8a38259f95ed%2C67e14bbf5b9e8a38259f95ee%2C67e14bbf5b9e8a38259f95ef%2C67e14bbf5b9e8a38259f95f0%2C67e14bbf5b9e8a38259f95f1" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records by Biosample Accession
""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **biosampleAccessions** (required): The accession number (s) assigned by
        :abbr:`ENA (European Nucleotide Archive)` [#f2]_ after sample submission  accession(s) of the sample records to
        be retrieved. Multiple biosample accessions [#f6]_  can be provided as a comma (,) separated list in this
        endpoint. Commas (,) are represented as ``%2C`` URL-encoded values in the API
        :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    * Please include at least the ``biosampleAccessions`` parameter value in the API URL to retrieve sample records
      by biosample accession. Replace ``{biosampleAccessions}`` with the desired biosample accession(s).

    * To apply filters, append them to the API URL as follows:
      ``sample/biosampleAccession/{biosampleAccessions}?standard=<standard>&return_type=<return_type>``. Replace
      ``{biosampleAccessions}``, ``<standard>`` and ``<return_type>`` with the desired values. See the example
      section below for full usage with optional filters.


    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/biosampleAccessions/{biosampleAccessions}

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/biosampleAccessions/{biosampleAccessions}" -H  "accept: application/json"

    This results in full sample information for the sample record returned from the given ``{biosampleAccessions}``.

   **Example**

    To retrieve sample records with the biosample accessions - ``SAMEA12816320``, ``SAMEA115502883``,
    ``SAMEA112168601`` and ``SAMEA112168603`` in the **mixs** standard and return the results in JSON format, use the
    following.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/biosampleAccessions/SAMEA12816320%2CSAMEA115502883%2CSAMEA112168601%2CSAMEA112168603?standard=mixs&return_type=json

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/biosampleAccessions/SAMEA12816320%2CSAMEA115502883%2CSAMEA112168601%2CSAMEA112168603?standard=mixs&return_type=json" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records by Field and Values
"""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **field** (required): The field to filter the sample records by. Choose from the list of available fields in this
        `endpoint <https://copo-project.org/static/swagger/apidocs_index.html#/Sample/get_sample_sample_field__field___values_>`__.
      * **values** (required): The value(s) of the field to filter the sample records by. Multiple values can be provided
        as a comma (,) separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded values in the API
        :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Some records may match multiple values for the ``field``, depending on the ``values`` input. This happens
       because ``values`` are treated as substring matches - so results may include records where your input appears
       within a longer string. You may need to further filter the results to narrow them down precisely.

    * Please include at least the ``field`` and ``values`` parameter values in the API URL to retrieve sample records
      by field and values. Replace ``{field}`` with the desired field name and ``{values}`` with the desired value(s).

    * To apply filters, append them to the API URL as follows:
      ``sample/sample_field/{field}/{values}?standard=<standard>&return_type=<return_type>``. Replace ``{field}``,
      ``{values}``, ``<standard>`` and ``<return_type>`` with the desired values. See the example section below for
      full usage with optional filters.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/sample_field/{field}/{values}

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/sample_field/{field}/{values}" -H  "accept: application/json"

   **Example**

    To retrieve sample records with the field ``SCIENTICFIC_NAME`` and values ``Marifugia cavatica``,
    ``Graellsia isabellae`` and ``Valencia hispanica`` in the **tol** standard and return the results in CSV format,
    use the following.

    The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or
    working in a terminal environment.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/sample_field/SCIENTIFIC_NAME/Marifugia%20cavatica%2CGraellsia%20isabellae%2CValencia%20hispanica?return_type=csv

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/sample_field/SCIENTIFIC_NAME/Marifugia%20cavatica%2CGraellsia%20isabellae%2CValencia%20hispanica?return_type=csv" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records by Sequencing Centre
""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **sequencing_centre** (required): The name of the sequencing centre used to filter sample records. Choose
        from the :ref:`list of available sequencing centres <faq-profiles-sequencing-centres-list>` provided in this
        `this endpoint <https://copo-project.org/static/swagger/apidocs_index.html#/Sample/get_sample_sequencing_centre>`__.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``sequencing_centre`` parameter value in the API URL to retrieve full sample information
    for that sequencing centre. Replace ``<sequencing-centre>`` with the desired sequencing centre name.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=<sequencing-centre>

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=<sequencing-centre>" -H  "accept: application/json"

   **Example**

    To retrieve sample records with the sequencing centre ``EARLHAM INSTITUTE`` in the default JSON format, use the
    following URL.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=EARLHAM%20INSTITUTE

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=EARLHAM%20INSTITUTE" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records by Taxon ID
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **taxon_ids** (required): The taxon ID(s) of the sample records to be retrieved. Multiple taxon IDs can be
        provided as a comma (,) separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded
        values in the API :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

         <br>

   **Usage**

    * Please include at least the ``taxon_ids`` parameter values in the API URL to retrieve sample records by taxon IDs.
      Replace ``{taxon_ids}`` in the URL below with the taxon ID(s) of the sample records to be retrieved.

    * To apply filters, append them to the API URL as follows:
      ``sample/taxon_id/{taxon_ids}?standard=<standard>&return_type=<return_type>``. Replace ``{taxon_ids}``,
      ``<standard>`` and ``<return_type>`` with the desired values. See the example section below for full usage with
      multiple taxon IDs and optional filters.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/taxon_id/{taxon_ids}

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/taxon_id/{taxon_ids}" -H  "accept: application/json"


   **Example**

    To retrieve sample records with the taxon IDs - ``6344``, ``199168`` and ``2614811`` in the **mixs** standard and
    return the results in JSON format, use the following.

    Please note that JSON is the default output format and does not need to be specified in the API URL. However, if
    you would like to explicitly state it, add ``&return_type=json`` to the end of the API URL.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/sample/taxon_id/6344%2C199168%2C2614811?standard=mixs

    .. centered:: OR

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X GET "https://copo-project.org/api/sample/taxon_id/6344%2C199168%2C2614811?standard=mixs" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Records that have Image Submissions
""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **profile_type** (required): The name of the project. [#f1]_
      * **associated_profile_type** (optional): The associated project type of the sample records. This is the project type that the sample is a subproject of.
        For example, a sample may be associated with a project type of :abbr:`BGE (Biodiversity Genomics Europe)` but the sample itself may be
        an :abbr:`ERGA (European Reference Genome Atlas)` sample.
      * **d_from** (optional): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **d_to** (optional): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    * Please include at least the ``project`` parameter value in the API URL to retrieve sample records that have image
      submissions. Replace ``<project>`` with the name of the project.

    * To apply filters, append them to the API URL as follows:
      ``sample/with_submitted_bioimages?project=<project>&from=<date>&to=<date>&return_type=<return_type>``. Replace
      ``<project>``, ``<from>``, ``<to>`` and ``<return_type>`` with the project name, start date, end date and return
      type respectively. See the example below.

   *Via a Web Browser (simply paste the URL in the address bar)*

   .. code-block:: bash

      https://copo-project.org/api/sample/with_submitted_bioimages?project=<project>

   .. centered:: OR

   *Via the Terminal using curl (for command-line users)*

   .. code::

      $ curl -X GET "https://copo-project.org/api/sample/with_submitted_bioimages?project=<project>" -H  "accept: application/json"

   **Example**

   Additional filters like ``from``, ``to`` and ``return_type`` are optional. Replace each parameter with the desired
   values. To retrieve sample records with image submissions for the project ``ERGA`` between
   1st January, 2025 and 1st May, 2025 and return the results in CSV format, use the following.

   The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or working
   in a terminal environment.

   *Via a Web Browser (simply paste the URL in the address bar)*

   .. code-block:: bash

      https://copo-project.org/api/sample/with_submitted_bioimages?project=erga&from=2025-01-01T00:00:00+00:0&to=2025-05-01T00:00:00+00:0&return_type=csv

   .. centered:: OR

   *Via the Terminal using curl (for command-line users)*

   .. code::

      $ curl -X GET "https://copo-project.org/api/sample/with_submitted_bioimages?project=erga&from=2025-01-01T00:00:00+00:0&to=2025-05-01T00:00:00+00:0&return_type=csv" -H  "accept: application/json"

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information
.. [#f2] See term: :term:`ENA`
.. [#f3] See term: :term:`Sample manager`
.. [#f4] See :ref:`copo-project-associated-projects` section for available subprojects.

   The associated project type refers to the subproject a sample is part of (e.g. a sample may be in the
   :abbr:`ERGA (European Reference Genome Atlas)` project but associated with the
   :abbr:`BGE (Biodiversity Genomics Europe)` subproject). In sample records, this is recorded as
   **associated_tol_project** whereas in profile records, as **associated_type**.
.. [#f5] Sample records are identified by a unique ID known as **copo_id** in COPO and as **alias** in
   :abbr:`ENA (European Nucleotide Archive)`.
.. [#f6] A biosample accession is a unique identifier (ID) assigned to a sample record by
         :abbr:`ENA (European Nucleotide Archive)` [#f2]_ after it has been submitted by a sample manager [#f3]_.
         In COPO, this ID is referred to as **biosampleAccession** while in ENA, it appears as **biosample_id**.

.. raw:: html

   <hr>

..
    Images declaration
..

.. |sample-collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link