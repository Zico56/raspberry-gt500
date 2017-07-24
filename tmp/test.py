
def mask():
    dat = 0x32
    for bit in range(0, 8):	
        print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(0x80 & (dat << bit)))
        print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(0x01 & (dat >> bit)))
        print()
        #print("data:" + str(bin(dat)) + " | bit:" + str(bit) + " | mask:" + bin(dat & (0x01 << bit)))
        
mask()