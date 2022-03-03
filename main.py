'''
Things to do:
1) Figure out the best way to handle a teleport. Based on what is there now it throws
error or does nothing at all when trying to manipulate snake body.
2) Create Start Screen, when game is initiated thought it should just display a simple screen
with the name of the game and say press "s" to start or something like that, if we decide to go with
a button that works too, just more work.
3) Game over Screen, when game ends it just stops with the last image of the snake and how it has collided
with itself. Thought that this is a good background to just have the words GAME OVER transposed on top of.
4) Given enough time find and implement 4 sprites, one for snake head, one for snake body, one for food
and one for teleporter. This is cosmetic and should probably be focused on last.

All of these except for the teleporter are merely suggestions and are in no way finalized, the teleporter
is what was specified by the customer, also given the fact that this is supposed to be all that the customer
has asked for we could just use this version of the game for the first itteration and just work on
implementing the items above for the next iterations and scrap any of my suggestions about what we might
want to achieve in further itterations. Again this is all things to discuss.
'''
from gameClasses import Snake, Food, Portal
import pygame as pg
import setup as s


# function to draw the grid
def draw_grid(surface):
    for y in range(0, int(s.GRID_HEIGHT)):
        for x in range(0, int(s.GRID_WIDTH)):
            rectangle = pg.Rect((x * s.GRID_SIZE, y * s.GRID_SIZE), (s.GRID_SIZE, s.GRID_SIZE))
            pg.draw.rect(surface, (196, 249, 255), rectangle)


def main_game_loop():
    # from pygame init to drawgrid() is all boilerplate for pygame environment
    pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT), 0, 32)

    surface = pg.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    my_font = pg.font.SysFont("comicsansms", 30)

    snake = Snake()
    food = Food()
    portal = Portal()

    # This is the main loop for game
    while True:
        # rate at which the game refreshes
        clock.tick(9)
        # handle keydown events
        snake.handle_keys()

        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.random_position()
        if snake.get_head_position() == portal.position:
            snake.hit_portal()
        snake.draw(surface)
        food.draw(surface)
        portal.draw(surface)
        screen.blit(surface, (0, 0))
        text = my_font.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pg.display.update()


main_game_loop()

