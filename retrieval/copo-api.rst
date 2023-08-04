.. _copo-api:

==============
Using COPO API
==============

The `COPO API <https://copo-project.org/api/>`_  is a RESTful website service that allows users to interact
with the COPO system. The API is built using the Django :abbr:`REST (REpresentational State Transfer)` [#f1]_ Framework.

.. important::

   Click this button to ensure that the API endpoints results in the live COPO API server results:
   |copo-api-live-server-button|


.. raw:: html

   <hr>

API End-points
---------------
The COPO :abbr:`API (Application Programming Interface)` [#f2]_ comprises manifest, sample, statistics and profile
endpoints. Their results are available for download in csv, json or ro-crate [#f3]_ file formats depending on the record
type as shown in the table below.

Each endpoint results contain metadata provided by the submitter.

+-----------------------+-------------------------------------------------+
| **File Format**       | **Available Record Types**                      |
+-----------------------+-------------------------------------------------+
| csv                   | Study, Sample, Manifest                         |
+-----------------------+-------------------------------------------------+
| json                  | Study, Sample, Manifest                         |
+-----------------------+-------------------------------------------------+
| ro-crate              | Sample                                          |
+-----------------------+-------------------------------------------------+

A summary of how to use the end-points to retrieve data are as follows:

.. _manifest-api-endpoints:

Manifest Endpoints
~~~~~~~~~~~~~~~~~~~~

Fetch Manifests
"""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest" -H  "accept: application/json"

This results in a list of all manifest :abbr:`IDs (Identifications)` [#f4]_. The manifest identification can be
used to retrieve records in the other endpoints.


Fetch Sample Records by Manifest ID
"""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/{manifest_id}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/{manifest_id}" -H  "accept: application/json"

This results in a list of sample records for the given manifest :abbr:`IDs (Identifications)` [#f4]_.


Fetch Manifests between Dates
"""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/{from}/{to}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/{from}/{to}" -H  "accept: application/json"

This results in a list of all manifest :abbr:`IDs (Identifications)` [#f4]_ recorded in the given date period.


Fetch Manifests between Dates for a Project
""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/{project}/{from}/{to}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/{project}/{from}/{to}" -H  "accept: application/json"

This results in a list of all manifest :abbr:`IDs (Identifications)` [#f4]_ recorded in the given date period for a
given project.


Fetch Sample Record Status in a Manifest
""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/{manifest_id}/sample_statuses

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/{manifest_id}/sample_statuses" -H  "accept: application/json"

This results in minimal sample status information for each sample contained in the given ``{manifest_id}``.


Validate Manifest by Profile ID
""""""""""""""""""""""""""""""""""""""""
.. note::

   Authentication is required in order to use this API method. Obtain an API token from the following endpoint
   before using this method:

.. code-block:: bash

   https://copo-project.org/api/manifest/validate


This results in the ID of the validation report to be queried.


Validate Manifest by Report ID
""""""""""""""""""""""""""""""""""""""""
.. note::

   Authentication is required in order to use this API method. Obtain an API token from the following endpoint
   before using this method:

.. code-block:: bash

   https://copo-project.org/api/manifest/validate/report/

.. centered:: **OR**

.. code::

   $ curl -X POST "https://copo-project.org/api/manifest/validate/report/" -H  "accept: */*" -H  "Content-Type: application/x-www-form-urlencoded" -d "validation_report_id={report-id}

This gives the status and/or validation errors for a manifest based on the manifest report ID.


Validate Manifest
"""""""""""""""""""
.. note::

   Authentication is required in order to use this API method. Obtain an API token from the following endpoint
   before using this method:

   .. code-block:: bash

      https://copo-project.org/api/apiKey


.. code-block:: bash

   https://copo-project.org/api/manifest/validations

.. centered:: **OR**

.. code::

   $ curl -X POST "https://copo-project.org/api/manifest/validations/" -H  "accept: */*" -d ""


This checks whether a given manifest passes or fails validation for the authorised user.


.. raw:: html

   <hr>

.. _sample-api-endpoints:

Sample Endpoints
~~~~~~~~~~~~~~~~~~~~

Fetch Sample Records by Project
""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/{project}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/{project}" -H  "accept: application/json"

This results in a list of all the samples of a project in COPO.


Fetch Sample Records by Associated Project Type
""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/associated_tol_project/{values}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/sample/associated_tol_project/{values}" -H  "accept: application/json"

This results in a list of all sample records of a given associated project type(s) in COPO.

Fetch Sample Records between Dates
"""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/{from}/{to}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/{from}/{to}" -H  "accept: application/json"

This results in a list of all samples recorded in the given date period.


Fetch Sample Records by COPO ID
""""""""""""""""""""""""""""""""""""""""
.. hint::

   * Sample records IDs are referred to as ``copo_id`` in COPO and ``alias`` in ENA.
   * Multiple ``copo_id`` can be provided as a comma separated list in this endpoint.

.. code-block:: bash

   https://copo-project.org/api/sample/copo_id/{copo_ids}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/copo_id/{copo_ids}" -H  "accept: application/json"

This results in full sample information for the sample records returned from the given ``{copo_ids}``.

Fetch Sample Records by Biosample ID
""""""""""""""""""""""""""""""""""""""""
.. note::

   Biosample accession IDs are assigned to sample records by ENA [#f6]_ after the samples have been approved by a sample
   manager [#f7]_. The ``biosample_id`` is referred to as ``biosampleAccession`` in COPO and ``biosample_id`` in ENA.

.. code-block:: bash

   https://copo-project.org/api/sample/biosample_id/{biosample_ids}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/biosample_id/{biosample_ids}" -H  "accept: application/json"

This results in full sample information for the sample records returned from the given ``{biosample_ids}``.


Fetch Sample Records by Field and Values
""""""""""""""""""""""""""""""""""""""""""""""""""
.. hint::

   * Multiple values can be provided as a comma separated list in this endpoint.

.. code-block:: bash

   https://copo-project.org/api/sample/sample_field/{field}/{values}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/sample_field/{field}/{values}" -H  "accept: application/json"

This results in full sample information for the sample records returned from the given ``{field}/{values}``.

Fetch Study Records by Sample ID
""""""""""""""""""""""""""""""""""""""""
.. hint::

   * Multiple ``sample_ids`` can be provided as a comma separated list in this endpoint.

.. code-block:: bash

   https://copo-project.org/api/sample/StudyFromSampleAccession/{sample_ids}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/StudyFromSampleAccession/{sample_ids}" -H  "accept: application/json"

This results in full sample information for the sample records returned from the given ``{sample_ids}``.


Fetch Sample Records by Study ID
""""""""""""""""""""""""""""""""""""""""
.. hint::

   * Multiple ``biostudyAccessions`` can be provided as a comma separated list in this endpoint.

.. code-block:: bash

   https://copo-project.org/api/sample/SampleFromStudyAccession/{biostudyAccessions}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/SampleFromStudyAccession/{biostudyAccessions}" -H  "accept: application/json"

This results in full sample information for the sample records returned from the given ``{biostudyAccessions}``.


.. raw:: html

   <hr>

.. _statistics-api-endpoints:

Statistics' Endpoints
~~~~~~~~~~~~~~~~~~~~~~

Fetch Number of COPO Users
""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/stats/number_of_users

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/stats/number_of_users" -H  "accept: application/json"

This results in the total number of registered users in COPO.


Fetch Number of DToL Sample Records
""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/stats/number_of_dtol_samples

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/stats/number_of_dtol_samples" -H  "accept: application/json"

This results in the total number of Darwin Tree of Life (DToL) [#f5]_ registered sample records in COPO.


.. raw:: html

   <hr>

.. _profile-api-endpoints:

Profile Endpoints
~~~~~~~~~~~~~~~~~~~~

Create Profile Record
"""""""""""""""""""""
.. note::

   Authentication is required in order to use this API method. Obtain an API token from the following endpoint
   before using this method:

   .. code-block:: bash

      https://copo-project.org/api/apiKey


.. code-block:: bash

   https://copo-project.org/api/profile//make_profile

.. centered:: **OR**

.. code::

   $ curl -X POST "https://copo-project.org/api/profile//make_profile" -H  "accept: */*" -d ""


This creates a profile record for the authenticated user.


Fetch Profile Records
"""""""""""""""""""""
.. note::

   Authentication is required in order to use this API method. Obtain an API token from the following endpoint
   before using this method:

   .. code-block:: bash

      https://copo-project.org/api/apiKey


.. code-block:: bash

   https://copo-project.org/api/profile/get_for_user

.. centered:: **OR**

.. code::

   $ curl -X POST "https://copo-project.org/api/profile/get_for_user" -H  "accept: */*" -d ""


This results in a list of all profiles for the authenticated user.


.. raw:: html

   <br>


.. rubric:: Footnotes
.. [#f1] See term: :term:`REST`
.. [#f2] See term: :term:`API`
.. [#f3] See term: :term:`RO-Crate`
.. [#f4] See term: :term:`Manifest ID`
.. [#f5] See term: :term:`DToL`
.. [#f6] See term: :term:`ENA`
.. [#f7] See term: :term:`Sample manager`


..
    Images declaration
..
.. |copo-api-live-server-button| image:: /assets/images/buttons/copo-api-live-server-button-option.png
   :height: 6ex
   :target:  /assets/images/buttons/copo-api-live-server-button-option.png