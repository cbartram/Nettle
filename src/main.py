# from picamera import PiCamera
import os
import configparser
import chalk
from pyfiglet import Figlet

f = Figlet(font='slant')
environment = os.getenv("ACTIVE_PROFILE", "local")
config = configparser.ConfigParser()
config.read(f'../resources/application-{environment}.ini')

def init():
    print(chalk.green(f.renderText('Nettle')))
    image = None

    if config['DEFAULT']['LoadImage']:
        print(chalk.blue(f'[INFO] Loading Image from: {config["DEFAULT"]["ImageSource"]}'))
        if config['DEFAULT']['ImageSource'].upper() == "S3":
            image = loadS3()
        else:
            image = loadLocal()


def loadS3():
    print(chalk.blue("Loading from S3..."))

def loadLocal():
    print(chalk.blue(f'Loading Local Image from: {config["DEFAULT"]["ImagePath"]}'))


if __name__ == "__main__":
    init()