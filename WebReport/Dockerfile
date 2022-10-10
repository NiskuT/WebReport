# syntax=docker/dockerfile:1

FROM node:16

COPY ["package.json", "package-lock.json", "./"]

RUN npm install

COPY . .

EXPOSE 3000

RUN mkdir -p /db

CMD ["node", "index.js"]
