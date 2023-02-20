import sys
import time
import RPi.GPIO as GPIO
from RF24 import RF24, RF24_PA_LOW
import time

radio = RF24(22,0)

counter = [0]

# select your digital input pin that's connected to the IRQ pin on the nRF24L01
IRQ_PIN = 12

def slave():

    # setup the first transmission's ACK payload
    buffer = b"World \x00" + bytes(counter)
    # we must set the ACK payload data and corresponding
    # pipe number [0,5]
    radio.writeAckPayload(1, buffer)  # load ACK for first response
    
    has_payload, pipe_number = radio.available_pipe()
    if has_payload:
        length = radio.getDynamicPayloadSize()  # grab the payload length
        received = radio.read(length)  # fetch 1 payload from RX FIFO
        # increment counter from received payload
        counter[0] = received[7:8][0] + 1 if received[7:8][0] < 255 else 0
        print(
            "Received {} bytes on pipe {}: {}{} Sent: {}{}".format(
                length,
                pipe_number,
                bytes(received[:6]).decode("utf-8"),
                received[7:8][0],
                buffer[:6].decode("utf-8"),
                buffer[7:8][0]
            )
        )
        buffer = b"World \x00" + bytes(counter)  # build a new ACK payload
        radio.writeAckPayload(1, buffer)  # load ACK for next response

def interrupt_handler(channel):
    """This function is called when IRQ pin is detected active LOW"""
    print("IRQ pin", channel, "went active LOW.")
    tx_ds, tx_df, rx_dr = radio.whatHappened()   # get IRQ status flags
    if tx_df:
        radio.flush_tx()
    slave()

# setup IRQ GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRQ_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(IRQ_PIN, GPIO.FALLING, callback=interrupt_handler)

if __name__ == "__main__":

    # initialize the nRF24L01 on the spi bus
    if not radio.begin():
        raise RuntimeError("radio hardware is not responding")

    # An address need to be a buffer protocol object (bytearray)
    address = [b"1Node", b"2Node"]

    radio_number = 1

    # ACK payloads are dynamically sized.
    radio.enableDynamicPayloads()  # to use ACK payloads

    # to enable the custom ACK payload feature
    radio.enableAckPayload()

    # set the Power Amplifier level to -12 dBm since this test example is
    # usually run with nRF24L01 transceivers in close proximity of each other
    radio.setPALevel(RF24_PA_LOW)  # RF24_PA_MAX is default

    # set the TX address of the RX node into the TX pipe
    radio.openWritingPipe(address[radio_number])  # always uses pipe 0

    # set the RX address of the TX node into a RX pipe
    radio.openReadingPipe(1, address[not radio_number])  # using pipe 1

    #radio.printPrettyDetails()

    try:
        radio.startListening()  # put radio in RX mode
        print("Radio started")
        
        while True:
            #slave()
            pass
    except KeyboardInterrupt:
        print(" Keyboard Interrupt detected. Exiting...")
        radio.powerDown()
        sys.exit()
