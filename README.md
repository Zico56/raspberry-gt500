# raspberry-gt500
Project for animating and lighting up a scale modele (GT500) with a raspberry pi

######### Power supply #########
Raspberry : 5V
Screen : 9V/12V
Electronic (with breadboard) : 9V
Smoke : 12V
Battery supply : 12V

# Ideas for additionnal features
Smoke
Demo mode
Engine (phone vibrator)

##################### GPIO Mapping #####################
######## BCM ######## : ### Cobbler Pin ### : ## Test ##
# gpio02 (I2C : SDA)  : SDA                 : I2C LCD screen
# gpio03 (I2C : SCL)  : SCL                 : Power function (on) + I2C LCD screen
# gpio04              : P7                  : Power function (off)
# gpio07 (SPI : CE1)  : CE1                 : Video IN (signal)
# gpio08 (SPI : CE0)  : CE0                 : Video OUT (button led)
# gpio09 (SPI : MISO) : MISO                : Light1 IN (signal)
# gpio10 (SPI : MOSI) : MOSI                : Light2 IN (signal)
# gpio11 (SPI : CLK)  : SCLK                : Light3 IN (signal)
# gpio14 (UART : TXD) : TXD                 : Light4 IN (signal)
# gpio15 (UART : RXD) : RXD                 : N/A (IR control ?)
# gpio17              : P0                  : Shift register SDI
# gpio18 (PWM)        : P1                  : Shift register RCLK
# gpio22              : P3                  : Gallery IN (signal)
# gpio23              : P4                  : Gallery OUT (button led)
# gpio24              : P5                  : Audio IN (signal)
# gpio25              : P6                  : Audio OUT (button led)
# gpio27              : P2                  : Shift register SRCLK

####################### 74HC595 Mapping ########################
# bit # : ######### Function of led ######### : ## Nb of leds ##
# 01    : head left position/turn indicator   : (x1)
# 02    : tail left turn indicator #1         : (x1)
# 03    : tail left turn indicator #2         : (x1)
# 04    : tail left turn indicator #3         : (x1)
# 05    : head right position/turn indicator  : (x1)
# 06    : tail right turn indicator #1        : (x1)
# 07    : tail right turn indicator #2        : (x1)
# 08    : tail right turn indicator #3        : (x1)
# 09    : fog lights                          : (x2)
# 10    : lateral position lights             : (x4)
# 11    : tail light                          : (x6)
# 12    : head lights                         : (x2)
# 13    : rear license plate (mutualisable?)  : (x2)
# 14    : dashboard                           : (x2)
# 15    : roof light                          : (x1)
# 16    : N/A