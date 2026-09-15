FROM nginx:1.31.3-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /ectc/nginx/conf.d/default.conf
COPY ./html /usr/share/nginx/html

EXPOSE 80