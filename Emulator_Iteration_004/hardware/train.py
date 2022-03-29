import sys
import time
from RF24 import RF24
from resources import utils

class Train():
    def __init__(self):
        self.radio=RF24(22,0)
        self.currSpeed=0

        if not self.radio.begin():
            raise RuntimeError("radio hardware is not responding. Please check the hardware")
        else:
            address=[b"1Node",b"2Node"]
            self.radio.openWritingPipe(address[1])
            self.radio.openReadingPipe(1,address[0])    
            self.radio.payloadSize=8

    def drive(self, spd, direction):
        self.radio.stopListening()
        spd= list(str(utils.convert_int(spd, 3)))
        temp0=int(spd[0])
        temp1=int(spd[1])
        temp2=int(spd[2])
        temp="DR"+str(temp0)+str(temp1)+str(temp2)+str(direction)+".\x00"
        buffer=bytes(temp, encoding='utf8')
        self.result=self.radio.write(buffer)

        if not self.result:
            print("Drive Transmission failed or timed out")
            
        else:
            print("Transmission Successful")
            self.radio.startListening()
            timout=time.monotonic()*1000+200
            
            while not self.radio.available() and time.monotonic()*1000<timout:
                pass
            
            self.radio.stopListening()
            received=self.radio.read(self.radio.payloadSize)
            self.currSpeed=int(received[7])
            print(int(received[7]))