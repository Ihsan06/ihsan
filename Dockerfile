# pull official base image
FROM python:3.6.4-alpine3.7
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update add --no-cache g++
# install dependencies
RUN pip install Cython
RUN pip install numpy
RUN pip install pandas
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/
EXPOSE 5000
RUN ls -la app/
ENTRYPOINT ["app/docker-entrypoint.sh"]

#scikit-learn==0.23.1
#scipy==1.4.1
#six==1.15.0