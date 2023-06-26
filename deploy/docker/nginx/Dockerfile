FROM nginx:stable-alpine3.17-slim

RUN mkdir /etc/nginx/templates
COPY ./nginx/nginx.conf /etc/nginx
COPY ./nginx/templates/default.conf.template  /etc/nginx/templates
