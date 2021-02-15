import random
import curses
from typing import NewType
s = curses.initsrc()
curses.curs_set(0)
height, width = s.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.timeout(1)
window.keypad(1)

snk_x = width/4
snk_y = height/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
food = [height/2, width/2]
window.addch(int(food[0]), int(food[1]), curses, ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] i n[0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

new_head = [snake[0][0], snake[0][1]]

if key == curses.KEY_DOWN:
    new_head[0] += 1
if key == curses.KEY_UP:
    new_head[0] -= 1
if key == curses.KEY_LEFT:
    new_head[1] -= 1
if key == curses.KEY_RIGHT:
    new_head[1] += 1

snake.insert(0, new_head)

if
