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
		self.rect.x = 350
		self.rect.y = 350
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
						self.playerSelect()
						return

	def playerSelect(self):
		self.colorimage = pygame.image.load("colorselect.png")
		self.screen.blit(self.colorimage, self.colorimage.get_rect())
		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if (pos[0] > 447 and pos[0] < 447+180 and pos[1] > 457 and pos[1] < 457+180):
						self.color = 'y'
						return
					if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 180 and pos[1] < 180+180):
						self.color = 'r'
						return
					if (pos[0] > 450 and pos[0] < 450+180 and pos[1] > 180 and pos[1] < 180+180):
						self.color = 'g'
						return
					if (pos[0] > 200 and pos[0] < 200+180 and pos[1] > 457 and pos[1] < 457+180):
						self.color = 'b'
						return


	def main(self):
		pygame.init()
		self.size = self.width, self.height = 800, 800
		self.screen = pygame.display.set_mode(self.size)
		self.menu()
		self.black = 0, 0, 0
		pygame.key.set_repeat(300, 50)

		self.player1 = Player('r')

		self.clock = pygame.time.Clock()
		self.screen.fill(self.black)
		self.blocks = []
		self.edge = []

		for n in range(800):
			self.edge.append(Block(0, n, 'w'))
			self.edge.append(Block(n, 0, 'w'))
			self.edge.append(Block(n, 800-8, 'w'))
			self.edge.append(Block(800-8, n, 'w'))

		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == KEYDOWN:
					if (event.key == K_LEFT):
						self.player1.dir = 'l'
						self.player1.tick()
						self.screen.blit(self.player1.image, self.player1.rect)
						block = Block(self.player1.rect.x, self.player1.rect.y, self.player1.color)
						self.blocks.append(block)
					if (event.key == K_RIGHT):
						self.player1.dir = 'r'
						self.player1.tick()
						self.screen.blit(self.player1.image, self.player1.rect)
						block = Block(self.player1.rect.x, self.player1.rect.y, self.player1.color)
						self.blocks.append(block)
					if (event.key == K_UP):
						self.player1.dir = 'u'
						self.player1.tick()
						self.screen.blit(self.player1.image, self.player1.rect)
						block = Block(self.player1.rect.x, self.player1.rect.y, self.player1.color)
						self.blocks.append(block)
					if (event.key == K_DOWN):
						self.player1.dir = 'd'
						self.player1.tick()
						self.screen.blit(self.player1.image, self.player1.rect)
						block = Block(self.player1.rect.x, self.player1.rect.y, self.player1.color)
						self.blocks.append(block)

			self.player1.tick()
			block = Block(self.player1.rect.x, self.player1.rect.y, self.player1.color)
			# self.blocks.append(block)

			self.screen.fill(self.black)

			for e in self.edge:
				self.screen.blit(e.image, e.rect)
				if self.player1.rect.colliderect(e):
					print ("collide")

			for b in self.blocks:
				self.screen.blit(b.image, b.rect)
				if self.player1.rect.colliderect(b):
					print ("collide")

			self.blocks.append(block)

			self.screen.blit(self.player1.image, self.player1.rect)

			pygame.display.flip()

if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
