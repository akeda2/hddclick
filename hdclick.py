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
    utime.sleep_ms(5)
    click.duty_u16(0)



#async def sens():
click.duty_u16(0)
print(hdsensA.read_u16())
print(hdsensA.read_u16()* 3.3/65535)
print(hdsens.value())
utime.sleep(2)
while True:
    led.low()
    if hdsens.value() == 1 or hdsensA.read_u16() >= 16000:
        #print("trrr")
        #trrr_worker = asyncio.create_task(trrr())
        led.high()
        trr()
        #print("sleep...")
    utime.sleep_ms(1)