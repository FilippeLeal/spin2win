from FGAme import *

world.add.margin(20)

# enemy = world.add.circle(10,pos=(100,100),vel=(300,0),omega=0,color='red')
# hero =  world.add.circle(10,pos=(700,500),vel=(-300,0),omega=0,color='blue')
hero = RegularPoly(6,length=40,pos=(300,30),vel=(-300,300),omega=20,color='blue')
enemy = RegularPoly(5,length=40,pos=(30,300),vel=(300,-300),omega=25,color='red')
hero.mass*=4

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
	
	
@listen('key-down','z')
def dash():
	hero.vel*=2

enemy.force = lambda t: -10000*(enemy.pos-pos.middle)
hero.force =  lambda t: -10000*(hero.pos-pos.middle)


run()