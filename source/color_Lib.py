import colorsys
class Color_Lib(object):
    def __init__(self):
        self.color_dict = {}
        hsv = []
        hueVal = []
        hue = ['red','orange','yellow','lime', 'green', 'aqua', 'teal','blue','indigo', 'lavender', 'purple', 'magenta']
        self.val = ['black', 'dark', 'mid', 'light', 'full']
        self.default_color = [0.0,0.0,0.25]
        size = [len(hue), len(self.val )]
        for i in range (size[0]):
            for j in range (1,(size[1])):
                #combine values with hues as plain english names
                hueVal.append('%s_%s' %(self.val[j],hue[i]))
                #add the hsv values
                hsv.append([(i/float(size[0])), 1.0, (j/float(size[1]))])
        #zip the colors and values into a dictionary
        self.color_dict = dict(zip(hueVal, hsv))  
                    
    def get_color(self, inputColor, mode = 'rgb'):
        
        if not any(id in inputColor for id in self.val):
            inputColor = ('full_'+inputColor)
        #return the colors so Maya can read them in RGB
        o = self.color_dict.setdefault(inputColor, self.default_color)
        if mode == 'rgb':
            return colorsys.hsv_to_rgb(o[0],o[1],o[2])
        else
            return (o[0],o[1],o[2])
        
    def list(self):
        return self.color_dict
        
        