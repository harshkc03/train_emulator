import sys
import time
from RF24 import RF24

class Radio():
    def __init__(self):
        self.radio=RF24(22,0)

        if not self.radio.begin():
            raise RuntimeError("radio hardware is not responding. Please check the hardware")
        else:
            address=[b"1Node",b"2Node"]
            self.radio.openWritingPipe(address[1])
            self.radio.openReadingPipe(1,address[0])    
            self.radio.payloadSize=8

    def demo(self):
        self.radio.stopListening()
        buffer=b"DE.....\x00"
        result=self.radio.write(buffer)

        if not result:
            print("Demo Transmission failed or timed out")
            time.sleep(1)
        else:
            print("Transmission Successful")

    def drive(self):
        self.radio.stopListening()
        buffer=b"DR.....\x00"
        result=self.radio.write(buffer)

        if not result:
            print("Drive Transmission failed or timed out")
            time.sleep(1)
        else:
            print("Transmission Successful")

    def simulate(self):
        self.radio.stopListening()
        buffer=b"SI     \x00"
        result=self.radio.write(buffer)

        if not result:
            print("Transmission failed or timed out")
            time.sleep(1)
        else:
            print("Transmission Successful")

    def test(self):
        self.radio.stopListening()
        buffer=b"sent\x00\x00\x00\x00"
        result=self.radio.write(buffer)

        while not result:
            print("Radio is not responding...")
            time.sleep(0.1)
            return self.test()
        
        print("Radio is ready to go")
            
   
    interrupt=False    
            
# if __name__=="__main__":
#     rf=Radio()
#     rf.demo()
#     rf.radio.powerDown()