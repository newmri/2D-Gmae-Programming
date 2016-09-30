from pico2d import *

def handle_events():
    global running
    global pointX,pointY
    global radius
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_a:
                if radius>=300:
                    radius=radius
                else:
                    radius+=30
            elif event.key==SDLK_d:
                if radius <= 30:
                    radius = radius
                else:
                    radius -= 30
            elif event.key==SDLK_RIGHT:
                if pointX<=800:
                    pointX+=30
            elif event.key==SDLK_LEFT:
                if pointX>=0:
                    pointX-=30
            elif event.key==SDLK_UP:
                if pointY<=600:
                    pointY+=30
            elif event.key == SDLK_DOWN:
                if pointY>=0:
                    pointY-=30
            elif event.key==SDLK_ESCAPE:
                running=False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            pointX,pointY=event.x,600-event.y


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
radius=100
degree=15
pointX=400
pointY=300
x=pointX+radius*math.cos(degree)
y=pointY+radius*math.sin(degree)
frame = 0
while (running):
    for idx in range(0,24):
          clear_canvas()
          grass.draw(400, 30)
          character.clip_draw(frame * 100, 0, 100, 100,x,y)
          update_canvas()
          frame = (frame + 1) % 8
          x = pointX + radius * math.cos(degree)
          y = pointY + radius * math.sin(degree)
          degree+=15
          delay(0.2)
          handle_events()

close_canvas()

