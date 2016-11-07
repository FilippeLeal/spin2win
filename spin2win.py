from FGAme import *
import pygame	
	
width=40
height=220
leftwall = world.add.aabb(shape=(width, height), pos=(0,300), mass='inf')
rigthwall = world.add.aabb(shape=(width, height), pos=(800,300), mass='inf')
topwall = world.add.aabb(shape=(height, width), pos=(400,600), mass='inf')
botwall = world.add.aabb(shape=(height, width), pos=(400,0), mass='inf')

normalmass=1500
defense = normalmass*10
attack = normalmass*5
world.damping=0.9

blue = RegularPoly(6,length=40,pos=(200,300),vel=(300,0),omega=20,color='blue',mass=normalmass*2)
red = RegularPoly(5,length=40,pos=(600,300),vel=(-300,0),omega=25,color='red',mass=normalmass)


blue.inertia='inf'
red.inertia='inf'

world.add(blue)
world.add(red)

dx=0
dy=0
is_force_blue_on=1
is_force_red_on=1
blue_in_dash='off'
red_in_dash='off'

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
main_sound = pygame.mixer.music.load("battle_theme.mp3")
main_sound = pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2);




@listen('long-press', 'left',dx=-5,dy=0)
@listen('long-press', 'right',dx=5,dy=0)
@listen('long-press', 'up',dy=5,dx=0)
@listen('long-press', 'down',dy=-5,dx=0)
def bluemove(dx,dy):
	if blue_in_dash == 'off':
		blue.vel+=(dx,dy)
	else: 
		blue.vel=blue.vel

@listen('long-press', 'a',d2x=-10,d2y=0)
@listen('long-press', 'd',d2x=10,d2y=0)
@listen('long-press', 'w',d2y=10,d2x=0)
@listen('long-press', 's',d2y=-10,d2x=0)
def redmove(d2x,d2y):
	if red_in_dash == 'off':
		red.vel+=(d2x,d2y)
	else: 
		red.vel=red.vel

@listen ('key-down','return')
@listen ('key-down','space')
def dashsound():
	dash_sound = pygame.mixer.Sound("dash.wav")
	dash_sound.set_volume(0.2)
	dash_sound.play()
	
		
@listen('key-down','return')
def bluedash():
	global is_force_blue_on
	is_force_blue_on=0
	global blue_in_dash
	blue_in_dash='on'
	blue.vel*=1.1
	blue.mass=attack
	blue.color='orange'
	schedule(1,nodashblue)	

	
def nodashblue():
	global blue_in_dash
	blue_in_dash='off'
	global is_force_blue_on
	is_force_blue_on = 1
	blue.color='blue'
	blue.mass=normalmass

@listen('long-press','space')
def reddash():
	global is_force_red_on
	is_force_red_on=0
	global red_in_dash
	red_in_dash='on'
	red.vel*=1.1
	red.mass=attack
	red.color='orange'
	schedule(1,nodashred)

def nodashred():
	global red_in_dash
	red_in_dash='off'
	global is_force_red_on
	is_force_red_on = 1
	red.color='red'
	red.mass=normalmass


@listen('key-down', 'p')	
@listen('key-down', 'x')
def defesesound():
	dash_sound = pygame.mixer.Sound("defense.wav")
	dash_sound.set_volume(0.3)
	dash_sound.play()

@listen('long-press','p')
def bluedefense():
	blue.vel*=0.9
	blue.mass=defense
	blue.color='black' 
	schedule(1,nodefenseblue)
	
@listen('long-press','x')
def reddefense():
	red.vel*=0.9
	red.mass=defense
	red.color='black'
	schedule(1,nodefensered)

def nodefenseblue():
	blue.mass=normalmass*2
	blue.color='blue'

def nodefensered():
	red.mass=normalmass
	red.color='red'

@listen('frame-enter')
def check_blue_lose():
	if blue.x < 0 or blue.x > 800 or blue.y < 0 or blue.y > 600:
		exit()
		
@listen('frame-enter')
def check_red_lose():
	if red.x < 0 or red.x > 800 or red.y < 0 or red.y > 600:
		exit()
		
red.force = lambda v: -10000*(red.pos-pos.middle)*is_force_red_on
blue.force =  lambda t: -10000*(blue.pos-pos.middle)*is_force_blue_on

run()
