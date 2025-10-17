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


      * **type** (required): The type of profile to be created. [#f1]_

   .. raw:: html

      <br>

   **Usage**

    Please include at least the ``title``, ``description`` and ``type`` parameter values in the API URL to
    create a profile record for the authenticated user. Replace ``<title>``, ``<description>`` and ``<type>``
    with the desired values.

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/profiles" -H  "accept: */*" -H "Content-Type: application/json" -d " {"title":"<title>", "description":"<"description>","type":"<type>"}"

   **Example**
    
     To create a profile record with the title ``Sample profile``, description ``A profile to record sample objects.``
     and profile type ``Genomics``, use the following URL:

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X POST "https://copo-project.org/api/profiles" -H  "accept: */*" -H  "Content-Type: application/json" -d "{"title": "Sample profile", "description": "A profile to record sample objects.", "type": "Genomics"}"

.. raw:: html

   <br>

Fetch Profile Records
"""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an API key from the
       :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    This endpoint retrieves all profile records associated with the authenticated user.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles" -H  "accept: */*"

.. raw:: html

   <br>

Fetch Profile Record by ID
"""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (optional): A hexadecimal identifier of a profile.

      To apply filters, append them to the API URL as follows:
      ``profiles/<profile_id>``

      Replace ``<profile_id>`` with the desired value. See the example below.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an API key from the
       :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    This endpoint retrieves a profile record matching the provided profile ID for the authenticated user.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/<profile_id>" -H  accept: application/json"

   **Example**

    To retrieve the profile record with the profile ID ``68a5e2804d9676aef9074394``, use the following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394 -H  "accept: application/json"

.. raw:: html

   <br>

Update Profile Record by ID
"""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      .. note::

         Profile types cannot be changed once a profile has been created. An error will be returned if you attempt to
         do so. The initial profile type must be retained and included in the update request in order to
         update the other fields(s).

      * **profile_id** (required): A hexadecimal identifier of a profile.

      To apply filters, append them to the API URL as follows:
      ``profiles/<profile_id>``

      Replace ``<profile_id>`` with the desired value. See the example below.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an API key from the
       :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    This endpoint updates a profile record that matches the provided profile ID. Replace ``<title>`` and
    ``<description>`` with the desired values.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/<profile_id>

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X PUT "https://copo-project.org/api/profiles/<profile_id>" -H  accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To update the ``description`` of the profile matching the ID ``68a5e2804d9676aef9074394``, use the following URL:
    Note that in that example, the initial ``title`` and ``type`` values are be retained in the update request.

    .. tab-set::

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X PUT "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{"title": "Sample profile", "description": "A profile to record sample and single-cell objects.", "type": "Genomics"}"

.. raw:: html

   <br>

Fetch Data File Names by Profile ID
"""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (required): A hexadecimal identifier of a profile.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an API key from the
       :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    This endpoint retrieves data file names for a profile by profile ID. Replace ``{profile_id`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/{profile_id}/files

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/{profile_id}/files" -H  accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To retrieve the data files uploaded for the profile matching the ID ``68a5e2804d9676aef9074394``, use the
    following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Data File Upload URL by Profile ID
""""""""""""""""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. collapse:: Show API query parameters

      .. raw:: html

         <br>

      * **profile_id** (required): A hexadecimal identifier of a profile.

   .. raw:: html

      <br>

   **Usage**

    .. note::

       Authentication is required in order to use this API method. Create an API key from the
       :ref:`/apiKey API endpoint <endpoints-api-key>` before using this method.

    This endpoint retrieves ``curl`` URL command  file names for a profile by profile ID. Replace ``{profile_id`` with the desired value.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/{profile_id}/files/presignedurls

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/{profile_id}/files/presignedurls" -H  accept: application/json" -H  "Content-Type: application/json" -d "{"title": "<title>", "description": "<description>", "type": "<type>"}"

   **Example**

    To retrieve the data files uploaded for the profile matching the ID ``68a5e2804d9676aef9074394``, use the
    following URL:

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files/presignedurls

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/68a5e2804d9676aef9074394/files" -H  "accept: application/json"

.. raw:: html

   <br>

Fetch Single-cell Checklists
""""""""""""""""""""""""""""

.. collapse:: Show endpoint details

   .. raw:: html

      <br>

   .. hint::

      The words, ``manifest`` and ``checklist`` are used interchangeably. They both refer to a spreadsheet.

   **Usage**

    This endpoint returns a list of available single-cell checklists namely, their checklist ID, name, description,
    standard and technology.

    .. tab-set::

       .. tab-item:: Web Browser

          .. code-block:: bash

             https://copo-project.org/api/profiles/singlecells/checklists

       .. tab-item:: Command Line (curl)

          .. code-block:: bash

             $ curl -X GET "https://copo-project.org/api/profiles/singlecells/checklists" -H  accept: application/json" -H

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Refer to the :ref:`copo-project-affiliations` section for more information


..
    Images declaration
..

.. |profile-collapsible-item-arrow| image:: /assets/images/icons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link