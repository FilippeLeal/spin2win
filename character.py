from FGAme import *

class Character(RegularPoly):
	def __init__(self, N, length,
                 pos, vel, omega,
                 **kwargs):
		self.in_dash = 'off'
		super(Character, self).__init__(N=N, length=length, pos=pos, vel=vel, omega=omega, color='blue',
                                          **kwargs)
		
	def draw_poly(obj,N,length,pos,vel,omega,color,mass):
		obj = RegularPoly(N=N,length=length,pos=pos,vel=vel,omega=omega,color=color,mass=mass)
		return obj
		
	#def move(obj, dx, dy):
	#	if obj.in_dash == 'off':
	#		obj.vel+=(dx,dy)
	#	else: 
	#		obj.vel=obj.vel