# raspberry-gt500
Project for animating and lighting up a scale model (Revell Shelby GT500 2010) with a raspberry pi

# Power supply
| Component | Voltage |
| --------|---------|
| Raspberry | 5V |
| Screen | 9V/12V |
| Electronic (with breadboard) | 9V |
| Smoke (not implemented) | 12V |
| Battery supply (not implemented) | 12V |

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

# Shift register '74HC595' Mapping
| bit | Function of led | Nb of leds |
| --------|---------|-------|
| 01 | head left position/turn indicator | (x1) |
| 02 | tail left turn indicator #1 | (x1) |
| 03 | tail left turn indicator #2 | (x1) |
| 04 | tail left turn indicator #3 | (x1) |
| 05 | head right position/turn indicator | (x1) |
| 06 | tail right turn indicator #1 | (x1) |
| 07 | tail right turn indicator #2 | (x1) |
| 08 | tail right turn indicator #3 | (x1) |
| 09 | fog lights | (x2) |
| 10 | lateral position lights | (x4) |
| 11 | tail light | (x6) |
| 12 | head lights | (x2) |
| 13 | rear license plate | (x2) |
| 14 | dashboard    | (x2) |
| 15 | roof light   | (x1) |
| 16 | stop light | N/A |

# Light features
| Button | Function of led |
| --------|---------|-------|
| LIGHT_01/LIGHT_02 | head left position/turn indicator |
| LIGHT_01 | tail left turn indicator #1 |
| LIGHT_01 | tail left turn indicator #2 |
| LIGHT_01 | tail left turn indicator #3 |
| LIGHT_01/LIGHT_02 | head right position/turn indicator |
| LIGHT_01 | tail right turn indicator #1 |
| LIGHT_01 | tail right turn indicator #2 |
| LIGHT_01 | tail right turn indicator #3 |
| LIGHT_02 | lateral position lights |
| LIGHT_02 | tail light |
| LIGHT_03 | head lights |
| LIGHT_03 | rear license plate |
| LIGHT_03 | dashboard    |
| LIGHT_04 | fog lights |
| LIGHT_04 | roof light   |
| LIGHT_04 | stop light |

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
