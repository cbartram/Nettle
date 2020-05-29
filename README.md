# Nettle

![PyPI](https://img.shields.io/pypi/v/Nettle)
![Travis (.org)](https://img.shields.io/travis/cbartram/Nettle)
![PyPI - Downloads](https://img.shields.io/pypi/dm/Nettle)
![GitHub repo size](https://img.shields.io/github/repo-size/cbartram/Nettle)

Raspberry Pi Camera extension which samples an image and updates the rooms lighting to align with the primary 
colors in the image.

## Getting Started

To get started with this project clone it from github using:

```shell script
$ git clone https://github.com/cbartram/Nettle.git
```

### Prerequisites

This project was built to run with Python 3 on the [Raspberry Pi](https://www.raspberrypi.org/). 
You can get the latest version of Python 3 for your system from [the python downloads](https://www.python.org/downloads/) page.

Although you can run this program locally with a sample image it was designed to be used with the [Raspberry Pi's camera module](https://www.raspberrypi.org/products/camera-module-v2/).

You will also need a set of [Feit Electric](https://www.feit.com/product-category/bulbs/smart-wifi-light-bulb/) or [Philips Hue](https://www2.meethue.com/en-us/bulbs) WiFi enabled lightbulbs.
More smart lighting brands will be supported in the future. 

Once you have everything setup and connected to your home network you can install the necessary dependencies:

```shell script
$ pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python 3](http://www.dropwizard.io/1.0.2/docs/) - The programming language used
* [Matplot Lib](https://maven.apache.org/) - Image analysis library
* [Numpy](https://rometools.github.io/rome/) - Statistical calculation library
* [Pip](https://rometools.github.io/rome/) - Dependency management & build tool

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/cbartram/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/cbartram/Nettle/tags). 

## Authors

* **Christian Bartram** - *Initial work* - [Cbartram](https://github.com/cbartram)

See also the list of [contributors](https://github.com/Nettle/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Python for a great programming language
* Raspberry PI for making awesome computers
* Philips hue for the fun light bulbs
