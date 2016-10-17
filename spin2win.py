from FGAme import *

espessura=40
comprimento=220
leftwall = world.add.aabb(shape=(espessura, comprimento), pos=(0,300), mass='inf')
rigthwall = world.add.aabb(shape=(espessura, comprimento), pos=(800,300), mass='inf')
topwall = world.add.aabb(shape=(comprimento, espessura), pos=(400,600), mass='inf')
botwall = world.add.aabb(shape=(comprimento, espessura), pos=(400,0), mass='inf')

# enemy = world.add.circle(10,pos=(100,100),vel=(300,0),omega=0,color='red')
# hero =  world.add.circle(10,pos=(700,500),vel=(-300,0),omega=0,color='blue')
hero = RegularPoly(6,length=40,pos=(200,300),vel=(300,0),omega=20,color='blue')
enemy = RegularPoly(5,length=40,pos=(600,300),vel=(-300,0),omega=25,color='red')
hero.mass*=2

world.damping=0.9
hero.inertia='inf'
enemy.inertia='inf'

world.add(hero)
world.add(enemy)

dx=0
dy=0

@listen('long-press', 'left',dx=-5,dy=0)
@listen('long-press', 'right',dx=5,dy=0)
@listen('long-press', 'up',dy=5,dx=0)
@listen('long-press', 'down',dy=-5,dx=0)
def heromove(dx,dy):
	hero.vel+=(dx,dy)

@listen('long-press', 'a',d2x=-10,d2y=0)
@listen('long-press', 'd',d2x=10,d2y=0)
@listen('long-press', 'w',d2y=10,d2x=0)
@listen('long-press', 's',d2y=-10,d2x=0)
def enemymove(d2x,d2y):
	enemy.vel+=(d2x,d2y)
	
@listen('long-press','return')
def herodash():
	hero.vel*=1.05
	
@listen('long-press','space')
def enemydash():
	enemy.vel*=1.05
	
	

enemy.force = lambda t: -10000*(enemy.pos-pos.middle)
hero.force =  lambda t: -10000*(hero.pos-pos.middle)


run()