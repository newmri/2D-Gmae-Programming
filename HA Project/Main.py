from MoveFunc import run
from CharClass import *
from BackGround import setBack
from map import Map

setBack()
open_canvas(375, 397,sync=True)
house=load_image('Resources\\Map\\MansHouse.png')
map=Map(house,375,397,'house')
map.draw()
skin=load_image('Resources\\MainCharacter\\Original.png')
man=User(skin,'Original')
retval,man=run('run',map,man)
while(True):
    if retval=='inhouse':
        open_canvas(375, 397,sync=True)
        house = load_image('Resources\\Map\\MansHouse.png')
        map = Map(house, 375, 397, 'house')
        map.draw()
        update_canvas()
        man.skin = load_image('Resources\\MainCharacter\\Original.png')
        man.skinType = 'Original'
        retval,man = run('run', map, man)
    elif retval=='outhouse':
        open_canvas(1008, 689,sync=True)
        outofhouse=load_image('Resources\\Map\\OutOfHouse.png')
        map=Map(outofhouse,1008,689,'outofhouse')
        man.skin=load_image('Resources\\MainCharacter\\Original.png')
        man.skinType='Original'
        retval,man=run('run',map,man)
    elif retval=='battle':
        bmap=load_image('Resources\\Map\\Battle.png')
        map=Map(bmap,1008,689,'battle')
        map.draw()
        man.update()
        delay(6)