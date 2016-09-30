from pico2d import *
import math
def handle_events():
    global r
    global running
    global x, y
    global pointx,pointy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            pointx, pointy = event.x, 599 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key ==SDLK_a:
                  r=min(r+20,300)
            elif event.key==SDLK_d:
                  r=max(r-10,20)
            elif event.key==SDLK_UP:
                  pointy=min(pointy+20,600)
            elif event.key==SDLK_DOWN:
                  pointy=max(pointy-20,0)
            elif event.key==SDLK_RIGHT:
                  pointx=min(pointx+20,600)
            elif event.key == SDLK_LEFT:
                pointx = max(pointx -20,0)


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True
x, y = 100, 100
pointx=400
pointy=300
frame = 0
degree=0
r=100
while (running):

    clear_canvas()
    grass.draw(400, 30)
    degree=(degree) %360
    x=pointx+r*math.cos(degree* (2*math.pi/360))
    y=pointy+r*math.sin(degree* (2*math.pi/360))
    character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    if degree!= 359:
        degree+=1
    else:
        degree=0


    handle_events()

close_canvas()




