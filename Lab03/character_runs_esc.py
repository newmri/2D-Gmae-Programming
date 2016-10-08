from pico2d import *

def handle_events():

    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            center_x, center_y = event.x, 599 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 0
frame = 0
while (x < 800 and running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 10, 10, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    handle_events()

close_canvas()

