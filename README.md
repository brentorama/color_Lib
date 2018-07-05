# color_Lib

Generate RGB values from plain english instructions eg:  ColorLib.get_color('green') = (0.0, 0.8, 0.0) #

import color_Lib
reload(color_Lib)

col = color_Lib.Color_Lib()

col.get_color('green', mode = 'rgb')
# Result: (0.0, 0.8, 0.0) # 

col.get_color('green', mode = 'hsv')
# Result: (0.3333333333333333, 1.0, 0.8) # 

col.get_color('dark_red')
# Result: (0.2, 0.0, 0.0) # 

for i in ['red','dark_yellow', 'orange', 'mid_blue']:
    result = col.get_color(i, mode = 'rgb')
    print result

#(0.8, 0.0, 0.0)
#(0.2, 0.2, 0.0)
#(0.8, 0.4, 0.0)
#(0.0, 0.2, 0.4)

col.list()
# Result: {'dark_aqua': [0.4166666666666667, 1.0, 0.2],
 'dark_blue': [0.5833333333333334, 1.0, 0.2],
 'dark_green': [0.3333333333333333, 1.0, 0.2],
 'dark_indigo': [0.6666666666666666, 1.0, 0.2],
 'dark_lavender': [0.75, 1.0, 0.2],
 'dark_lime': [0.25, 1.0, 0.2],
 'dark_magenta': [0.9166666666666666, 1.0, 0.2],
 'dark_orange': [0.08333333333333333, 1.0, 0.2],
 'dark_purple': [0.8333333333333334, 1.0, 0.2],
 'dark_red': [0.0, 1.0, 0.2],
 'dark_teal': [0.5, 1.0, 0.2],
 'dark_yellow': [0.16666666666666666, 1.0, 0.2] ....