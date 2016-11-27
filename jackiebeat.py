import random

import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

from bibliopixel import *
from bibliopixel.font import fonts
import bibliopixel.image as image
from bibliopixel.animation import BaseMatrixAnim


import numpy
from PIL import Image, ImageDraw

class JBFireworks(BaseMatrixAnim):
	def __init__(self, led, fps=None):
		#The base class MUST be initialized by calling super like this
		super(JBFireworks, self).__init__(led)
		#Create a color array to use in the animation
		self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]
		self._fps = fps
		self._scene1_start = 0
		self._scene2_start = self._fps
		self._scene3_start = self._fps * 2
		self._scene4_start = self._fps * 3
		self._scene5_start = self._fps * 4
		self._scene6_start = self._fps * 5
		log.debug("JBFireworks initialized...")
	
	def step(self, amt = 1):
		
		if self._step >= self._scene1_start:
			curr_step = (self._step - self._scene1_start) % 75
			self._firework(curr_step, colors.White, colors.Yellow, 7, 16, 16, -3, -3)
		if self._step >= self._scene2_start:
			curr_step = (self._step - self._scene2_start) % 75
			self._firework(curr_step, colors.White, colors.Yellow, 7, 16, 19, -3, -3)
			self._firework(curr_step, colors.White, colors.Yellow, 7, 19, 16, -3, -3)
		if self._step >= self._scene3_start:
			curr_step = (self._step - self._scene3_start) % 75
			self._firework(curr_step, colors.White, colors.Yellow, 7, 16, 22, -3, -3)
			self._firework(curr_step, colors.White, colors.Yellow, 7, 22, 16, -3, -3)
		if self._step >= self._scene4_start:
			curr_step = (self._step - self._scene4_start) % 75
			self._firework(curr_step, colors.White, colors.Yellow, 7, 16, 25, -3, -3)
			self._firework(curr_step, colors.White, colors.Yellow, 7, 25, 16, -3, -3)
		if self._step >= self._scene5_start:
			curr_step = (self._step - self._scene5_start) % 75
			self._firework(curr_step, colors.White, colors.Yellow, 7, 16, 28, -3, -3)
			self._firework(curr_step, colors.White, colors.Yellow, 7, 28, 16, -3, -3)
			self.animComplete = True
		
		if self._step >= self._scene6_start and self._step <= (self._scene6_start + 16):
			curr_step = self._step - self._scene6_start
			if curr_step > 16:
				curr_step = 16
			for i in range(curr_step):
				self._led.drawLine(16 + i, 0, self._led.width, 16 - i, colors.Red)
				self._led.drawLine(0, 16 + i, 16 - i, self._led.height, colors.Red)
		self._step += amt
	
	def _firework(self, step, color_head, color_tail, length_tail, start_x, start_y, inc_x, inc_y):
		end_x = start_x + (step * inc_x)
		end_y = start_y + (step * inc_y)
		tail_start_x = end_x + length_tail
		tail_start_y = end_y + length_tail	
		self._led.drawLine(tail_start_x, tail_start_y, end_x, end_y, color_tail)
		self._led.drawLine(start_x, start_y, tail_start_x, tail_start_y, colors.Black)
		self._led.set(end_x, end_y, color_head)


#class JBRainbow(BaseMatrixAnim):
	#def __init__(self, led, fps=None):
		##The base class MUST be initialized by calling super like this
		#super(JBRainbow, self).__init__(led)
		##Create a color array to use in the animation
		#self._colors = [colors.Red, colors.Red, colors.Red, 
		#colors.Orange, colors.Orange, colors.Orange, 
		#colors.Yellow, colors.Yellow, colors.Yellow, 
		#colors.Green, colors.Green, colors.Green, 
		#colors.Blue, colors.Blue, colors.Blue, 
		#colors.Indigo, colors.Indigo, colors.Indigo]
		#self._fps = fps
		#log.debug("JBRainbow initialized...")
	
	#def step(self, amt = 1):
		## Draw rainbow chase lines on diagonal
		#for i in range(self._led.width * 2):
			#a = 0
			#b = i
			#if b >= self._led.width:
				#a = i - self._led.width
				#b = self._led.width - 1
			#self._led.drawLine(a, b, b, a, self._colors[(i + self._step) % len(self._colors)]) 
		#self._step += amt

#class JBRainbowStar(BaseMatrixAnim):
	#def __init__(self, led, fps=None):
		##The base class MUST be initialized by calling super like this
		#super(JBRainbowStar, self).__init__(led)
		##Create a color array to use in the animation
		#self._colors = [colors.Red, colors.Red, colors.Red, 
		#colors.Orange, colors.Orange, colors.Orange, 
		#colors.Yellow, colors.Yellow, colors.Yellow, 
		#colors.Green, colors.Green, colors.Green, 
		#colors.Blue, colors.Blue, colors.Blue, 
		#colors.Indigo, colors.Indigo, colors.Indigo]
		#self._fps = fps
		#log.debug("JBRainbowStar initialized...")
	
	#def step(self, amt = 1):
		## Draw rainbow chase lines on diagonal
		#for i in range(self._led.width * 2):
			#a = 0
			#b = i
			#if b >= self._led.width:
				#a = i - self._led.width
				#b = self._led.width - 1
			#self._led.drawLine(a, b, b, a, self._colors[(i + self._step) % len(self._colors)])
		#self._led.fillTriangle(0, 0, 7, 14, 0, 23, colors.Black)
		##self._led.fillTriangle(0, 31, 10, 24, 0, 23, colors.Black)  
		#self._led.fillTriangle(0, 0, 23, 0, 14, 7, colors.Black)
		##self._led.fillTriangle(0, 31, 0, 23, 15, 21,  colors.Black)
		##self._led.fillTriangle(23, 0, 22, 14, 31, 0, colors.Black)
		##self._led.fillTriangle( 15, 21, 15, 31, 0, 32, colors.Black) 
		##self._led.fillTriangle( 22, 14, 31, 0, 31, 15,  colors.Black) 
		##self._led.fillRect(18, 18, 14, 14, colors.Black)      
		#self._step += amt
		
		
class JBColorBlocks(BaseMatrixAnim):
	def __init__(self, led, fps=None):
		#The base class MUST be initialized by calling super like this
		super(JBColorBlocks, self).__init__(led)
		self._fps = fps
		self._colors = [colors.DarkCyan, colors.Chocolate, colors.White]
		self._scene1_start = 0
		self._scene2_start = self._fps
		self._scene3_start = self._fps * 2
		self._scene4_start = self._fps * 5
		log.debug("JBColorBlocks initialized...")
	
	def step(self, amt = 1):
		if self._step == self._scene1_start:
			self._led.fillRect(0, 0, 16, 16, self._colors[0])
		if self._step == self._scene2_start:
			self._led.fillRect(0, 16, 16, 16, self._colors[1])
		if self._step == self._scene3_start:
			self._led.fillRect(16, 0, 16, 16, self._colors[2])
		if self._step >= self._scene4_start:
			self._led.fillRect(0, 0, 16, 16, self._colors[self._step % 3])
			self._led.fillRect(0, 16, 16, 16, self._colors[(self._step +1) % 3])
			self._led.fillRect(16, 0, 16, 16, self._colors[(self._step +2) % 3])
		self._step += amt
		
#class JBStar(BaseMatrixAnim):
	#def __init__(self, led, fps=None):
		##The base class MUST be initialized by calling super like this
		#super(JBStar, self).__init__(led)
		#self._fps = fps
		#log.debug("JBStar initialized...")
		
	
	#def preRun(self, amt=1):
		#self._step = 100
	
	#def preStep(self, amt):
		#self._img = image.loadImage(self._led, "star.png", offset=(0, 0), brightness=self._step)
		#self._led.setTexture(self._img)
	
	#def step(self, amt = 1):
		#self._led.fillScreen()
		#self._step += amt
		#if self._step > 255:
			#self._step = 255;

#class JBStar2(BaseMatrixAnim):
	#def __init__(self, led, fps=None):
		##The base class MUST be initialized by calling super like this
		#super(JBStar2, self).__init__(led)
		#self._fps = fps
		#log.debug("JBStar2 initialized...")
		
	#def preRun(self, amt=1):
		#self._led.fillScreen(colors.Yellow)
		#self._led.fillTrangle(0, 0, 20, 0, 0, 20, colors.Black)
		#self._led.setMasterBrightness(0)
	
	#def step(self, amt = 1):
		#self._led.driver[0].setMasterBrightness(self._step)
		#self._step += amt
		#if self._step > 255:
			#self._step = 255;


#class JBRainbowMask(BaseMatrixAnim):
	#def __init__(self, led, mask, fps=None, mask_color=colors.Black, invert=False):
		##The base class MUST be initialized by calling super like this
		#super(JBRainbowMask, self).__init__(led)
		#self._colors = [colors.Red, colors.Red, colors.Red, 
		#colors.Orange, colors.Orange, colors.Orange, 
		#colors.Yellow, colors.Yellow, colors.Yellow, 
		#colors.Green, colors.Green, colors.Green, 
		#colors.Blue, colors.Blue, colors.Blue, 
		#colors.Indigo, colors.Indigo, colors.Indigo]
		#self._fps = fps
		#self._mask = mask
		#self._mask_color = mask_color
		#self._invert = invert
		#log.debug("JBRainbowMask initialized...")

	
	#def step(self, amt = 1):
		#for i in range(self._led.width * 2):
			#a = 0
			#b = i
			#if b >= self._led.width:
				#a = i - self._led.width
				#b = self._led.width - 1
			#self._led.drawLine(a, b, b, a, self._colors[(i + self._step) % len(self._colors)]) 
		#for i in range(self._led.width):
			#for j in range(self._led.height):
				#if self._invert and not self._mask[i,j]:
					#self._led.set(i,j,self._mask_color) 
				#elif not self._invert and self._mask[i,j]:
					#self._led.set(i,j,self._mask_color)
		#self._step += amt
		#if self._step > 255:
			#self._step = 255;

from enum import Enum
class Direction(Enum):
	UP = 0
	DOWN = 1
	UP_RIGHT = 2
	UP_LEFT = 3
	DOWN_RIGHT = 4
	DOWN_LEFT = 5

class BaseMatrixMask(BaseMatrixAnim):
	def __init__(self, led, mask, mask_fn, bg_fn):
		#The base class MUST be initialized by calling super like this
		super(BaseMatrixMask, self).__init__(led)
		self._mask = mask
		self._mask_fn = mask_fn
		self._bg_fn = bg_fn
		log.debug("BaseMatrixMask initialized...")
	
	def step(self, amt = 1):
		for x in range(self._led.width):
			for y in range(self._led.height):
				if self._mask[x,y]:
					self._mask_fn(self._led, self._step, x, y, self._mask) 
				else:
					self._bg_fn(self._led, self._step, x, y, self._mask) 
		self._step += amt
	
	@staticmethod
	def generateMask(polygon, width, height):
		img = Image.new('L', (width, height), 0)
		ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
		return numpy.array(img)
	
	@staticmethod
	def makeSingleColor(color):
		def singleColor(led, step, x, y, mask):
			led.set(x,y,color)
			return color
		return singleColor
		
	@staticmethod
	def makeChase(colors, direction=Direction.UP):
		def chase(led, step, x, y, mask):
			# Default is up
			i = step + y
			if direction == Direction.DOWN:
				i = step - y
			elif direction == Direction.UP_RIGHT:
				i = step + y - x
			elif direction == Direction.UP_LEFT:
				i = step + y + x
			elif direction == Direction.DOWN_RIGHT:
				i = step - y - x
			elif direction == Direction.DOWN_LEFT:
				i = step - y + x
			color = colors[i % len(colors)]
			led.set(x,y,color)
			return color
		return chase
		
class MatrixMaskFadeIn(BaseMatrixMask):
	def __init__(self, led, mask, mask_fn, bg_fn, init_bright=50, increment=2):
		#The base class MUST be initialized by calling super like this
		super(MatrixMaskFadeIn, self).__init__(led=led, mask=mask, mask_fn=mask_fn, bg_fn=bg_fn)
		self._init_bright = init_bright
		self._increment = increment
	
	def preRun(self, amt=1):
		self._led.setMasterBrightness(self._init_bright)
		
	def preStep(self, amt = 1):
		curr_brightness = self._led.masterBrightness
		new_brightness =  curr_brightness + self._increment
		if new_brightness > 255:
			new_brightness = 255
			
		self._led.setMasterBrightness(new_brightness)
