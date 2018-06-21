# Docker examples

This is a repo with examples to help to explain docker workflow

## Running containers by command line  

- Building and running node app:  

``` Dockerfile
docker image build -t nodeapp node-app/.
docker container run --name node-app -dp 3000:3000 nodeapp
```

- Building and running php-app:  

``` Dockerfile
docker image build -t phpapp php-app/.
docker container run --name php-app -dp 8080:80 phpapp
```

- Building and running nginx:  

``` Dockerfile
docker image build -t mynginx nginx/.
docker container run --name nginx -dp 80:80 mynginx
```

- Building and running python-app:

``` Dockerfile
docker image build -t pythonapp python-app/.
docker container run --name python-app -d pythonapp
```
