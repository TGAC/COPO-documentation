.. _project-application-structure:

====================================
COPO Project Application Structure
====================================

Before setting up the project, it is essential to understand the structure of a Django project and application. This
knowledge will help you navigate the project and locate the necessary files for setting up the project.

COPO uses the Django framework to build the application, which follows the Model-View-Template (MVT) architecture. In
this architecture, the model represents the data structure, the view handles the logic and the template manages the
presentation.

A Django project consists of one or more applications, each of which contains models, views, templates, and other
components that define the functionality of the application.

A typical structure of a Django project looks like this:

.. code-block:: bash

     myproject/
         manage.py
         myproject/
             __init__.py
             settings.py
             urls.py
             wsgi.py
             asgi.py
         myapp/
             __init__.py
             admin.py
             apps.py
             models.py
             tests.py
             views.py
             migrations/
                 __init__.py
             templates/
             static/
             forms.py
             urls.py

.. raw:: html

   <br>

.. seealso::

   * :ref:`Profile Structure <profile-structure>`

.. raw:: html

   <hr>

Project Root Directory (myproject/)
-----------------------------------

**manage.py**: A command-line utility that lets you interact with your Django project. You use this to run commands
like runserver, makemigrations, migrate etc.

Project Directory (myproject/myproject/)
----------------------------------------

**__init__.py**: An empty file that tells Python that this directory should be considered a Python package.

**settings.py**: Contains all the settings and configuration for your Django project (database settings, installed apps, middleware, etc.).

**urls.py**: The URL declarations for this Django project; a "table of contents" of your Django-powered site.

**wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project. Used for deployment.

**asgi.py**: An entry-point for ASGI-compatible web servers to serve your project. Used for deployment with asynchronous support.

Application Directory (myproject/myapp/)
-----------------------------------------

.. seealso::

   Refer to the :ref:`profile-setup-component-creation` section for insights into creating Django applications for each
   component used in the COPO project

**__init__.py**: An empty file that tells Python that this directory should be considered a Python package.

**admin.py**: Register your models here to make them accessible via the Django admin interface.

**apps.py**: Contains the application configuration class.

**models.py**: Define your database models here.

**tests.py**: Write your tests here.

**views.py**: Define your view functions or class-based views here.

**migrations/**: This directory contains database migration files.

        **__init__.py**: An empty file that tells Python that this directory should be considered a Python package.

**templates/**: Contains HTML templates for your application.

**static/**: Contains static files (:abbr:`CSS (Cascading Style Sheets)`, :abbr:`JS (JavaScript)`, images) for your application.

**forms.py**: Define your form classes here.

**urls.py**: Define URL patterns specific to this application.