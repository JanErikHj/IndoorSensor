import utilities.fonts as fonts
import utilities.colors as colors
#from utilities.ili9341 import Display, color565

epsilon = 0.00000000001
def scale_array(values, new_min, new_max):
    old_min = min(values)
    old_max = max(values)
    scaled_values = [new_min + (x - old_min) * (new_max - new_min) / (old_max - old_min+epsilon) for x in values]
    return scaled_values


def array_to_graph(display, array, start_x, start_y, min_v, max_v):
    max_t = max(array)
    min_t = min(array)
    
    new_array = scale_array(array, min_v+1, max_v-1)
    display.draw_text(start_x, start_y-10, f"{min_t}-{max_t}", fonts.BALLY, colors.FG_SHAPE_L,  background=colors.BG)

    for i in range(len(new_array)):
        display.draw_vline(start_x+i, start_y+1, max_v, colors.BG)
        display.draw_vline(start_x+i, start_y+(max_v-int(new_array[i])), int(new_array[i]), colors.FG_TEXT_L)
        
        
