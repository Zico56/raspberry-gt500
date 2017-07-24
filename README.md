# raspberry-gt500
Project for animating and lighting up a scale modele (GT500) with a raspberry pi

######### Features #########
Lights (front/rear)
Warning/left-right indicators
Lateral light (rear/front & left/right)
Interior lights
Fog lights

Video
Audio
Smoke
Demo mode
Engine (phone vibrator)
Shutdown command (easter egg ?) (need 1 GPIO input)
IR command ? (need 1 GPIO output)


######### GPIO Mapping (3.3V/5V/GND exluded) #########
SDA           : LCD I2C Display
SCL           : LCD I2C Display
gpio09 (MISO) : input  : smoke
gpio10 (MOSI) : output : smoke   
gpio17 (P0)   : input  : gallery
gpio18 (P1)   : input  : video player
gpio27 (P2)   : input  : warning lights
gpio22 (P3)   : output : warning lights

######## BCM ######## : ### Cobbler Pin ### : ## Test ##
# gpio02 (I2C : SDA)  : SDA                 : KO (already set)
# gpio03 (I2C : SCL)  : SCL                 : KO (already set)
# gpio04              : P7                  : OK
# gpio07 (SPI : CE1)  : CE1                 : KO (legere lumiere)
# gpio08 (SPI : CE0)  : CE0                 : KO (legere lumiere)
# gpio09 (SPI : MISO) : MISO                : OK
# gpio10 (SPI : MOSI) : MOSI                : OK
# gpio11 (SPI : CLK)  : SCLK                : OK
# gpio14 (UART : TXD) : TXD                 : KO (already set)
# gpio15 (UART : RXD) : RXD                 : KO (legere lumiere)
# gpio17              : P0                  : OK
# gpio18 (PWM)        : P1                  : OK
# gpio22              : P3                  : OK
# gpio23              : P4                  : OK
# gpio24              : P5                  : OK
# gpio25              : P6                  : OK
# gpio27              : P2                  : OK


######### 74HC595 #1 Mapping #########
input 1 : P0
input 2 : P1
input 3 : P2
output 1 : rear left indicator #1
output 2 : rear left indicator #2
output 3 : rear left indicator #3
output 4 : rear right indicator #1
output 5 : rear right indicator #2
output 6 : rear right indicator #3
output 7 : front left indicator
output 8 : front right indicator

######### 74HC595 #1 Mapping #########
input 1 : P3 (or reuse P0 ?)
input 2 : P4 (or reuse P1 ?)
input 3 : P5 (or reuse P2 ?)
output 1 : Front lights
output 2 : Front fog lights
output 3 : 
output 4 : 
output 5 : 
output 6 : 
output 7 : 
output 8 : 