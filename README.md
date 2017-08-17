# raspberry-gt500
Project for animating and lighting up a scale modele (GT500) with a raspberry pi

######### Power supply #########
Raspberry : 5V
Screen : 9V/12V
Electronic (with breadboard) : 9V
Smoke : 12V
Battery supply : 12V

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
# gpio15 (UART : RXD) : RXD                 : N/A (IR command ?)
# gpio17              : P0                  : Shift register SDI
# gpio18 (PWM)        : P1                  : Shift register RCLK
# gpio22              : P3                  : Gallery IN (signal)
# gpio23              : P4                  : Gallery OUT (button led)
# gpio24              : P5                  : Audio IN (signal)
# gpio25              : P6                  : Audio OUT (button led)
# gpio27              : P2                  : Shift register SRCLK

# Ideas for additionnal features
Smoke
Demo mode
Engine (phone vibrator)

######### 74HC595 Mapping #########
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
---


######### 74HC595 #1 Mapping #########
input 1 : P3 (or reuse P0 ?)
input 2 : P4 (or reuse P1 ?)
input 3 : P5 (or reuse P2 ?)
output 1 : Front lights
output 2 : Front fog lights
output 3 : Rear left lights #1 #2 #3
output 4 : Rear right lights #1 #2 #3
output 5 : Lateral front lights
output 6 : Lateral rear lights
output 7 : Interior lights (tableau de bord)
output 8 : Interior lights (plafonnier)
rear license plate