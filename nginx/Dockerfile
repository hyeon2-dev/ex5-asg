FROM nginx:1.31.3-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY ./html /usr/share/nginx/html

EXPOSE 80