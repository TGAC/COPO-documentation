Environment Set Up
==================

We are running the central instance of COPO on a pool of three virtual machines and the documentation is structured for a similar set up. Feel free to make changes for a bigger or smaller pool.

Install Docker (follow the official `documentation <https://docs.docker.com/engine/install/>`_ for your distribution).

Make changes to your firewall, iptables and security groups to serve a website, use Docker swarm and redis. Which ports will depends on your setup and if you choose to use the default ports for each service.


Start a Docker swarm. On the swarm manager machine run::

	docker swarm init --advertise-addr <the IP of the machine you want to advertise>

This command will return a token. You need this token to make the other VMs join the swarm. On the other machines run::

	docker-swarm join --token <the token returned by the previous command> <the IP advertised previously>:2377

Check out the Docker documentation if you want to change the default port.

.. note:: You may need to change the following instructions depending on the server you are deplying to. Please consider which services need to run in the backend or frontend network.

Now you can label the nodes:

Node 1::

	docker node update \
		--label-add web-service=true \
		--label-add nginx-service=true \
		--label-add mongo-service=false \
		--label-add postgres-service=false \
		--label-add backup-service=false \
		copo-0

Node 2::

	docker node update \
	        --label-add web-service=false \
		--label-add nginx-service=false \
	        --label-add mongo-service=false \
	        --label-add postgres-service=true \
	        --label-add backup-service=true \
	        copo-1

Node 3::

	docker node update \
	     --label-add web-service=false \
	     --label-add nginx-service=false \
	     --label-add mongo-service=true \
	     --label-add postgres-service=false \
	     --label-add backup-service=false \
	     copo-2

Install a plugin to persist volumes::

	curl -fsSL https://raw.githubusercontent.com/CWSpear/local-persist/master/scripts/install.sh | sudo bash

Create volumes on the manager. Make sure to subsitute your paths in the below commands before running it::

	docker volume create -d local-persist -o mountpoint=/path/to/web-data --name=web-data
	docker volume create -d local-persist -o mountpoint=/path/to/static-data --name=static-data
	docker volume create -d local-persist -o mountpoint=/path/to/submission-data --name=submission-data
	docker volume create -d local-persist -o mountpoint=/path/to/logs-data --name=logs-data
	docker volume create -d local-persist -o mountpoint=/path/to/mongo-data --name=mongo-backup
	docker volume create -d local-persist -o mountpoint=/path/to/dev_copo/postgres-data --name=postgres-backup

	docker volume create mongo-data
	docker volume create postgres-data

On the swarm manager create two networks::

	docker network create -d overlay copo-frontend-network
	docker network create -d overlay copo-backend-network

Create secrets. All secrets are file based. You will need to create some of the keys with third parties and choose passwords before proceeding with the COPO setup.::

	docker secret create copo_mongo_initdb_root_password copo_mongo_initdb_root_password
	docker secret create copo_mongo_user_password copo_mongo_user_password
	docker secret create copo_postgres_user_password copo_postgres_user_password
	docker secret create copo_web_secret_key copo_web_secret_key
	docker secret create copo_orcid_secret_key copo_orcid_secret_key
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

Create services:

MongoDB. (As always change the configuration and environmental variable is appropriate)::

	docker service create \
	     --name copo-mongo \
	     --replicas 1 \
	     --network copo-backend-network \
	     --endpoint-mode dnsrr \
	     --constraint 'node.labels.mongo-service == true' \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --user mongodb \
	     --mount type=volume,source=mongo-data,destination=/data/db \
	     --reserve-cpu .4 --limit-cpu .4 --reserve-memory  4GB --limit-memory 4GB \
	     --secret copo_mongo_initdb_root_password \
	     --secret copo_mongo_user_password \
	     -e MONGO_INITDB_ROOT_USERNAME="copo_admin" \
	     -e MONGO_INITDB_ROOT_PASSWORD_FILE="/run/secrets/copo_mongo_initdb_root_password" \
	     -e MONGO_USER="copo_user" \
	     -e MONGO_USER_PASSWORD_FILE="/run/secrets/copo_mongo_user_password" \
	     -e MONGO_DB="copo_mongo" \
	     copo/copo-mongo:20

PostgreSQL.::

	docker service create \
	     --name copo-postgres \
	     --replicas 1 \
	     --network copo-backend-network \
	     --endpoint-mode dnsrr \
	     --constraint 'node.labels.postgres-service == true' \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --mount type=volume,source=postgres-data,destination=/var/lib/postgresql/data \
	     --reserve-cpu .3 --limit-cpu .3 --reserve-memory  2GB --limit-memory 2GB \
	     --secret copo_postgres_user_password \
	     -e POSTGRES_DB="copo" \
	     -e POSTGRES_USER="copo_user" \
	     -e POSTGRES_PASSWORD_FILE="/run/secrets/copo_postgres_user_password" \
	     postgres:9.6

Redis::

	docker service create \
	     --name copo-redis \
	     --replicas 1 \
	     --constraint 'node.labels.web-service == true' \
	     --network copo-frontend-network \
	     --endpoint-mode dnsrr \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --reserve-cpu .3 --limit-cpu .3 --reserve-memory  512mb --limit-memory 512mb \
	     library/redis

Web service

.. note:: the code is under active development. As such the Docker tag below needs to be changed to reflect the most recent version available in DockerHub. Please check the most recent version there. You can safely ignore the \*feature tags as they are not stable releases. For stable releases look for \*rc.

.. note:: there are a number of parameters in the command below that need to be updated or you may want to change for your local deployment. Please read through carefully.

.. warning:: the ENA_SERVICE environment variable is set to the ENA development server. All submission to this server will be deleted after 24hours. To submit to the production ENA server remove \"dev\"

::

	docker service create \
	     --name copo-web \
	     --replicas 1 \
	     --network copo-frontend-network \
	     --network copo-backend-network \
	     --endpoint-mode dnsrr \
	     --constraint 'node.labels.web-service == true' \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --mount type=volume,source=web-data,destination=/copo/media \
	     --mount type=volume,source=static-data,destination=/copo/static \
	     --mount type=volume,source=logs-data,destination=/copo/exceptions_and_logging/logs \
	     --mount type=volume,source=submission-data,destination=/copo/submission/data \
	     --reserve-cpu .4 --limit-cpu .4 --reserve-memory  7GB --limit-memory 7GB \
	     --secret copo_web_secret_key \
	     --secret copo_postgres_user_password \
	     --secret copo_mongo_user_password \
	     --secret copo_google_secret_key \
	     --secret copo_figshare_client_id_key \
	     --secret copo_facebook_secret_key \
	     --secret copo_twitter_secret_key \
	     --secret copo_orcid_secret_key \
	     --secret copo_figshare_client_secret_key \
	     --secret copo_figshare_consumer_secret_key \
	     --secret copo_webin_user \
	     --secret copo_webin_user_password \
	     --secret copo_nih_api_key \
	     --secret copo_public_name_service_api_key \
	     --secret copo_mail_password \
	     -e ENVIRONMENT_TYPE="prod" \
	     -e ASPERA_PLUGIN_DIRECTORY="aspera_linux_plugin" \
	     -e SECRET_KEY_FILE="/run/secrets/copo_web_secret_key" \
	     -e MEDIA_PATH="media/" \
	     -e DEBUG="false" \
	     -e REDIS_HOST="copo-redis" \
	     -e REDIS_PORT="6379" \
	     -e WEBIN_USER_FILE="/run/secrets/copo_webin_user" \
	     -e WEBIN_USER_PASSWORD_FILE="/run/secrets/copo_webin_user_password" \
	     -e ENA_SERVICE="https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/" \
	     -e MONGO_USER="copo_user" \
	     -e MONGO_USER_PASSWORD_FILE="/run/secrets/copo_mongo_user_password" \
	     -e MONGO_DB="copo_mongo" \
	     -e MONGO_HOST="copo-mongo" \
	     -e MONGO_PORT="27017" \
	     -e MONGO_MAX_POOL_SIZE="100" \
	     -e POSTGRES_DB="copo" \
	     -e POSTGRES_USER="copo_user" \
	     -e POSTGRES_PORT="5432" \
	     -e POSTGRES_SERVICE="copo-postgres" \
	     -e POSTGRES_PASSWORD_FILE="/run/secrets/copo_postgres_user_password" \
	     -e ORCID_SECRET_FILE="/run/secrets/copo_orcid_secret_key" \
	     -e FIGSHARE_CONSUMER_SECRET_FILE="/run/secrets/copo_figshare_consumer_secret_key" \
	     -e FIGSHARE_CLIENT_ID_FILE="/run/secrets/copo_figshare_client_id_key" \
	     -e FIGSHARE_CLIENT_SECRET_FILE="/run/secrets/copo_figshare_client_secret_key" \
	     -e GOOGLE_SECRET_FILE="/run/secrets/copo_google_secret_key" \
	     -e TWITTER_SECRET_FILE="/run/secrets/copo_twitter_secret_key" \
	     -e FACEBOOK_SECRET_FILE="/run/secrets/copo_facebook_secret_key" \
	     -e NIH_API_KEY_FILE="/run/secrets/copo_nih_api_key" \
	     -e PUBLIC_NAME_SERVICE_API_KEY_FILE="/run/secrets/copo_public_name_service_api_key" \
	     -e MAIL_PASSWORD_FILE="/run/secrets/copo_mail_password" \
	     -e MAIL_PORT="587" \
	     -e MAIL_ADDRESS=""youremail@domain \
	     -e MAIL_SERVER="mailserver.com" \
	     -e MAIL_USERNAME="yourmail@domain" \
	     -e ALLOWED_HOSTS=”” \ #insert comma separated list of allowed hosts here
	     -e PUBLIC_NAME_SERVICE='https://id.tol.sanger.ac.uk/api/v2/'
	     copo/copo-web:v1.2.2

Nginx::

	docker service create \
	     --name copo-nginx \
	     --replicas 1 \
	     --network copo-frontend-network \
	     --constraint 'node.labels.nginx-service == true' \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --publish 80:80 \
	     --publish 443:443 \
	     --mount type=volume,source=static-data,destination=/www/static \
	     --reserve-cpu .3 --limit-cpu .3 --reserve-memory  3GB --limit-memory 3GB \
	     --secret copo-project.crt \
	     --secret copo-project.key \
	     copo/copo-nginx:19-12-19

Backup service::

	docker service create \
	     --name copo-backup \
	     --replicas 1 \
	     --network copo-backend-network \
	     --endpoint-mode dnsrr \
	     --constraint 'node.labels.backup-service == true' \
	     --update-delay 10s \
	     --update-parallelism 1 \
	     --restart-condition 'on-failure' \
	     --mount type=volume,source=mongo-backup,destination=/backup/mongo \
	     --mount type=volume,source=postgres-backup,destination=/backup/postgres \
	     --reserve-cpu .3 --limit-cpu .3 --reserve-memory  1GB --limit-memory 1GB \
	     --secret copo_mongo_initdb_root_password \
	     -e MONGO_HOST="copo-mongo" \
	     -e MONGO_PORT="27017" \
	     -e MONGO_INITDB_ROOT_USERNAME="copo_admin" \
	     -e MONGO_INITDB_ROOT_PASSWORD_FILE="/run/secrets/copo_mongo_initdb_root_password" \
	     -e MONGO_DB="copo_mongo" \
	     --secret copo_postgres_user_password \
	     -e POSTGRES_DB="copo" \
	     -e POSTGRES_USER="copo_user" \
	     -e POSTGRES_PORT="5432" \
	     -e POSTGRES_SERVICE="copo-postgres" \
	     -e POSTGRES_PASSWORD_FILE="/run/secrets/copo_postgres_user_password" \
	     copo/copo-backup

Updating the server
-------------------

The COPO project is currently under active development and it's being updated quite frequently.
To update your instance to a newer (or the latest) version, on the swarm manager run::

	docker service update --image copo/copo-web:<new-tag> copo-web
	docker service update --force copo-nginx

If you update often we recommend taking care of removing old docker images regularly.





