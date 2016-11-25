from FGAme import *
import pygame	
from spin2win.arena import *
from spin2win.music import Music
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))

#Verificar quais dados é possível tirar desse main	
normalmass=1500
defense = normalmass*10
attack = normalmass*3

dx=0
dy=0
is_force_blue_on=1
is_force_red_on=1
blue_in_dash='off'

red_in_dash='off'

main_sound = os.path.join(_ROOT, 'sounds/battle_theme.mp3')
Music.play_music(main_sound)

@listen ('key-down','return')
@listen ('key-down','space')
def dashsound():
	dash_sound = os.path.join(_ROOT, 'sounds/dash.wav')
	Music.play_sound(dash_sound)
		
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
	red.mass=2*normalmass


@listen('key-down', 'p')	
@listen('key-down', 'x')
def defesesound():
	defense_sound = os.path.join(_ROOT, 'sounds/defense.wav')
	Music.play_sound(defense_sound)

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

arena = Arena()