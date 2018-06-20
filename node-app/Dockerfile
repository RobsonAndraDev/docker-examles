FROM node:alpine
LABEL mainteiner="Robson Andrade"

RUN mkdir /app

COPY src/package.json /app/

WORKDIR /app

RUN npm install

COPY src/. .

EXPOSE 3000

CMD ["npm", "start"]