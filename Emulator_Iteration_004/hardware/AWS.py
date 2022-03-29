import time
from threading import Thread

class AWS:
    {"The class which implements the entire logic of AWS"}
    def __init__(self,train,shiftReg):
        self.shifter=shiftReg
        self.train=train
        self.permission=false

    def signalCrossed(self,signal):
        if signal.isGreen:
            if self.train.currSpeed>self.train.maxSpeed:
                self.spdLimCrossed(self.train.maxSpeed,None)
        elif signal.isYellow:
           if self.train.currSpeed>77.5:
                self.spdLimCrossed(77.5,yellow)
        elif signal.isRed():
            if self.permission:
                if self.train.currSpeed>15:
                    self.spdLimCrossed(15,None)
    
    def spdLimCrossed(limit,mode):
        self.brakingThread=threading.Thread(target=self.spdLim, args=(limit,mode,bn       ))

    def spdLim(self,spdLimit,mode):
        spd=self.train.currSpeed
        if mode==yellow:
            if spd>95:
                self.train.drive(spd-1)
                time.sleep(0.01)
                self.spdLim(95, yellow)
        