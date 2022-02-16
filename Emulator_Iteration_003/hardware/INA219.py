from ina219 import INA219
import time

ina = INA219(shunt_ohms=0.1,
             max_expected_amps = 0.6,
             address=0x40)

ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)

while 1:
    v = ina.voltage()
    i = ina.current()
    p = ina.power()
    
    print('{0:0.1f}V {1:0.1f}mA'.format(v, i))
    print('\n{0:0.1f} Watts'.format(p/1000))
    time.sleep(1)