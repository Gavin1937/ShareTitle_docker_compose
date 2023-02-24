
# docker-compose setup for ShareTitle project

My project ShareTitle contains 2 repositories

* A backend application: [ShareTitle](https://github.com/Gavin1937/ShareTitle)
* A frontend application: [ShareTitle_react](https://github.com/Gavin1937/ShareTitle_react)

This repository contains all the necessary files to setup ShareTitle project with [docker-compose](https://docs.docker.com/compose/)

# requirements

* **make sure to recursively clone this repo to download entire ShareTitle project**
* [docker](https://docs.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) installed
* [Python >= 3.8](https://www.python.org/) for [one script setup](#one-script-setup) only

# setup

## one script setup

once you have python >= 3.8 installed in your machine, run:

```sh
python setup_app.py
```

## manual setup

1. create a new folder under this repository call **data**
2. copy [./ShareTitle/data/docker_config.json](https://github.com/Gavin1937/ShareTitle/blob/main/data/docker_config.json) to **./data/config.json**
3. copy [./ShareTitle/data/parseScript.json](https://github.com/Gavin1937/ShareTitle/blob/main/data/parseScript.json) to **./data/parseScript.json**
4. follow the instruction in [ShareTitle repo](https://github.com/Gavin1937/ShareTitle#configuration) to change these config files
5. update [./.env](./.env) file and set **APP_PORT** to your desire port
6. run command `docker-compose up -d --build` to build & launch ShareTitle project

# use docker-compose

* to deploy ShareTitle project, run:

```sh
docker-compose up -d
```

* to undeploy ShareTitle project, run:

```sh
docker-compose down
```

# interact with ShareTitle application

once you deploy the application, you can go to your browser and visit the frontend: **http://localhost:${APP_PORT}/sharetitle**

default `${APP_PORT}` value is set to `80` in [./.env](./.env) file

you can also use ShareTitle backend api in other place, checkout [Backend Api Documentation](https://github.com/Gavin1937/ShareTitle/blob/main/doc/ApiDocumentation.md)

