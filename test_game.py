#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_game.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import pygame, time, sys 
from pygame.locals import *



pygame.init()

#Drawig the Window
DISPLAYSURF = pygame.display.set_mode((500,400), 1, 32)
pygame.display.set_caption("Test Game")

#set colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PURPLE =(192,   0, 180)

DISPLAYSURF.fill(GREEN)
pygame.display.update()
time.sleep(2)

DISPLAYSURF.fill(RED)
pygame.display.update()
time.sleep(2)

DISPLAYSURF.fill(WHITE)
pygame.display.update()
time.sleep(2)

DISPLAYSURF.fill(BLUE)
pygame.display.update()
time.sleep(2)

DISPLAYSURF.fill(BLACK)
pygame.display.update()
time.sleep(2)

DISPLAYSURF.fill(PURPLE)
pygame.display.update()
time.sleep(2)
	
for event in pygame.event.get():
	if event.type == QUIT:
		pygame.quit()
		sys.exit()
		




