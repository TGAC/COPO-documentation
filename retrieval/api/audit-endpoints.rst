.. _endpoints-audit:

Audit Endpoints
~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |audit-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |audit-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of Life (ToL) standard. You do not need to
     specify these unless you want to override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already includes other parameters.

.. raw:: html

   <hr>

Fetch Sample Updates
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **copo_id** (optional): A unique identifier of the sample record. It is known as ``alias`` in ENA. Multiple
        ``copo_id`` can be provided as a comma separated list in this endpoint.
      * **project** (optional): The name of the project [#f1]_
      * **updatable_field** (optional): Fields that can be updated when a manifest is reuploaded/resubmitted in COPO
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

        To apply filters, append them to the API URL as follows ``audit/samples/?copo_id=<copo_id>&project=<project>&updatable_field=<updatable_field>&return_type=<return_type>``.

        Replace ``<copo_id>``, ``<project>``, ``<updatable_field>`` and ``<return_type>`` with the sample ID, project
        name, updatable field and return type respectively. See the example below.

   .. raw:: html

         <br>

   **Usage**

    This endpoint results in a list of sample updates that occurred in COPO.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/samples

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/samples" -H  "accept: application/json"

   **Example**

    To retrieve sample updates for the sample with the COPO ID ``67d461e318e6e19d10b37901`` in the project
    ``DTOL`` by the  updatable field `SCIENTIFIC_NAME` and return the results in JSON format, use the following:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/samples?copo_id=67d461e318e6e19d10b37901&project=DTOL&updatable_field=SCIENTIFIC_NAME&return_type=json

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/samples?copo_id=67d461e318e6e19d10b37901&project=DTOL&updatable_field=SCIENTIFIC_NAME&return_type=json" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Updates Between Dates
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **from** (required): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **to** (required): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

        To apply filters, append them to the API URL as follows ``audit/sample/{from}/{to}?return_type=<return_type>``.

        Replace ``{from}``, ``{to}`` and ``<return_type>`` with the start date, end date and return type respectively.
        See the example below.

   .. raw:: html

         <br>

   **Usage**

    Please include at least the ``from`` and ``to`` parameters in the API URL to retrieve sample updates that occurred
    between a given date period. Replace ``{from}`` and ``{to}`` with the start date and end date respectively.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/sample/{from}/{to}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/sample/{from}/{to}" -H  "accept: application/json"

   **Example**

    To retrieve sample updates between 1st January, 2025 and 1st May, 2025 and return the results in CSV format, use the
    following:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/sample/2025-01-01T00:00:00+00:0/2025-05-01T00:00:00+00:0?return_type=csv

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/sample/2025-01-01T00:00:00+00:0/2025-05-01T00:00:00+00:0?return_type=csv" -H  "accept: application/json"

.. raw:: html

   <br>

.. _audit-api-endpoint-sample-update-by-manifest-id:

Fetch Sample Updates by Manifest ID
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **manifest_id** (required): The manifest ID (s) assigned to sample records. Multiple manifest IDs can be
        provided as a comma (,) separated list in this endpoint. Commas (,) are represented as ``%2C`` URL-encoded
        values in the API :abbr:`URL (Uniform Resource Locator)`.
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to query the endpoint. Options include
        **tol** (default), **dwc**, **ena** and **mixs**.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

        To apply filters, append them to the API URL as follows ``audit/sample/manifest_id/{manifest_id}?standard=<standard>&return_type=<return_type>``.

        Replace ``{manifest_id}``, ``<standard>`` and ``<return_type>`` with the desired values. See the example below.

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``manifest_id`` value to retrieve a list of sample updates by manifest
    :abbr:`IDs (Identifications)` [#f2]_. Replace ``{manifest_id}`` in the URL below with the desired manifest ID(s).

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/sample/manifest_id/{manifest_id}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/sample/manifest_id/{manifest_id}" -H  "accept: application/json"

   **Example**

    To retrieve sample records with the manifest IDs - ``f8e5c23d-f735-439f-bfaf-a6886e31741e`` and
    ``046632f0-0869-4a3b-b3c3-cd22158b4b12`` in the **ena** standard and return the results in **csv** format, use the
    following.

    The browser method will prompt a download of the CSV while the curl method is helpful if you are scripting or
    working in a terminal environment.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/sample/manifest_id/f8e5c23d-f735-439f-bfaf-a6886e31741e%2C046632f0-0869-4a3b-b3c3-cd22158b4b12?standard=ena&return_type=csv

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/sample/manifest_id/f8e5c23d-f735-439f-bfaf-a6886e31741e%2C046632f0-0869-4a3b-b3c3-cd22158b4b12?standard=ena&return_type=csv" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Updates by Update Type
""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **project** (optional): The name of the project [#f1]_
      * **update_type** (required): The type of update to filter by. Options include:

            * **system**: Updates performed by COPO
            * **user**: Updates performed by a user reuploading a manifest with amended sample metadata
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

        To apply filters, append them to the API URL as follows ``/audit/sample/update_type/{update_type}?project=<project>&return_type=<return_type>``.

        Replace ``{update_type}``, ``<project>`` and ``<return_type>`` with the desired values. See the example below.

   .. raw:: html

         <br>

   **Usage**

    Please include at least the ``update_type`` value to retrieve a list of sample updates by update type. Replace
    ``{update_type}`` in the URL below with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/sample/update_type/{update_type}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/sample/update_type/{update_type}" -H  "accept: application/json"

   **Example**

    To retrieve sample updates performed by the ``user`` for the ``ASG``, ``DTOL`` and ``ERGA`` projects and return
    the results in JSON format, use the following:

    .. tab-set::

        .. tab-item:: Web Browser

            .. code-block:: bash

               https://copo-project.org/api/audit/sample/update_type/user?project=ASG&project=DTOL&project=ERGA

        .. tab-item:: Command Line (curl)

            .. code-block:: bash

               $ curl -X GET "https://copo-project.org/api/audit/sample/update_type/user?project=ASG&project=DTOL&project=ERGA" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Sample Updates by Field and Field Value
""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **field** (required): The sample field to filter updates by. Options include:

        * RACK_OR_PLATE_ID
        * SPECIMEN_ID
        * TUBE_OR_WELL_ID
        * biosampleAccession
        * public_name
        * sraAccession
      * **field_value** (required): The value of the sample field to filter updates by.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

        To apply filters, append them to the API URL as follows ``/audit/sample/{field}/{field_value}?return_type=<return_type>``.

        Replace ``{field}``, ``{field_value}`` and ``<return_type>`` with the desired values. See the example below.

   .. raw:: html

         <br>

   **Usage**

    Please include at least the ``field`` and ``field_value`` values to retrieve a list of sample updates by field and
    field value. Replace ``{field}`` and ``{field_value}`` in the URL below with the desired field and field value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/audit/sample/{field}/{field_value}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/audit/sample/{field}/{field_value}" -H  "accept: application/json"

    **Example**

     To retrieve sample updates for the sample with the field, ``SPECIMEN_ID``, value ``ERGA_JB_4431_00001``
     and return the results in JSON format, use the following:

     .. tab-set::

        .. tab-item:: Web Browser

           .. code-block:: bash

              https://copo-project.org/api/audit/sample/SPECIMEN_ID/ERGA_JB_4431_00001

        .. tab-item:: Command Line (curl)

           .. code-block:: bash

              $ curl -X GET "https://copo-project.org/api/audit/sample/SPECIMEN_ID/ERGA_JB_4431_00001" -H  "accept: application/json"

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information
.. [#f2] See term: :term:`Manifest ID`

.. raw:: html

   <hr>
..
    Images declaration
..

.. |audit-collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link