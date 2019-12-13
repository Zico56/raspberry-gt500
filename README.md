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
| POWER | Start/Stop the system |
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

| POWER | Power lights |
| --------|---------|
| Lights up at boot|Plugged on serial port: TxD & RxD pin (GPIO 14 &15). Needs activation of UART mode (GPIO15 cannot be used as input/output anymore)|


# Lights feature and shift register '74HC595' mapping
| bit | Function of led | Nb of leds |
| -------- | --------- | ------- |
| 00 | Left head position/turn indicator | (x1) |
| 01 | Left tail turn indicator #1 | (x1) |
| 02 | Left tail turn indicator #2 | (x1) |
| 03 | Left tail turn indicator #3 | (x1) |
| 04 | Right head position/turn indicator | (x1) |
| 05 | Right tail turn indicator #1 | (x1) |
| 06 | Right tail turn indicator #2 | (x1) |
| 07 | Right tail turn indicator #3 | (x1) |
| 08 | Fog lights | (x2) |
| 09 | Head lights | (x2) |
| 10 | Tail light | (x6) |
| 11 | Side position lights | (x4) |
| 12 | License plate | (x2) |
| 13 | Dashboard    | (x2) |
| 14 | Roof light   | (x1) |
| 15 | Reverse lights | (x4) |

# GPIO Mapping
 BCM | Cobbler Pin | Function |
| --------|---------|-------|
| gpio 02 (I2C : SDA) | SDA | I2C LCD screen |
| gpio 03 (I2C : SCL) | SCL | 'POWER' button "on" signal + I2C LCD screen |
| gpio 04 | P7 | 'POWER' button "off" signal |
| gpio 07 (SPI : CE1) | CE1 | 'LIGHT_2' button input signal |
| gpio 08 (SPI : CE0) | CE0 | 'LIGHT_1' button input signal |
| gpio 09 (SPI : MISO) | MISO | 'LIGHT_4' led output signal |
| gpio 10 (SPI : MOSI) | MOSI | 'LIGHT_4' button input signal |
| gpio 11 (SPI : CLK) | SCLK  | 'LIGHT_3' button input signal |
| gpio 14 (UART : TXD) | TXD | 'POWER' led output signal |
| gpio 15 (UART : RXD) | RXD | NC (because of UART activated) |
| gpio 17 | P0  | Shift register SDI/SER |
| gpio 18 (PWM) | P1 | Shift register RCLK |
| gpio 22 | P3 | N/A |
| gpio 23 | P4 | 'AUDIO' button input signal |
| gpio 24 | P5 | 'VIDEO' button input signal |
| gpio 25 | P6 | 'GALLERY' button input signal |
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

**GPIO PCB**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/GPIO-In-Out-PCB.png?raw=true)

**Shift register PCB**
![alt text](https://github.com/Zico56/raspberry-gt500/blob/master/wiring/Shift-register-PCB.png?raw=true)

# Ideas for additionnal features
Smoke<br>
Demo mode<br>
Engine (phone vibrator)<br>
Battery mode<br>
Remote control (wifi/phone)<br>
