import sys
import time
from RF24 import RF24

radio=RF24(22,0)
counter=[0]

def master():
    radio.stopListening()
    failures=0
    while failures<999:
        buffer=b"Hello \x00"+bytes(counter)
        start_timer=time.monotonic_ns()
        result=radio.write(buffer)
        
        if not result:
            failures+=1
            print("Transmission failed or timed out")
        else:
            radio.startListening()
            timout=time.monotonic()*1000+200
            
            while not radio.available() and time.monotonic()*1000<timout:
                pass
            
            radio.stopListening()
            end_timer=time.monotonic_ns()

            print("Transmission successful. sent: {}{}.".format(
                  buffer[:6].decode("utf-8"),counter[0]),end=" ")

            has_payload, pipe_number=radio.available_pipe()
            if has_payload:
                received = radio.read(radio.payloadSize)
                counter[0]=received[7:8][0]
                print("Received {} bytes on pipe {}: {}{}. "
                      "Round-trip delay : {} us. ".format(radio.payloadSize,
                                                          pipe_number,
                                                          bytes(received[:6]).decode("utf-8"),
                                                          counter[0],
                                                          (end_timer-start_timer)/1000))
            else:
                print("No response received.")
        time.sleep(1)

    print(failures," failures detected. Leaving TX role.")


def slave(timeout=6):
    radio.startListening()
    start_timer=time.monotonic()

    while(time.monotonic()-start_timer)<timeout:
        has_payload,pipe_number=radio.available_pipe()
        if has_payload:
            received=radio.read(radio.payloadSize)
            counter[0]=received[7]+1 if received[7]<255 else 0

            buffer=b'world x\00' + bytes(counter)

            radio.stopListening()
            radio.writeFast(buffer)
            radio.txStandBy(150)
            radio.startListening

            print("Received {} bytes on pipe {}: {}{}.".format(radio.payloadSize,
                                                               pipe_number,
                                                               bytes(received[:6]).decode("utf-8"),
                                                               received[7]),end=" ")

            if result:
                print("sent {}{}".format(buffer[:6].decode("utf-8"),
                                         cunter[0]))
            else: 
                print("Response faied or timed out")
            start_timer=time.monotonic()
    
    print("nothing received in ",timeout," seconds. leaving RX role")
    radio.stopListening()

def set_role():
    user_input = input(
        "*** Enter 'R' for receiver role.\n"
        "*** Enter 'T' for transmitter role.\n"
        "*** Enter 'Q' to quit example.\n"
    ) or "?"
    user_input = user_input.split()
    if user_input[0].upper().startswith("R"):
        if len(user_input) > 1:
            slave(int(user_input[1]))
        else:
            slave()
        return True
    elif user_input[0].upper().startswith("T"):
        master()
        return True
    elif user_input[0].upper().startswith("Q"):
        radio.powerDown()
        return False
    print(user_input[0], "is an unrecognized input. Please try again.")
    return set_role()

if __name__=="__main__":
    if not radio.begin():
        raise RuntimeError("radio hardware is not responding")

    address = [b"1Node", b"2Node"]

    radio.openWritingPipe(address[1])
 
    radio.openReadingPipe(1,address[0])

    radio.payloadSize=8
    try:
        master()

    except KeyboardInterrupt:
        print(" Keyboard Interrupt detected. Exiting...")
        radio.powerDown()
        sys.exit()








        
