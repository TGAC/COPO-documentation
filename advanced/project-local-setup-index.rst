.. _project-local-setup-index:

===============================
Setting Up COPO Project Locally
===============================

.. _copo-project-setup-with-docker:

With Docker
------------
The central instance of COPO runs on a pool of three virtual machines. The following set up instructions are structured
in a similar manner using one node. Feel free to make changes for a bigger or smaller pool.

Clone the `GitHub COPO project repository <https://github.com/TGAC/COPO-production>`__.

Visual Studio Code (VSCode) is recommended for running the COPO project after having sat up the Docker environment.
You can download VSCode from `here <https://code.visualstudio.com/>`__ for your local machine.

.. note::

   There are a number of parameters in the command below that need to be updated or you may want to change
   for your local deployment. Please read through carefully.

.. hint::
   A Python virtual environment is not required to run the COPO project application locally since the project is
   running via Docker containers. However, if you would like to run the project locally without Docker and within
   a Python virtual environment, please refer to the
   :doc:`COPO project setup with PyCharm documentation <copo-project-setup-without-docker>`.


.. warning::
   The **ENA_SERVICE** environment variable is set to the ENA development server. All submission to this
   server will be deleted after 24 hours. To submit to the production ENA server remove ``dev`` and set ``prod``.

.. raw:: html

   <hr>

Install Docker
~~~~~~~~~~~~~~
Follow the official `Docker installation documentation <https://docs.docker.com/engine/install/>`__ for your
distribution.

Make changes to your firewall, iptables and security groups to serve a website, use Docker swarm and redis.
The port number will depend on your setup and if you choose to use the default ports for each service.

Initialise Docker Swarm
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: docker
   :caption: Start a Docker swarm

    docker swarm init --advertise-addr <the IP of the machine you want to advertise>

**e.g.** ``$ docker swarm init 127.0.0.1`` where ``127.0.0.1`` is the IP address of localhost.

This command will return a token. You need this token to make the other VMs join the swarm if you plan to use more
than one one node. On the other machines run:

.. code-block:: docker
   :caption: Command to make other VMs join the swarm manager

    docker-swarm join --token <the token returned by the previous command> <the IP advertised previously>:2377

Check out the Docker documentation if you want to change the default port.

.. note::

   You may need to change the following instructions depending on the server you are deploying to.
   Please consider which services need to run in the backend or frontend network.


.. raw:: html

   <hr>

Add Docker Node Labels
~~~~~~~~~~~~~~~~~~~~~~~
Label the node as a web service, nginx service, mongo service, postgres service and backup service. The web service
and nginx service will be deployed on the frontend network. The mongo service, postgres service and backup service
will be deployed on the backend network.

Adding One Docker Node Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. hint::
   ``$HOSTNAME`` is a bash variable that returns the hostname of the machine. You can use the hostname of the machine
   instead of the variable. In a Linux OS, you can run ``$ echo $HOSTNAME`` to get the hostname.

   If you are using more than one node, you will need to label the other nodes as well.

.. code-block:: docker
   :caption: Documentation for the Docker swarm command

   docker node update \
       --label-add web-service=true \
       --label-add nginx-service=true \
       --label-add mongo-service=true \
       --label-add postgres-service=true \
       --label-add backup-service=true \
       $HOSTNAME

Adding More than Docker One Node Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are using more than one Docker node, you can label the other nodes as follows:

**Node 1**

.. code-block:: docker
   :caption: Node 1 Docker label command

   docker node update \
       --label-add web-service=true \
       --label-add nginx-service=true \
       --label-add mongo-service=false \
       --label-add postgres-service=false \
       --label-add backup-service=false \
       copo-0

**Node 2**

.. code-block:: docker
   :caption: Node 2 Docker label command

    docker node update \
            --label-add web-service=false \
        --label-add nginx-service=false \
            --label-add mongo-service=false \
            --label-add postgres-service=true \
            --label-add backup-service=true \
            copo-1

**Node 3**

.. code-block:: docker
   :caption: Node 3 Docker label command

    docker node update \
         --label-add web-service=false \
         --label-add nginx-service=false \
         --label-add mongo-service=true \
         --label-add postgres-service=false \
         --label-add backup-service=false \
         copo-2

.. raw:: html

   <hr>

Create Docker Volumes
~~~~~~~~~~~~~~~~~~~~~~

Docker volumes are used to persist data via the plugin, **local-persist**. This ensures that the data is not lost when
the containers are restarted. Volumes are created on the swarm manager.

Substitute the paths in commands before running it.

.. hint::
    You may need to install curl before running the command below. You can install curl by running
    $ ``sudo apt-get install curl``.

    You may need to install the **local-persist** plugin to persist volumes before running the command below. You can install
    it by running:
    $ ``curl -fsSL https://raw.githubusercontent.com/MatchbookLab/local-persist/master/scripts/install.sh | sudo docker``


.. code-block:: docker
   :caption: Commands to create Docker volumes

    docker volume create -d local-persist -o mountpoint=/path/to/web-data --name=web-data
    docker volume create -d local-persist -o mountpoint=/path/to/static-data --name=static-data
    docker volume create -d local-persist -o mountpoint=/path/to/submission-data --name=submission-data
    docker volume create -d local-persist -o mountpoint=/path/to/logs-data --name=logs-data
    docker volume create -d local-persist -o mountpoint=/path/to/mongo-data --name=mongo-backup
    docker volume create -d local-persist -o mountpoint=/path/to/postgres-data --name=postgres-backup

    docker volume create mongo-data
    docker volume create postgres-data

.. raw:: html

   <hr>

Create Networks on Docker Swarm Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the swarm manager create two networks - one for the frontend and one for the backend. The front-end network will be
used by the web service and the nginx service while the backend network will be used by the database services.

.. code-block:: docker
   :caption: Commands to create Docker networks on the swarm manager

    docker network create -d overlay copo-frontend-network
    docker network create -d overlay copo-backend-network

.. code-block::
   :caption: View networks created on Docker swarm manager

   docker network ls

.. raw:: html

   <hr>

Create Secrets on Docker Swarm Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All secrets are file based. You will need to create some of the keys with third parties
and choose passwords before proceeding with the COPO setup.

.. code-block:: docker
   :caption: Commands to create secrets on Docker swarm manager

   docker secret create copo_mongo_initdb_root_password copo_mongo_initdb_root_password
   docker secret create copo_mongo_user_password copo_mongo_user_password
   docker secret create copo_postgres_user_password copo_postgres_user_password
   docker secret create copo_web_secret_key copo_web_secret_key
   docker secret create copo_orcid_secret_key copo_orcid_secret_key
   docker secret create copo_orcid_client_id copo_orcid_client_id
   docker secret create copo_figshare_consumer_secret_key copo_figshare_consumer_secret_key
   docker secret create copo_figshare_client_id_key copo_figshare_client_id_key
   docker secret create copo_figshare_client_secret_key copo_figshare_client_secret_key
   docker secret create copo_google_secret_key copo_google_secret_key
   docker secret create copo_twitter_secret_key copo_twitter_secret_key
   docker secret create copo_facebook_secret_key copo_facebook_secret_key
   docker secret create copo_webin_user copo_webin_user
   docker secret create copo_webin_user_password copo_webin_user_password
   docker secret create copo-project.crt copo-project.crt
   docker secret create copo-project.key copo-project.key
   docker secret create copo_nih_api_key copo_nih_api_key
   docker secret create copo_public_name_service_api_key copo_public_name_service_api_key
   docker secret create copo_mail_password copo_mail_password
   docker secret create copo_bioimage_path copo_bioimage_path
   docker secret create ecs_secret_key ecs_secret_key

.. code-block:: docker
   :caption: View secrets created on Docker swarm manager

   docker secret ls

.. raw:: html

   <hr>

Build COPO Project Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the Dockerfile :download:`Dockerfile_local  <../assets/files/setup/Dockerfile_local>`.
for your local machine.

Place the downloaded Dockerfile in the COPO project root directory.

Alternatively, you can use the Dockerfile present in the root project directory :download:`Dockerfile for demonstration environment <https://raw.githubusercontent.com/TGAC/COPO/development/services/web20/Dockerfile>`.

.. note::
    The Dockerfile is configured to build the **local_copo_web** container image with the tag, ``v1.0.1``. If you have
    a different tag and container name, you will need to change the Dockerfile accordingly.

    If you are using a Mac OS, download the :download:`Dockerfile_mac  <../assets/files/setup/Dockerfile_mac>`.


Visit `here <https://docs.docker.com/get-started/02_our_app/>`__ for more information on how to build an application
with a Docker image.


.. code-block:: bash
   :caption: Navigate to COPO project root directory

    cd <path-to-project-root-directory>/COPO

.. code-block:: docker
   :caption: Build Docker image

    docker build . -f  Dockerfile_local -t local_copo_web:v1.0.1

.. raw:: html

   <hr>

Deploy Docker Image on Docker Swarm Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **redis**, **postgres** and **mongo** Docker services are created on the swarm manager. Download the
:download:`local compose file </assets/files/setup/local_copo.compose.yaml>` file to create the services.

Alternatively, you can download :download:`compose file for demonstration environment
<https://raw.githubusercontent.com/TGAC/COPO/development/services/copo.compose.yaml>`.

Replace the ``<path-to-project-root-directory>`` with the absolute path to the COPO project root directory.

.. note::
    The Docker compose file is configured to use the secrets and volumes created above. If you have used different
    names for the secrets and volumes, you will need to change the compose file accordingly.

    If you are using a Mac OS, download the :download:`Mac compose file  </assets/files/setup/mac_copo.compose.yaml>`.

    The following commands should be run from the root directory of the COPO project.

.. warning::
   The **ENA_SERVICE** environment variable is set to the ENA development server. All submission to this
   server will be deleted after 24hours. To submit to the production ENA server remove \"dev\"

.. code-block:: bash
   :caption: Edit Compose file to container tag e.g. local_copo_web:v1.0.1

   nano local_copo.compose.yaml

Update the tag, save the file then, exit by inputting: ``CTRL + O`` then, ``ENTER`` then, ``CTRL + X``

.. code-block:: docker
   :caption: Command to deploy Docker image, local_copo_web:v1.0.1

    docker stack deploy --compose-file '<path-to-file>/local_copo.compose.yaml' copo

.. raw:: html

   <br>

.. collapse:: Compose file to configure COPO project application locally with Docker

   .. literalinclude:: /assets/files/setup/local_copo.compose.yaml
      :language: yaml
      :caption: Local Compose file for COPO project application

.. raw:: html

   <br>

.. code-block:: docker
    :caption: View services created on Docker swarm manager

     docker service ls
     docker ps
     docker ps -a

.. code-block:: docker
    :caption: Inspect created image and check if it is running
    
     docker image inspect local_copo_web:v1.0.1

.. code-block:: docker
    :caption: Start ``copo_web`` Docker container (if it is not started)
    
     docker service scale copo_web=1

.. code-block:: docker
    :caption: Command to stop ``copo_web`` Docker container
    
     docker service scale copo_web=0

.. raw:: html

   <hr>

Set up PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~

In the terminal, navigate to the root directory of the COPO project application then, run the following commands.:

.. hint::
    Retrieve the **local_copo_web** container ID by running the $ ``docker ps`` command below in the root project
    directory of the COPO project application in the terminal for the **local_copo_web:v1.0.1**  Docker image.

.. code-block:: docker
   :caption: Install PostgreSQL database version 9.6 in terminal

    docker run --name postgresql -e POSTGRES_USER=<postres-username> -e POSTGRES_PASSWORD=<postres-password> -p 5432:5432 -v /data:/var/lib/postgresql/data -d postgres:9.6

Replace ``<postgres-username>`` and ``<postgres-password>`` with the username and password for PostgreSQL database respectively.

.. code-block:: docker
   :caption: Enter the **local_copo_web** container

    docker exec -it <local_copo_web-container-id> bash

.. code-block:: python
   :caption: Setup scripts to be run in the **local_copo_web** Docker container

   python manage.py makemigrations
   python manage.py makemigrations chunked_upload
   python manage.py makemigrations allauth
   python manage.py migrate
   python manage.py setup_groups
   python manage.py setup_schemas
   python manage.py createcachetable
   python manage.py social_accounts

.. code-block:: python
   :caption: Install Python requirements for the project

   python manage.py makemigrations
   python manage.py makemigrations chunked_upload
   python manage.py makemigrations allauth
   python manage.py migrate
   python manage.py setup_groups
   python manage.py setup_schemas
   python manage.py createcachetable
   python manage.py social_accounts

.. code-block:: python
   :caption: Create a Django admin/superuser

   python3 manage.py createsuperuser

Enter the required details to create the Django admin/superuser. The Django admin/superuser can log into the COPO
project application from the local `Django admin website <http://127.0.0.1:8000/admin>`__.

.. code-block:: bash
   :caption: Exit the **local_copo_web** Docker container

   CTRL + P
   CTRL + Q
   exit

The commands above can be accessed in the :download:`postgresqlDB_setup.sh script <https://raw.githubusercontent.com/TGAC/COPO/development/setup_scripts/postgresqlDB_setup.sh>`.
This file is located in the **set_up_scripts** directory of the COPO project root directory.

.. raw:: html

   <br>

In the following steps, we will create the PostgreSQL database for the COPO project application in the
root directory of the project.

.. hint::
    Retrieve the PostgreSQL container ID by running the command below in the root project directory of the COPO project
    application in the terminal for the **postgres:9.6**  Docker image:
    $ ``docker ps``

.. code-block:: docker
   :caption: Enter the PostgreSQL container

    docker exec -it <postgres-container-id> bash

.. code-block:: bash
   :caption: Run setup scripts in the PostgreSQL Docker container

   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c 'DELETE FROM socialaccount_socialapp_sites'
   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c 'DELETE FROM django_site'
   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c 'DELETE FROM socialaccount_socialapp'
   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c "INSERT INTO django_site (id, domain, name) VALUES (1, 'www.copo-project.org', 'www.copo-project.org')"
   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c "INSERT INTO socialaccount_socialapp (id, provider, name, client_id, secret, key) VALUES (1, 'orcid', 'Orcid', '$ORCID_CLIENT_ID', '$ORCID_SECRET', '')"
   psql -h 'localhost' -U  $POSTGRES_USER -d 'copo' -c 'INSERT INTO socialaccount_socialapp_sites (id, socialapp_id, site_id) VALUES (1, 1, 1)'

The commands above can be accessed in the :download:`postgresqlDB_setup.sh script <https://raw.githubusercontent.com/TGAC/COPO/development/setup_scripts/postgresqlDB_setup.sh>`.
This file is located in the **set_up_scripts** directory of the COPO project root directory.

.. raw:: html

   <hr>

Updating COPO Website Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The COPO project is updated frequently and as such is under active development. To update your instance to a newer
(or the latest) version, download the
:download:`local compose file </assets/files/setup/local_copo.compose.yaml>`  or the :download:`compose file for
demonstration environment
<https://raw.githubusercontent.com/TGAC/COPO/development/services/copo.compose.yaml>`
on the swarm manager or root directory of the project if you have one node.

Then, run the following commands in the terminal:

.. note::

   The Docker tag below needs to be changed to reflect the most recent version available in DockerHub.
   Please check the latest version there. You can safely ignore the \*feature tags as they are not stable releases.
   For stable releases look for ``*rc``.

.. hint::

    * Retrieve the **copo-web** container ID by running the $ ``docker ps`` command below in the root project
      directory of the COPO project application in the terminal for the **copo/copo-web:v1.0.1**  Docker image.

    * To check if the web service is running, run the command below in the root project directory of the COPO project
      application in the terminal for the **copo/copo-web:v1.0.2**  Docker image:
      $ ``docker logs -f <container-ID-for-updated-copo-web>``

    * If you update often we recommend taking care of removing old docker images regularly.

.. code-block:: bash
   :caption: Edit Compose file by updating the Docker container tag on the Docker swarm manager

   nano local_copo.compose.yaml

Update the Docker tag, save the file then, exit it by inputting: ``CTRL + O`` then, ``ENTER`` then, ``CTRL + X``

.. code-block:: docker
   :caption: Command to deploy updated Docker image: local_copo_web:v1.0.2 on the Docker swarm manager

    docker stack deploy --compose-file '<path-to-file>/local_copo.compose.yaml' copo

.. raw:: html

   <hr>

Launch COPO Website
~~~~~~~~~~~~~~~~~~~
The COPO project application can be accessed locally on `port 8100 <http://127.0.0.1:8100/>`__ via the VSCode browser
extension.

Within the VSCode IDE browser, add a new configuration by following the steps below:

#. Navigate to Run -> Add Configuration
#. Edit the **launch.json** file that is created with the following file contents:

.. collapse:: VSCode configuration file

   .. literalinclude:: /assets/files/setup/launch.json
      :language: json
      :caption: VSCode **launch.json** configuration file contents

.. raw:: html

   <br>

The COPO project application can be accessed locally on `on port 80000 <http://127.0.0.1:8000>`__
or `on port 81000 <http://127.0.0.1:8000>`__.


.. note::
   Install required VSCode extensions for the COPO project application by following the steps below:

    #. Navigate to the **Extensions** tab on the left-hand side of the VSCode IDE
    #. Search for and install the following extensions:

       * Python   (required)


   If your local machine is restarted, you will need to start the Docker container again at startup. To do this, run the
   following command in the terminal: $ ``docker start <container-ID-for-copo-web>``. You can retrieve the container ID
   by running the command below in the root project directory of the COPO project application in the terminal for the
   **copo/copo-web:v1.0.2**  Docker image: $ ``docker ps``

.. raw:: html

   <hr>

Tips
~~~~~

* Enable **Manage Unsafe Repositories** in **Source Control** in VSCode browser application to allow VSCode to access
  the COPO GitHub project repository.

* Install the following VSCode extensions:

   * GitHub Copilot
   * Prettier - Code formatter
   * Git Extension Pack

.. code-block:: bash
   :caption: Set GitHub configuration in terminal

   git config --global user.name "<GitHub-username>"
   git config --global user.email "<GitHub-email-address>"

.. code-block:: bash
   :caption: Create a tag via the terminal

   git tag <tagname>

.. code-block:: bash
   :caption: Push a particular tag to GitHub via the terminal

   git push origin <tagname>

.. code-block:: bash
   :caption: Remove an existing tag from GitHub via the terminal

   git tag -d <tag-name>

.. code-block:: docker
   :caption: Docker command used to list all the running Docker containers

   docker ps

.. code-block:: docker
   :caption: Docker command used to start, stop and restart a Docker service

   sudo systemctl start docker
   sudo systemctl stop docker
   sudo systemctl restart docker

.. code-block:: docker
   :caption: Docker command used to start, stop and restart a container respectively

   docker start
   docker stop
   docker restart

.. code-block:: docker
   :caption: Docker command used to execute a command in a running container

   docker exec it <container-ID> bash

.. code-block:: docker
   :caption: Docker command used to find the installed version of docker

   docker version

.. code-block:: docker
   :caption: Docker command used to know the details of all the running, stopped, or exited containers

   docker ps -a

.. code-block:: docker
   :caption: Docker command used to create a volume so that the docker container can use it to store data

   docker volume create <volume-name>

.. raw:: html

   <hr>

.. include:: copo-project-setup-without-docker.rst


