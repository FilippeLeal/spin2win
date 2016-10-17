from FGAme import *

espessura=40
comprimento=220
leftwall = world.add.aabb(shape=(espessura, comprimento), pos=(0,300), mass='inf')
rigthwall = world.add.aabb(shape=(espessura, comprimento), pos=(800,300), mass='inf')
topwall = world.add.aabb(shape=(comprimento, espessura), pos=(400,600), mass='inf')
botwall = world.add.aabb(shape=(comprimento, espessura), pos=(400,0), mass='inf')

normalmass=1500
defense = normalmass*3
world.damping=0.9

azul = RegularPoly(6,length=40,pos=(200,300),vel=(300,0),omega=20,color='blue',mass=normalmass*2)
vermelho = RegularPoly(5,length=40,pos=(600,300),vel=(-300,0),omega=25,color='red',mass=normalmass)


azul.inertia='inf'
vermelho.inertia='inf'

world.add(azul)
world.add(vermelho)

dx=0
dy=0

@listen ('frame-enter')
def normalize():
	azul.mass=normalmass*2
	vermelho.mass=normalmass
	azul.color='blue'
	vermelho.color='red'

@listen('long-press', 'left',dx=-5,dy=0)
@listen('long-press', 'right',dx=5,dy=0)
@listen('long-press', 'up',dy=5,dx=0)
@listen('long-press', 'down',dy=-5,dx=0)
def azulmove(dx,dy):
	azul.vel+=(dx,dy)

@listen('long-press', 'a',d2x=-10,d2y=0)
@listen('long-press', 'd',d2x=10,d2y=0)
@listen('long-press', 'w',d2y=10,d2x=0)
@listen('long-press', 's',d2y=-10,d2x=0)
def vermelhomove(d2x,d2y):
	vermelho.vel+=(d2x,d2y)
	
@listen('long-press','return')
def azuldash():
	azul.vel*=1.05
	azul.color='orange'
	
@listen('long-press','space')
def vermelhodash():
	vermelho.vel*=1.05
	vermelho.color='orange'

@listen('long-press','p')
def azuldefense():
	azul.vel*=0.9
	azul.mass=defense
	azul.color='black'
	

@listen('long-press','x')
def vermelhodefense():
	vermelho.vel*=0.9
	vermelho.mass=defense
	vermelho.color='black'

@listen('frame-enter')	
def check_azul_lose():
	if azul.x < 0 or azul.x > 800 or azul.y < 0 or azul.y > 600:
		exit()
		
@listen('frame-enter')	
def check_vermelho_lose():
	if vermelho.x < 0 or vermelho.x > 800 or vermelho.y < 0 or vermelho.y > 600:
		exit()
		
vermelho.force = lambda t: -10000*(vermelho.pos-pos.middle)
azul.force =  lambda t: -10000*(azul.pos-pos.middle)


run()