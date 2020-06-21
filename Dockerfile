FROM frankwolf/rpi-python3
MAINTAINER cbartram3@gmail.com

WORKDIR /usr/src/app

EXPOSE 80
EXPOSE 443

RUN pip3 install --index-url https://pypi.python.org/simple/ --upgrade pip
RUN pip3 install --index-url=https://pypi.python.org/simple/ pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]