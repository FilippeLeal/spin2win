from FGAme import *
import pygame	
from spin2win.arena import *
from spin2win.music import Music
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))

main_sound = os.path.join(_ROOT, 'sounds/battle_theme.mp3')
Music.play_music(main_sound)
			
arena = Arena()
