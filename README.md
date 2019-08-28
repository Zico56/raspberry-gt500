# raspberry-gt500
Project for animating and lighting up a scale model (Revell Shelby GT500 2010) with a raspberry pi

# Power supply (TODO)
| Component | Voltage |
| --------|---------|
| Raspberry | 5V |
| Screen | 9V/12V |
| Electronic (with breadboard) | 9V |


# Features
| Button | Feature |
| --------|---------|
| GALLERY | Display/Hide pictures gallery |
| AUDIO | Play GT500 engine sound samples |
| VIDEO | Play GT500 presentation video |
| LIGHT_01 | Head lights <br> Tail lights <br> Front  position lights <br> Side position lights <br> Dashboard <br> (+ License plate?) |
| LIGHT_02 | Fog lights |
| LIGHT_03 | Roof light <br> Reverse lights |
| LIGHT_04 | Turn lights |


# Specific lights behaviour
| LIGHT_04 | Turn lights |
| --------|---------|
| Fist press | Left front/tail turn indicator blinking (sequential light for rear lights) | 
| Second press | Right front/tail turn indicator blinking (sequential light for rear lights) | 
| Third press | Warning lights (all blinking at the same time) | 
| Fourth press | All blinking off | 

# Lights feature and shift register '74HC595' mapping
| bit | Function of led | Nb of leds |
| -------- | --------- | ------- |
| 01 | Left head position/turn indicator | (x1) |
| 02 | Left tail turn indicator #1 | (x1) |
| 03 | Left tail turn indicator #2 | (x1) |
| 04 | Left tail turn indicator #3 | (x1) |
| 05 | Right head position/turn indicator | (x1) |
| 06 | Right tail turn indicator #1 | (x1) |
| 07 | Right tail turn indicator #2 | (x1) |
| 08 | Right tail turn indicator #3 | (x1) |
| 09 | Fog lights | (x2) |
| 10 | Head lights | (x2) |
| 11 | Tail light | (x6) |
| 12 | Side position lights | (x4) |
| 13 | License plate | (x2) |
| 14 | Dashboard    | (x2) |
| 15 | Roof light   | (x1) |
| 16 | Reverse lights | (x4) |

# GPIO Mapping
 BCM | Cobbler Pin | Function |
| --------|---------|-------|
| gpio 02 (I2C : SDA) | SDA | I2C LCD screen |
| gpio 03 (I2C : SCL) | SCL | Power function (on) + I2C LCD screen |
| gpio 04 | P7 | Power function (off) |
| gpio 07 (SPI : CE1) | CE1 | Light1 IN (signal) |
| gpio 08 (SPI : CE0) | CE0 | Light2 IN (signal) |
| gpio 09 (SPI : MISO) | MISO | Light3 IN (signal) |
| gpio 10 (SPI : MOSI) | MOSI | Light4 IN (signal) |
| gpio 11 (SPI : CLK) | SCLK  | Light4 OUT (button led) |
| gpio 14 (UART : TXD) | TXD | Power Led |
| gpio 15 (UART : RXD) | RXD | NC (because of UART activated) |
| gpio 17 | P0  | Shift register SDI |
| gpio 18 (PWM) | P1 | Shift register RCLK |
| gpio 22 | P3 | Gallery IN (signal) |
| gpio 23 | P4 | Audio IN (signal) |
| gpio 24 | P5 | Video IN (signal) |
| gpio 25 | P6 | N/A (IR control ?) |
| gpio 27 | P2 | Shift register SRCLK |





# Wiring

**Power supply**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Power-supply.png?raw=true)

**GPIO input/output**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Pi-GPIO.png?raw=true)

**Shift register**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Shift-register.png?raw=true)

**Led system**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Led-system.png?raw=true)

**PCB**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Shift-register-PCB.png?raw=true)

# Ideas for additionnal features
Smoke
Demo mode
Engine (phone vibrator)
Battery mode
