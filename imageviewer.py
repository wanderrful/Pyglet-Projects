import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('wanderrful.png')
labelError = pyglet.text.Label(
    'There was an error loading the image.',
    font_name='Times New Roman',
    font_size=36,
    x=window.width//2,y=window.height//2,
    anchor_x='center',anchor_y='center'
    )

@window.event
def on_draw():
    window.clear()
    try:
        image.blit(0,0) #blit requires coords
    except ResourceNotFoundException(name):
        labelError.draw() #draw doesn't because the coords were defined when i instantiated the object

if __name__ == '__main__':
    pyglet.app.run()
