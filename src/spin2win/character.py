from FGAme import *

class Character(RegularPoly):
	def __init__(self, in_dash=False, *args, **kwargs):
		self.in_dash = in_dash
		super(Character, self).__init__(inertia='inf', *args, **kwargs)
											
	def move_character(self, dx, dy):
		if self.in_dash == False:
			self.vel+=(dx,dy)
		else: 
			self.vel=self.vel
		