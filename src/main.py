# from picamera import PiCamera
import os
import chalk
import configparser
import matplotlib.pyplot as plt
from threading import Timer
from pyfiglet import Figlet
from util.util import to_hex, rgb_to_xy
from collections import Counter
from sklearn.cluster import KMeans
from EnvInterpolation import EnvInterpolation
from loader.LoaderFactory import LoaderFactory
from hue.Hue import Hue
from time import sleep
import numpy as np
loader = None
config = None
hue = None

"""
Initializes the application and sets up configuration. This is the main 
method which runs the script.
"""
def init():
    global loader
    global hue
    global config

    # Read configuration and parse env vars from config file
    f = Figlet(font='slant')
    environment = os.getenv("ACTIVE_PROFILE", "local")
    config = configparser.ConfigParser(interpolation=EnvInterpolation())
    config.read(f'../resources/application-{environment}.ini')

    print(chalk.green(f.renderText('Nettle')))

    # Create a loader based on the configuration
    loader_factory = LoaderFactory(config=config)
    loader = loader_factory.createLoader()
    hue = Hue(config)


def main(arg):
    print(chalk.blue("[INFO] Looping"))

    # Load the image appropriately
    image = loader.load()

    print(chalk.blue("[INFO] Analyzing Colors..."))
    # Analyze colors in the image
    colors = get_colors(image, 8, True)

    print(chalk.blue("[INFO] Colors: " + str(colors)))

    print(chalk.blue("[INFO] Setting Hue Lights to color..."))
    hue.set_color(7, rgb_to_xy(round(colors[0][0], 0), round(colors[0][1], 0), round(colors[0][2], 0)))

'''
Computes the primary colors that comprise and image and plots them on a Pie chart.
This algorithm uses KMeans clustering to find the most prevalent pixels in an image
'''
def get_colors(image, number_of_colors, show_chart):
    # Resize and Reshape the image (KMeans expects a flattened array as input)
    # modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    print(image)
    modified_image = np.array(image)
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


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

if __name__ == "__main__":
    init()
    rt = RepeatedTimer(int(config['GENERAL']['PollingInterval']), main, None)
    try:
        sleep(50)  # your long-running job goes here...
    finally:
        rt.stop()

