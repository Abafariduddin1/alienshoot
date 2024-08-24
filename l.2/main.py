import pgzrun
import random
WIDTH=400
HEIGHT=600
TITLE="Shooting game"
alien=Actor("ailein.png")
alien.pos=100,200
message="Shoot it."
def draw():
    screen.fill("White")
    alien.draw()
    screen.draw.text(message,(100,100),fontsize=60,color="Black",shadow=(1,1),scolor="grey",gcolor="red")

def moving():
        alien.pos=random.randint(0,400),random.randint(0,600)

def on_mouse_down(pos):
      global message
      if alien.collidepoint(pos):
            moving()
            message="Nice shot!"
      else:
           message="You missed."




pgzrun.go()