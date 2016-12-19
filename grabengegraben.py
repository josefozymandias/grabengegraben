import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 600, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Graben Gegraben")

clock = pygame.time.Clock()

FILLCOLOR = (0,128,128)

while True:
	clock.tick(60)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(FILLCOLOR)
	pygame.display.flip()
