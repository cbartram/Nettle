# from picamera import PiCamera
import os
import io

import matplotlib.pyplot as plt
import boto3
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

    if config['DEFAULT']['LoadImage'] == 'True':
        print(chalk.blue(f'[INFO] Loading Image from: {config["DEFAULT"]["ImageSource"]}'))
        if config['DEFAULT']['ImageSource'].upper() == "S3":
            image = loadS3()
        else:
            image = loadLocal()
    else:
        print(chalk.blue("[INFO] Using Raspberry Pi Camera module."))

'''
Loads an image from the configuration and pulls
it into memory from AWS S3.
'''
def loadS3():
    s3 = boto3.resource('s3', region_name='us-east-1')
    print(chalk.blue("Loading from S3..."))
    if(os.getenv("AWS_ACCESS_KEY_ID") == None or os.getenv("AWS_SECRET_ACCESS_KEY") == None):
        print(chalk.red("[ERROR] Missing aws credentials. Ensure access key id and secret access key values are properly set."))
        os._exit(1)

    if not config["DEFAULT"]["ImagePath"].startswith("s3://"):
        print(chalk.red("[ERROR] S3 Image location configuration option must begin with the \"s3://\" prefix."))
        os._exit(1)

    # Parse bucket and path from given configuration
    idx = config["DEFAULT"]["ImagePath"][5:].index('/')
    bucketName = config["DEFAULT"]["ImagePath"][5:][:idx]
    path = config["DEFAULT"]["ImagePath"][5:][idx + 1:]

    bucket = s3.Bucket(bucketName)
    object = bucket.Object(path)

    file_stream = io.StringIO()
    object.download_fileobj(file_stream)
    return plt.imread(file_stream)

'''
Loads an image from the local filesystem
'''
def loadLocal():
    print(chalk.blue(f'Loading Local Image from: {config["DEFAULT"]["ImagePath"]}'))
    return plt.imread(config["DEFAULT"]["ImagePath"])


if __name__ == "__main__":
    init()