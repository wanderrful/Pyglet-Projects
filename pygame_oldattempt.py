import pygame, sys, math, random
from pygame.locals import *

# DECLARE COLOR RGB VALUES
AQUA = (0,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
FUSCHIA = (255,0,255)
GRAY = (128,128,128)
GREEN = (0,128,0)
LIME = (0,255,0)
MAROON = (128,0,0)
NAVYBLUE = (0,0,128)
OLIVE = (128,128,0)
PURPLE = (128,0,128)
RED = (255,0,0)
SILVER = (192,192,192)
TEAL = (0,128,128)
WHITE = (255,255,255)
YELLOW = (255,255,0)
# END

# DECLARE THE CLASSES
class Paddle:
	""" A rectangle image that has only an (x,y) position and an update method """
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dy = 0
	
	def update(self, surface, newy):
		self.y = newy
		pygame.draw.rect(surface, WHITE, (self.x, self.y, 10, 30), 5)
class Ball:
	""" A circle image that has an (x,y) position and an update method """
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.initial_direction = 0
		pickInitialDirection()
		
	def update(self, surface, newx, newy):
		self.x = newx
		self.y = newy
		pygame.draw.circle(surface, WHITE, (self.x, self.y), 5, 5)
		
	def pickInitialDirection(self):
		self.initial_direction = 2*math.pi*random.random()
# END

# INITIALIZE THE ATTRIBUTES
RESOLUTION = (400, 300)
WINDOW_TITLE = "Hello world!"
FPS = 30
fpsClock = pygame.time.Clock()

OBJECT_SPEED = 10

pygame.init()
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(WINDOW_TITLE)

DISPLAYSURF.fill(BLACK)

player1 = Paddle(20, 120)
player2 = Paddle(370, 120)
ball = Ball(200,150)
# END

while True:
# HANDLE EVENTS
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		elif event.type = KEYDOWN:
			if event.key == K_UP:
				player.dy = SPEED
			elif event.key == K_DOWN:
				player1.dy = (-1)*SPEED
				
		elif event.type = KEYUP:
			if event.key == K_UP:
				player1.dy = 0
			elif event.key == K_DOWN:
				player1.dy = 0
# END

# UPDATE GAME STATE
	player1.update(DISPLAYSURF, player1.y+player1.dy)
	player2.update(DISPLAYSURF, player2.y+player2.dy)
	
	# UPDATE THE BALL'S DIRECTION
	ball.dx = SPEED*math.cos(ball.initial_direction)
	ball.dy = SPEED*math.sin(ball.initial_direction)
	# END
	ball.update(DISPLAYSURF, ball.x+ball.dx, ball.y+ball.dy)
# END

# DRAW SCREEN
	pygame.display.update()
	fpsClock.tick(FPS)
# END