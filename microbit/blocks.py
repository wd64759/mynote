import sys
import random
import keyboard

canvas = [[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
bricks = [[1,1],[1,0]], [[1,1],[1,1]], [[1,0],[1,0]]
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
    to_x, to_y = loc; i = 0
    for bl in brick:
       canvas[to_x + i][to_y:to_y + len(bl)] = bl
       i += 1    

def clean_brick(brick, loc):
    to_x, to_y = loc; i = 0
    for bl in brick:
        rev_line = [x^1 for x in bl]
        reg_area = canvas[to_x + i][to_y:to_y + len(bl)]
        up_area = [x[0]&x[1] for x in zip(rev_line, reg_area)]
        canvas[to_x + i][to_y:to_y + len(bl)] = up_area

def set_pixel(x, y, signal):
    print(x, y, signal)

def refresh_line(loc_x):
    for i,y in canvas[loc_x][1:-1]:
        set_pixel(loc_x, i, y)

def hit_check(brick, loc):
    to_x, to_y = loc; i = 0; hit = False
    for bl in brick:
        overlap = canvas[to_x + i][to_y:to_y + len(bl)]
        i += 1; el = 0
        while el < len(bl):
            if overlap[el] + bl[el] > 1:
                hit = True
                break
            el += 1
    return hit

def out_range(brick, loc):
    to_x, to_y = loc
    r_chk = (to_x > 0 and to_x < len(canvas) - len(brick))
    return r_chk if not r_chk else (to_y > 0 and to_y < len(canvas[0]) - len(brick[0]))

def mprint(box):
    for line in box:
        print(line)

def test():
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

            print("clean brick")
            clean_brick(t, (2,0))
            mprint(canvas)

def key_down(x):
    loc_x, loc_y = 0, 0
    if x.event_type == 'down' and x.event_name == 'left':
        loc_y = -1
    if x.event_type == 'down' and x.event_name == 'right':
        loc_y = 1
    if x.event_type == 'down' and x.event_name == 'down':
        loc_x = 1

    return loc_x, loc_y

def main():
    keyboard.hook(key_down)
    keyboard.wait()
    # gameOn = True
    # frameCount = 0
    # while gameOn:
    #     # sleep(50)
    #     print('sleep -- 50')


main()