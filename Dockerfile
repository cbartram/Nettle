FROM frankwolf/rpi-python3
MAINTAINER cbartram3@gmail.com

WORKDIR /usr/src/app

EXPOSE 80
EXPOSE 443

# Update APT package cache
RUN apt-get update && apt-get -y install curl

# Install necessary libs for Python3 dependencies
RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran

# Ensure pip, setuptools, and wheel is up to date
RUN pip3 install --index-url https://pypi.python.org/simple/ --upgrade pip setuptools wheel

# Install package dependencies
RUN pip3 install --index-url=https://pypi.python.org/simple/ pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]