#!/usr/bin/env python

from pygame import init, display, draw, time, event

# ideally we import individual event type names here, it's cleaner, IMO
from pygame import QUIT

from sys import exit

i = init()
if i != (6, 0):
    raise Exception('bad pygame init')

screen = display.set_mode((640, 480))
clock = time.Clock()

############################################################
##  CLASSES 
############################################################

class 


while True: 
    clock.tick(60)

    # so interaction is going to get handled here
    # more info here: http://www.pygame.org/docs/ref/event.html
    for ev in event.get():
        if ev.type == QUIT:
            exit(0)

    # here is where you'd do the actual drawing stuff.


    

    # end drawing
    display.flip()
    # end loop


