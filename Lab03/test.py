from pico2d import *
import math
PI = 3.14 / 180

def handle_events():
    global running
    global r
    global center_x
    global center_y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                if(r < 300):
                    r = r + 10
            elif event.key == SDLK_d:
                if(r > 20):
                    r = r - 10
            elif event.key == SDLK_UP:
                center_y += 20
            elif event.key == SDLK_DOWN:
                center_y -= 20
            elif event.key == SDLK_RIGHT:
                center_x += 20
            elif event.key == SDLK_LEFT:
                center_x += 20
        elif event.type == SDL_MOUSEMOTION:
            center_x, center_y = event.x, 599 - event.y

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

running = True
r = 100
angle = 0
center_x, center_y = 400, 300
frame = 0
#hide_cursor()

while (running):
    clear_canvas()
    grass.draw(400, 30)
    x = center_x + (r * math.cos(angle * PI))
    y = center_y + (r * math.sin(angle * PI))
    character.draw(x, y)
    update_canvas()
    angle = angle + 10

    delay(0.05)
    handle_events()
    get_events()

close_canvas()
