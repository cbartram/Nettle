FROM hypriot/rpi-python

WORKDIR /usr/src/app

RUN pip install pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]