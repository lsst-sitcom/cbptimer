# cbptimer

This is a command line utility for use with the Raspberry Pi based logic timer units used in the calibration
system for colimated beam projector (CBP) at the Rubin Observatory.  The utility leverages
[pigpio](https://abyz.me.uk/rpi/pigpio/) to generate CSV file logs of &mu;-second ticks corresponding to
edge events on the timer units' TTL trigger input.
