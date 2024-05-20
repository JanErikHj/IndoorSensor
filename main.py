
from utilities.ili9341 import Display
from machine import Pin, SPI
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
import dht

# Timer Delays
forecast_wait = 900000
indoor_wait = 60000

# Logging Variables
i_temp = []
i_hum = []
f_temp = []
f_hum = []
f_press = []
f_wind = []
f_feels = []


# Display setup
spi = SPI(1, baudrate=60000000, sck=Pin(48), mosi=Pin(38), miso=Pin(47))
display = Display(spi, dc=Pin(8, Pin.OUT), cs=Pin(10, Pin.OUT), rst=Pin(9, Pin.OUT), width=320, height=240, rotation=90)


# Indoor sensor setup
dht_pin = Pin(7)
dht_sensor = dht.DHT22(dht_pin)

# Get initial weather forecast and indoor temp hum
wf = get_weather_forecast()
indoor = read_indoor_sensor(dht_sensor)

# First Log
log_value(i_temp, indoor['temperature'])
log_value(i_hum, indoor['humidity'])
log_value(f_temp, wf['current_temperature'])
log_value(f_hum, wf['humidity'])
log_value(f_press, wf['pressure'])
log_value(f_wind, wf['wind_speed'])
log_value(f_feels, wf['feels_like'])

draw_static(display)
draw_current_weather(display, wf)
draw_indoor(display, indoor['temperature'], indoor['humidity'], i_temp, i_hum)


start_tick_forecast = ticks_ms()
start_tick_indoor = ticks_ms()

while True:
    current_tick = ticks_ms()
    
    if current_tick-start_tick_forecast > forecast_wait:
        wf = get_weather_forecast()
        log_value(f_temp, wf['current_temperature'])
        log_value(f_hum, wf['humidity'])
        log_value(f_press, wf['pressure'])
        log_value(f_wind, wf['wind_speed'])
        log_value(f_feels, wf['feels_like'])
        draw_current_weather(display, wf)
        draw_trend_f(display, f_temp, f_hum, f_press, f_wind, f_feels)
        start_tick_forecast = current_tick
        
    if current_tick-start_tick_indoor > indoor_wait:
        indoor = read_indoor_sensor(dht_sensor)
        log_value(i_temp, indoor['temperature'])
        log_value(i_hum, indoor['humidity'])
        draw_indoor(display, indoor['temperature'], indoor['humidity'], i_temp, i_hum)
        start_tick_indoor = current_tick
        
    sleep(1)
    


