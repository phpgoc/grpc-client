FROM node:lts

RUN apt-get -qq update && apt-get -qq install -y \
  unzip

WORKDIR /tmp

COPY protoc-gen-grpc-web-1.5.0-linux-x86_64 /usr/local/bin/protoc-gen-grpc-web
COPY protoc /usr/local/bin/protoc

RUN  npm install nrm -g --registry=https://registry.npmmirror.com

RUN nrm use taobao

RUN npm install -g protoc-gen-js

WORKDIR /src