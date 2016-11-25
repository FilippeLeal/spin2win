from FGAme import *
from spin2win.music import Music
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))

class Character(RegularPoly):
	def __init__(self, in_dash=False, is_force_on = 1, *args, **kwargs):
		self.in_dash = in_dash
		self.is_force_on = is_force_on
		super(Character, self).__init__(inertia='inf', *args, **kwargs)

		on('key-down','return').do(self.dashsound)
		on('key-down', 'space').do(self.dashsound)
		on('key-down', 'p').do(self.defesesound)
		on('key-down', 'x').do(self.defesesound)
											
	def move_character(self, dx, dy):
		if self.in_dash == False:
			self.vel+=(dx,dy)
		else: 
			self.vel=self.vel
	
	def dashsound(self):
		dash_sound = os.path.join(_ROOT, 'sounds/dash.wav')
		Music.play_sound(dash_sound)
		
	def defesesound(self):
		defense_sound = os.path.join(_ROOT, 'sounds/defense.wav')
		Music.play_sound(defense_sound)
		
	def dash(self, r_mass, r_color):
		attack = 1500*3
		print(self.color)
		#FIX ME: Não está alterando a cor ao dar o dash se o uso o schedule para chamar o proximo método
		self.color = 'orange'
		print(self.color)
		self.is_force_on = 0
		self.in_dash = True
		self.vel *= 1.1
		self.mass=attack
		#FIX ME: Schedule (o periodo de tempo) parece não estar funcionando
		schedule(1, self.nodash(r_mass=r_mass, r_color=r_color))	
	
	def nodash(self, r_mass, r_color):
		self.in_dash = False
		self.is_force_on = 1
		self.color = r_color
		self.mass = r_mass
		
	def defense(self, r_mass, r_color):
		defense = 1500*10
		self.vel*=0.9
		self.mass=defense
		self.color='black' 
		schedule(1, self.nodefense(r_mass, r_color))
	
	def nodefense(self, r_mass, r_color):
		self.mass=r_mass
		self.color=r_color
	
	def check_lose(self):
		if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
			exit()