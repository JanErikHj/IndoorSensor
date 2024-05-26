
def get_wind_direction(degrees):
    if degrees <=22 or degrees >= 338:
        return "SO.raw"
    elif degrees >= 23 and degrees <= 67:
        return "SW.raw"
    elif degrees >= 68 and degrees <= 112:
        return "WE.raw"
    elif degrees >= 113 and degrees <= 157:
        return "NW.raw"
    elif degrees >= 158 and degrees <= 202:
        return "NO.raw"
    elif degrees >= 203 and degrees <= 247:
        return "NE.raw"
    elif degrees >= 248 and degrees <= 292:
        return "EA.raw"
    elif degrees >= 293 and degrees <= 337:
        return "SE.raw"

def get_feels_like(value):
    if value < 5:
        return "cold_face.raw"
    elif value > 20:
        return "hot_face.raw"
    else:
        return "temp_face.raw"


        
def log_value(array, value):
    if len(array) >= 68:
        array.pop(0)
    array.append(value)
    
def get_trend(array):
    if len(array)<2:
        
        return "level"
    if array[-1] > array[-2]:
        
        return "up"
    elif array[-1] < array[-2]:
        
        return "down"
    elif array[-1] == array[-2]:
        
        return "level"  