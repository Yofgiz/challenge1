# base Docker image that we will build on
FROM python:3.9.1
# set up the working directory inside the container
WORKDIR /app
ENTRYPOINT [ "bash" ]