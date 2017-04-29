#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import math

class Block:
	def __init__(self, x, y, c):
		self.color = c
		if c == 'r':
			self.image = pygame.image.load("red.png")
		elif c == 'b':
			self.image = pygame.image.load("blue.png")
		elif c == 'y':
			self.image = pygame.image.load("yellow.png")
		elif c == 'g':
			self.image = pygame.image.load("green.png")
		else:
			self.image = pygame.image.load("white.png")

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Player:
	def __init__(self, c):
		self.color = c
		if c == 'r':
			self.image = pygame.image.load("red.png")
		elif c == 'b':
			self.image = pygame.image.load("blue.png")
		elif c == 'y':
			self.image = pygame.image.load("yellow.png")
		elif c == 'g':
			self.image = pygame.image.load("green.png")
		else:
			self.image = pygame.image.load("white.png")

		self.rect = self.image.get_rect()
		# self.rect.x = 350
		# self.rect.y = 350
		self.dir = 'r'
		self.visited = []

	def tick(self):
		if self.dir == 'l':
			self.rect.x -= 8
		elif self.dir == 'r':
			self.rect.x +=8
		elif self.dir == 'u':
			self.rect.y -= 8
		else:
			self.rect.y +=8


class GameSpace:
	def menu(self):
		self.menuimage = pygame.image.load("menu.png")
		self.screen.blit(self.menuimage, self.menuimage.get_rect())
		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if (pos[0] > 270 and pos[0] < 270+260 and pos[1] > 560 and pos[1] < 560+80):
						return

	def playerSelect(self):
		self.colorimage = pygame.image.load("colorselect.png")
		self.screen.blit(self.colorimage, self.colorimage.get_rect())
		pygame.display.flip()
		playerpicking = 1
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if (playerpicking == 1):
						if (pos[0] > 447 and pos[0] < 447+180 and pos[1] > 457 and pos[1] < 457+180):
							self.color1 = 'y'
							playerpicking = 2
						if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 180 and pos[1] < 180+180):
							self.color1 = 'r'
							playerpicking = 2
						if (pos[0] > 450 and pos[0] < 450+180 and pos[1] > 180 and pos[1] < 180+180):
							self.color1 = 'g'
							playerpicking = 2
						if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 457 and pos[1] < 457+180):
							self.color1 = 'b'
							playerpicking = 2
					elif (playerpicking == 2):
						if (pos[0] > 447 and pos[0] < 447+180 and pos[1] > 457 and pos[1] < 457+180):
							self.color2 = 'y'
							return
						if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 180 and pos[1] < 180+180):
							self.color2 = 'r'
							return
						if (pos[0] > 450 and pos[0] < 450+180 and pos[1] > 180 and pos[1] < 180+180):
							self.color2 = 'g'
							return
						if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 457 and pos[1] < 457+180):
							self.color2 = 'b'
							return
					else:
						continue

	def collision(self, r, p):
		self.collideimage = pygame.image.load("explosion1.png")
		self.collideimagerect = self.collideimage.get_rect()
		self.collideimagerect.x = r.rect.x - 25
		self.collideimagerect.y = r.rect.y - 25
		counter = 0
		while counter < 20:
			print (str(counter))
			counter  = counter + 1
			self.screen.fill(self.black)
			for e in self.edge:
				self.screen.blit(e.image, e.rect)
			for b in self.blocks:
				self.screen.blit(b.image, b.rect)
			self.screen.blit(self.player1.image, self.player1.rect)
			self.screen.blit(self.player2.image, self.player2.rect)
			self.screen.blit(self.collideimage, self.collideimagerect)
			pygame.display.flip()

		if self.collideplayer == 1:
				print ("Player 2 wins!")
		else:
			print ("Player 1 wins!")

		restart = False
		while not restart:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == KEYDOWN:
					if (event.key == K_q):
						sys.exit()
					if (event.key == K_r):
						return
					else:
						pass
				else:
					pass
						# restart = True
						# self.blocks = []
						# self.edge = []
						# self.collided = False
						# #self.playerSelect()


	def main(self):
		pygame.init()
		self.size = self.width, self.height = 800, 800
		self.screen = pygame.display.set_mode(self.size)
		self.color1 = 'r'
		self.color2 = 'b'
		self.menu()
		self.black = 0, 0, 0
		pygame.key.set_repeat(300, 50)

		while 1:
			self.playerSelect()
			self.exploderect = None
			self.collideplayer = None
			self.player1 = Player(self.color1)
			self.player1.rect.x = 200
			self.player1.rect.y = 400
			self.player2 = Player(self.color2)
			self.player2.rect.x = 500
			self.player2.rect.y = 400

			self.clock = pygame.time.Clock()
			self.screen.fill(self.black)
			self.blocks = []
			self.edge = []

			for n in range(800):
				self.edge.append(Block(0, n, 'w'))
				self.edge.append(Block(n, 0, 'w'))
				self.edge.append(Block(n, 800-8, 'w'))
				self.edge.append(Block(800-8, n, 'w'))

			self.collided = False
			while not self.collided:
				self.clock.tick(60)
				for event in pygame.event.get():
					if event.type == pygame.QUIT: sys.exit()
					if event.type == KEYDOWN:
						if (event.key == K_LEFT):
							self.player1.dir = 'l'
							self.player1.tick()
							self.screen.blit(self.player1.image, self.player1.rect)
							block = Block(self.player1.rect.x, self.player1.rect.y, self.color1)
							self.blocks.append(block)
						if (event.key == K_RIGHT):
							self.player1.dir = 'r'
							self.player1.tick()
							self.screen.blit(self.player1.image, self.player1.rect)
							block = Block(self.player1.rect.x, self.player1.rect.y, self.color1)
							self.blocks.append(block)
						if (event.key == K_UP):
							self.player1.dir = 'u'
							self.player1.tick()
							self.screen.blit(self.player1.image, self.player1.rect)
							block = Block(self.player1.rect.x, self.player1.rect.y, self.color1)
							self.blocks.append(block)
						if (event.key == K_DOWN):
							self.player1.dir = 'd'
							self.player1.tick()
							self.screen.blit(self.player1.image, self.player1.rect)
							block = Block(self.player1.rect.x, self.player1.rect.y, self.color1)
							self.blocks.append(block)

						if (event.key == K_a):
							self.player2.dir = 'l'
							self.player2.tick()
							self.screen.blit(self.player2.image, self.player2.rect)
							block = Block(self.player2.rect.x, self.player2.rect.y, self.color2)
							self.blocks.append(block)
						if (event.key == K_d):
							self.player2.dir = 'r'
							self.player2.tick()
							self.screen.blit(self.player2.image, self.player2.rect)
							block = Block(self.player2.rect.x, self.player2.rect.y, self.color2)
							self.blocks.append(block)
						if (event.key == K_w):
							self.player2.dir = 'u'
							self.player2.tick()
							self.screen.blit(self.player2.image, self.player2.rect)
							block = Block(self.player2.rect.x, self.player2.rect.y, self.color2)
							self.blocks.append(block)
						if (event.key == K_s):
							self.player2.dir = 'd'
							self.player2.tick()
							self.screen.blit(self.player2.image, self.player2.rect)
							block = Block(self.player2.rect.x, self.player2.rect.y, self.color2)
							self.blocks.append(block)



				self.player1.tick()
				self.player2.tick()
				block1 = Block(self.player1.rect.x, self.player1.rect.y, self.color1)
				block2 = Block(self.player2.rect.x, self.player2.rect.y, self.color2)

				self.screen.fill(self.black)

				for e in self.edge:
					self.screen.blit(e.image, e.rect)
					if self.player1.rect.colliderect(e):
						self.collision(e, 1)
						self.collided = True
						# self.exploderect = e
						# self.collideplayer = 1
					if self.player2.rect.colliderect(e):
						self.collision(e, 2)
						self.collided = True
						# self.exploderect = e
						# self.collideplayer = 2

				for b in self.blocks:
					self.screen.blit(b.image, b.rect)
					if self.player1.rect.colliderect(b):
						self.collision(b, 1)
						self.collided = True
						# self.exploderect = b
						# self.collideplayer = 1
					if self.player2.rect.colliderect(b):
						self.collision(b, 2)
						self.collided = True
						# self.exploderect = b
						# self.collideplayer = 2

				self.blocks.append(block1)
				self.blocks.append(block2)

				self.screen.blit(self.player1.image, self.player1.rect)
				self.screen.blit(self.player2.image, self.player2.rect)

				pygame.display.flip()



if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
