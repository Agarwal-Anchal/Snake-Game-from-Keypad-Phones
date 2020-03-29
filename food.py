#food.py
import pygame
import random

class Food:
	def __init__(self, posx, posy, width, height):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.red = random.randint(155, 255)
	def draw(self, Display):
		pygame.draw.rect(Display, [self.red, 0, 0], [self.posx, self.posy, self.width, self.height])
	def get_pos(self):
		return self.posx, self.posy
	def respawn(self, ScreenW, ScreenH):
		self.posx = random.randint(1, (ScreenW - 16)/16) * 16 - 8
		self.posy = random.randint(1, (ScreenH - 16)/16) * 16 
		self.red = random.randint(155, 255)