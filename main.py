import pygame



FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
PIPEGAPSIZE  = 80
BASEY        = SCREENHEIGHT * 0.79
pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
IMAGES, HITMASK = {}, {}

PLAYER = ('assets/redbird-downflap.png'), ('assets/redbird-midflap.png'),('assets/redbird-upflap.png')

BACKGROUND = ('assets/background-day1.png')
PIPES = ('assets/pipe-green.png')

def fnc():

  pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
  
  IMAGES['numbers'] = (
  pygame.image.load('assets/0.png').convert_alpha(),
  pygame.image.load('assets/1.png').convert_alpha(),
  pygame.image.load('assets/2.png').convert_alpha(),
  pygame.image.load('assets/3.png').convert_alpha(),
  pygame.image.load('assets/4.png').convert_alpha(),
  pygame.image.load('assets/5.png').convert_alpha(),
  pygame.image.load('assets/6.png').convert_alpha(),
  pygame.image.load('assets/7.png').convert_alpha(),
  pygame.image.load('assets/8.png').convert_alpha(),
  pygame.image.load('assets/9.png').convert_alpha()
  )
IMAGES['gameover'] = pygame.image.load('assets/gameover.png').convert_alpha()
   
IMAGES['startgame'] = pygame.image.load('assets/startgame.png').convert_alpha()
    
IMAGES['base'] = pygame.image.load('assets/base.png').convert_alpha()

while True:
  IMAGES['PLAYER'] = (
    pygame.image.load('assets/redbird-midflap.png').convert_alpha()
  )
  IMAGES['BACKGROUND'] = (
    pygame.image.load('assets/background-day1.png').convert_alpha()
  )
  IMAGES['pipe'] = (
    pygame.transform.flip(
    pygame.image.load('assets/pipe-green.png').convert_alpha(), False, True),
    pygame.image.load('assets/pipe-green.png').convert_alpha()
  )
  
HITMASK['pipe'] = (
HITMASK(IMAGES['pipe'])
)
HITMASK['player'] = (
HITMASK(IMAGES['player'][0]),
HITMASK(IMAGES['player'][1]),
HITMASK(IMAGES['player'][2])
)

fnc()

