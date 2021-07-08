# weddpics 
Weddpics is a simple photo gallery. The goal is to enable newlyweds to manage the photos sent by guests.

API Documentation: https://weddpics.herokuapp.com/api/docs

Technologies used:
## Frontend:
- VueJS
- Vuetifyjs
- Vuex

## Backend:
- Python
- Flask
- Flask-restx
- MongoDB (Atlas)
- AWS S3


I this repository is present the Backend code for Weddpics API

Client repository: https://gitlab.com/glaubersilva/weddpics-client

Running application: https://weddpics-client.herokuapp.com

## Instalation
1. Clone  respository: `git clone https://gitlab.com/glaubersilva/weddpics`.
2. Access the directory: `cd weddpics`.
3. run: 
   ```bash
   sudo apt-get install docker
   sudo apt-get install docker-compose
   ```
4. Check the Docker version: `docker -v`.
```bash
Docker version 20.10.5, build 55c4c88
```
5. Check the docker-compose version : `docker-compose -v`
```bash
docker-compose version 1.21.2, build a133471
``` 

## Start the app
For start the application its necessary a S3 account, you can found information about how setting up here: https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html

Update the env_app file with AWS S3 key and follow:

1. In the project root set the env files for docker-compose: `mv env_app .env`
2. In the project root directory run: `docker-compose up -d` 
3. After all container got running, run: `sudo docker ps` should appears:


```bash
CONTAINER ID   IMAGE                      COMMAND                  CREATED       STATUS              PORTS                      NAMES
158d5b63d833   weddpics_web               "/bin/sh /app/entryp…"   9 hours ago   Up About a minute   0.0.0.0:5000->5000/tcp     weddpics_web
8c4c9b5b25f9   mongo-express              "tini -- /docker-ent…"   4 days ago    Up 9 hours          0.0.0.0:8081->8081/tcp     weddpics_mongo_express_1
49f1c1ad439b   mongo:latest               "docker-entrypoint.s…"   4 days ago    Up 9 hours          0.0.0.0:27017->27017/tcp   weddpics_mongodb_1
```