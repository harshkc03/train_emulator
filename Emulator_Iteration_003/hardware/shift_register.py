import RPi.GPIO as IO
import time

class Shifter:
    def __init__(self,dataPin,latchPin,clkPin,numOfReg,numPinsUsed,direction):
        
        self.data=dataPin
        self.latch=latchPin
        self.clk=clkPin

        self.direction=direction

        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        IO.setup(dataPin,IO.OUT)
        IO.setup(latchPin,IO.OUT)
        IO.setup(clkPin,IO.OUT)

        self.registers=numOfReg
        if direction=="F":
            self.forward=[[0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0]]
        
            self.backward=[[0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0]]
        elif direction=="B":
            self.forward=[[0,0,0,1],
                          [0,0,0,1],
                          [0,0,0,1],
                          [0,0,0,1]]
    
            self.backward=[[0,0,0,0],
                           [1,0,0,1],
                           [0,0,0,1],
                           [0,0,0,1]]  
        self.genGarb(numOfReg,numPinsUsed)

        self.masterUpdate()

        self.masterArray=self.forward+self.backward+self.garbage

        self.push()

    def masterUpdate(self):
        self.masterArray=self.forward+self.backward+self.garbage




    def genGarb(self,reg,pins):
        self.garbage=[]
        for i in range(reg+1-int(pins/8)):
            temp=[]
            for j in range(4):
                temp.append(0)
            self.garbage.append(temp)


    def clearPins(self):
        for y in range(self.registers*8):
            IO.output(self.data,0)
            time.sleep(0.0000001)
            IO.output(self.clk,1)
            time.sleep(0.0000001)
            IO.output(self.clk,0)

        IO.output(self.latch,1)
        time.sleep(0.0001)
        IO.output(self.latch,0)
    
    def setForward(self,forwardArray):
        self.forward=forwardArray
        self.masterUpdate()
        self.push()

    def setBackward(self,backwardArray):
        self.backward=backwardArray
        self.masterUpdate()
        self.push()

    def push(self):
        
        self.masterUpdate()
        for y in range(10):
            for x in range(4):    
                IO.output(self.data,self.masterArray[10-y-1][3-x])
                time.sleep(0.001)
                IO.output(self.clk,1)
                time.sleep(0.001)
                IO.output(self.clk,0)
                # print(y,x)

        IO.output(self.latch,1)
        time.sleep(0.001)
        IO.output(self.latch,0)

    def launchAudio(self):
        self.masterArray[9][3]=1
        self.push()
        
    def stopAudio(self):
        self.masterArray[9][3]=0
        self.push()

    def reset(self):
        if self.direction=="F":
            self.forward=[[0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0]]
        
            self.backward=[[0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0]]
        elif self.direction=="B":
            self.forward=[[0,0,0,1],
                          [0,0,0,1],
                          [0,0,0,1],
                          [0,0,0,1]]
    
            self.backward=[[0,0,0,1],
                           [0,0,0,1],
                           [0,0,0,1],
                           [0,0,0,1]]
        
        self.push()