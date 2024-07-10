# DOCKER

Follow these steps to install and run ForbiddenPass in Docker.

## Clone the Repository

First, clone the repository:

```bash

git clone https://github.com/gotr00t0day/forbiddenpass.git

cd forbiddenpass
```
## Build the Docker Image

Build the Docker image using the following command in the same directory where the Dockerfile is located.

```bash
docker build -t forbiddenpass .
```
## Usage

Once the image is built, you can run the container using the following commands:

 Domains to check
 ```
 docker run --rm -v $(pwd):/app forbiddenpass -d domains.txt
 ```

 Domains to check with a path
 ```
 docker run --rm -v $(pwd):/app forbiddenpass -d domains.txt --path login
 ```


 > **Note**
-v $(pwd):/app: This option mounts the current working directory on your host machine to the /app directory inside the container. This allows the container to access files in your current directory, such as domains.txt

 > **Note**
Ensure that domains.txt is located in your current working directory when executing the docker run command.
 
Scan a single target
 ```
docker run --rm forbiddenpass -t https://site
 ```
Scan a single target with a path
 ```
  docker run --rm forbiddenpass -t https://site --path login
 ````
