'''Class to define Snake object'''

import pygame as pg
import random
import setup as s
import sys
from pathlib import Path


class Snake(object):
    ''' Constructor for Snake object
    '''
    def __init__(self):
        self.length = 1
        self.positions = [((s.SCREEN_WIDTH / 2), (s.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([s.UP, s.DOWN, s.LEFT, s.RIGHT])
        self.color = (0, 0, 0)
        # initiate the score to zero
        self.score = 0
        
    '''Getter method for first element of position property (snake head)
    '''
    def get_head_position(self):
        return self.positions[0]
    '''Turn snake 
    '''
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # this method is currently where Im trying to figure out how to teleport snake(not functioning)
    def hit_portal(self):
        new_position = self.get_head_position()

        # position_variant = random.randint(1, 10)
        # for position in self.positions:
        #     position = position * position_variant
        

        return new_position
    '''Draw the snake object on the surface. Snake is a rect at the moment.
    '''
    def draw(self, surface):
        for pos in self.positions:
            rect = pg.Rect((pos[0], pos[1]), (s.GRID_SIZE, s.GRID_SIZE))
            pg.draw.rect(surface, self.color, rect)
            pg.draw.rect(surface, (93, 216, 218), rect, 1)

