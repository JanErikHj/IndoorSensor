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
# DRAW STATIc DISPLAY ELEMENTS
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
        
    display.draw_sprite(temp_sprite_m, 10, 60, 30, 30)
    display.draw_sprite(hum_sprite_m, 160, 60, 30, 30)
    display.draw_sprite(atmo_sprite_m, 10, 100, 30, 30)
    display.draw_sprite(wind_sprite_m, 160, 100, 30, 30)
    display.draw_sprite(temp_sprite_m, 10, 180, 30, 30)
    display.draw_sprite(hum_sprite_m, 100, 180, 30, 30)
    display.draw_sprite(atmo_sprite_m, 200, 180, 30, 30)
   
   
    display.draw_rectangle(10,10,300,40,colors.FG_SHAPE_L)

# DRAW CURRENT WEATHER
def draw_current_weather(display, wf):
        
    weather_sprite = display.load_sprite(f"icons/{wf['icon'][:2]}d.raw", 30, 30)
    wind_dir_sprite = display.load_sprite(f"icons/{get_wind_direction(wf['wind_direction'])}", 30, 30)
    feels_like_sprite = display.load_sprite(f"icons/{get_feels_like(wf['feels_like'])}", 30, 30)
        
    weather_sprite_m = memoryview(weather_sprite)
    wind_dir_sprite_m = memoryview(wind_dir_sprite)
    feels_like_sprite_m = memoryview(feels_like_sprite)
    
    
    
    # Display Main Weather
    display.fill_rectangle(11, 11, 298, 38, colors.BG)
    display.draw_sprite(weather_sprite_m, 270, 15, 30, 30)
    display.draw_text(15, 21, f"Forecast: ", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(100, 14, f"{wf['main_forecast']}", fonts.UNISPACE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_text(15, 38, f"{wf['description_forecast']}", fonts.BALLY, colors.FG_TEXT_L,  background=colors.BG)

    
    # Display Current Temperature
    display.fill_rectangle(40, 60, 110, 30, colors.BG)
    display.draw_text(42, 70, f"{wf['current_temperature']}C", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)

    
    #Display Current Humidity
    display.fill_rectangle(190, 60, 110, 30, colors.BG)
    display.draw_text(192, 70, f"{wf['humidity']}%", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)

    
    # Display Current Pressure
    display.fill_rectangle(40, 100, 110, 30, colors.BG)
    display.draw_text(42, 110, f"{wf['pressure']}hPa", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)

    
    # Display Current Wind Speed
    display.fill_rectangle(190, 100, 50, 30, colors.BG)
    display.draw_sprite(wind_dir_sprite_m, 250, 100, 30, 30)
    display.draw_text(192, 110, f"{wf['wind_speed']}m/s", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)

    
    # Display Current Feels Like
    display.draw_sprite(feels_like_sprite_m, 10, 140, 30, 30)
    display.draw_text(42, 150, f"Feels Like: {wf['feels_like']}C", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)
    

# DRAW INDOOR MEASUREMENTS AND TREND
def draw_indoor(display, temp, hum,press, i_temp, i_hum, i_press):

    # Get Indoor Trend Icons
    up_sprite = display.load_sprite(r"icons/ARROW_UP.raw", 30, 30)
    down_sprite = display.load_sprite(r"icons/ARROW_DOWN.raw", 30, 30)
    level_sprite = display.load_sprite(r"icons/ARROW_LEVEL.raw", 30, 30)

    sprites = {"up": up_sprite,
               "down": down_sprite,
               "level": level_sprite}

    i_temp_sprite = sprites[get_trend(i_temp)]
    i_hum_sprite = sprites[get_trend(i_hum)]
    i_press_sprite = sprites[get_trend(i_press)]

    i_temp_sprite_m = memoryview(i_temp_sprite)
    i_hum_sprite_m = memoryview(i_hum_sprite)
    i_press_sprite_m = memoryview(i_press_sprite)

    # Display Indoor Temperature
    display.fill_rectangle(40, 180, 70, 30, colors.BG)
    display.draw_text(45, 190, f"{temp}", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_sprite(i_temp_sprite_m, 10, 210, 30, 30)
    array_to_graph(display, i_temp, 40,210,0,30)
    
    # Display Indoor Humidity
    display.fill_rectangle(130, 180, 70, 30, colors.BG)
    display.draw_text(135, 190, f"{hum}", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_sprite(i_hum_sprite_m, 100, 210, 30, 30)
    array_to_graph(display, i_hum, 130,210,0,30)
    
    # Display Indoor Pressure
    display.fill_rectangle(230, 180, 70, 30, colors.BG)
    display.draw_text(235, 190, f"{press}", fonts.ARCADE, colors.FG_TEXT_L,  background=colors.BG)
    display.draw_sprite(i_press_sprite_m, 200, 210, 30, 30)
    array_to_graph(display, i_press, 230,210,0,30)


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

    display.draw_sprite(f_temp_sprite_m, 110, 60, 30, 30)
    display.draw_sprite(f_hum_sprite_m, 280, 60, 30, 30)
    display.draw_sprite(f_atmo_sprite_m, 110, 100, 30, 30)
    display.draw_sprite(f_wind_sprite_m, 280, 100, 30, 30)
    display.draw_sprite(f_feels_sprite_m, 280, 140, 30, 30)
    
    
    
    
    
    
    