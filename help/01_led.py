#!/usr/bin/env python
from emulator.GPIOEmulator import App
from emulator.GPIOEmulator import GPIO 
import time

App()

####### BCM ######### : ### Cobbler Pin ### : ## Test ##
# gpio02 (I2C : SDA)  : SDA                 : KO (already set)
# gpio03 (I2C : SCL)  : SCL                 : KO (already set)
# gpio04              : P7                   : OK
# gpio07 (SPI : CE1)  : CE1                 : KO (legere lumiere)
# gpio08 (SPI : CE0)  : CE0                 : KO (legere lumiere)
# gpio09 (SPI : MISO) : MISO                : OK
# gpio10 (SPI : MOSI) : MOSI                : OK
# gpio11 (SPI : CLK)  : SCLK                : OK
# gpio14 (UART : TXD) : TXD                 : KO (already set)
# gpio15 (UART : RXD) : RXD                 : KO (legere lumiere)
# gpio17              : P0                   : OK
# gpio18 (PWM)        : P1                   : OK
# gpio22              : P3                   : OK
# gpio23              : P4                   : OK
# gpio24              : P5                   : OK
# gpio25              : P6                   : OK
# gpio27              : P2                   : OK


LedPin = 2    # gpioXX

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		print('...led on')
		GPIO.output(LedPin, GPIO.LOW)  # led on
		time.sleep(0.5)
		print('led off...')
		GPIO.output(LedPin, GPIO.HIGH) # led off
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

