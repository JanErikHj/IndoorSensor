from sys import modules
from utilities.utils import get_wind_direction, get_trend, get_feels_like
import utilities.fonts as fonts
import utilities.colors as colors
from time import sleep
from utilities.graphing import array_to_graph


"""
        icon = display.load_sprite('icons/icon.raw', icon_WIDTH, icon_HEIGHT)
        # Use memoryview to improve memory usage
        mv_icon = memoryview(icon)


        display.draw_sprite(mv_icon, x, y, icon_WIDTH, icon_HEIGHT)

"""
# DRAW STATIS DISPLAY ELEMENTS
def draw_static(display):
    display.clear(color=colors.BG, hlines=24)
    temp_sprite = display.load_sprite(r"icons/THERMOMETER_30.raw", 30, 30)
    hum_sprite = display.load_sprite(r"icons/HUMIDITY_30.raw", 30, 30)
    atmo_sprite = display.load_sprite(r"icons/BAROMETER_30.raw", 30, 30)
    wind_sprite = display.load_sprite(r"icons/WIND_30.raw", 30, 30)
    temp_sprite_m = memoryview(temp_sprite)
    hum_sprite_m = memoryview(hum_sprite)
    atmo_sprite_m = memoryview(atmo_sprite)
    wind_sprite_m = memoryview(wind_sprite)
        
    display.draw_sprite(temp_sprite_m, 10, 50, 30, 30)
    display.draw_sprite(hum_sprite_m, 10, 90, 30, 30)
    display.draw_sprite(atmo_sprite_m, 10, 130, 30, 30)
    display.draw_sprite(wind_sprite_m, 10, 170, 30, 30)
    display.draw_text(225, 10, f"Indoor", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_rectangle(210, 90, 110, 30, colors.FG_SHAPE_D)
    display.draw_rectangle(210, 170, 110, 30, colors.FG_SHAPE_D)

# DRAW CURRENT WEATHER
def draw_current_weather(display, wf):
        
    weather_sprite = display.load_sprite(f"icons/{wf['icon'][:2]}d.raw", 30, 30)
    wind_dir_sprite = display.load_sprite(f"icons/{get_wind_direction(wf['wind_direction'])}", 30, 30)
    feels_like_sprite = display.load_sprite(f"icons/{get_feels_like(wf['feels_like'])}", 30, 30)
        
    weather_sprite_m = memoryview(weather_sprite)
    wind_dir_sprite_m = memoryview(wind_dir_sprite)
    feels_like_sprite_m = memoryview(feels_like_sprite)
    
    display.draw_sprite(wind_dir_sprite_m, 170, 170, 30, 30)
    
    # Display Main Weather
    display.fill_rectangle(10, 10, 160, 30, colors.BG)
    display.fill_rectangle(170, 30, 150, 10, colors.BG)
    display.draw_sprite(weather_sprite_m, 10, 10, 30, 30)
    display.draw_text(35, 10, f"{wf['main_forecast']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(35, 31, f"{wf['description_forecast']}", fonts.BALLY, colors.FG_TEXT_L,  background=colors.BG)
    sleep(0.25)
    
    # Display Current Temperature
    display.fill_rectangle(70, 50, 100, 30, colors.BG)
    display.draw_text(73, 55, f"{wf['current_temperature']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 65, f"C", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    sleep(0.25)
    
    #Display Current Humidity
    display.fill_rectangle(70, 90, 100, 30, colors.BG)
    display.draw_text(73, 95, f"{wf['humidity']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 105, f"%", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    sleep(0.25)
    
    # Display Current Pressure
    display.fill_rectangle(70, 130, 100, 30, colors.BG)
    display.draw_text(73, 135, f"{wf['pressure']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 145, f"hPa", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    sleep(0.25)
    
    # Display Current Wind Speed
    display.fill_rectangle(70, 170, 100, 30, colors.BG)
    display.draw_text(73, 175, f"{wf['wind_speed']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 185, f"m/s", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    sleep(0.25)
    
    # Display Current Feels Like
    display.draw_sprite(feels_like_sprite_m, 10, 210, 30, 30)
    display.draw_text(73, 216, f"{wf['feels_like']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 228, f"C", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)

# DRAW INDOOR MEASUREMENTS AND TREND
def draw_indoor(display, temp, hum, i_temp, i_hum):

    # Get Indoor Trend Icons
    up_sprite = display.load_sprite(r"icons/ARROW_UP.raw", 30, 30)
    down_sprite = display.load_sprite(r"icons/ARROW_DOWN.raw", 30, 30)
    level_sprite = display.load_sprite(r"icons/ARROW_LEVEL.raw", 30, 30)

    sprites = {"up": up_sprite,
               "down": down_sprite,
               "level": level_sprite}

    i_temp_sprite = sprites[get_trend(i_temp)]
    i_hum_sprite = sprites[get_trend(i_hum)]

    i_temp_sprite_m = memoryview(i_temp_sprite)
    i_hum_sprite_m = memoryview(i_hum_sprite)

    # Display Indoor Temperature
    display.fill_rectangle(210, 50, 110, 30, colors.BG)
    display.draw_text(210, 53, f"{temp} C", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_sprite(i_temp_sprite_m, 280, 50, 30, 30)
    sleep(0.25)
    
    array_to_graph(display, i_temp, 210,90,0,30)
    sleep(0.25)
    
    
    # Display Indoor Humidity
    display.fill_rectangle(210, 130, 110, 30, colors.BG)
    display.draw_text(210, 133, f"{hum} %", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_sprite(i_hum_sprite_m, 280, 130, 30, 30)
    sleep(0.25)

    array_to_graph(display, i_hum, 210,170,0,30)

# DRAW CURRENT WEATHER TREND
def draw_trend_f(display, f_temp, f_hum, f_press, f_wind, f_feels): 
    up_sprite = display.load_sprite(r"icons/ARROW_UP.raw", 30, 30)
    down_sprite = display.load_sprite(r"icons/ARROW_DOWN.raw", 30, 30)
    level_sprite = display.load_sprite(r"icons/ARROW_LEVEL.raw", 30, 30)
    
    sprites = {"up": up_sprite,
               "down": down_sprite,
               "level": level_sprite}
    
    f_temp_sprite = sprites[get_trend(f_temp)]
    f_hum_sprite = sprites[get_trend(f_hum)]
    f_atmo_sprite = sprites[get_trend(f_press)]
    f_wind_sprite = sprites[get_trend(f_wind)]
    f_feels_sprite = sprites[get_trend(f_feels)]
    
    f_temp_sprite_m = memoryview(f_temp_sprite)
    f_hum_sprite_m = memoryview(f_hum_sprite)
    f_atmo_sprite_m = memoryview(f_atmo_sprite)
    f_wind_sprite_m = memoryview(f_wind_sprite)
    f_feels_sprite_m = memoryview(f_feels_sprite)
    
    display.draw_sprite(f_temp_sprite_m, 40, 50, 30, 30)
    display.draw_sprite(f_hum_sprite_m, 40, 90, 30, 30)
    display.draw_sprite(f_atmo_sprite_m, 40, 130, 30, 30)
    display.draw_sprite(f_wind_sprite_m, 40, 170, 30, 30)
    display.draw_sprite(f_feels_sprite_m, 40, 210, 30, 30)
    
    
    
    
    
    
    