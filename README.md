# Steps to complete task
----------------------

1. Created flask app to return the mentioned json ( refer app/y42app.py )

2. Written dockerfile to containerise the application, while setting the build timestamp ( refer app/Dockerfile )

3. Written deployment and service manifest to deploy application in Kubernetes 



# Tech Stack
-----------

Coding: Vim

Builds: Docker

Deploy: Kubernetes 


# Commands
--------

1. To build the image

docker build -t deltacrayo/y42 --build-arg build_date="$(date +%s)" .


2. To deploy the container

kubectl apply -f deploy.yaml


# Running the project
-------------------

$ git clone https://github.com/thecloudknight/y42_task.git
$ cd y42_task && sh autobot.sh 
