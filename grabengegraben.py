import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

size = width, height = 526, 726
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Graben Gegraben")

clock = pygame.time.Clock()

BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
line_spacing = 25
player_x = 10
player_y = 14
map = []
for y in range(50):
	map.append([])
	for x in range(50):
		map[y].append(0)

def draw_grid(screen, width, height, line_spacing, color):
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, color, (x,0),(x,height-1))
	for y in range(0, height, line_spacing):
		pygame.draw.line(screen, color, (0,y),(width-1,y))

def draw_square(x, y, size):
	for i in range(size):
		map[y][x + i] = 1
		map[y+size-1][x + i] = 1
		map[y + i][x] = 1
		map[y + i][x+size-1] = 1

def print_map():
	line = ""
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == 0: line += ' '
			elif map[y][x] == 1: line += '#'
		print(line)
		line = ""

draw_square(5, 5, 10)
print_map()
while True:
	clock.tick(30)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	if keys[K_w]: player_y -= 1
	if keys[K_r]: player_y += 1
	if keys[K_a]: player_x -= 1
	if keys[K_s]: player_x += 1

	if player_y < 0: player_y = 0
	if player_x < 0: player_x = 0
	if player_x > 20: player_x = 20
	if player_y > 28: player_y = 28

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()


	screen.fill(BLACK)
	draw_grid(screen, width, height, line_spacing, CYAN)
	pygame.draw.rect(screen,RED,(player_x*line_spacing+6,player_y*line_spacing+6,14,14))
	pygame.display.flip()
