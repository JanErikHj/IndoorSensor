
def read_indoor_sensor(sensor):
    sensor.measure()
    sensor_reading = {"temperature":round(sensor.temperature(),1),
                      "humidity":round(sensor.humidity(),1)
                    }

    return sensor_reading