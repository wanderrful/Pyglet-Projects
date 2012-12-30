#works fine~
import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width = 485
        self.height = 300

        self.needToUpdate = True
        '''
        This flag is manually set to True whenever a property changes and
        will be automatically set to False after performing self.on_update()
        '''
        self.gs = 0
        '''
        0 -> main menu
        1 -> in game
        2 -> game over
        3 -> exit
        '''
        

        #content batches
        self.mainMenu_batch = pyglet.graphics.Batch()
        self.inGame_batch = pyglet.graphics.Batch()
        self.gameOver_batch = pyglet.graphics.Batch()
        self.exitMenu_batch = pyglet.graphics.Batch()
        
        #mainMenu_batch content
        self.mainMenuTitle = pyglet.text.Label('Game name!',
                                            font_name='Times New Roman',
                                            font_size=36,
                                            x=self.width//2,y=self.height//2+100,
                                            anchor_x='center',
                                            batch=self.mainMenu_batch
                                            )
        self.mainMenu_choice = 0
        '''
        0 -> start game
        1 -> quit
        '''
        self.mainMenuOptions = []
        self.mainMenuOptions.append(pyglet.text.Label('Start game',
                                              font_name='Times New Roman',
                                              font_size=24,
                                              x=self.width//2,y=self.height//2,
                                              anchor_x='center',
                                              batch=self.mainMenu_batch
                                              ))
        self.mainMenuOptions.append(pyglet.text.Label('Quit',
                                              font_name='Times New Roman',
                                              font_size=24,
                                              x=self.width//2,y=self.height//2-30,
                                              anchor_x='center',
                                              batch=self.mainMenu_batch
                                              ))
        #inGame_batch content
        self.inGameContent = []
        self.inGameContent.append(pyglet.text.Label('Game in progress!',
                                            font_name='Times New Roman',
                                            font_size=36,
                                            x=self.width//2,y=self.height//2+100,
                                            anchor_x='center',
                                            batch=self.inGame_batch
                                            ))
        #gameOver_batch content
        self.gameOverContent = []
        self.gameOverContent.append(pyglet.text.Label('Game over!',
                                            font_name='Times New Roman',
                                            font_size=36,
                                            x=self.width//2,y=self.height//2+100,
                                            anchor_x='center',
                                            batch=self.gameOver_batch
                                            ))
        #exit_batch content
        self.exitMenuTitle = pyglet.text.Label('Exit?!',
                                            font_name='Times New Roman',
                                            font_size=36,
                                            x=self.width//2,y=self.height//2+100,
                                            anchor_x='center',
                                            batch=self.exitMenu_batch
                                            )
        self.exitMenu_choice = 0
        '''
        0 -> yes
        1 -> no
        '''
        self.exitMenuOptions = []
        self.exitMenuOptions.append(pyglet.text.Label('Yes',
                                              font_name='Times New Roman',
                                              font_size=24,
                                              x=self.width//2,y=self.height//2,
                                              anchor_x='center',
                                              batch=self.exitMenu_batch
                                              ))
        self.exitMenuOptions.append(pyglet.text.Label('No',
                                              font_name='Times New Roman',
                                              font_size=24,
                                              x=self.width//2,y=self.height//2-30,
                                              anchor_x='center',
                                              batch=self.exitMenu_batch
                                              ))
        
    def on_draw(self):
        self.clear()
        if self.needToUpdate:
            self.on_update()
            self.needToUpdate = False
        else:
            pass

        if self.gs == 0:
            self.mainMenu_batch.draw()
        elif self.gs == 1:
            self.inGame_batch.draw()
        elif self.gs == 2:
            self.gameOver_batch.draw()
        elif self.gs == 3:
            self.exitMenu_batch.draw()

    def on_key_press(self, symbol, modifiers):
        #debug F keys to change self.gs manually
        if symbol == pyglet.window.key.F1: self.gs == 0
        elif symbol == pyglet.window.key.F2: self.gs == 1
        elif symbol == pyglet.window.key.F3: self.gs == 2
        elif symbol == pyglet.window.key.F4: self.gs == 3
        #!debug
        
        if self.gs == 0: #main menu
            if symbol == pyglet.window.key.UP:
                self.mainMenuOptions[self.mainMenu_choice].text = self.mainMenuOptions[self.mainMenu_choice].text[2:-2] #remove the '> <' marks
                self.mainMenu_choice = (self.mainMenu_choice - 1) % len(self.mainMenuOptions)
                self.needToUpdate = True
            elif symbol == pyglet.window.key.DOWN:
                self.mainMenuOptions[self.mainMenu_choice].text = self.mainMenuOptions[self.mainMenu_choice].text[2:-2]
                self.mainMenu_choice = (self.mainMenu_choice + 1) % len(self.mainMenuOptions)
                self.needToUpdate = True
            elif symbol in {pyglet.window.key.ENTER,pyglet.window.key.SPACE}:
                self.mainMenuOptions[self.mainMenu_choice].text = self.mainMenuOptions[self.mainMenu_choice].text[2:-2]
                if self.mainMenu_choice == 0: #start game has been selected
                    self.gs = 1
                elif self.mainMenu_choice == 1: #quit has been selected
                    self.gs = 3
                else:
                    pass
                self.needToUpdate = True
                self.mainMenu_choice = 0
                
        elif self.gs == 1: #in-game
            if symbol in {pyglet.window.key.ENTER, pyglet.window.key.SPACE}:
                self.gs = 0
                self.needToUpdate = True
            elif symbol == pyglet.window.key.ESCAPE:
                self.gs = 3
                self.needToUpdate = True
            else:
                pass
        
        elif self.gs == 2: #game over
            if symbol in {pyglet.window.key.ENTER, pyglet.window.key.SPACE}:
                self.gs = 0
                self.needToUpdate = True
            elif symbol == pyglet.window.key.ESCAPE:
                self.gs = 3
                self.needToUpdate = True
            else:
                pass
        
        elif self.gs == 3: #exit
            if symbol == pyglet.window.key.UP:
                self.exitMenuOptions[self.exitMenu_choice].text = self.exitMenuOptions[self.exitMenu_choice].text[2:-2] #remove the '> <' marks
                self.exitMenu_choice = (self.exitMenu_choice - 1) % len(self.exitMenuOptions)
                self.needToUpdate = True
            elif symbol == pyglet.window.key.DOWN:
                self.exitMenuOptions[self.exitMenu_choice].text = self.exitMenuOptions[self.exitMenu_choice].text[2:-2]
                self.exitMenu_choice = (self.exitMenu_choice + 1) % len(self.exitMenuOptions)
                self.needToUpdate = True
            elif symbol in {pyglet.window.key.ENTER,pyglet.window.key.SPACE}:
                self.exitMenuOptions[self.exitMenu_choice].text = self.exitMenuOptions[self.exitMenu_choice].text[2:-2]
                if self.exitMenu_choice == 0: #yes has been selected
                    self.close()
                    pyglet.app.exit()
                elif self.exitMenu_choice == 1: #no has been selected
                    self.gs = 0
                else:
                    pass
                self.needToUpdate = True
                self.exitMenu_choice = 0

    def on_key_release(self, symbol, modifiers):
        pass

    def on_update(self): #not in the api
        if self.gs == 0: #main menu stuff
            self.mainMenuOptions[self.mainMenu_choice].text = '> ' + self.mainMenuOptions[self.mainMenu_choice].text + ' <'
        elif self.gs == 1: #in-game stuff
            pass
        elif self.gs == 2: #game over stuff
            pass
        elif self.gs == 3: #exit menu stuff
            self.exitMenuOptions[self.exitMenu_choice].text = '> ' + self.exitMenuOptions[self.exitMenu_choice].text + ' <'

if __name__=='__main__':
    mainWindow = MainWindow()
    #pyglet.clock.schedule_interval(1/120.0, update) #I need to learn how to use this...
    pyglet.app.run()
