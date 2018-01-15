####################
Deployment
####################

COPO is deployed using `Docker Swarm <https://docs.docker.com/engine/swarm/>`_ - a tool for clustering and orchestrating `Docker <https://www.docker.com>`_ containers, and is built around the following tools:


The application images are available for download at  `Docker Hub <https://hub.docker.com/r/copo/>`_.

From development to production - building a COPO docker image
--------------------------------------------------------------
As mentioned, docker is used to ochestrate the deployment of COPO. In this section we describe the process of building a docker image for deployment. We focus on building a web docker image.

.. note::

   The steps described above can be applied to building images of other components in COPO (e.g., MongoDB image).

 
1. git commit and push to remote.
2. pip freeze and update web/src/requirements/base.txt

#. run docker build -t copo-web . in /COPO/web (location of Dockerfile).
#. docker tag [image id] copo/copo-web:latest (image id obtained by running docker images)
#. docker push copo/copo-web:latest
