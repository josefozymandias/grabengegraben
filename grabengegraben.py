import pygame
from pygame.locals import *
import sys
from random import randint, seed
from os import listdir

pygame.init()

size = width, height = 1920, 1080
#size = width, height = 800, 600
screen = pygame.display.set_mode(size,FULLSCREEN)
#screen = pygame.display.set_mode(size)
pygame.display.set_caption("Graben Gegraben")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
MAGENTA= (255,   0, 255)
line_spacing = 40
player_x = 0
player_y = 0
x_max = width // line_spacing
y_max = height // line_spacing
map = []
map_size = 75
min_room_size = 2
max_room_size = 5
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
	#pygame.draw.rect(screen,color,(x*ls+1, y*ls+1, ls-1, ls-1))
	pygame.draw.rect(screen,color,(x*ls, y*ls, ls, ls))

def draw_map():
	global item_images, cobblestone,lava
	for y in range(len(map)):
		for x in range(len(map[y])):
			#if map[y][x] == 0:
			#	screen.blit(cobblestone, (x * line_spacing, y * line_spacing))
			if map[y][x] == 1:
				#draw_square(x,y,BLUE)
				screen.blit(lava, (x*line_spacing, y*line_spacing))
			elif map[y][x] >= 50:
				#draw_square(x,y,MAGENTA)
				screen.blit(item_images[map[y][x]-50], (x * line_spacing, y * line_spacing))

def rand_rooms():
	for i in range(40):
		make_room(randint(0,x_max-max_room_size),randint(0,y_max-max_room_size),randint(min_room_size, max_room_size))

def rand_items():
	global item_images
	num = len(item_images)-1
	for i in range(60):
		map[randint(0,y_max-1)][randint(0,x_max-1)] = 50 + randint(0,num)

def new_map(seed_val):
	global map
	map = []
	seed(seed_val)
	init_map()
	rand_items()
	rand_rooms()

item_images = []
file_names = listdir("tiles/items")
cobblestone = pygame.image.load("tiles/items/cobblestone.bmp")
cobblestone = pygame.transform.scale2x(cobblestone)
lava = pygame.image.load("tiles/items/lava.bmp")
lava = pygame.transform.scale2x(lava)
goldsamurai = pygame.image.load("tiles/items/goldsamurai.bmp")
goldsamurai.set_colorkey(MAGENTA)
goldsamurai = pygame.transform.scale2x(goldsamurai)
flame_north = pygame.image.load("tiles/effects/flame_north.bmp")
flame_north.set_colorkey(MAGENTA)
flame_north = pygame.transform.scale2x(flame_north)
flame_south = pygame.image.load("tiles/effects/flame_south.bmp")
flame_south.set_colorkey(MAGENTA)
flame_south = pygame.transform.scale2x(flame_south)
flame_east = pygame.image.load("tiles/effects/flame_east.bmp")
flame_east.set_colorkey(MAGENTA)
flame_east = pygame.transform.scale2x(flame_east)
flame_west = pygame.image.load("tiles/effects/flame_west.bmp")
flame_west.set_colorkey(MAGENTA)
flame_west = pygame.transform.scale2x(flame_west)

#print(file_names)
for file_name in file_names:
	name = "tiles/items/" + file_name
	item_images.append(pygame.transform.scale2x(pygame.image.load(name)))

for item_image in item_images:
	item_image.set_colorkey(MAGENTA)

#print(item_images)
NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3
player_dir = EAST
seed_val = 1337
new_map(seed_val)
attack = False
#print_map()
while True:
	clock.tick(20)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	#if keys[K_ESCAPE]: break
	if keys[K_SPACE]: attack = True
	if keys[K_w]:
		player_dir = NORTH
		player_y -= 1
		if player_y < 0:
			player_y = y_max-1
			seed_val += 10000
			new_map(seed_val)
		if map[player_y][player_x] == 1: player_y += 1
	if keys[K_s]:
		player_dir = SOUTH
		player_y += 1
		if player_y >= y_max-1:
			player_y = 0
			seed_val -= 10000
			new_map(seed_val)
		if map[player_y][player_x] == 1: player_y -= 1
	if keys[K_a]:
		player_dir = WEST
		player_x -= 1
		if player_x < 0:
			player_x = x_max - 1
			seed_val += 1
			new_map(seed_val)
		if map[player_y][player_x] == 1: player_x += 1
	if keys[K_d]:
		player_dir = EAST
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


	#screen.fill(GREEN)
	#draw_grid(screen, width, height, line_spacing, CYAN)
	for y in range(y_max):
		for x in range(x_max):
			screen.blit(cobblestone, (x*line_spacing, y*line_spacing))
	draw_map()
	screen.blit(goldsamurai, (player_x*line_spacing, player_y*line_spacing))
	if attack:
		if player_dir == NORTH:
			screen.blit(flame_north, (player_x*line_spacing,(player_y-1)*line_spacing))
		elif player_dir == SOUTH:
			screen.blit(flame_south, (player_x*line_spacing,(player_y+1)*line_spacing))
		elif player_dir == EAST:
			screen.blit(flame_east, ((player_x+1)*line_spacing,player_y*line_spacing))
		elif player_dir == WEST:
			screen.blit(flame_west, ((player_x-1)*line_spacing,player_y*line_spacing))
		attack = False
	pygame.display.flip()
