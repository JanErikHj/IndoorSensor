
def read_indoor_sensor(thp_sensor, lum_sensor):
    luminosity = lum_sensor.read_lux()
    temperature = thp_sensor.temperature
    humidity = thp_sensor.humidity
    pressure = thp_sensor.pressure
    
    sensor_reading = {"temperature":float(temperature),
                      "humidity":float(humidity),
                      "pressure": float(pressure),
                      "luminosity": luminosity
                    }

    return sensor_reading