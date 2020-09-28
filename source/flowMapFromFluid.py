import maya.cmds as cmd			
def colorflud(multi, res, den):
	fluidShape = 'flowMapFluidShape'
	fludArr = cmd.getAttr('%s.fieldData.fieldDataVelocity' % fluidShape)
	massArr = cmd.getAttr('%s.fieldData.fieldDataMass ' % fluidShape)
	i = 0
	for y in (range(res)):
		for x in (range(res)): 
			cmd.setFluidAttr(fluidShape, at='color', vv = [(fludArr[i][1] * multi), (fludArr[i][0]* multi), (massArr[i]*den)], xi=x, yi=y, zi=0 )
			i+=1
						
			