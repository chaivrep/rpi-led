import logging
from bibliopixel import *
import bibliopixel.colors as colors
import bibliopixel.image as image
from bibliopixel.animation import AnimationQueue
from adamatrix import DriverAdaMatrix
from jackiebeat import *

driver = DriverAdaMatrix(rows=32, chain=1)
driver.SetPWMBits(6) #decrease bit-depth for better performance
#MUST use serpentine=False because rgbmatrix handles the data that way
led = LEDMatrix(driver, 32, 32, serpentine=False)

#Must have code downloaded from GitHub for matrix_animations
#from matrix_animations import *

import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

rainbow = [colors.Red, colors.Red, colors.Red, 
	colors.Orange, colors.Orange, colors.Orange, 
	colors.Yellow, colors.Yellow, colors.Yellow, 
	colors.Green, colors.Green, colors.Green, 
	colors.Blue, colors.Blue, colors.Blue, 
	colors.Indigo, colors.Indigo, colors.Indigo]
	
star = BaseMatrixMask.generateMask([(2,2), (16,8), (24,0), (24,12), (31,14), (31,16), (20,20), (16,31), (14,31), (12,24), (0,24), (8,16)], 32, 32)
full_panel = BaseMatrixMask.generateMask([(0,0), (31,0), (31,31), (0,31)], 32, 32)

try:
	queue = AnimationQueue(led)
	fps=10
	queue.addAnim(JBFireworks(led, fps=fps), amt=1, fps=fps, untilComplete=True, max_cycles=240)
	queue.addAnim(BaseMatrixMask(led=led, mask=full_panel, mask_fn=BaseMatrixMask.makeChase(rainbow, direction=Direction.UP_LEFT), bg_fn=BaseMatrixMask.makeSingleColor(colors.Off)), amt=1, fps=fps, max_steps=100)
	queue.addAnim(MatrixMaskFadeIn(led=led, mask=star, mask_fn=BaseMatrixMask.makeSingleColor(colors.Yellow), bg_fn=BaseMatrixMask.makeSingleColor(colors.Off), increment=10), amt=1, fps=fps, max_steps=100)
	queue.addAnim(BaseMatrixMask(led=led, mask=full_panel, mask_fn=BaseMatrixMask.makeSingleColor(colors.White), bg_fn=BaseMatrixMask.makeSingleColor(colors.White)), amt=1, fps=fps, max_steps=2)
	queue.addAnim(BaseMatrixMask(led=led, mask=star, mask_fn=BaseMatrixMask.makeChase(rainbow, direction=Direction.DOWN_RIGHT), bg_fn=BaseMatrixMask.makeSingleColor(colors.Off)), amt=1, fps=fps, max_steps=100)
	queue.addAnim(BaseMatrixMask(led=led, mask=full_panel, mask_fn=BaseMatrixMask.makeSingleColor(colors.White), bg_fn=BaseMatrixMask.makeSingleColor(colors.White)), amt=1, fps=fps, max_steps=2)
	queue.addAnim(BaseMatrixMask(led=led, mask=star, mask_fn=BaseMatrixMask.makeSingleColor(colors.Off), bg_fn=BaseMatrixMask.makeChase(rainbow, direction=Direction.UP_LEFT)), amt=1, fps=fps, max_steps=100)
	fps=10
	queue.addAnim(JBColorBlocks(led, fps=fps), amt=1, fps=fps, max_steps=180)
	queue.run()
    
except KeyboardInterrupt:
    led.all_off()
    led.update()
