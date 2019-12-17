import sys
import random

canvas = [[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
bricks = [[9,9],[9,0]], [[9,9],[9,9]], [[9,0],[9,0]]
rnd_p = random.randint(0, len(bricks) - 1)
rnd_r = random.randint(0, 3)

def to_brick(b):
    return [[b[0], b[3]], [b[1], b[2]]]

def from_brick(b):
    return [b[0][0], b[1][0], b[1][1], b[0][1]]

def rotate(brick, times):
    times = times%4
    brick = from_brick(brick)
    t = brick[-times:]
    t.extend(brick[0:-times])
    return to_brick(t)

def mov_brick(brick, loc):    
    to_x, to_y = loc; i = 0;
    for bl in brick:
       canvas[to_x + i][to_y:to_y + len(bl)] = bl
       i += 1    

def hit_check(brick, loc):
    to_x, to_y = loc; i = 0; hit = False
    for bl in brick:
        overlap = canvas[to_x + i][to_y:to_y + len(bl)]
        i += 1; el = 0
        while el < len(bl):
            if overlap[el] + bl[el] > 9:
                hit = True
                break
            el += 1
    return hit

def out_range(brick, loc):
    to_x, to_y = loc
    r_chk = (to_x > 0 and to_x < len(canvas) - len(brick))
    return r_chk if not r_chk else (to_y > 0 and to_y < len(canvas[0]) - len(brick[0]))

def clean_brick(brick, loc):
    to_x, to_y = loc; i = 0; hit = False
    for bl in brick:
        loc_x, loc_y = to_x + i + 1, to_y + 1 
        overlap = canvas[loc_x][loc_y:loc_y + len(bl)]
        el = 0
        while el < len(bl):
            if bl[el] > 1:
                canvas[loc_x][loc_y + el] = 0

# def upd_canvas(brick, loc):
#     to_x, to_y = loc; i = 0
#     for bl in brick:
#         canvas[to_x + i][to_y:to_y + len(bl)] = bl



def redraw():
    pass
    # display.set_pixel(x, y, brick[0])
    # display.set_pixel(x, y + 1, brick[1])
    # display.set_pixel(x + 1, y, brick[2])
    # display.set_pixel(x + 1, y + 1, brick[3])

def mprint(box):
    for line in box:
        print(line)

def main():
    # chosen = rotate(bricks[rnd_p], rnd_r)
    mprint(canvas)
    b = bricks[2]
    mprint(b)
    print("from brick:")
    print(from_brick(b))
    print("-------")
    mprint(to_brick((from_brick(b))))
    print("rotate brick:")
    t = rotate(b, 3)
    mprint(t)

    loc = (2,1)
    r_flag = out_range(t, loc)
    print("range chk - " + str(r_flag))
    if r_flag:
        h_flag = hit_check(t, loc)
        print("hit check - " + str(h_flag))
        if not h_flag:
            print("move brick")
            mov_brick(t, loc)
            mprint(canvas)

main()