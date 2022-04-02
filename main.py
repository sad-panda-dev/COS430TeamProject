'''
Things to do:
1) Figure out the best way to handle a teleport. Based on what is there now it throws
error or does nothing at all when trying to manipulate snake body.

2) Create Start Screen, when game is initiated thought it should just display a simple screen
with the name of the game and say press "s" to start or something like that, if we decide to go with
a button that works too, just more work. (done!)

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

import sys
import Snake as sn
import Food as fd
import Portal as pd
import pygame as pg
import setup as s

    
# function to draw the grid after refactoring
def draw_grid(surface):

    for y in range(0, int(s.GRID_HEIGHT)):
        for x in range(0, int(s.GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pg.Rect((x*s.GRID_SIZE, y*s.GRID_SIZE),
                            (s.GRID_SIZE, s.GRID_SIZE))
                pg.draw.rect(surface, (232, 244, 248), r)
                    # 93, 216, 228), r)
            else:
                r = pg.Rect((x*s.GRID_SIZE, y*s.GRID_SIZE),
                             (s.GRID_SIZE, s.GRID_SIZE))
                pg.draw.rect(surface, (232, 244, 248), r)
                             # (196, 249, 255), rr)

''' Defines text rectangle and centers it on the screen. Offset argument specifies offset from the horizontal center
and is convenient when multiple lines of text are written to the screen
    :param screen: the screen object 
    :param text: string to be written to screen
    :param font_size: integer size of font
    :param color: color in RGB format
    :param offset: integer horizontal offset from center 
    '''
def message_to_screen(screen, text, font_size, color, offset = 0):
    font = pg.font.SysFont("arialblack", font_size)
    screen_text = font.render(text, True, color)
    text_rect = screen_text.get_rect()
    text_rect.center = (s.SCREEN_HEIGHT // 2 , s.SCREEN_WIDTH // 2 -offset)
    screen.blit(screen_text, text_rect)
    pg.display.update()

'''Defines the starting screen: sets the color of background, and text to be written on screen. Calls 
message_to_screen() to write text. Listens for user input until 'S' is pressed.
'''
def start_menu():
    screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT), 0, 32)
    screen.fill((255,255,255))

    text = 'SNAKE TELEPORTER'
    text2 = 'PRESS \"S\" TO START GAME'
    message_to_screen(screen, text ,62, (50,205, 50),300)
    snake_image = pg.image.load('SnakeImage.jpeg').convert_alpha()
    # r = snake_image.get_rect()
    # print(r)
    # print(pg.font.get_fonts())
    w = 2396
    h = 3316
    img = pg.transform.scale(snake_image, (w/5,h/5))
    screen.blit(img, (170,150))
    message_to_screen(screen, text2 ,20, (50,205, 50), -350)
    start_press = False
    while not start_press:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    start_press = True
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

''' Listens for key events and runs the game according to pressed keys.
Navigates the movement of snake object when up,down,left or right keys are pressed. Closes the window when 'X' 
in the right corner of the window is pressed or when user hits Escape key. Pauses game if user hits Space key. 
'''
def handle_keys(snake,screen, clock):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.turn(s.UP)
            elif event.key == pg.K_DOWN:
                snake.turn(s.DOWN)
            elif event.key == pg.K_LEFT:
                snake.turn(s.LEFT)
            elif event.key == pg.K_RIGHT:
                snake.turn(s.RIGHT)
            elif event.key == pg.K_SPACE:
                pause(screen, clock)
            elif event.key == pg.K_ESCAPE:
                 pg.quit()
                 sys.exit()

''' Pauses the game. Displays text on the screen prompting user to hit Space to continue.
    :param screen: the screen object
    :param clock: clock for regulating frames for game
'''
def pause(screen, clock):
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    paused = False
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        screen.fill((255, 255, 255))
        text = 'PAUSED'
        text2 = 'Press Space to continue'
        message_to_screen(screen, text2, 20, (50, 205, 50), 60)
        message_to_screen(screen, text ,62, (50,205,50))
        clock.tick(5)


'''Notifies that the game has ended. Displays the score and prompts user to play again. Listens for user input and
if user hits 'S' key, then starts another game.
    :param screen: the screen object
    :param clock: clock for the game
    :param score: integer user score 
'''
def game_over(screen, clock, score):
    screen.fill((255, 255, 255))
    text = 'GAME OVER'
    text2 = 'YOUR SCORE IS '
    text3 = str(score)
    text4 = 'PRESS "S" TO PLAY AGAIN'
    message_to_screen(screen, text, 62, (50, 205, 50))
    message_to_screen(screen, text2, 20, (50, 205, 50), -70)
    message_to_screen(screen, text3, 32, (50, 205, 50), -100)
    message_to_screen(screen, text4, 20, (50, 205, 50), -130)
    clock.tick(5)
    play_again = False
    while not play_again:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    play_again = True
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
    run()
'''Gets the position of the Snake object parameter, and checks if snake colided with itself. If this is the case, 
calls game_over(), othervise moves the snake object one square ahead.
    :param screen: screen object
    :param clock: clock for the game
    :param snake: snake object
'''
def move_snake(screen, clock, snake):

    curr = snake.get_head_position()
    x, y = snake.get_direction()
    new = (((curr[0] + (x * s.GRID_SIZE)) % s.SCREEN_WIDTH),
           (curr[1] + (y * s.GRID_SIZE)) % s.SCREEN_HEIGHT)

    if len(snake.get_positions()) > 2 and new in snake.get_positions()[2:]:
        game_over(screen, clock, snake.get_score())
    else:
        snake.get_positions().insert(0, new)
        if (len(snake.get_positions()) > snake.get_length()):
            snake.get_positions().pop()

'''Runs the game. Defines the clock, sets the screen, and defines snake, food and portal objects. Runs the while 
loop until snake collides with its tail or user exits the screen.
'''
def run():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT), 0, 32)

    surface = pg.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    my_font = pg.font.SysFont("arialblack", 30)

    snake = sn.Snake()
    food = fd.Food()
    portal = pd.Portal()
    # This is the main loop for game
    while True:
        # rate at which the game refreshes
        clock.tick(9)
        # handle keydown events
        handle_keys(snake, screen, clock)
        draw_grid(surface)
        move_snake(screen, clock, snake)

        if snake.get_head_position() == food.get_position():
            snake.add_length(1)
            snake.update_score(1)
            food.random_position()

        if snake.get_head_position() == portal.get_position():
            snake.hit_portal()

        snake.draw(surface)
        food.draw(surface)
        # portal.draw(surface)
        screen.blit(surface, (0, 0))
        text = my_font.render("Score {0}".format(snake.get_score()), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pg.display.update()


def main():
    pg.init()
    start_menu()
    run()


main()
