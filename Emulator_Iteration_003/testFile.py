import threading

def convert_int(number,decimals) :
    return str(number).zfill(decimals)

if __name__=="__main__":
    spd=255
    spd= list(str(convert_int(spd, 3)))
    temp0=int(spd[0])
    temp1=int(spd[1])
    temp2=int(spd[2])
    print(temp0, temp1, temp2)