import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image = pyglet.resource.image('wanderrful.png')
image.x = window.width//2
image.y = window.height//2

VELX = 0
VELY = 0
SPEED = 3

images = [image]




@window.event
def on_key_press(symbol,modifiers):
    if symbol == -1:
        pass
    elif symbol == key.A:
        image.x = window.width //2
        image.y = window.height//2
    elif symbol == key.LEFT:
        VELX -= SPEED
    elif symbol == key.RIGHT:
        VELX += SPEED
    elif symbol == key.UP: #because (0,0) is in bottom left corner
        VELY += SPEED
    elif symbol == key.DOWN:
        VELY -= SPEED


@window.event
def on_draw():
    window.clear()
    for i in images: #this works
        i.blit(i.x+VELX,i.y+VELY)
    

if __name__=='__main__':    
    pyglet.app.run()
