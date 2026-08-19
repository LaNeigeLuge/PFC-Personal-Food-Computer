import Python_DHT

sensor = Python_DHT.DHT11
pin = 4
humidity, temperature = Python_DHT.read_retry(sensor, pin)
print('Temperature = '+str(temperature)+'C Humidity = '+str( humidity)+'%')
