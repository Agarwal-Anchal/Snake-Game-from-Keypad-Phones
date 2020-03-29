#snakehead.py
import pygame

class Snakehead:
	def __init__(self, posx, posy, width, height):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.movement = 'null'
		self.speed = 16
	def draw(self, Display):     #RGB #coordinates/dimentions
		pygame.draw.rect(Display, [0, 0, 0], [self.posx, self.posy, self.width, self.height])
	def read_input(self, key):
		if (key == pygame.K_a or key == pygame.K_LEFT) and self.movement != 'right':
			self.movement = 'left'
		elif (key == pygame.K_d or key == pygame.K_RIGHT) and self.movement != 'left':
			self.movement = 'right'
		elif (key == pygame.K_w or key == pygame.K_UP) and self.movement != 'down':
			self.movement = 'up'
		elif (key == pygame.K_s or key == pygame.K_DOWN) and self.movement != 'up':
			self.movement = 'down'
		print(self.movement)
	def get_pos(self):
		return self.posx, self.posy
	def get_movement(self):
		return self.movement
	def restart(self, ScreenW, ScreenH):
		self.posx = ScreenW / 2 - 16/2
		self.posy = ScreenH / 2 - 16/2
	def move(self, SW, SH):

		if self.movement == 'right':
			self.posx += self.speed # self.posx = self.posx + self.speed
		elif self.movement == 'left':
			self.posx -= self.speed # self.posx = self.posx - self.speed
		elif self.movement == 'up':
			self.posy -= self.speed # self.posy = self.posy - self.speed
		elif self.movement == 'down':
			self.posy += self.speed # self.posy = self.posy + self.speed