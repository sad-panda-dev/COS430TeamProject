'''Class to define Food object'''
import pygame as pg
import random
import setup as s

class Food(object):

    '''Constructor for the Food object'''
    def __init__(self):
        self.position = (0, 0)
        self.color = (204, 0, 0)
        self.random_position()

    ''' Places food randomly upon every generation'''
    def random_position(self):
        self.position = (random.randint(0, s.GRID_WIDTH - 1) * s.GRID_SIZE,
                         random.randint(0, s.GRID_HEIGHT - 1) * s.GRID_SIZE)

    ''' set up to be a red square right now can be changed to be sprite later'''
    def draw(self, surface):
        rect = pg.Rect((self.position[0], self.position[1]), (s.GRID_SIZE, s.GRID_SIZE))
        pg.draw.rect(surface, self.color, rect)
        pg.draw.rect(surface, (93, 216, 228), rect, 1)
