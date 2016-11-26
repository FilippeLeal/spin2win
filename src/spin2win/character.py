from FGAme import *
from spin2win.music import Music
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))

class Character(RegularPoly):
	def __init__(self, health,armor,in_dash=False,dash_cd=False,defense_cd=False, is_force_on = 1,*args, **kwargs):
		self.in_dash = in_dash
		self.is_force_on = is_force_on
		self.dash_cd= dash_cd
		self.defense_cd= defense_cd
		super(Character, self).__init__(inertia='inf', *args, **kwargs)
		on('pre-collision').do(self.sound_col)
		on('post-collision').do(self.deal_damage)
		self.health=health
		self.armor=armor
		self.damage=1000/armor
											
	def move_character(self, dx, dy):
		if self.in_dash == False:
			self.vel+=(dx,dy)
		else: 
			pass
	
	def dash(self, r_mass, r_color):
		if self.dash_cd == False:	
			dash_sound = os.path.join(_ROOT, 'sounds/dash.wav')
			Music.play_sound(dash_sound)
			attack = 5000
			self.color = 'orange'
			self.is_force_on = 0
			self.in_dash = True
			self.vel= self.vel/abs(self.vel)*1000
			self.mass=attack
			schedule(.5, self.nodash, r_mass=r_mass, r_color=r_color)
			self.dash_cd = True
			
		else:
			pass
	def dash_out_cd(self):
		self.dash_cd= False
		
	def nodash(self, r_mass, r_color):
		self.in_dash = False
		self.is_force_on = 1
		self.color = r_color
		self.mass = r_mass
		schedule(3,self.dash_out_cd)
		
		
	def defense(self, r_mass, r_color):
		if self.defense_cd == False:	
			defense_sound = os.path.join(_ROOT, 'sounds/defense.wav')
			Music.play_sound(defense_sound)
			defense = 30000
			self.vel=vec(0,0)
			self.is_force_on = 0
			self.mass=defense
			self.color = 'black' 
			schedule(1, self.nodefense, r_mass=r_mass, r_color=r_color)
			self.defense_cd = True
			
		else:
			pass
			
	def defense_out_cd(self):
		self.defense_cd = False
	
	def nodefense(self, r_mass, r_color):
		self.mass = r_mass
		self.color = r_color
		self.is_force_on = 1
		schedule(3, self.defense_out_cd)
	#FIX-ME ele fala que estamos passando 3 argumentos, então estamos pedindo 3 tbm
	def sound_col(self,col,dx):
		sound_col = os.path.join(_ROOT, 'sounds/collision_small.wav')
		Music.play_sound(sound_col)
	
	def deal_damage(self,col,damage):
		print(Character)
		if isinstance(col, Character): #and isinstance(B, self):
			self.health-=self.damage
			print(self.health)
		
		
	def check_lose(self):
		if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
			exit()