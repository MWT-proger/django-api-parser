FROM nginx:stable-alpine3.17-slim

RUN mkdir /etc/nginx/templates
COPY nginx.conf /etc/nginx
COPY templates/default.conf.template  /etc/nginx/templates
