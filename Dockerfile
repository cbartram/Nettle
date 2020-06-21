FROM hypriot/rpi-python

WORKDIR /usr/src/app

RUN pip3 install --index-url https://pypi.python.org/simple/ --upgrade pip
RUN pip3 install --index-url=https://pypi.python.org/simple/ pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]