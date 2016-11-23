from FGAme import *

class Character(RegularPoly):
	def __init__(self, *args, **kwargs):
		self.in_dash = 'off'
		super(Character, self).__init__(inertia='inf', *args, **kwargs)
											
	
		