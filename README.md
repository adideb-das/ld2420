
# Initialise LD2420 with Raspberry Pi

Connect the LD2420 sensor with UART configuration of  Raspberry Pi. 

Both RPi 4  Model B and RPi Zero has been tested with this sensor. 

To know if  serial port is enabled, give the command
```
ls /dev/ttyS*
```
You will get an output that gives the serial port name , like /dev/ttyS0 or /dev/ttyS1.

Minicom is already installed , so you can skip this step.

Then give the command 
```
minicom -D /dev/ttyS0
```

or 
```
minicom -D /dev/ttyS1
```

You will get UART readings from LD2420 sensor, which will change as objects is far/near. Since the firmaware is preloaded to plug and play , we have verified that the sensor is working.


The python file attached is already tasted and verified , and LD2420 sensor is currently configured at 8 meters, with a one second delay. 



