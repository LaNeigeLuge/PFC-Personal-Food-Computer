import Adafruit_DHT

sensor=Adafruit_DHT.DHT11

pin=18

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
humidity = humidity
temperature = temperature

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Erreur de connexion... Try again')
