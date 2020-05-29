![logo](https://github.com/cbartram/Nettle/blob/master/resources/images/logo.png)

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

### Installing

Before installing any dependencies you should create and activate a [virtual environment](https://docs.python.org/3/library/venv.html). This quick
and simple process helps keep python projects and packages isolated from other system site directories.

```shell script
$ python3 -m venv venv

# Activate the virtual env in your current bash session
$ source ./venv/bin/activate
``` 

Once you have everything setup and connected to your home network you can install the necessary dependencies:

```shell script
$ pip3 install -r requirements.txt
```

To start the application run:

```shell script
$ python3 ./src/main.py
```

## Running the tests

Tests are managed with [PyTest](https://docs.pytest.org/en/latest/) and can be run by executing the following
command in the root directory of this project:

```shell script
$ pytest
```

### Integration Tests

There are no integration tests for this project yet.

### Performance Tests

There are no performance tests for this project yet.

## Deployment

This project is designed to be deployed using [Docker](https://docker.com). Don't worry if you are unfamiliar with [Docker](https://docker.com) there
are just a few simple steps to follow to build and deploy an image to your own Raspberry Pi!

### Create Image

First we need to create a new image using the [Dockerfile](https://github.com/cbartram/Nettle/blob/master/Dockerfile). This creates a repeatable template
that is used to run a container for the chosen version of the software. 

The image is already formatted to use the ARM CPU architecture that runs on Raspberry Pi.

```shell script
$ docker build . -t nettle:0.0.1
```

### Push Image

Now we can push the image to [Dockerhub](https://hub.docker.com) where we can easily pull it down onto our Pi.

```shell script
$ docker push 
```

###

Finally after SSH'ing into the Raspberry Pi we can pull the image and run the container:

```shell script
$ docker run --name nettle -d -p 8080:8080 nettle:0.0.1
```

You can validate the container is deployed and running using:

```shell script
$ docker ps
$ docker logs nettle
```
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
