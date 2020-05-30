# from picamera import PiCamera
import configparser
import chalk
from pyfiglet import Figlet
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import os

from loader.LoaderFactory import LoaderFactory
from util.util import to_hex

f = Figlet(font='slant')
environment = os.getenv("ACTIVE_PROFILE", "local")
config = configparser.ConfigParser()
config.read(f'../resources/application-{environment}.ini')

def init():
    print(chalk.green(f.renderText('Nettle')))
    loader_factory = LoaderFactory(config)
    loader = loader_factory.createLoader()
    image = loader.load()
    colors = get_colors(image, 8, True)
    print(chalk.blue(f'[INFO] Colors in image: {colors}'))


def plot_image(image):
    print("The type of this input is {}".format(type(image)))
    print("Shape: {}".format(image.shape))
    get_colors(image, 8, True)


'''
Computes the primary colors that comprise and image and plots them on a Pie chart.
This algorithm uses KMeans clustering to find the most prevalent pixels in an image
'''
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

if __name__ == "__main__":
    init()