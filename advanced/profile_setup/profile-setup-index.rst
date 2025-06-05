.. _profile-setup-index:

================================
Profile Setup via Python/Django
================================

Django Admin is a powerful and flexible interface for managing and configuring data models within a Django application.
In this section, we will explore how to set up and configure a profile consisting of several subparts: **ProfileType**,
**Component**, **RecordActionButton** and **TitleButton**. Each of these subparts will have its own Django Admin
model, enabling comprehensive management through the Django Admin interface.

Before setting up the profile, it is essential to understand the structure of a Django project and application. This
knowledge will help you navigate the project and locate the necessary files for configuring the profile.

See :ref:`Project Application Structure <project-application-structure>` section for more information.

.. note::

   This section assumes that you have a basic understanding of Django and Python.

   If you are new to them, you can refer to the `official Django documentation <https://docs.djangoproject.com>`__ and
   the `official Python documentation <https://docs.python.org>`__ for more information.

.. seealso::

   * :ref:`How to set up COPO project <project-local-setup-index>`

.. raw:: html

   <hr>


.. _profile-structure:

1. Defining the Profile Structure
-----------------------------------

The profile [#f1]_ setup is designed to be modular and extensible, with each subpart encapsulated in its own model.
This modularity ensures that each component can be managed independently while still being part of a cohesive profile
configuration.

Each subpart has its own PostgreSQL table and corresponding Django Admin model, which facilitates the management of
complex configurations within a profile.

By understanding the purpose and configuration of each subpart, administrators can efficiently manage complex profiles
and their components, enhancing the overall functionality and usability of the Django application.

Click the desired link below for guidance on configuring and setting up each subpart.

.. toctree::
   :titlesonly:

   profile-setup-profile-type
   profile-setup-component
   profile-setup-record-action-button
   profile-setup-title-button

.. raw:: html

   <hr>

.. _django-model-definition:

2. Defining Django Model
--------------------------

Define the  model in a ``models.py`` Python file: This file will contain the model definition that represents the
structure of the  database table.

.. note::

   The  ``models.py`` file should be located in the same directory as the ``admin.py`` file. It can be used to define
   all models for the Django application. There is **no** need to create a separate model file for each model.

.. hint::

   * Click the |collapsible-item-arrow| button below to view the contents of the Python Django model file.

   * View the actual implementation of the models used in the `COPO project <https://raw.githubusercontent.com/TGAC/COPO-production/main/src/apps/copo_core/models.py>`__
     on GitHub.

.. collapse:: ProfileType Django Model

   .. literalinclude:: /assets/files/setup/profile/profile_type_model.py
      :language: python
      :caption: ProfileType Python Django model definition

.. raw:: html

   <br>

.. collapse:: Component Django Model

   .. literalinclude:: /assets/files/setup/profile/component_model.py
      :language: python
      :caption: Component Python Django model definition

.. raw:: html

   <br>

.. collapse:: RecordActionButton Django Model

   .. literalinclude:: /assets/files/setup/profile/record_action_button_model.py
      :language: python
      :caption: RecordActionButton Python Django model definition

.. raw:: html

   <br>

.. collapse:: TitleButton Django Model

   .. literalinclude:: /assets/files/setup/profile/title_button_model.py
      :language: python
      :caption: TitleButton Python Django model definition


.. raw:: html

   <hr>

.. _profile-setup-register-django-model:

3. Registering Django Model with Django Admin site
-----------------------------------------------------

This step makes the model available in the Django Admin interface after the model has been defined.

An admin class can be defined in the ``admin.py`` file to describe how the model is displayed in the Django Admin
interface. the display and behaviour of each field in the model can be customised on the Django admin interface like
filters, search fields and more.

No admin class is required if you want to use the default Django Admin interface for the model. The example below
demonstrates how to register a model with the default Django Admin interface using the ``admin.site.register()`` method.

The ``admin.site.register()`` method associates the model with the admin class and makes it available in the
Django Admin interface.

.. note::

   * The  ``admin.py`` file should be located in the same directory as the ``models.py`` file. It can be used to register
     all models with the Django Admin interface. There is **no** need to create a separate admin file for each model.

   * Replace ``ModelName`` with the actual model name in the code snippet below.

.. hint::

   View the actual implementation of the ``admin.py`` file used in the `COPO project <https://raw.githubusercontent.com/TGAC/COPO-production/main/src/apps/copo_core/admin.py>`__
   on GitHub.

.. code-block:: python

   # admin.py
   from django.contrib import admin
   # Import the model. Replace ModelName with the actual model name
   from .models import ModelName

   # Register the admin class with the associated model
   admin.site.register(ModelName)

.. raw:: html

   <hr>

.. _profile-setup-migrating-django-models:

4. Make Migrations and Migrate the Django Model
------------------------------------------------

.. important::

   Skipping these steps means that the database will not reflect the changes in the models, leading to
   inconsistencies and errors when you try to interact with the database through Django.

Running the Python ``makemigrations`` and ``migrate`` commands are essential after creating and registering a
Django model because these commands handle the creation and application of database schema changes based on the
model definitions.

The ``makemigrations`` command is responsible for generating migration files based on the changes in the models
while the ``migrate`` command is responsible for applying the migrations to the database.

To create and apply migrations, run the following commands in the terminal:

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

.. raw:: html

   <hr>

.. _creating-setup-profile-python-command:

5. Automating Profile Creation with manage.py
---------------------------------------------

After defining and registering the models, you can automate the creation of profiles and their subparts using a
management command in Django. This approach streamlines the setup process, ensuring consistency and reducing manual
effort.

Management Command
~~~~~~~~~~~~~~~~~~

Create a new management command by adding a file ``setup_profile_types.py`` in the Django app’s ``management/commands``
directory.

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents of the **setup_profile_types.py** Python management
   command file.

   The actual implementation may vary based on your specific requirements.

   Click `here <https://raw.githubusercontent.com/TGAC/COPO-production/main/src/apps/copo_core/management/commands/setup_profile_types.py>`__
   to view the actual implementation of the management command used in the COPO project.

.. collapse:: Setup profile management command

   .. literalinclude:: /assets/files/setup/profile/setup_profile_types.py
      :language: python
      :caption: Python **setup_profile_types.py** Python management command file contents

.. raw:: html

   <br><br>

To run this command, use:

.. code-block:: bash

   python manage.py setup_profile_types

This command will automatically setup a profile with the predefined subparts, ensuring a quick and consistent setup.

.. raw:: html

   <hr>

.. _visual-visual-representation-profile-subparts:

Visual Representation of Profile Subparts within COPO Project
----------------------------------------------------------------

Click the link below to view a visual representation of the profile subparts within the COPO project.

* :ref:`Profile type <visual-representation-profile-type>`

* :ref:`Component <visual-representation-component>`

* :ref:`RecordActionButton <visual-representation-record-action-button>`

* :ref:`TitleButton <visual-representation-title-button>`

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as COPO profile. See: :term:`COPO profile or work profile<COPO profile>`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. Indices and tables
.. ==================
..
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`