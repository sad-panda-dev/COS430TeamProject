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
        self.__length = 1
        self.__positions = [((s.SCREEN_WIDTH / 2), (s.SCREEN_HEIGHT / 2))]
        self.__direction = random.choice([s.UP, s.DOWN, s.LEFT, s.RIGHT])
        self.__color = (0, 255, 0)
        # initiate the score to zero
        self.__score = 0

    '''Getter method for first element of position property (snake head)
    '''
    def get_head_position(self):
        return self.__positions[0]

    '''Getter for length property'''
    def get_length(self):
        return self.__length

    '''Getter for positions property'''
    def get_positions(self):
        return self.__positions
    '''Getter for direction'''
    def get_direction(self):
        return self.__direction
    '''Getter for score'''
    def get_score(self):
        return self.__score
    '''Setter for position'''
    '''Trying to change all positions by x for teleport'''
    def set_positions(self, x):

        for i in self.__positions:
            self.__positions[i] = self.__positions[i] + x

    '''Function to add to the length of snake'''
    def add_length(self, integer):
        self.__length += integer

    '''Function to update score'''
    def update_score(self, integer):
        self.__score += integer

    '''Turn snake 
    '''
    def turn(self, point):
        if self.__length > 1 and (point[0] * -1, point[1] * -1) == self.__direction:
            return
        else:
            self.__direction = point

    # this method is currently where Im trying to figure out how to teleport snake(not functioning)
    def hit_portal(self):
        pd_pos = (random.randint(0, s.GRID_WIDTH - 1) * s.GRID_SIZE, random.randint(0, s.GRID_HEIGHT - 1) * s.GRID_SIZE)
        self.__positions[0] = pd_pos

        return pd_pos
    '''Draw the snake object on the surface. Snake is a rect at the moment.
    '''
    def draw(self, surface):
        for pos in self.__positions:
            rect = pg.Rect((pos[0], pos[1]), (s.GRID_SIZE, s.GRID_SIZE))
            pg.draw.rect(surface, self.__color, rect)
            pg.draw.rect(surface, (93, 216, 218), rect, 1)

