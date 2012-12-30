#works properly~
import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width = 485
        self.height = 300

        self.gs = 0 #gamestate
        '''
        key for gs:
        0   ->  aaa
        1   ->  aaa
        2   ->  aaa
        '''

        self.main_batch = pyglet.graphics.Batch()

        self.label1 = pyglet.text.Label(
            'label1',
            x=100,y=100,
            batch = self.main_batch
            )
        self.label2 = pyglet.text.Label(
            'label2',
            x=250,y=250,
            batch = self.main_batch
            )    
    
    def on_draw(self):
        self.clear()
        
        self.main_batch.draw()

    def on_key_press(self, symbol, modifier):
        pass
    
if __name__=='__main__':
    mainWindow = MainWindow()
    pyglet.app.run()
