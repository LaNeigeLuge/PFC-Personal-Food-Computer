import RPi.GPIO as GPIO
import time

channel_light = 27
#channel_fan = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_light, GPIO.OUT)
#GPIO.setup(channel_fan, GPIO.OUT)

def gpio_off(pin):
    GPIO.output(pin, GPIO.HIGH)

def gpio_on(pin):
    GPIO.output(pin, GPIO.LOW)


try:
    gpio_on(channel_light)
    #gpio_on(channel_fan)
    time.sleep(5)
    gpio_off(channel_light)
    #gpio_off(channel_fan)
    time.sleep(5)
    gpio_on(channel_light)
    #gpio_on(channel_fan)
    time.sleep(5)
    gpio_off(channel_light)
    #gpio_off(channel_fan)

except KeyboardInterrupt:
    GPIO.cleanup
        
        
