#!/usr/bin/env python
import LCD1602
import time

def setup():
    LCD1602.init(0x27, 1)    # init(slave address, background light)
    LCD1602.write(0, 0, 'CPU Temperature:')
    LCD1602.write(1, 1, getCPUtemperature())
    time.sleep(2)

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n","") + chr(223) + "C")

def destroy():
    pass    

if __name__ == "__main__":
    try:
        setup()
        while True:
            pass
    except KeyboardInterrupt:
        destroy()
