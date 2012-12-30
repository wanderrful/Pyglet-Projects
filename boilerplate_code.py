import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width = 485
        self.height = 300

        self.main_batch = pyglet.graphics.Batch()

    def on_draw(self):
        self.clear()

        self.main_batch.draw()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

if __name__=='__main__':
    mainWindow = MainWindow()
    pyglet.app.run()
