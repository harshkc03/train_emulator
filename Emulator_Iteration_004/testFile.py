from hardware import *
import time
 
pin=11


mode="F"

register=shift_register.Shifter(16,20,21,5,32,mode)

# mcp=Multiplexer.Multi([0x20,0x21,0x24],[14,17,27],register,mode)

register.stopAudio()
# while True:
#     pass


