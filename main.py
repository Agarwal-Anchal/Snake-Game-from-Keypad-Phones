#main.py
import pygame
import snakehead
import food
import tail as t
import random

ScreenW = 1280
ScreenH = 720

sheadX = 0
sheadY = 0

fX = 0
fY = 0

counter = 0

gameover = False

pygame.init()
pygame.display.set_caption("Snake Game")

Display = pygame.display.set_mode([ScreenW, ScreenH])
Display.fill([255, 255, 255]) #RGB white

black = [0, 0, 0]
font = pygame.font.SysFont(None, 30)
score = font.render("Score: 0", True, black)

shead = snakehead.Snakehead(ScreenW / 2 - 16/2, ScreenH / 2 - 16/2, 16, 16)
f = food.Food(random.randint(0, (ScreenW - 16)/16) * 16 - 8, random.randint(0, (ScreenH - 16)/16) * 16, 16, 16)
tails = []

Fps = 8
timer_clock = pygame.time.Clock()

while not gameover: #gameover == False
	Display.fill([255, 255, 255])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True
			break
		elif event.type == pygame.KEYDOWN:
			shead.read_input(event.key)
			##### added outide #####
			if event.key == pygame.K_ESCAPE:
				exit = False
				while exit == False:
					for e in pygame.event.get():
						if e.type == pygame.KEYDOWN:
							if e.key == pygame.K_ESCAPE:
								exit = True
			###################

	sheadX, sheadY = shead.get_pos()
	fX, fY = f.get_pos()
	#detect collision
	if sheadX + 16 > fX and sheadX < fX + 16:
		if sheadY + 16 > fY and sheadY < fY + 16:
			#collision
			f.respawn(ScreenW, ScreenH)
			counter += 1 # counter = counter + 1
			score = font.render("Score: " + str(counter), True, black)
			if len(tails) == 0:
				tails.append(t.Tail(sheadX, sheadY, 16, 16))
			#tails.append(tail.Tail(sheadX, sheadY, 16, 16, shead.get_movement()))
			else:
				tX, tY = tails[-1].get_pos()
				tails.append(t.Tail(tX, tY, 16, 16))
			
			print(tails)

	for i in range(len(tails)):
		try:
			tX, tY = tails[i].get_pos()
			sX, SY = shead.get_pos()
			if i != 0 and i != 1:
				if tX == sX and tY == sY:
					#collision
					shead.restart(ScreenW, ScreenH)
					tails.clear()
					counter = 0
					Display.blit(score, (10, 10))
					pygame.display.flip()
					pygame.display.update()
		except:
			shead.restart(ScreenW, ScreenH)
			tails.clear()
	sX, sY = shead.get_pos()
	if sX < 0 or sX + 16 > ScreenW:
			shead.restart(1280, 720)
			counter = 0
			Display.blit(score, (10, 10))
			pygame.display.flip()
			pygame.display.update()
			tails.clear()
			#restart
	elif sY < 0 or sY + 16 > ScreenH:
		shead.restart(1280, 720)
		counter = 0
		Display.blit(score, (10, 10))
		pygame.display.flip()
		pygame.display.update()
		tails.clear()
			#restart

	for i in range(1, len(tails)):
		tX, tY = tails[len(tails) - i - 1].get_pos() # y = b - x
		tails[len(tails) - i].move(tX, tY) 
	if len(tails) > 0:
		tX, tY = shead.get_pos()
		tails[0].move(tX, tY)
	shead.move(ScreenW, ScreenH)
	shead.draw(Display)
	Display.blit(score, (10, 10))
	for tail in tails:
		tail.draw(Display)
	f.draw(Display)
	pygame.display.flip()
	pygame.display.update()
	timer_clock.tick(Fps)