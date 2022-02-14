from tkinter import *
from resources import *
from hardware import *
from ina219 import INA219
import threading
import time

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x800")
        self.attributes("-fullscreen")
        self.config(bg="#000000")
        utils.gridConfigure(self.numberOfRows,self.numberOfColumns,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()
        self.initWidgets()
        self.launchLogin()
        self.startTasks()

    def createWidgets(self):
        #Info frame
        self.infoFrame=child_frames.InfoFrame(self)        

        #Button Holder Frame
        self.buttonsFrame=child_frames.ButtonHolder(self)
        
        #Parent frame for all sub frames
        self.topLevelFrame=Frame(self,bg="#000000")

        #login Frame
        self.frame01=Frame(master=self.topLevelFrame,bg="#000000")
        self.loginFrame=child_frames.Login(self.frame01,self)      
        self.frame02=child_frames.Frame02(self.topLevelFrame,root=self)
        self.frame03=child_frames.Frame03(master=self.topLevelFrame,root=self)   
        self.frame04=child_frames.Frame04(master=self.topLevelFrame,root=self)
        self.frame05=child_frames.Frame05(master=self.topLevelFrame,root=self)
        self.frame06=child_frames.Frame06(master=self.topLevelFrame,root=self)
        self.frame07=child_frames.Frame07(master=self.topLevelFrame,root=self)
        self.frame08=child_frames.Frame08(master=self.topLevelFrame,root=self)
        self.frame09=child_frames.Frame09(master=self.topLevelFrame,root=self)
        self.frame10=child_frames.Frame10(master=self.topLevelFrame,root=self)
        self.frame11=child_frames.Frame11(master=self.topLevelFrame,root=self)   
          
        #Dictionary containing frames and an index
        self.frameDict={self.frame01:1,
                        self.frame02:2,
                        self.frame03:3,
                        self.frame04:4,
                        self.frame05:5,
                        self.frame06:6,
                        self.frame07:7,
                        self.frame08:8,
                        self.frame09:9,
                        self.frame10:10,
                        self.frame11:11}

    def configureWidgets(self):
            
        #configuring topLevelFrame grid       
        utils.gridConfigure(self.numberOfRows-2,self.numberOfColumns,self.topLevelFrame)

        utils.gridConfigure(1,3,self.frame03)

    def placeWidgets(self):
        #infoFrame
        self.infoFrame.grid(row=0,column=0,columnspan=self.numberOfColumns,sticky="news",pady=2)       

        #Buttons
        self.buttonsFrame.grid(row=1,column=0,columnspan=self.numberOfColumns,sticky="news")
        self.buttonsFrame.configureWidgets()
        self.buttonsFrame.placeWidgets()

        #TopLevelFrame
        self.topLevelFrame.grid(row=2,rowspan=self.numberOfRows-2,
                                       column=0,columnspan=self.numberOfColumns,
                                       sticky="news",pady=2)

        self.loginFrame.place(relx=0.5,rely=0.5,relheight=1,relwidth=0.8,anchor='center')
     
    def initWidgets(self):
        print("Initializing......")
       
    def launchLogin(self):
        print("launching login")
        self.buttonsFrame.disableButtonsExcept([1])
        self.buttonsFrame.button01.invoke()   
    
    def setState(self,state):
        if state == "Driver":
            self.buttonsFrame.disableButtonsExcept([1,3,5,7,9,11])
        elif state == "Maintenance":
            self.buttonsFrame.enableAll()
        elif state=="Exit":
            quit()
        elif state=="Lock":
            self.buttonsFrame.disableButtonsExcept([1])
    
    def startTasks(self):
        self.stop=threading.Event()
        self.guiThread=threading.Thread(target=self.mainThreadLoop, args=(self.stop,))
        self.guiThread.start()

        self.rf=nrf.Radio()
        self.adc=MCP3008.MCP3008()
        self.ina219 = INA219(shunt_ohms=0.1, max_expected_amps = 0.6, address=0x40)
        self.ina219.configure(voltage_range=self.ina219.RANGE_16V,
                              gain=self.ina219.GAIN_AUTO,
                              bus_adc=self.ina219.ADC_128SAMP,
                              shunt_adc=self.ina219.ADC_128SAMP)

    def mainThreadLoop(self, stop):

        # print(self.infoFrame.modeLabel.cget("text"))
        while not stop.isSet():
            curMode=self.infoFrame.modeLabel.cget("text")

            if curMode == "Drive":
                adc_val = self.adc.read(channel=0)
                spd = int(utils.translate(adc_val, 0, 1023, 0, 255))
                print(spd)
                time.sleep(0.05)
                self.rf.drive(spd,1)
            elif curMode == "Simulate":
                self.rf.simulate()
                time.sleep(0.5)
            elif curMode == "Demo":
                self.rf.demo(1,0) # (1,1) = (Start, Forward)
                time.sleep(0.05)

    def sayHitoRpi(self):
        print("hello Rpi!")
        

    #Variables
    numberOfRows=12
    numberOfColumns=11
    mainRadioButtonVar=1
    modeSelectButtonVar=2
    defaultFont="Calibri 15"

app=MainWindow()
app.mainloop()