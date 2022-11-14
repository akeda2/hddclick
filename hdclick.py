#import uasyncio as asyncio
import rp2
import utime
from machine import Pin, PWM, ADC

# Digital input:
hdsens = Pin(21, Pin.IN,Pin.PULL_DOWN)
# ADC input:
adc = Pin(26, Pin.IN)
hdsensA = ADC(adc)
# Outputs: (inbuilt LED and speaker PWM out)
led = Pin(25, Pin.OUT)
click = PWM(Pin(2))
# Set by htsthd() to signal input mode: (+5V(standard) or +-5V(Dell-mode))
dellMode = False

# asyncio test: (not used, just for reference)
#async def trrr():
#    click.freq(109)
#    click.duty_u16(16000)
#    await asyncio.sleep_ms(5)
#    click.duty_u16(0)
def trr():
    click.freq(30)
    click.duty_u16(16000)
    utime.sleep_ms(10)
    click.duty_u16(0)

def testhd():
    global dellMode
    s = 0
    inputType = 0
    print("input test")
    while s < 5:
        led.high()
        Dval = hdsens.value()
        Aval = hdsensA.read_u16()
        print("Dval:", Dval)
        print("Aval:", Aval, Aval * 3.3/65535,"V")
        if Aval > 16000:
            inputType += 1
        s += 1
        print(s)
        led.low()
        utime.sleep(1)
    if inputType >= 3:
        dellMode = True
        print("Aval:", Aval, Aval * 3.3/65535,"V", "inputType=",inputType, "Dell-mode is ON")
    s=0
    print("output test")
    while s < 5:
        led.high()
        trr()
        s += 1
        print(s)
        led.low()
        utime.sleep(1)
    print("test end..")

# Starts here:
#
# Set duty to 0
click.duty_u16(0)
# Run initial tests:
# Input check: +5V&GR or +-5V. Are we using digital or analog inputs?
# Output check: Test speaker/piezo or whatever we use for output.
testhd()
utime.sleep(2)

# Main loop:
while True:
    led.low()
    Dval = hdsens.value()
    Aval = hdsensA.read_u16()
    if Dval == 1:
#	Testing asyncio: (not used, just left for reference)
        #print("trrr")
        #trrr_worker = asyncio.create_task(trrr())
        led.high()
        trr()
        print("Dval:", Dval)
    elif dellMode and Aval <= 1000:
        led.high()
        trr()
        print("Aval:", Aval, "D")
    elif not dellMode and Aval >= 16000:
        led.high()
        trr()
        print("Aval:", Aval, "S")
# Uncomment for debugging: (will hog resources!)
#    else:
#        print("No signal Dval:", Dval, "Aval:", Aval)
    utime.sleep_ms(1)