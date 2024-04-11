FROM python:3-alpine
LABEL maintainer ="Bolaji Aina <neoandey@yahoo.com>"

ARG FLASK_APP=seait.py
ARG FLASK_ENV=production
ARG MONGODB_URL
ARG MONGODB_DB
ARG MONGODB_HOST
ARG MONGODB_PORT
ARG MONGODB_USERNAME
ARG MONGODB_PASSWORD
ARG MONGODB_USE_SSL
ARG MONGODB_REPLICASET
ARG MONGODB_DIRECT_CONNECTION
ARG MONGODB_AUTH_MECHANISM
ARG SESSION_TYPE
ARG REDIS_URL
ARG REDIS_QUEUE_NAME
ARG PORT

ENV FLASK_APP=$FLASK_APP
ENV FLASK_ENV=$FLASK_ENV
ENV MONGODB_URL=$MONGODB_URL
ENV MONGODB_DB=$MONGODB_DB
ENV MONGODB_HOST=$MONGODB_HOST
ENV MONGODB_PORT=$MONGODB_PORT
ENV MONGODB_USERNAME=$MONGODB_USERNAME
ENV MONGODB_PASSWORD=$MONGODB_PASSWORD
ENV MONGODB_USE_SSL=$MONGODB_USE_SSL
ENV MONGODB_REPLICASET=$MONGODB_REPLICASET
ENV MONGODB_DIRECT_CONNECTION=$MONGODB_DIRECT_CONNECTION
ENV MONGODB_AUTH_MECHANISM=$MONGODB_DIRECT_CONNECTION
ENV SESSION_TYPE=$SESSION_TYPE
ENV REDIS_URL=$REDIS_URL
ENV REDIS_QUEUE_NAME=$REDIS_QUEUE_NAME
ENV PORT=$PORT

RUN  mkdir -p "/opt/seait/app/static"  &&  mkdir -p "opt/seait/settings" &&  apk update && apk upgrade && apk add --no-cache bash \
   gcc \
   libcurl \
   python3-dev \
   gpgme-dev \
   libc-dev 

COPY [".flaskenv","./config.py","./seait.py","./seait.py","./Procfile","./redis_worker.py","./requirements.txt", "/opt/seait/"]
COPY ["./default_settings/cpanel.json","/opt/seait/settings/cpanel.json"]
COPY ["./settings/configuration.json","/opt/seait/settings/configuration.json"]
COPY ["./app",  "/opt/seait/app"]
#RUN rm -rf ./opt/seait/app/static && rm -rf ./opt/seait/app/template
#COPY ["./app/static","/opt/seait/app/static"]
#COPY ["./app/templates",  "/opt/seait/app/templates"]
RUN  python -m pip install --upgrade pip &&  python -m pip install -r  /opt/seait/requirements.txt && apk add bash 
COPY [ "./overrides/json.py", "/usr/local/lib/python3.12/site-packages/flask_mongoengine/"]
WORKDIR /opt/seait
EXPOSE $PORT 6379 443 80
CMD python redis_worker.py & gunicorn -w 2 -b 0.0.0.0:$PORT  'seait:app' 