'''
FOR SOME REASON,
I CANNOT SEEM TO MAKE THE GS VARIABLE CHANGE.
EVERYTHING ELSE SEEMS TO WORK FINE, THOUGH.
'''

import pyglet
from pyglet.window import key

global gs
gs = 0
getGS = lambda: gs
def setGS(val):
    gs = val
'''
0 : main
1 : ingame
2 : options
'''

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        setGS(0)
        print 'A was pressed!'
    elif symbol == key.LEFT:
        setGS(1)
        print 'LEFT was pressed!'
    elif symbol == key.ENTER:
        setGS(2)
        print 'ENTER was pressed!'
    else:
        pass

@window.event
def on_draw():
    window.clear()
    if getGS() == 0:
        labelX.draw()
    elif getGS() == 1:
        labelIngame.draw()
        print getGS()
    elif getGS() == 2:
        labelOptions.draw()
        print getGS()
if __name__ == '__main__':
    window = pyglet.window.Window()
    window.set_caption('Handlingmouse.py')
    pyglet.app.run()

    labelX = pyglet.text.Label( # is shown at the (0,0) coordinates - bottom left
        'hey hey hey! ASDF'
    )
    labelTitle = pyglet.text.Label(
        'Title screen!',
        font_name='Arial', font_size=36,
        x=window.width//2,y=window.height//2,
        anchor_x='center',anchor_y='center'
    )
    labelIngame = pyglet.text.Label(
        'Ingame screen!',
        font_name='Times New Roman', font_size=36,
        x=window.width//2,y=window.height//2,
        anchor_x='center',anchor_y='center'
    )
    labelOptions = pyglet.text.Label(
        'Options screen!',
        font_name='Courier New', font_size=36,
        x=window.width//2,y=window.height//2,
        anchor_x='center',anchor_y='center'
    )
