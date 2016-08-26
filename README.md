# Gameduino library for pcDuino

Modified GD.h, GD.cpp to allow compiling on pcDuino.
Tested with pcDuino3 Nano.

Not all examples have been converted. Possible updates needed are:

- *char* changed to *signed char* 
- The addition of the SPI_CONTINUE or SPI_LAST as a second parameter to the SPI.transfer method.

Forked from jamesbowman/gd1

This is the driver library for
[Gameduino 1](http://excamera.com/sphinx/gameduino/),
an Arduino game adapter.

To build the distribution `Gameduino.zip`, run

    python publish.py
