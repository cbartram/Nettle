FROM hypriot/rpi-python

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install --index-url=https://pypi.python.org/simple/ pychalk matplotlib pyfiglet sklearn numpy

COPY . /app
WORKDIR /app

CMD [ "python3", "./src/main.py" ]