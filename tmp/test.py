
def mask():
    dat = 0x32
    for bit in range(0, 8):	
        print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(0x80 & (dat << bit)))
        print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(0x01 & (dat >> bit)))
        print()
        #print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(dat & (0x01 << bit)))
        
#mask()

led01 =  0x0001
led05 =  0x0010
led09 =  0x0100
led13 =  0x1000

leds = led01 | led05 | led09 | led13
print(bin(leds))
print(bin(0x8000))