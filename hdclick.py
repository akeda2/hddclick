import uasyncio as asyncio
import rp2
import utime
from machine import Pin, PWM, ADC

hdsens = Pin(21, Pin.IN,Pin.PULL_DOWN)
adc = Pin(26, Pin.IN)
hdsensA = ADC(adc)

led = Pin(25, Pin.OUT)

click = PWM(Pin(2))
#click.freq(25000)

async def trrr():
    click.freq(109)
    click.duty_u16(16000)
    await asyncio.sleep_ms(5)
    click.duty_u16(0)
    #self.bell.deinit()
def trr():
    click.freq(30)
    click.duty_u16(16000)
    #await asyncio.sleep_ms(5)
    utime.sleep_ms(10)
    click.duty_u16(0)

def testhd():
    s = 0
    print("input test")
    while s < 5:
        led.high()
        print(hdsensA.read_u16())
        print(hdsens.value())
        s += 1
        print(s)
        led.low()
        utime.sleep(1)
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

#async def sens():
click.duty_u16(0)
#print(hdsensA.read_u16())
#print(hdsensA.read_u16()* 3.3/65535)
#print(hdsens.value())
testhd()
utime.sleep(2)
while True:
    led.low()
    Dval = hdsens.value()
    Aval = hdsensA.read_u16()
    if Dval == 1:
        #print("trrr")
        #trrr_worker = asyncio.create_task(trrr())
        led.high()
        trr()
        print("Dval:", Dval)
    elif Aval <= 1000:
        led.high()
        trr()
        print("Aval:", Aval)
    else:
        print("No signal Dval:", Dval, "Aval:", Aval)
    utime.sleep_ms(1)