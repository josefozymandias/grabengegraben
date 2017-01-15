import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

size = width, height = 1920, 1080 
screen = pygame.display.set_mode(size,FULLSCREEN)
pygame.display.set_caption("Graben Gegraben")

clock = pygame.time.Clock()

BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
line_spacing = 20
player_x = 10
player_y = 14
x_max = width / line_spacing - 1
y_max = height / line_spacing - 1
map = []
map_size = 50
min_room_size = 5
max_room_size = 15 
def init_map():
	for y in range(map_size):
		map.append([])
		for x in range(map_size):
			map[y].append(0)

def draw_grid(screen, width, height, line_spacing, color):
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, color, (x,0),(x,height-1))
	for y in range(0, height, line_spacing):
		pygame.draw.line(screen, color, (0,y),(width-1,y))

def make_room(x, y, size):
	#print(str(x) + ' ' + str(y) + ' ' + str(size))
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

def draw_square(x,y,color):
	ls = line_spacing
	pygame.draw.rect(screen,color,(x*ls+1, y*ls+1, ls-1, ls-1))
			 

def draw_map():
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == 1:
				draw_square(x,y,GREEN)

def rand_rooms():
	for i in range(10):
		make_room(randint(0,map_size-max_room_size),randint(0,map_size-max_room_size),randint(min_room_size, max_room_size))

def new_map():
	global map
	map = []
	init_map()
	rand_rooms()

new_map()
print_map()
while True:
	clock.tick(30)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	if keys[K_w]: player_y -= 1
	if keys[K_r]: player_y += 1
	if keys[K_a]: player_x -= 1
	if keys[K_s]: player_x += 1
	if keys[K_F1]: new_map()

	if player_y < 0: player_y = 0
	if player_x < 0: player_x = 0
	if player_x > x_max: player_x = x_max 
	if player_y > y_max: player_y = y_max

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()


	screen.fill(BLACK)
	draw_grid(screen, width, height, line_spacing, CYAN)
	draw_map()
	draw_square(player_x,player_y,RED)
	pygame.display.flip()
