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
        #man.update()
        update_canvas()
        while (True):


            handle_events(man)
            get_events()
            if man.x>=317.5 and man.y<=183.5 and man.y>=158.5:
                close_canvas()
                return 'outhouse',man
            if man.movePosition[UP]:
                clear_canvas()
                map.draw()
                #man.y += 5
                man.y += man.distance
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[DOWN]:
                #man.y -= 5
                man.y -= man.distance
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[RIGHT]:
                #man.x += 5
                man.x+=man.distance
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[LEFT]:
                #man.x -= 5
                man.x-=man.distance
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
        skin2=load_image('Resources\\Monster\\Dragon.png')
        skin3=load_image('Resources\\Monster\\Lion.png')
        rocket=Monster(skin,'Rocket')
        dragon=Monster(skin2,'Dragon')
        lion=Monster(skin3,'Lion')
        map.setMonster(rocket,dragon,lion)
        map.monster.x=map.x/2
        map.monster.y=map.y/2
        map.dragon.x=map.x/2-150
        map.dragon.y = map.y / 2 - 30
        map.lion.x=map.x/2-70
        map.lion.y=map.y/2+40
        map.draw()
        map.monster.drawFirst()
        map.dragon.drawFirst()
        man.drawFirst()
        man.update()
        while (True):          # y 300 700 x 469~534

            if map.chk == True:
                if 25>= dist(man, map.monster):
                    clear_canvas()
                    return 'battle', man,'Rocket'
                elif 50>= dist(man, map.dragon):
                    clear_canvas()
                    return 'battle', man,'Dragon'
                elif 25>=dist(man,map.lion):
                    clear_canvas()
                    return 'battle',man,'Lion'

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
                #man.y += 5
                man.y += man.distance
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[DOWN]:
                #man.y -= 5
                man.y -= man.distance
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[RIGHT]:
               # man.x += 5
                man.x += man.distance
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)

            if man.movePosition[LEFT]:
                #man.x -= 5
                man.x -= man.distance
                clear_canvas()
                map.draw()
                man.draw()
                man.update()
                delay(0.05)
    return 'outofhouse'