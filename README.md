# Pimoroni Displayotron Hat Example

This is a simple example of using python to drive the Display-o-Tron
by Pimoroni in an virtual environment in python3

## Hardware Interface

This display-a-tron HAT actually contains several difference components.
The 3 line LCD uses the st7036 LCD driver, using a SPI interface to simply
the connection.

It uses the sn3218 18 channel LED driver to control the back lighting.

## Prerequisite

* use raspi-config to enable both SPI and I2C interfaces
* make sure you have python3-smbus installed globally


## Virtual Environment

I like to use virtualenv when I work on python, even on sometime small like a RaspberryPi. Using venv helps keep experimenting with different libraries clean.

### Installation
```
# Create a project directory and a python3 virtual env:
mkdir myproject
python3 -m venv myproject

# Clone this repo into a src subdirectory
cd myproject
git clone git@github.com:pkshiu/rpi-dothat-example.git src

# do not forget to activate the virtual env!
cd src
source ../bin/activate

# install dependencies inside your virtual env
pip install -r requirements.txt


```
### Installing Display-o-tron library

The installation of the code for the DOT is more complicated. By default Pimironi provides a complete [python library](https://github.com/pimoroni/displayotron) that supports the DOT HAT and DOT 3000 boards. However it is installed globally and will not play nice with python virtualenv.

To use the code inside a virtualenv, do the following:

```
# download the entire library somewhere local, for example
git clone https://github.com/pimoroni/displayotron somedir

# copy the displayotron/library/dothat to where your source code resides, e.g.
cp somedir/displayotron/library/dothat myproject/src

```

There are only a few files in that python module. Once copied over you will be able to import the `lcd` and `backlight` support library.

## Using the Example

After installation, you should be able to run the code:
`python disp.py`

You should see the LCD display some text, a date time, and the side 6 white
LED bar graph changes over time.


