.. _profile-setup-component:

Component
~~~~~~~~~

Components [#f1]_ are individual elements or modules that make up the profile. These can include various functionalities or
data points that contribute to the profile's overall purpose.

.. seealso::

   * :ref:`Defining Component Django model <django-model-definition>`
   * `ProfileType structure <profile-setup-profile-type>`_
   * `RecordActionButton structure <profile-setup-record-action-button>`_
   * `TitleButton structure <profile-setup-title-button>`_

..
   * :ref:`Genomics profile components <genomics-profile-components>`
   * :ref:`ToL profile components <tol-profile-components>`
   * :ref:`Accessions profile component <accessions-component>`

.. raw:: html

   <hr>

Component Database Table Structure
-----------------------------------

Each component that make up a profile has specific settings and functionalities that contribute to the profile's
overall purpose.

The PostgreSQL table **Component** consists of the following fields:

* ``id`` (Integer): The unique identifier for the component
* ``name`` (String): The name of the component
* ``title`` (String): The display title of the component
* ``widget_icon`` (String): The icon associated with the component
* ``widget_colour`` (String): The colour associated with the component, used for UI elements
* ``widget_icon_class`` (String): The :abbr:`CSS (Cascading Style Sheets)` class for the icon
* ``table_id`` (String): The identifier for the associated table
* ``reverse_url`` (String): The URL used for reversing the component
* ``subtitle`` (String): The subtitle of the component, providing additional context

.. hint::

   Click the |collapsible-item-arrow| button below to view the contents

.. collapse:: Component database fields

   .. code-block:: bash

       id |         name         |        title         | widget_icon  | widget_colour | widget_icon_class  |      table_id       |                    reverse_url                     |      subtitle
      ----+----------------------+----------------------+--------------+---------------+--------------------+---------------------+----------------------------------------------------+---------------------
        1 | profile              | Work Profiles        |              |               |                    | copo_profiles_table |                                                    | #component_subtitle
        2 | accessions           | Accessions           | sitemap      | pink          | fa fa-sitemap      | accessions_table    | copo_accession:copo_accessions                     |
        3 | accessions_dashboard | Accessions           | pink         |               | fa fa-sitemap      | accessions_table    | copo_accession:copo_accessions                     |
        4 | assembly             | Assembly             | puzzle piece | violet        | fa fa-puzzle-piece | assembly_table      | copo_assembly_submission:copo_assembly             |
        5 | taggedseq            | Barcoding Manifests  | barcode      | red           | fa fa-barcode      | tagged_seq_table    | copo_barcoding_submission:copo_taggedseq           | #component_subtitle
        6 | files                | Files                | file         | blue          | fa fa-file         | files_table         | copo_file:copo_files                               |
        7 | sample               | Samples              | filter       | olive         | fa fa-filter       | sample_table        | copo_sample:copo_samples                           |
        8 | read                 | Reads                | dna          | orange        | fa fa-dna          | read_table          | copo_read_submission:copo_reads                    | #component_subtitle
        9 | seqannotation        | Sequence Annotations | tag          | yellow        | fa fa-tag          | seqannotation_table | copo_seq_annotation_submission:copo_seq_annotation |

.. raw:: html

   <br><br>

.. collapse:: Description of each Component record

   .. raw:: html

      <br>

   * **profile**: Work Profiles component
         The first step to getting work done in COPO is to create a work profile. A profile is a collection of
         'research objects' or components that form part of your research project or study.

   * **accessions** and **accessions_dashboard**:

         Both relate to the accessions component. The accessions component provides a platform for retrieving and
         analysing biological samples that have biosample accession, SRA accession and submission accession associated
         with them as part of a project after the samples have been accepted.

   * **assembly**: Assembly component

         The assembly component provides a platform for aligning and merging fragments of a Deoxyribonucleic acid (DNA)
         sequence to reconstruct the original structure of the DNA.

   * **taggedseq**: Barcoding Manifests component

         This component provides a platform for submitting assembled and annotated sequences
         representing interesting features or gene regions.

   * **files**: Files component
         With this component, files can be uploaded from a cluster or from one's local (computer) system.

   * **sample**: Samples component

         Biological samples, obtained as part of a project, are described and managed in this component.

   * **read**: Reads component

         This component is associated with assembled and annotated sequences representing interesting features or
         gene regions.

   * **seqannotation**: Sequence Annotations component

         Specific features, in this component, are marked in a Deoxyribonucleic acid (DNA), Ribonucleic acid (RNA) or
         protein sequence with descriptive information about structure or function. Sequence annotations are usually
         done after a genome is sequenced and assembled.

.. raw:: html

   <hr>

.. _profile-setup-component-creation:

Creation of Component
----------------------

.. note::

   * This section assumes that you have installed Django, Python and created a Django project.

   * The migrations folder is automatically created within your app directory when you create your app. It contains
     database migration files.

.. seealso::

   * :ref:`Django application structure <project-application-structure>`  for an snapshot of Django
     application's structure

To create a component in the project, a Django application has to be created for the component. Then, the component has
to be associated with a profile type defined in the `ProfileType structure <profile-setup-profile-type>`_ section.
This association will allow the component to be accessible and visible on the **Work Profiles** web page.

Explore the implementation details of each component of the Django application used in the COPO project through the
links provided below:

* |globe| `Accessions component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_accession>`__

* |globe| `Assembly component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_assembly_submission>`__

* |globe| `Barcoding component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_barcoding_submission>`__

* |globe| `Files component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_file>`__

* |globe| `Reads component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_read_submission>`__

* |globe| `Samples component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_sample>`__

* |globe| `Sequence Annotations component Django application <https://github.com/TGAC/COPO-production/tree/main/src/apps/copo_seq_annotation_submission>`__

Other Django applications created in the COPO project can be found in the ``src/apps`` folder of the
`COPO GitHub repository <https://github.com/TGAC/COPO-production/tree/main/src/apps>`__.

.. raw:: html

   <hr>

.. code-block:: bash
   :caption: Navigate to the project directory

   cd /path/to/project

.. code-block:: bash
   :caption: Create a new Django application using the startapp command

   python manage.py startapp myapp

.. code-block:: python
   :caption: Register app by adding it to the INSTALLED_APPS list in myproject/settings.py

    INSTALLED_APPS = [
        # ... other installed apps,
        'myapp',
    ]

.. code-block:: bash
   :caption: Create a static folder inside the app directory to store static files like CSS, JavaScript and images:

    mkdir myapp/static

.. code-block:: bash
   :caption: Create a css folder inside the static folder in the app directory to store  CSS files

    mkdir myapp/static/myapp/css
    cd myapp/static/myapp/css
    touch myapp.css

.. code-block:: bash
   :caption: Create a JavaScript (js) folder inside the static folder in the app directory to store JavaScript files

    mkdir myapp/static/myapp/js
    cd myapp/static/myapp/js
    touch myapp.js

.. code-block:: bash
   :caption: Create a templates folder inside the app directory to store HTML templates

    mkdir -p myapp/templates/myapp

.. code-block:: python
   :caption: Set up the configuration of the app in the an apps.py file inside the app directory

   from django.apps import AppConfig

   class MyappConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'myapp'


.. code-block:: python
   :caption: Define URL routes in the urls.py file inside the app directory

   from django.urls import path
   from . import views

   urlpatterns = [
      path('', views.index, name='index')
   ]

.. code-block:: python
   :caption: Define view functions in the views.py file inside the app directory

   from django.shortcuts import render
   from .models import ProfileType, Component

   def index(request):
       profile_type_models = ProfileType.objects.all()
       component_models = Component.objects.all()

       return render(request, 'myapp/index.html', {'profile_type_def': profile_type_models, 'component_def': component_models})

.. raw:: html

   <hr>

* Create an ``component.html`` file inside myapp/templates/myapp:

.. collapse:: Component example template

   .. literalinclude:: /assets/files/setup/profile/component.html
      :language: html

.. raw:: html

   <hr>

Create the following files in the application directory:

* ``admin.py`` - to register models with the Django admin site. See the
  :ref:`Registering Django models <profile-setup-register-django-model>` section for more information.

* ``models.py`` - to define database models. See the :ref:`Defining Django models <django-model-definition>` section
  for more information.

* ``tests.py`` - to write tests for the Django application.

.. raw:: html

   <hr>

.. _visual-representation-component:

Visualisation of Created Component
-----------------------------------

.. figure:: /assets/images/django_admin_interface/profile/component/visualisation_component_button_tol_profile_components.png
   :alt: Viewing components associated with a profile on the 'Work Profiles' web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/django_admin_interface/profile/component/visualisation_component_button_tol_profile_components.png
   :class: with-shadow with-border
   :height: 400px

   **Tree of Life Profile: Components**

* The following components make up a :abbr:`ToL (Tree of Life)` [#f2]_ profile:

  * |accessions-component-button|
  * |assembly-component-button|
  * |barcoding-manifest-component-button|
  * |files-component-button|
  * |reads-component-button|
  * |samples-component-button|
  * |sequence-annotations-component-button|

Each profile will have a set of components that are associated with it. These components will be displayed on a profile
on the **Work Profiles** web page.

Components will also appear to the top-right of web pages for easy navigation to them, depending on the component that
is being viewed. For example,the **Reads** component leads to the **Reads** web page and the other components are
displayed as indicated by the arrows in the image below:

.. figure:: /assets/images/django_admin_interface/profile/component/visualisation_component_button_on_specific_web_page.png
   :alt: Profile types web page
   :align: center
   :target: https://raw.githubusercontent.com/TGAC/Documentation/main/assets/images/django_admin_interface/profile/component/vvisualisation_component_button_on_specific_web_page.png
   :class: with-shadow with-border
   :height: 300px

   **Reads web page: Other components are displayed at the top-right of the screen and can be clicked for easy navigation**

If the current web page is not the **Reads** web page, the **Reads** component, |reads-icon|, will be displayed at the
top-right corner of the web page.

.. raw:: html

   <hr>

.. rubric:: Footnotes

.. [#f1] Also known as profile component. See term: :term:`Profile component`.

         Research objects refer to files, reads, assemblies, files samples,
         barcodes (also known as targeted sequences in European Nucleotide Archive (ENA)) and sequence annotations.

         A Tree of Life (ToL) profile is considered as a *project* research object.

.. [#f2] See term: :term:`Tree of Life (ToL) <ToL>`.

..
    Images declaration
..

.. |collapsible-item-arrow| image:: /assets/images/buttons/collapsible_item_arrow.png
   :height: 2ex
   :class: no-scaled-link

.. |accessions-component-button| image:: /assets/images/buttons/components_accessions_button.png
   :height: 3ex
   :class: no-scaled-link

.. |assembly-component-button| image:: /assets/images/buttons/components_assembly_button.png
   :height: 3ex
   :class: no-scaled-link

.. |barcoding-manifest-component-button| image:: /assets/images/buttons/components_barcoding_manifest_button.png
   :height: 3ex
   :class: no-scaled-link

.. |files-component-button| image:: /assets/images/buttons/components_files_button.png
   :height: 3ex
   :class: no-scaled-link

.. |reads-component-button| image:: /assets/images/buttons/components_reads_button.png
   :height: 3ex
   :class: no-scaled-link

.. |reads-icon| image:: /assets/images/buttons/reads-icon.png
   :height: 3ex
   :class: no-scaled-link

.. |samples-component-button| image:: /assets/images/buttons/components_samples_button.png
   :height: 3ex
   :class: no-scaled-link

.. |sequence-annotations-component-button| image:: /assets/images/buttons/components_sequence_annotations_button.png
   :height: 3ex
   :class: no-scaled-link

..
    Unicode declaration
..

.. |globe| unicode:: U+1F310

.. |section| unicode:: U+1F4D6