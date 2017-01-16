import pygame
from pygame.locals import *
import sys
from random import randint, seed

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
MAGENTA= (255,   0, 255)
line_spacing = 20
player_x = 43
player_y = 23
x_max = width / line_spacing 
y_max = height / line_spacing
map = []
map_size = 75
min_room_size = 5
max_room_size = 10 
def init_map():
	for y in range(y_max):
		map.append([])
		for x in range(x_max):
			map[y].append(0)

def draw_grid(screen, width, height, line_spacing, color):
	for x in range(0, width, line_spacing):
		pygame.draw.line(screen, color, (x,0),(x,height-1))
	for y in range(0, height, line_spacing):
		pygame.draw.line(screen, color, (0,y),(width-1,y))

def make_room(x, y, size):
	#print(str(x) + ' ' + str(y) + ' ' + str(size))
	#for i in range(size):
	#	map[y][x + i] = 1
	#	map[y+size-1][x + i] = 1
	#	map[y + i][x] = 1
	#	map[y + i][x+size-1] = 1
	#for y2 in range(size-2):
	#	for x2 in range(size-2):
	#		map[y+1+y2][x+1+x2] = 0
	for y2 in range(size):
		for x2 in range(size):
			map[y+y2][x+x2] = 1

def print_map():
	line = ""
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == 0: line += ' '
			elif map[y][x] == 1: line += '#'
			elif map[y][x] == 2: line += "@"
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
			elif map[y][x] == 2:
				draw_square(x,y,MAGENTA)

def rand_rooms():
	for i in range(60):
		make_room(randint(0,x_max-max_room_size),randint(0,y_max-max_room_size),randint(min_room_size, max_room_size))

def rand_items():
	for i in range(20):
		map[randint(0,y_max-1)][randint(0,x_max-1)] = 2

def new_map(seed_val):
	global map
	map = []
	seed(seed_val)
	init_map()
	rand_items()
	rand_rooms()
	
seed_val = 1337
new_map(seed_val)
print_map()
while True:
	clock.tick(20)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	if keys[K_w]:
		player_y -= 1
		if player_y < 0: 
			player_y = y_max-1
			seed_val += 10000
			new_map(seed_val) 
		if map[player_y][player_x] == 1: player_y += 1
	if keys[K_r]: 
		player_y += 1
		if player_y >= y_max-1: 
			player_y = 0
			seed_val -= 10000
			new_map(seed_val) 
		if map[player_y][player_x] == 1: player_y -= 1
	if keys[K_a]: 
		player_x -= 1
		if player_x < 0:
			player_x = x_max - 1
			seed_val += 1
			new_map(seed_val)
		if map[player_y][player_x] == 1: player_x += 1
	if keys[K_s]: 
		player_x += 1
		if player_x >= x_max-1: 
			player_x = 0
			seed_val -= 1
			new_map(seed_val)
		if map[player_y][player_x] == 1: player_x -= 1
	#if keys[K_F1]: new_map()

	#if player_y < 0: player_y = 0
	#if player_x < 0: player_x = 0
	#if player_x > x_max: player_x = x_max 
	#if player_y > y_max: player_y = y_max

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()


	screen.fill(BLACK)
	#draw_grid(screen, width, height, line_spacing, CYAN)
	draw_map()
	draw_square(player_x,player_y,RED)
	pygame.display.flip()
