FROM arm32v7/python:3.7.7-buster
MAINTAINER cbartram3@gmail.com

EXPOSE 80
EXPOSE 443

# Update APT package cache and
# Install necessary libs for Python3 dependencies
#RUN apt-get update && apt-get install -y liblapack-dev libblas-dev libatlas-base-dev gfortran

# Ensure pip, setuptools, and wheel is up to date
RUN pip3 install --index-url https://pypi.python.org/simple/ --upgrade pip setuptools wheel

# Install package dependencies
RUN pip3 install pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]