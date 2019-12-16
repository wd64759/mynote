import sys
import random

canvas = [[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
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

def move(brick, loc, mov):
    to_x, to_y = loc
    to_x = to_x + mov
    to_y = to_y + 1 if mov == 0 else to_y

    canvas[to_x][to_y]

def mov_brick(brick, loc):
    to_x, to_y = loc; i = 0; hit = False
    for bl in brick:
        overlap = canvas[to_x + i][to_y:to_y + len(bl)]
        el = 0
        while el < len(bl):
            if overlap[el] + bl[el] > 1:
                hit = True
                break
    return hit

def upd_canvas(brick, loc):
    to_x, to_y = loc; i = 0
    for bl in brick:
        canvas[to_x + i][to_y:to_y + len(bl)] = bl

def clean_brick(brick, loc):
    to_x, to_y = loc

def redraw():
    pass
    # display.set_pixel(x, y, brick[0])
    # display.set_pixel(x, y + 1, brick[1])
    # display.set_pixel(x + 1, y, brick[2])
    # display.set_pixel(x + 1, y + 1, brick[3])

def main():
    chosen = rotate(bricks[rnd_p], rnd_r)
