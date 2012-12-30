import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width = 485
        self.height = 300
        pyglet.gl.glClearColor(*(120,120,120,255))

        self.main_batch = pyglet.graphics.Batch()

        self.dota2_img = pyglet.image.load('wanderrful.png')
        self.dota2_sprite = Dota2Sprite(
            self.dota2_img,
            x=self.width//2, y=self.height//2,
            batch=self.main_batch
            )

    def on_update(self): #not part of the api
        self.dota2_sprite.rotation += self.dota2_sprite.rotationalVelocity

    def on_draw(self):
        self.on_update()
        
        self.clear()

        self.main_batch.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.dota2_sprite.rotationalVelocity = (-1)*self.dota2_sprite.turnSpeed
        elif symbol == pyglet.window.key.RIGHT:
            self.dota2_sprite.rotationalVelocity = 1*self.dota2_sprite.turnSpeed

    def on_key_release(self, symbol, modifiers):
        if symbol in {pyglet.window.key.LEFT, pyglet.window.key.RIGHT}:
            self.dota2_sprite.rotationalVelocity = 0

class Dota2Sprite(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Dota2Sprite, self).__init__(*args, **kwargs)
        self.rotationalVelocity = 0
        self.turnSpeed = 5

if __name__=='__main__':
    mainWindow = MainWindow()
    pyglet.app.run()
