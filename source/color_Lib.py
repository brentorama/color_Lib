import colorsys
class Color_Lib(object):
    def __init__(self):
        self.color_dict = {}
        hsv = []
        hueVal = []
        self.hue = ["red","orange","yellow","lime", "green", "aqua", "teal","blue","indigo", "lavender", "purple", "magenta"]
        self.val = ["black", "dark", "mid", "light", "full"]
        self.default_color = [0.0,0.0,0.25]
        size = [len(self.hue), len(self.val)]
		
        for i in range (size[0]):
            for j in range (1,(size[1])):
                hueVal.append("%s_%s" %(self.val[j],self.hue[i]))
                hsv.append([(i/float(size[0])), 1.0, (j/float(size[1]))])
				
        self.color_dict = dict(zip(hueVal, hsv))  
                    
    def get_color(self, inputColor, mode = "rgb"):
        
        if not any(id in inputColor for id in self.val):
            inputColor = ("full_"+inputColor)
        o = self.color_dict.setdefault(inputColor, self.default_color)
		
        if mode == "rgb":
            return colorsys.hsv_to_rgb(o[0],o[1],o[2])
        elif mode == "plainText":
            print "not implemented"
            return (o[0],o[1],o[2])
        else:
            return (o[0],o[1],o[2])
        
    def list(self):
        return self.color_dict


def changeColor(omenu, cDict, *ignore):
    crvSel = cmds.ls(sl=True)
    crv_shape = cmds.listRelatives(crvSel, s = True)
    if crv_shape is None:
        print("Nothing selected")
    else:
        cmds.setAttr(crv_shape[0] + ".overrideEnabled", 1)
        cmds.setAttr(crv_shape[0] + ".overrideRGBColors", 1)
        key = cmds.optionMenu(omenu, q=True, v=True)
        val = cDict.get(key, 0)
        cmds.setAttr(crv_shape[0] + ".overrideColor", val)


def buildMenu():
    if cmds.window("change_colors", exists = True):
        cmds.deleteUI("change_colors")
    cmds.window("change_colors")

    cmds.columnLayout()
    omenu = cmds.optionMenu( label="Colors")
    colorDict = {"Red" : 13, "Blue": 6, "Yellow": 17, "Green": 14, "Pink" : 9, "Light Blue" : 18}
    for k in sorted(colorDict.keys()):
        cmds.menuItem( label=k )
    cmds.optionMenu(omenu, e = True, cc=partial(changeColor, omenu, colorDict))
    cmds.showWindow()
