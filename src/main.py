# from picamera import PiCamera
import io
import boto3
import configparser
import chalk
from pyfiglet import Figlet
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import os

from loader.LoaderFactory import LoaderFactory

f = Figlet(font='slant')
environment = os.getenv("ACTIVE_PROFILE", "local")
config = configparser.ConfigParser()
config.read(f'../resources/application-{environment}.ini')

def init():
    print(chalk.green(f.renderText('Nettle')))
    loader_factory = LoaderFactory(config)
    loader = loader_factory.createLoader()
    image = loader.load()
    plot_image(image)

def to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def plot_image(image):
    print("The type of this input is {}".format(type(image)))
    print("Shape: {}".format(image.shape))
    get_colors(image, 8, True)


def get_colors(image, number_of_colors, show_chart):
    # Resize and Reshape the image (KMeans expects a flattened array as input)
    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_

    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [to_hex(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)
        plt.show()

    return rgb_colors

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
    image = cv2.imread(file_stream)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

'''
Loads an image from the local filesystem
'''
def loadLocal():
    print(chalk.blue(f'Loading Local Image from: {config["DEFAULT"]["ImagePath"]}'))
    image = cv2.imread(config["DEFAULT"]["ImagePath"])
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


if __name__ == "__main__":
    init()