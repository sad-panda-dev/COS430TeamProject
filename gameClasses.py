import pygame as pg
import sys
import random
import setup as s


# SNAKE OBJECT #
class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((s.SCREEN_WIDTH / 2), (s.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([s.UP, s.DOWN, s.LEFT, s.RIGHT])
        # just set up to be a green square for now, can add sprite to change that
        #self.color = (0, 230, 0)
        #changed to black
        self.color = (0, 0, 0)
        # initiate the score to zero
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        curr = self.get_head_position()
        x, y = self.direction
        new = (((curr[0] + (x * s.GRID_SIZE)) % s.SCREEN_WIDTH),
               (curr[1] + (y * s.GRID_SIZE)) % s.SCREEN_HEIGHT)
        # this detects if the snake has run into itself causing game over
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.game_over
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # this method is currently where Im trying to figure out how to teleport snake(not functioning)
    def hit_portal(self):
        new_position = self.get_head_position()
        # position_variant = random.randint(1, 10)
        # for position in self.positions:
        #     position = position * position_variant
        return new_position

    def game_over(self):
        pg.quit()

    def draw(self, surface):
        for pos in self.positions:
            rect = pg.Rect((pos[0], pos[1]), (s.GRID_SIZE, s.GRID_SIZE))
            pg.draw.rect(surface, self.color, rect)
            pg.draw.rect(surface, (93, 216, 218), rect, 1)

    # KEY EVENT HANDLING #
    def handle_keys(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.turn(s.UP)
                elif event.key == pg.K_DOWN:
                    self.turn(s.DOWN)
                elif event.key == pg.K_LEFT:
                    self.turn(s.LEFT)
                elif event.key == pg.K_RIGHT:
                    self.turn(s.RIGHT)
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()


# FOOD OBJECT #
class Food(object):

    # Constructor
    def __init__(self):
        self.position = (0, 0)
        self.color = (204, 0, 0)
        self.random_position()

    # Places food randomly upon every generation
    def random_position(self):
        self.position = (random.randint(0, s.GRID_WIDTH - 1) * s.GRID_SIZE,
                         random.randint(0, s.GRID_HEIGHT - 1) * s.GRID_SIZE)

    # set up to be a red square right now can be changed to be sprite later
    def draw(self, surface):
        rect = pg.Rect((self.position[0], self.position[1]), (s.GRID_SIZE, s.GRID_SIZE))
        pg.draw.rect(surface, self.color, rect)
        pg.draw.rect(surface, (93, 216, 228), rect, 1)


# PORTAL OBJECT #
class Portal(object):

    # Constructor
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 128, 255)
        self.random_position()

    # Places teleporter randomly upon every generation
    def random_position(self):
        self.position = (random.randint(0, s.GRID_WIDTH - 1) * s.GRID_SIZE,
                         random.randint(0, s.GRID_HEIGHT - 1) * s.GRID_SIZE)

    # Set up to be a blue square right now can be changed to be a sprite later
    def draw(self, surface):
        rect = pg.Rect((self.position[0], self.position[1]), (s.GRID_SIZE, s.GRID_SIZE))
        pg.draw.rect(surface, self.color, rect)
        pg.draw.rect(surface, (93, 216, 228), rect, 1)