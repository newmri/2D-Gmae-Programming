from CharClass import *
from pico2d import *
from Monster import dist
def handle_events(char):


    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
           if event.key == SDLK_UP:
               char.movePosition[UP]=True
           elif event.key == SDLK_DOWN:
              char.movePosition[DOWN]=True
           elif event.key == SDLK_RIGHT:
              char.movePosition[RIGHT]=True
           elif event.key == SDLK_LEFT:
              char.movePosition[LEFT]=True


        if event.type==SDL_KEYUP:
            if event.key == SDLK_UP:
              char.movePosition[UP]=False
            elif event.key == SDLK_DOWN:
              char.movePosition[DOWN]=False
            elif event.key == SDLK_RIGHT:
              char.movePosition[RIGHT]=False
            elif event.key == SDLK_LEFT:
              char.movePosition[LEFT]=False


def run(chk,map,man):

    if chk == 'run' and map.name == 'house':
        man.x = map.x/2
        man.y = map.y/2
        man.drawFirst()
        man.update()
        while (True):
            print(man.x, man.y)

            handle_events(man)
            get_events()
            if man.x>=317.5 and man.y<=183.5 and man.y>=158.5:
                close_canvas()
                return 'outhouse',man
            if man.movePosition[UP]:
                clear_canvas()
                map.draw()
                man.y += 5
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[DOWN]:
                man.y -= 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[RIGHT]:
                man.x += 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[LEFT]:
                man.x -= 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)


    elif chk == 'run' and map.name == 'outofhouse':
        man.x = 654
        man.y = 284.5
        man.movePosition=[False,False,False,False]
        skin=load_image('Resources\\Monster\\rocket.png')
        rocket=Monster(skin,'Rocket')
        map.setMonster(rocket)
        map.monster.x=map.x/2
        map.monster.y=map.y/2
        map.draw()
        map.monster.drawFirst()
        man.drawFirst()
        man.update()
        while (True):          # y 300 700 x 469~534
            #print(man.x, man.y)
            if map.chk == True:
                if 25>= dist(man, map.monster):
                    clear_canvas()
                    return 'battle',man
            handle_events(man)
            get_events()
            if man.x>=469 and man.x<=534 and man.y>=700:
                return 'fight'
            if man.x>=654 and man.y>=300:
                close_canvas()
                return 'inhouse',man
            if man.movePosition[UP]:
                clear_canvas()
                map.draw()
                man.y += 5
                man.draw()
                man.update()
                delay(0.1)

            if man.movePosition[DOWN]:
                man.y -= 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.1)

            if man.movePosition[RIGHT]:
                man.x += 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.1)

            if man.movePosition[LEFT]:
                man.x -= 5
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.1)
        return 'outofhouse'




        
        
        
    


    




 












