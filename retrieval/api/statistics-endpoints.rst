.. _endpoints-statistics:

Statistics Endpoints
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   * To view details of the endpoint, click the |statistics-collapsible-item-arrow| *Show endpoint details* button.

   * Then, inside that section, click the |statistics-collapsible-item-arrow| *Show API query parameters* button to see
     input parameter details.

   * JSON is the default output format and does not need to be specified in the API URL. However, if you would like to
     explicitly state it, add ``?return_type=json`` if no other query parameters are present, or ``&return_type=json``
     if the URL already includes parameters.

Retrieve Total Number of COPO Users
"""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    This endpoint returns the total number of registered users in COPO

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/stats/number_of_users

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

              $ curl -X GET "https://copo-project.org/api/stats/number_of_users" -H  "accept: application/json"

.. raw:: html

   <br>

Retrieve Number of Sample Records by Type and Date
"""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **sample_type** (required): The type of sample records to be counted. [#f1]_
      * **d_from** (optional): Start date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)
      * **d_to** (optional): End date for filtering (format: YYYY-MM-DDTHH:MM:SS+00:00)

   .. raw:: html

         <br>

   **Usage**

    * Please include at least the ``sample_type`` parameter value in the API URL to retrieve the total number of samples
      for that sample type. Replace ``{sample_type}`` with the desired value.

    * To apply filters, append them to the API URL as follows:
      ``sample_type/{sample_type}?d_from=<start_date>&d_to=<end_date>``. Replace ``{sample_type}``, ``<start_date>``
      and ``<end_date>`` with the desired values. See the example below.

    * If no sample type, no start date and no end date are provided, COPO will return the total number of samples.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/stats/number_of_samples/{sample_type}

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/stats/number_of_samples/{sample_type}" -H  "accept: application/json"

   **Example**

    To retrieve the total number of ``asg`` sample records between 1st January, 2025 and 1st May, 2025, use the
    following URL.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/stats/number_of_samples/asg?d_from=2025-01-01T00:00:00+00:00&d_to=2025-05-01T00:00:00+00:00

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/stats/number_of_samples/asg?d_from=2025-01-01T00:00:00+00:00&d_to=2025-05-01T00:00:00+00:00" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Tree of Life (ToL) Projects Submitted via COPO
""""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    This endpoint returns a list of main/primary projects brokered by COPO.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/stats/tol_projects

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/stats/tol_projects" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Associated Tree of Life (ToL) Projects Brokered by COPO
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    This endpoint returns a list of child projects/subprojects brokered by COPO.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/stats/associated_tol_projects

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/stats/associated_tol_projects" -H  "accept: application/json"

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information

..
    Images declaration
..

.. |statistics-collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link