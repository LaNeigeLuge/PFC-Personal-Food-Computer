import RPi.GPIO as GPIO
import adafruit_dht
import board

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup

instance = adafruit_dht.DHT11(board.D14)
result = instance.humidity

if result.is_valid():
    print("Humidity: %-3.1f %%" %result)
else:
    print("Error: %d" % result.error_code)
