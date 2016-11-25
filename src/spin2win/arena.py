from FGAme import *
from spin2win.character import Character

class Arena(World):
	def init(self, is_force_on = 1):
		self.blue = Character(N=6,length=40,pos=(200,300),vel=(300,0),omega=20, color = 'blue', mass=3000)
		self.red = Character(N=5, length=40, pos=(600,300), vel=(-300, 0), omega=25, color = 'red', mass=1500)
		self.add([self.blue, self.red])
		self.red.force = lambda v: -10000*(self.red.pos-pos.middle)*is_force_on
		self.blue.force =  lambda t: -10000*(self.blue.pos-pos.middle)*is_force_on
		
		self.damping=0.9
		
		self.draw_walls()
		
		#FIX-ME: Pensar em um jeito melhor de fazer isso
		on('long-press', 'left').do(self.blue.move_character, -5, 0)
		on('long-press', 'right').do(self.blue.move_character, 5, 0)
		on('long-press', 'up').do(self.blue.move_character, 0, 5)
		on('long-press', 'down').do(self.blue.move_character, 0, -5,)
		on('long-press', 'a').do(self.red.move_character, -10, 0)
		on('long-press', 'd').do(self.red.move_character, 10, 0)
		on('long-press', 'w').do(self.red.move_character, 0, 10)
		on('long-press', 's').do(self.red.move_character, 0, -10)
		
		
	def draw_walls(self):
		width=40
		height=220
		self.leftwall = self.add.aabb(shape=(width, height), pos=(0,300), mass='inf')
		self.rigthwall = self.add.aabb(shape=(width, height), pos=(800,300), mass='inf')
		self.topwall = self.add.aabb(shape=(height, width), pos=(400,600), mass='inf')
		self.botwall = self.add.aabb(shape=(height, width), pos=(400,0), mass='inf')
		
	#@listen('frame-enter')
	#def check_lose(self):
	#	if blue.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
	#		exit()
	
	