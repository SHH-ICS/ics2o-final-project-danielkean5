from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
PIPEGAPSIZE  = 80
BASEY        = SCREENHEIGHT * 0.79

IMAGES, HITMASK = {}, {}

PLAYER = (
  'assets/redbird-downflap.png'
  'assets/redbird-midflap.png'
  'assets/redbird-upflap.png'
)
BACKGROUND = ('assets/background-day1.png')
PIPES = ('assets/pipe-green.png')

def fnc():
  
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

while true:
  IMAGES['player'] = (
    pygame.image.load(PLAYER[playerindex]).convert()
  )
  IMAGES['background'] = (
    pygame.image.load(BACKGROUND[backgroundindex]).convert()
  )
  IMAGES['pipe'] = (
    pygame.transform.flip(
      pygame.image.load(PIPES[pipeindex]).convert_alpha(), False, True),
    pygame.image.load(PIPES[pipeindex]).convert_alpha(),
        )
  
HITMASK['pipe'] = (
getHitmask(images['pipe'])
)
HITMASK['player'] = (
getHitmask(images['player'][0]),
getHitmask(images['player'][1]),
getHitmask(images['player'][2])
)

fnc()