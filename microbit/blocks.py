import sys
import random

bricks = [[9,9,9,0], [9,9,9,9], [9,0,9,0]]
rnd_p = random.randint(0, len(bricks) - 1)
rnd_r = random.randint(0, 3)

def to_brick(b):
    return [b[0], b[3], b[1], b[2]]

def from_brick(b):
    return [b[0], b[2], b[3], b[1]]

def rotate(brick, times):
    times = times%4
    brick = from_brick(brick)
    t = brick[-times:]
    t.extend(brick[0:-times])
    return to_brick(t)

chosen = rotate(bricks[rnd_p], rnd_r)

def show(brick, offset):
    x, y = offset
    # display.set_pixel(x, y, brick[0])
    # display.set_pixel(x, y + 1, brick[1])
    # display.set_pixel(x + 1, y, brick[2])
    # display.set_pixel(x + 1, y + 1, brick[3])