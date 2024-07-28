.. _copo-project-setup-linux:

Set Up COPO Project on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::
   If you are using a different :abbr:`OS (Operating system)` other than Ubuntu, you can skip this step.
   See :doc:`COPO project guidelines for Windows users <copo-project-setup-windows>` if Windows is your preferred OS.

Install Python
^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo apt -y install software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt -y install python3.8

.. raw:: html

   <hr>

Install Python Development Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo apt -y install python3.8-distutils
   sudo apt -y install build-essential libssl-dev libffi-dev
   sudo apt -y install libxml2-dev libxslt1-dev python3-django
   sudo apt update && sudo apt install -y default-jre rsync git nano libxml2-dev python build-essential make gcc python3-dev locales python3-pip ruby-dev rubygems poppler-utils

.. raw:: html

   <hr>

Install Required Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
   :caption: Install required packages and enable the databases to start on boot

   sudo apt -y install supervisor
   sudo gem install sass
   sudo apt -y install redis mongodb postgresql
   sudo systemctl enable mongodb
   sudo systemctl enable postgresql
   sudo systemctl enable redis

.. code-block:: bash
   :caption: Install MongoDB on your local machine

   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
   echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
   sudo apt update
   sudo apt -y install mongodb-org

.. raw:: html

   <hr>

Install Integrated Development Environment (IDE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Any :abbr:`IDE (Integrated Development Environment)` can be used to work on the project. However, we recommend using
one of the following IDEs:

**PyCharm Professional**

A cross-platform IDE that provides consistent experience on the Windows, macOS, and Linux operating systems.

.. code-block:: bash

   sudo snap install pycharm-professional --classic

.. centered:: **OR**

Visit `PyCharm website <https://www.jetbrains.com/pycharm/download>`__ to download an appropriate version for your
:abbr:`OS (Operating system)` or download it from the
`Ubuntu Software Center <https://snapcraft.io/pycharm-professional>`__.

.. raw:: html

   <br>

**Visual Studio Code**

:abbr:`VSCode (Visual Studio Code)` is a lightweight but powerful source code editor which runs on your desktop and
is available on Windows, macOS and Linux.

It comes with built-in support for JavaScript (JS), TypeScript and Node.js and has a rich ecosystem of extensions for
other languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and Unity).

Visit `VSCode website <https://code.visualstudio.com/download>`__ to download an appropriate version for your
:abbr:`OS (Operating system)` or download it from the `Ubuntu Software Center <https://snapcraft.io/code>`__

.. raw:: html

   <hr>

Configure IDE
^^^^^^^^^^^^^^

PyCharm
""""""""
.. note::
   If using VSCode IDE, you can skip this step.

.. warning::
    If you encounter the error, ``Error: Please enable Django support for the project``, navigate to
    File->Settings->Languages & Frameworks->Django->Enable Django to enable Django support for the project.


If using PyCharm IDE, add a new configuration by following the steps below:

#. Navigate to Add New Configuration
#. Select **Django server**
#. Click **Save**

Visit `Run/debug configurations <https://www.jetbrains.com/help/pycharm/run-debug-configuration.html>`__ to learn how to
create a configuration in PyCharm.

.. raw:: html

   <hr>

VSCode
""""""""
If using VSCode IDE, add a new configuration by following the steps below:

#. Navigate to Run -> Add Configuration
#. Edit the **launch.json** file that is created with the following file contents:

.. literalinclude:: /assets/files/setup/project/launch.json
   :language: json
   :caption: VSCode **launch.json** configuration file contents


Declare Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set secrets in the environment variables in the **.bashrc** file. Activate  **.bashrc** file by running the
command: ``source .bashrc``

If using PyCharm IDE, declare the environment variables in the following places:

* Edit Configurations > Environment variables
* File->Settings->Build, Execution, Deployment->Console->Python console
* File->Settings->Build, Execution, Deployment->Console->Django console
* File->Settings->Languages & Frameworks->Django->Enable Django

Set up Python Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run the following commands within the project directory to set up a Python virtual environment for the project

Alternatively, you can create a virtual environment for the project with the command: ``python3 -m venv venv``

.. code-block:: bash
   :caption: Install packages with pip3 and Python3

    sudo apt install -y python3-virtualenv
    source venv/bin/activate
    pip3 install -r requirements/base.txt
    pip3 install celery
    python manage.py migrate && python manage.py social_accounts && python manage.py setup_groups && python manage.py setup_schemas && python manage.py createcachetable && supervisord -c celery.conf && supervisorctl -c celery.conf start all
    python manage.py createsuperuser

.. warning::
    Here are solutions to possible errors that you might encounter after having ran the above commands:

    * **Possible error #1**: TypeError: 'Collection' object is not callable. If you meant to call the 'authenticate'
      method on a 'Database' object it is failing because no such method exists.

      **Solution #1**: Run the command: ``$ pip3 install pymongo==3.11.4``
      **Reason**: pymongo versions >4 is incompatible with the COPO project

      .. raw:: html

         <hr>

    * **Possible error #2**: Issues related to **importlib**, **rdlib**, **lxml**, **numpy**, **pandas** and **cffi** Python packages

      **Solution #2**:
      #. In the ``requirements/base.txt`` file located in the project directory, change the version numbers for the
      following packages so that all packages can be compatible with each other

        * ``asgiref==3.7.2``
        * ``cffi==1.15.1``
        * ``importlib-metadata==1.6.1``
        * ``lxml==4.9.3``
        * ``numpy==1.20.0``
        * ``pandas==1.2.2``


      #. Change line 12 in **wizard_helper.py** file from ``pandas.io.json import json_normalize`` to
         ``from pandas import json_normalize``
      #. Run the command: ``pip3 install -r requirements/base.txt`` again to install the packages

    * **Possible error #2**: text index required for $text query

      **Solution #3**: Create an index in the SampleCollection in mongoDB: ``db.SampleCollection.createIndex( { "$**": "text" } )``

.. raw:: html

   <br>


Set Up Mongo Database in COPO Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
   Replace the username and password for MongoDB with your username and password

Run the **4_mongo_setup.sh** `MongoDB set up script <https://github.com/TGAC/COPO-production/blob/main/shared_tools/scripts/setup/mongoDB_setup.sh>`__ to configure the MongoDB database on your machine


Set up MongoDB in Studio3T
""""""""""""""""""""""""""""
.. note::
   Replace the ``<username>`` and ``<password>`` for MongoDB with your MongoDB username and password
   By default, the username for MongoDB is ``copo_user``.
   The hostname,``localhost``,, can also be substituted with the IP address of ``127.0.0.1``

Create a new MongoDB connection manually with the following details:

* **Connection Name**: ``copo_mongo``
* **Connection Type**: ``Standalone Connection``
* **Hostname**: ``localhost``
* **Port**: ``27017``
* **Authentication**: Username and Password
* **Username**: ``copo_user``
* **Password**: ``<password>``
* **Authentication Database**: ``admin``

.. centered:: OR

**MongoDB URI**: ``mongodb://copo_user:password@localhost:27017/?retryWrites=true&loadBalanced=false&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin``

.. raw:: html

   <hr>

Set Up PostgreSQL Database in COPO Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Replace the username and password of PostgreSQL with your username and password

Run the **postgresqlDB_setup.sh** `PostgreSQL set up script <https://github.com/TGAC/COPO-production/blob/main/shared_tools/scripts/setup/postgresqlDB_setup.sh>`__ to configure the PostgreSQL database on your machine

.. raw:: html

   <hr>

Launch COPO Website
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
   :caption: Launch COPO website using the following command

   python manage.py runserver

Alternatively, click the **Run** button (i.e the green play button) on the top-right corner of the PyCharm IDE
to launch the website.