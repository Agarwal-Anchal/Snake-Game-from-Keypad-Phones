#tail.py
import pygame
import random

class Tail:
	def __init__(self, posx, posy, width, height):
		self.width = width
		self.height = height
		self.posx = posx
		self.posy = posy
		self.RGB = [random.randint(0, 255) for i in range(3)]
		
	def draw(self, Diplay):
		pygame.draw.rect(Diplay, self.RGB, [self.posx, self.posy, 16, 16])

	def move(self, px, py):
		self.posx = px
		self.posy = py

	def get_pos(self):
		return self.posx, self.posy