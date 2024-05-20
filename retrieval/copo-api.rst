.. _copo-api:

==============
Using COPO API
==============

The `COPO API <https://copo-project.org/api/>`_  is a RESTful website service that allows users to interact
with the COPO system. The API is built using the Django :abbr:`REST (REpresentational State Transfer)` [#f1]_ Framework.

.. hint::

   The button, |copo-api-live-server-button|, indicates that the API method endpoints will produce results from the
   website host server i.e. if the live COPO website is used to query the endpoint, then, the live results will
   be retrieved while the opposite occurs if one uses the demo website to query the API method endpoints.


.. raw:: html

   <hr>

API End-points
---------------

The COPO :abbr:`API (Application Programming Interface)` [#f2]_ comprises manifest, sample, statistics and profile
endpoints. Their results are available for download in csv, json or ro-crate [#f3]_ file formats depending on the record
type as shown in the table below.

Most of the API endpoints can be queried by a desired standard. See the **Available Standards for Records** table
below for the record types that can be queried in each standard. This enhances interoperability since systems may be
compliant with other standards.

To query by multiple standards, provide them as a ``%2C%20`` separated in the API :abbr:`URL (Uniform Resource Locator)`.
``%2C%20`` is the encoding URL for the comma (,) character.

For example, to query the endpoint in the standards - Darwin Core (DWC), European Nucleotide Archive (ENA) and
Minimum Information about any (x) Sequence (MIxS), add the separator to the end of the API URL like this:
``?standard=dwc%2C%20ena%2C%20mixs``

By default, the API endpoints will return results in the **tol** (Tree of Life) standard.

Each endpoint results contain metadata provided by the submitter.

.. list-table:: Available Result Formats for Records
   :width: 100%
   :align: center
   :header-rows: 1

   * - File Format
     - Available Record Types
   * - csv
     - Audit, Sample, Manifest
   * - json
     - Audit, Sample, Manifest
   * - ro-crate
     - Sample

.. list-table:: Available Standards for Records
   :width: 100%
   :align: center
   :header-rows: 1

   * - Standard
     - Backronym
     - Available Records Types
   * - dwc
     - Darwin Core
     - Sample, Manifest
   * - ena
     - European Nucleotide Archive
     - Sample, Manifest
   * - mixs
     - Minimum Information about any (x) Sequence
     - Sample, Manifest
   * - tol
     - Tree of Life
     - Sample, Manifest

.. note::

   The live COPO website API endpoints are used in the examples below.

   To use the demo website API endpoints, replace ``https://copo-project.org/api/`` with
   ``https://demo.copo-project.org/api/`` in the examples below.

.. _audit-api-endpoints:

Audit Endpoints
~~~~~~~~~~~~~~~~~~~~

Fetch Sample Updates Between Dates
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/{from}/{to}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/{from}/{to}" -H  "accept: application/json"

This results in a list of sample updates that occurred between a given date period.

Fetch Sample Updates by Manifest ID
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/manifest_id/{manifest_id}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/manifest_id/{manifest_id}" -H  "accept: application/json"

This results in a list of sample updates by manifest :abbr:`IDs (Identifications)` [#f4]_.

Fetch Sample Updates by COPO ID
""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/{copo_id}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/copo_id/{copo_id}" -H  "accept: application/json"

This results in a list of sample updates based on ``{copo_id}``.

Fetch Sample Updates by Update Type
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/update_type/{update_type}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/update_type/{update_type}" -H  "accept: application/json"

This results in a list of sample updates based who performed the update. The ``update_type`` can be **system**
or **user**.

A **system** update occurs when the update was performed by COPO while a **user** update occurs when a user reuploads
a manifest with amended sample metadata.

Please note that not all sample information that has been uploaded already can be updated when the manifest is
reuploaded. Only fields that are updatable are updated when a manifest is reuploaded.

See the :ref:`samples-update` section for more information as well as the
:ref:`Fetch updatable fields by project <sample-api-endpoints-updatable-fields>` API method.


Fetch Sample Updates by Field and Field Value
""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/{field}/{field_value}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/{field}/{field_value}" -H  "accept: application/json"

This results in a list of sample updates based on a sample field value and one of the following sample fields:

* RACK_OR_PLATE_ID
* SPECIMEN_ID
* TUBE_OR_WELL_ID
* biosampleAccession
* public_name
* sraAccession

Fetch Sample Updates by ASG Sample Type
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/asg

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/asg" -H  "accept: application/json"

This results in a list of updates for :abbr:`ASG (Aquatic Symbiosis Genomics)` [#f8]_. sample types.

Fetch Sample Updates by DTOL Sample Type
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/dtol

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/dtol" -H  "accept: application/json"

This results in a list of updates for :abbr:`DToL (Darwin Tree of Life Samples)` [#f9]_. sample types.

Fetch Sample Updates by ERGA Sample Type
""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/audit/sample/erga

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/audit/sample/erga" -H  "accept: application/json"

This results in a list of updates for :abbr:`ERGA (European Reference Genome Atlas)` [#f10]_. sample types.

.. raw:: html

   <hr>

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

Fetch Manifests by Sequencing Centre
""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=<sequencing-centre>

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/sequencing_centre?sequencing_centre=<sequencing-centre>" -H  "accept: application/json"

This results in a list of manifest :abbr:`IDs (Identifications)` [#f4]_ that are associated with the
given ``sequencing_centre``. In the API URL, replace ``<sequencing-centre>`` with the name of the sequencing centre.

The manifest identification can be used to retrieve records in the other endpoints.


Fetch Current Manifest Versions
"""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/manifest/current_version

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/manifest/current_version" -H  "accept: application/json"

This displays the current or latest manifest version of each manifest project brokered through COPO.


Fetch Sample Records in a Manifest by Manifest ID
""""""""""""""""""""""""""""""""""""""""""""""""""""

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

.. hint::

   * The associated project type is the project type that the sample is a subproject of. For example, a sample may be
     associated with a project type of :abbr:`BGE (Biodiversity Genomics Europe)` but the sample itself may be
     an :abbr:`ERGA (European Reference Genome Atlas)` sample.

   * In sample records, the associated project type is referred to as **associated_tol_project** whereas in profile
     records, it is referred to as **associated_type**.

   * To query by multiple associated project types, provide them as a ``%2C%20`` separated in the API URL. ``%2C%20``
     is the URL encoding for the comma (,) character.

     For example, to query the endpoint for the associated project types :abbr:`BGE (Biodiversity Genomics Europe)`
     and :abbr:`ERGA_PILOT (European Reference Genome Atlas - Pilot)`, add ``BGE%2C%20ERGA_PILOT``
     like this: ``sample/associated_tol_project/BGE%2C%20ERGA_PILOT`` to the end of the API URL.

.. code-block:: bash

   https://copo-project.org/api/sample/associated_tol_project/{values}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/associated_tol_project/{values}" -H  "accept: application/json"

This results in a list of all sample records of a given associated project type(s) in COPO.

Fetch Sample Project Fields by Manifest Version
""""""""""""""""""""""""""""""""""""""""""""""""""
.. code-block:: bash

   https://copo-project.org/api/sample/project/manifest_version/fields

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/project/manifest_version/fields" -H  "accept: application/json"

This results in a list of sample fields by project and manifest version.

If no manifest version is provided, the latest manifest version is used. If no project is provided, all project
types are used.

Fetch Sample Records between Dates
"""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/project/manifest_version/fields

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/project/manifest_version/fields}" -H  "accept: application/json"

This results in a list of fields of a project for a given manifest version.

Fetch Sample Records between Dates
"""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/{from}/{to}

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/{from}/{to}" -H  "accept: application/json"

This results in a list of all samples recorded in the given date period.

.. _sample-api-endpoints-updatable-fields:

Fetch Updatable Fields by Project
""""""""""""""""""""""""""""""""""""""""
.. code-block:: bash

   https://copo-project.org/api/sample/updatable_fields/{project}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/updatable_fields/{project}" -H  "accept: */*"

This results in list of fields that can be updated when a manifest is reuploaded/resubmitted in COPO based on the
given ``{project}``.

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

Fetch Sample Records by Biosample Accession
""""""""""""""""""""""""""""""""""""""""""""
.. note::

   * A biosample accession is a unique identifier (ID) that is assigned to a sample record by ENA [#f9]_ after the
     sample has been accepted by a sample manager [#f10]_.
   * The ``biosampleAccession`` is referred to as ``biosampleAccession`` in COPO and ``biosample_id``
     in :abbr:`ENA (European Nucleotide Archive)`.
   * To query by multiple biosample accessions, provide them as a comma separated list in this endpoint.


.. code-block:: bash

   https://copo-project.org/api/sample/biosampleAccession/{biosampleAccessions}

.. centered:: OR

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/biosampleAccession/{biosampleAccessions}" -H  "accept: application/json"

This results in full sample information for the sample record returned from the given ``{biosampleAccessions}``.

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

Fetch Sample Records by Sequencing Centre
""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=<sequencing-centre>

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/sample/sequencing_centre?sequencing_centre=<sequencing-centre>" -H  "accept: application/json"

This results in full sample information for the sample records based on the given ``sequencing_centre``.
In the API URL, replace ``<sequencing-centre>`` with the name of the sequencing centre.

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


Fetch Number of Sample Records by Sample Type and Date
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/stats/number_of_samples

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/stats/number_of_samples" -H  "accept: application/json"

This results in the total number of registered sample records in COPO by a given sample type and date.

If no sample type is provided and no start date and end date are provided, COPO will return the total number
of samples.

Fetch Tree of Life (ToL) Projects Brokered by COPO
""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/stats/tol_projects

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/stats/tol_projects" -H  "accept: application/json"

This results in a list of all main/primary projects brokered by COPO.

Fetch Associated Tree of Life (ToL) Projects Brokered by COPO
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: bash

   https://copo-project.org/api/stats/associated_tol_projects

.. centered:: **OR**

.. code::

   $ curl -X GET "https://copo-project.org/api/stats/associated_tol_projects" -H  "accept: application/json"

This results in a list of all child projects/ subprojects brokered by COPO.


.. raw:: html

   <hr>
   <br><br>


.. rubric:: Footnotes
.. [#f1] See term: :term:`REST`
.. [#f2] See term: :term:`API`
.. [#f3] See term: :term:`RO-Crate`
.. [#f4] See term: :term:`Manifest ID`
.. [#f5] See term: :term:`ASG`.
.. [#f6] See term: :term:`DToL`.
.. [#f7] See term: :term:`ERGA`.
.. [#f8] See term: :term:`DToL`
.. [#f9] See term: :term:`ENA`
.. [#f10] See term: :term:`Sample manager`


..
    Images declaration
..
.. |copo-api-live-server-button| image:: /assets/images/buttons/copo-api-live-server-button-option.png
   :height: 6ex
   :target:  https://raw.githubusercontent.com/collaborative-open-plant-omics/Documentation/main/assets/images/buttons/copo-api-live-server-button-option.png