.. _endpoints-mapping:

Mapping Endpoints
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |mapping-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |mapping-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * By default, the API returns results in JSON format and uses the Tree of Life (ToL) standard. You do not need to
     specify these unless you want to override them.

     To explicitly include them in the API URL:

        * Use ``?return_type=json`` or ``?standard=tol`` if there are no other query parameters.
        * Use ``&return_type=json`` or ``&standard=tol`` if the URL already includes other parameters.

.. raw:: html

   <hr>

Fetch Mapped fields for the latest manifest version
""""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **project** (required): The name of the project [#f1]_
      * **standard** (optional): The :ref:`standard <mapping-api-standards>` to retrieve the manifest in. Options
        include **tol** (default), **dwc**, **ena** and **mixs**.
      * **return_type** (optional): Output format for the results. Options include **json** (default) and **csv**

      To apply filters, append them to the API URL as follows ``mapping?project=<project>&standard=<standard>&return_type=<return_type>``.

      Replace ``<project>``, ``<standard>`` and ``<return_type>`` with the desired values. See the example below.

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``project`` parameter value in the API URL to retrieve the mapped fields for the latest
    manifest version. Replace ``<project>`` with the desired project name.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/mapping?project=<project>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/mapping?project=<project>" -H  "accept: application/json"

   **Example**

    To retrieve the ``dwc`` mapped fields for the ``dtol`` project in the default return format, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/mapping?project=dtol&standard=dwc

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/mapping?project=dtol&standard=dwc" -H  "accept: application/json"

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information on the projects brokered
   through COPO.

..
    Images declaration
..

.. |mapping-collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link