
from utilities.ili9341 import Display
from machine import Pin, SPI, I2C
from micropython import const  
import utilities.fonts as fonts
import utilities.colors as colors
from weather_forecast import get_weather_forecast
from indoor_sensor import read_indoor_sensor
from utilities.utils import get_wind_direction, log_value, get_trend
from time import ticks_ms, sleep
from utilities.draw_screen import draw_static, draw_current_weather, draw_indoor, draw_trend_f
import utilities.fonts as fonts
import utilities.colors as colors
import utilities.veml7700 as veml7700
import utilities.BME280 as BME280
import _thread

# Set Up Thread Lock
thread_lock = _thread.allocate_lock()

# Timer Delays
forecast_wait = 900000
indoor_wait = 60000

# Logging Variables
i_temp = []
i_hum = []
i_press = []
i_lum = []
f_temp = []
f_hum = []
f_press = []
f_wind = []
f_feels = []
wf = {}
indoor = {}

# Display setup
spi = SPI(1, baudrate=60000000, sck=Pin(48), mosi=Pin(38), miso=Pin(47))
display = Display(spi, dc=Pin(8, Pin.OUT), cs=Pin(10, Pin.OUT), rst=Pin(9, Pin.OUT), width=320, height=240, rotation=90)

# I2C Setup
i2c = I2C(1, scl=Pin(12), sda=Pin(11), freq=10000)


# Indoor sensor setup
lum_sensor = veml7700.VEML7700(address=0x10, i2c=i2c, it=50, gain=1/8)
thp_sensor = BME280.BME280(i2c=i2c)

# Get initial weather forecast and indoor temp hum
wf = get_weather_forecast()
indoor = read_indoor_sensor(thp_sensor, lum_sensor)

# First Log
log_value(i_temp, indoor['temperature'])
log_value(i_hum, indoor['humidity'])
log_value(i_press, indoor['pressure'])
log_value(i_lum, indoor['luminosity'])
log_value(f_temp, wf['current_temperature'])
log_value(f_hum, wf['humidity'])
log_value(f_press, wf['pressure'])
log_value(f_wind, wf['wind_speed'])
log_value(f_feels, wf['feels_like'])

#draw_static(display)
#draw_current_weather(display, wf)
#draw_indoor(display, indoor['temperature'], indoor['humidity'], indoor['pressure'], i_temp, i_hum, i_press)


start_tick_forecast = ticks_ms()
start_tick_indoor = ticks_ms()

#while True:
#    current_tick = ticks_ms()
#    
#    if current_tick-start_tick_forecast > forecast_wait:
#        wf = get_weather_forecast()
#        log_value(f_temp, wf['current_temperature'])
#        log_value(f_hum, wf['humidity'])
#        log_value(f_press, wf['pressure'])
#        log_value(f_wind, wf['wind_speed'])
#        log_value(f_feels, wf['feels_like'])

#        start_tick_forecast = current_tick
        
#    if current_tick-start_tick_indoor > indoor_wait:
#        indoor = read_indoor_sensor(thp_sensor, lum_sensor)
#        log_value(i_temp, indoor['temperature'])
#        log_value(i_hum, indoor['humidity'])
#        log_value(i_press, indoor['pressure'])
#        start_tick_indoor = current_tick

#    sleep(1)
    


def get_data_values():
    global i_temp
    global i_hum
    global i_press
    global i_lum
    global f_temp
    global f_hum
    global f_press
    global f_wind
    global f_feels
    global wf
    global indoor
    global start_tick_forecast
    global start_tick_indoor
    
    while True:
        thread_lock.acquire()
        current_tick = ticks_ms()
    
        if current_tick-start_tick_forecast > forecast_wait:
            wf = get_weather_forecast()
            log_value(f_temp, wf['current_temperature'])
            log_value(f_hum, wf['humidity'])
            log_value(f_press, wf['pressure'])
            log_value(f_wind, wf['wind_speed'])
            log_value(f_feels, wf['feels_like'])

            start_tick_forecast = current_tick
            
        if current_tick-start_tick_indoor > indoor_wait:
            indoor = read_indoor_sensor(thp_sensor, lum_sensor)
            log_value(i_temp, indoor['temperature'])
            log_value(i_hum, indoor['humidity'])
            log_value(i_press, indoor['pressure'])
            start_tick_indoor = current_tick
        thread_lock.release()
        sleep(30)

def update_display():
    global i_temp
    global i_hum
    global i_press
    global i_lum
    global f_temp
    global f_hum
    global f_press
    global f_wind
    global f_feels
    global wf
    global indoor

    while True:
        thread_lock.acquire()
        i_temp_log = i_temp
        i_hum_log = i_hum
        i_press_log = i_press
        i_lum_log = i_lum
        f_temp_log = f_temp
        f_hum_log = f_hum
        f_press_log = f_press
        f_wind_log = f_wind
        f_feels_log = f_feels
        weather_forecast = wf
        indoor_values = indoor
        thread_lock.release()
        
        draw_current_weather(display, weather_forecast)
        draw_trend_f(display, f_temp_log, f_hum_log, f_press_log, f_wind_log, f_feels_log)
        draw_indoor(display, indoor_values['temperature'], indoor_values['humidity'], indoor_values['pressure'], i_temp_log, i_hum_log, i_press_log)

        sleep(60)


_thread.start_new_thread(get_data_values,())

_thread.start_new_thread(update_display, ())









