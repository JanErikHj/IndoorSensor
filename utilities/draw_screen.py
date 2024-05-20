from sys import modules
from utilities.utils import get_wind_direction, get_trend
import utilities.fonts as fonts
import utilities.colors as colors


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
        
    display.draw_sprite(temp_sprite_m, 5, 50, 30, 30)
    display.draw_sprite(hum_sprite_m, 5, 90, 30, 30)
    display.draw_sprite(atmo_sprite_m, 5, 130, 30, 30)
    display.draw_sprite(wind_sprite_m, 5, 170, 30, 30)
    display.draw_text(225, 10, f"Indoor", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)

# DRAW CURRENT WEATHER
def draw_current_weather(display, wf):
    display.fill_rectangle(43, 10, 160, 230, colors.BG)
    
    weather_sprite = display.load_sprite(f"icons/{wf['icon'][:2]}d.raw", 30, 30)
    wind_dir_sprite = display.load_sprite(f"icons/{get_wind_direction(wf['wind_direction'])}", 30, 30)
    
    weather_sprite_m = memoryview(weather_sprite)
    wind_dir_sprite_m = memoryview(wind_dir_sprite)
    
    display.draw_sprite(weather_sprite_m, 5, 10, 30, 30)
    display.draw_sprite(wind_dir_sprite_m, 170, 170, 30, 30)
    
    display.draw_text(35, 10, f"{wf['main_forecast']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    #display.draw_text(5, 37, f"{wf['description_forecast']}", fonts.BALLY, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(73, 55, f"{wf['current_temperature']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 65, f"C", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    #display.draw_text(132, 59, f"Max: {wf['max_temperature']}", fonts.BALLY, colors.FG_SHAPE_L,  background=colors.BG)
    #display.draw_text(132, 69, f"Min: {wf['min_temperature']}", fonts.BALLY, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(73, 95, f"{wf['humidity']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 105, f"%", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(73, 135, f"{wf['pressure']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 145, f"hPa", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(73, 175, f"{wf['wind_speed']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(140, 185, f"m/s", fonts.ARCADE, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(5, 216, f"Feels Like", fonts.UNISPACE, colors.FG_SHAPE_L,  background=colors.BG)
    display.draw_text(140, 216, f"{wf['feels_like']}", fonts.UNISPACE, colors.FG_SHAPE_L,  background=colors.BG)

# DRAW INDOOR MEASUREMENTS AND TREND
def draw_indoor(display, temp, hum, i_temp, i_hum):
    display.fill_rectangle(207, 45, 106, 172, colors.BG)
    display.draw_text(210, 55, f"{temp} C", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(210, 133, f"{hum} %", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
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
   
    display.draw_sprite(i_temp_sprite_m, 280, 55, 30, 30)
    display.draw_sprite(i_hum_sprite_m, 280, 133, 30, 30)


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
    display.draw_sprite(f_feels_sprite_m, 180, 210, 30, 30)
    
    
    
    
    
    
    