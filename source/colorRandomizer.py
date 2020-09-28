import maya.cmds as cmd
import sys
from . import color_Lib

def RandomizeColors(sel=[]):

    colorList = []
    for key in color_Lib.Color_Lib().list():
        colorList.append(color_Lib.Color_Lib().get_color(key))

    if not sel:
        sel = cmd.ls(sl=True)

    for one in range(len(sel)):
        for rgb, abc in zip('RGB', '012'):
            cmd.setAttr('%s.overrideColor%s' % (sel[one], rgb), colorList[one][int(abc)])
        cmd.setAttr('%s.overrideEnabled' % sel[one], 1)
        cmd.setAttr('%s.overrideRGBColors' % sel[one], 1)


