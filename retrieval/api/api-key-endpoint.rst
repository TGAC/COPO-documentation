.. _endpoints-api-key:

API key Endpoint
~~~~~~~~~~~~~~~~~~~~

.. note::

   The examples below use API endpoints from the live COPO website.

   To use the demo website instead, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the URLs.

.. tip::

   * To view details of the endpoint, click the |api-key-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |api-key-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

.. raw:: html

   <hr>

Obtain an API key for authentication
"""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         This endpoint allows users to obtain an API key for authentication purposes. The API key is required for
         accessing certain API methods that require user authentication.

      * **username** (required): The username of the individual for whom the API key is being requested.
      * **password** (required): The password of the individual for whom the API key is being requested.

   .. raw:: html

         <br>

   **Usage**

    Please include at least the ``username`` and ``password`` parameter values in the API URL to obtain an API key for
    authentication. Replace ``<username>`` and ``<password>`` with the desired values.

    *Via a Web Browser (simply paste the URL in the address bar)*

    .. code-block:: bash

       https://copo-project.org/api/apiKey

    .. centered:: **OR**

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X POST "https://copo-project.org/api/apiKey" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "username=<username>&password=<password>"


   **Example**

    To create an API key for the user with username ``janedoe`` and password ``password123``, use the following URL:

    *Via the Terminal using curl (for command-line users)*

    .. code::

       $ curl -X POST "https://copo-project.org/api/apiKey" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "username=janedoe&password=password123"

.. raw:: html

   <hr>

..
    Images declaration
..

.. |api-key-collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link
