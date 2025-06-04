.. _setup-django-admin-interface:

==============================================================
Navigating to, Accessing and Using the Django Admin Interface
==============================================================

The Django Admin interface is a powerful tool for managing a web application’s data and models through a
user-friendly web-based interface.

After having created Django models and adding sample information using management
commands, the Django Admin interface can be used to manage these models easily.

.. seealso::

  * `Official Django documentation <https://docs.djangoproject.com>`__ and the
    `official Python documentation <https://docs.python.org>`__ for more information.

  * :ref:`How to set up COPO project <project-application-structure>`

  * :ref:`How to configure profiles on COPO <profile-setup-index>`

.. raw:: html

   <hr>

1. Setting Up the Admin Interface
----------------------------------

Before you can use the Django Admin interface, you need to ensure that your project is configured correctly:

**Admin App**: Ensure that ``django.contrib.admin`` is included in your **INSTALLED_APPS** setting in ``settings.py``.

.. code-block:: python
    :caption: Snippet of settings.py file

    INSTALLED_APPS = [
        ...
        'django.contrib.admin',
        ...
    ]

**URLs**: Ensure that the admin URLs are included in the project’s ``urls.py`` file.

.. code-block:: python
   :caption: Snippet of urls.py file

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('myapp/', include('myapp.urls')),
    ]

**Superuser**: Create a superuser account to access the admin interface

.. code-block:: bash
   :caption: Command to create a superuser

    python manage.py createsuperuser

Follow the prompts to create a username, email, and password.

.. raw:: html

   <hr>

2. Navigating to the Admin Interface
------------------------------------

**Run the development server**: Ensure that the development server is running.

.. code-block:: bash

    python manage.py runserver

**Access the Admin Interface**: Open your web browser and navigate to http://copo-project.org/admin/. You will be
presented with the Django admin login page.

.. raw:: html

   <hr>

3. Logging into the Admin Interface
-----------------------------------

**Login**: Use the superuser credentials you created earlier to log in. Enter your username and password, then
click the ``Log in`` button.

.. raw:: html

   <hr>

4. Using the Admin Interface
------------------------------

Once logged in, you will be directed to the Django Admin dashboard, which provides an overview of all registered models
and available actions.

**Admin Dashboard Overview**

   **Site Administration**: This section lists all the models registered in the admin site. For example, if you
   registered the :ref:`ProfileType model <profile-setup-profile-type>`, it will appear here.

   See the :ref:`Registering Django models <profile-setup-register-django-model>` section for more information on
   registering models.

**Groups and Users**: By default, Django includes models for managing users and groups.


**Managing Actions**

    **Bulk Actions**: Perform actions on multiple profiles simultaneously, such as deleting multiple profiles.
    **Custom Actions**: Define custom actions for specific tasks.