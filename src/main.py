# from picamera import PiCamera
import os
import cv2
import chalk
import configparser
import matplotlib.pyplot as plt
from pyfiglet import Figlet
from util.util import to_hex, rgb_to_hsl
from collections import Counter
from sklearn.cluster import KMeans
from EnvInterpolation import EnvInterpolation
from loader.LoaderFactory import LoaderFactory
from hue.Hue import Hue
import colorsys

"""
Initializes the application and sets up configuration. This is the main 
method which runs the script.
"""
def init():
    # Read configuration and parse env vars from config file
    f = Figlet(font='slant')
    environment = os.getenv("ACTIVE_PROFILE", "local")
    config = configparser.ConfigParser(interpolation=EnvInterpolation())
    config.read(f'../resources/application-{environment}.ini')

    print(chalk.green(f.renderText('Nettle')))

    print(colorsys.rgb_to_hls(255 / 255, 100 / 255, 15 / 255))

    # Create a loader based on the configuration
    loader_factory = LoaderFactory(config=config)
    loader = loader_factory.createLoader()

    # Load the image appropriately
    image = loader.load()

    # Analyze colors in the image
    colors = get_colors(image, 8, False)
    print(chalk.blue(f'[INFO] Colors in image: {colors}'))
    hue = Hue(config)

    hls = colorsys.rgb_to_hls(colors[0][0] / 255, colors[0][1] / 255, colors[0][2] / 255)
    hue.set_color(7, (hls[0] * 100, hls[1] * 100, hls[2] * 100))

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