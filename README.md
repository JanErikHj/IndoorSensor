# IndoorSensor

This project is to make an indoor climate sensor also with current outdoor forecast, for my home.

CURRENT STATE: Initial testing 

### Hardware:
- Arduino Nano ESP32
- DHT22 Temperature and Humidity Sensor
- 3.2" ili9341 SPI Display

### Software
- Micro Python
- Display Driver: ili9341 from: [https://github.com/rdagger/micropython-ili9341](https://github.com/rdagger/micropython-ili9341)
- api.openweathermap.org is used for weather forecast


### Schematic
Current Schematic ![Image](/Docs/Cirquit.png)

### Housing:
Have not yet decided on wether to make this from wood or to 3D print it. It would be a great excuse to buy a 3D printer!

## Future:

The plan is to replace the DHT22 sensor with a BME280 that includes air pressure as well as temperature and humidity. I have not yet decided on what sensor to use for air pollutants and gasses, or what sensor to use for ambient luminocity.

More to come as the project develops.


