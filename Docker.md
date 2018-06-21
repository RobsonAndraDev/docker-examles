# Docker overview

## O que é Docker

Docker é uma plataforma aberta para desenvolvimento, publicação e execução de aplicações.

## A plataforma Docker

O Docker permite o empacotamento e execução de uma aplicação em um ambiente minimalista e isolado chamado container.

## Docker Engine

Docker Engine é uma aplicação client-server com esses principais componentes:  

- Um servidor: que é um serviço chamado daemon;  
- Command Line Interface(CLI) cliente(o comando docker);  
- E uma REST API.

## Dockerfile instructions  

- FROM: Referência a imagem base
- RUN: Executa comandos dentro da imagem no momento da sua criação
- ENV: Configura uma variável de ambiente dentro imagem
- ADD ou COPY: Copia arquivos do host para a imagem
- WORKDIR: Configura uma pasta como raiz
- EXPOSE: Exibe a porta que será exposta pelo container
- ENTRYPOINT: Comando executando ao iniciar o container
- CMD: Comando executando ao iniciar o container
- VOLUME: Usa uma pasta do host dentro do container

exemplo de uso da instrução ENV: <https://github.com/docker-library/openjdk/blob/054cea7585e6c0e4e98d133378ea38061a2ae3ac/7-jdk/Dockerfile>

## Comandos básicos Docker

**docker image COMMAND**:  

- pull: Baixa uma imagem de um repositório;
- build: Construi uma imagem;
- ls: Lista as images;
- tag: Cria uma tag para uma imagem;
- rm: Remove uma imagem.

**docker container COMMAND**:  

- run: Executa um comando em um novo container;
- start: Inicia containers parados;
- stop: Para containers em execução;
- restart: Reinicia containers em execução;
- rm: Remove containers;
- ls: Lista containers
- logs: Exibe os logs de um container;
- exec: Executa um comando em um container em execução.

## Extra  

Comando que exibe as labels:  

``` Dockerfile
docker inspect node-app| jq -c ".[].Config.Labels" | jq .
```
