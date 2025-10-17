.. _endpoints-manifest:

Manifest Endpoints
~~~~~~~~~~~~~~~~~~~~

The manifest endpoints are used to manage and retrieve information about sample manifests, including fetching
manifests, sample records and validation reports.

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |manifest-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |manifest-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of Life (ToL) standard. You do not need to
     specify these unless you want to override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already includes other parameters.

.. seealso::

   See term :term:`Manifest` for more information.

.. raw:: html

   <hr>

Fetch Manifests
"""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    * This endpoint returns a list of manifest :abbr:`IDs (Identifications)` of sample records.

    * After having retrieved a ``manifest_id`` value, you can use it to retrieve full sample information using the
      :ref:`manifest-api-endpoint-sample-record-by-manifest-id` endpoint or updates using the
      :ref:`audit-api-endpoint-sample-update-by-manifest-id` endpoint.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Manifests Filtered by Sequencing Centre
""""""""""""""""""""""""""""""""""""""""""""""

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
        `endpoint <https://copo-project.org/static/swagger/apidocs_index.html#/Sample/get_sample_sequencing_centre>`__.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``sequencing_centre`` parameter value in the API URL to retrieve a list of manifest
    IDs records by that sequencing centre. Replace ``<sequencing-centre>`` with the desired sequencing centre name.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=<sequencing-centre>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=<sequencing-centre>" -H  "accept: application/json"

   **Example**

    To retrieve manifest IDs associated with the sequencing centre ``EARLHAM INSTITUTE`` in the default JSON format,
    use the following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=EARLHAM%20INSTITUTE

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=EARLHAM%20INSTITUTE" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Current Manifest Versions
"""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **manifest_type** (optional): The type of the manifest [#f2]_. If no manifest type is provided, COPO returns a
        list of project names along with the latest manifest version associated with each.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/current_version

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/current_version" -H  "accept: application/json"

   **Example**

    To retrieve the current manifest version of the ``DTOL`` project in the default JSON format, use the following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/current_version?manifest_type=DTOL

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/current_version?manifest_type=DTOL" -H  "accept: application/json"

.. raw:: html

   <br>

.. _manifest-api-endpoint-sample-record-by-manifest-id:

Fetch Sample in Manifest by Manifest ID
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

      * **manifest_id** (required): The manifest ID [#f1]_ assigned to sample records.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include:
        **tol** (default), **dwc**, **ena** and **mixs**
      * **return_type** (optional): Output format for the results. Options include **json** (default), **csv** and
        **rocrate**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``manifest_id`` parameter value in the API URL to retrieve sample records for that
    manifest. Replace ``{manifest_id}`` with the desired manifest ID.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/{manifest_id}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/{manifest_id}" -H  "accept: application/json"

   **Example**

    To retrieve sample records for the manifest ID ``f8e5c23d-f735-439f-bfaf-a6886e31741e`` in the ``rocrate``
    format, use the following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

              https://copo-project.org/api/manifest/f8e5c23d-f735-439f-bfaf-a6886e31741e?return_type=rocrate

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

            $ curl -X GET "https://copo-project.org/api/manifest/f8e5c23d-f735-439f-bfaf-a6886e31741e?return_type=rocrate" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Manifests between Dates
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
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``from`` and ``to`` parameter values in the API URL to retrieve a list of
    manifest :abbr:`IDs (Identifications)`  [#f1]_ in a given date period. Replace ``{from}`` and ``{to}`` with the
    desired start and end dates respectively.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/{from}/{to}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/{from}/{to}" -H  "accept: application/json"

    **Example**

    To retrieve manifest IDs recorded between 1st January, 2025 and 1st May, 2025 in the default JSON format,
    use the following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/2025-01-01T00:00:00+00:00/2025-05-01T00:00:00+00:00

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/2025-01-01T00:00:00+00:00/2025-05-01T00:00:00+00:00" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Manifests between Dates for a Project
""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **project** (required): The name of the project [#f2]_
      * **from** (required): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **to** (required): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``project``, ``from`` and ``to`` parameter values in the API URL to retrieve a list
    of manifest :abbr:`IDs (Identifications)`  [#f1]_  in a given date period for that project. Replace ``{project}``,
    ``{from}`` and ``{to}`` with the desired start and end dates respectively.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/{project}/{from}/{to}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/{project}/{from}/{to}" -H  "accept: application/json"

    **Example**

    To retrieve manifest IDs for the ``ERGA`` project recorded between 1st January, 2025 and 1st May, 2025
    in the default JSON format, use the following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/erga/2025-01-01T00:00:00+00:00/2025-05-01T00:00:00+00:00

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/erga/2025-01-01T00:00:00+00:00/2025-05-01T00:00:00+00:00" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Status in a Manifest
"""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. tip::

         Filters are applied by appending them as query parameters in the API URL. See the **Usage** and **Example**
         sections for details.

      * **manifest_id** (required):The manifest ID [#f1]_ assigned to sample records.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``manifest_id`` parameter value in the API URL to retrieve minimal sample status
    information for each sample for that manifest ID. Replace ``{manifest_id}`` with the desired manifest ID.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/{manifest_id}/sample_status

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/{manifest_id}/sample_status" -H  "accept: application/json"

   **Example**

    To retrieve status information for sample records with the manifest ID ``f8e5c23d-f735-439f-bfaf-a6886e31741e`` in
    the default CSV format, use the following URL.

    The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or
    working in a terminal environment.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/f8e5c23d-f735-439f-bfaf-a6886e31741e/sample_status?return_type=csv

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/manifest/f8e5c23d-f735-439f-bfaf-a6886e31741e/sample_status?return_type=csv" -H  "accept: application/json"

.. raw:: html

   <br>

Validate Manifest by Profile ID
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an API key from the
         :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

      * **profile_id** (required): The identifier of the profile associated with the manifest to be validated.
      * **file** (optional): The manifest file to be validated. This should be a valid **CSV** or **XLSX** manifest file.

   .. raw:: html

         <br>

   **Usage**

    * Please include at least the ``profile_id`` parameter value in the API URL to validate a manifest associated with
      that profile and receive the validation report ID. Replace ``{profile_id}`` with the desired profile ID.

    * After having retrieved the validation report ID, you can use it to retrieve the validation report using the
      :ref:`manifest-api-endpoint-validation-report-by-id` endpoint.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/validate

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/manifest/validate" -H  "accept: */*" -d "title=<title>&description=<description>&profile_type=<profile_type>"

.. raw:: html

   <br>

.. _manifest-api-endpoint-validation-report-by-id:

Validate Manifest by Report ID
"""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Authentication is required in order to use this API method. Create an API key from the
         :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

      **validation_report_id** (required): The identifier of the validation report.

   .. raw:: html

         <br>

   **Usage**

    Please include the ``validation_report_id`` parameter value in the API URL to retrieve the manifest validation
    report associated with that ID.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/validate/report

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/manifest/validate/report" -H  "accept: */*" -d "title=<title>&description=<description>&profile_type=<profile_type>"

.. raw:: html

   <br>

Validate Manifest
"""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    This endpoint all manifest validations performed by the authenticated user.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/manifest/validations

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/manifest/validations/" -H  "accept: */*" -d ""

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] See term: :term:`Manifest ID`
.. [#f2] Refer to the :ref:`copo-project-affiliations` section for more information

..
    Images declaration
..

.. |manifest-collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link