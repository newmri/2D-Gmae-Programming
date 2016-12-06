from MoveFunc import run
from CharClass import *
from BackGround import setBack
from map import Map
from Battle import battle

setBack()
open_canvas(375, 397)
house=load_image('Resources\\Map\\MansHouse.png')
map=Map(house,375,397,'house')
map.draw()
skin=load_image('Resources\\MainCharacter\\Original.png')
man=User(skin,'Original')
retval,man=run('run',map,man)
Run=True
while(Run):
    if retval=='inhouse':
        open_canvas(375, 397)
        house = load_image('Resources\\Map\\MansHouse.png')
        map = Map(house, 375, 397, 'house')
        map.draw()
        update_canvas()
        man.skin = load_image('Resources\\MainCharacter\\Original.png')
        man.skinType = 'Original'
        retval,man = run('run', map, man)
    elif retval=='outhouse':
        open_canvas(1008, 689)
        outofhouse=load_image('Resources\\Map\\OutOfHouse.png')
        map=Map(outofhouse,1008,689,'outofhouse')
        map.bgm=load_music('Resources\\SoundTrack\\BGM.mp3')
        map.bgm.set_volume(64)
        map.bgm.repeat_play()
        if man.won=='Rocket':
            man.skin=load_image('Resources\\Monster\\rocket.png')
            man.skinType='Rocket'
        elif man.won=='Dragon':
            man.skin=load_image('Resources\\Monster\\Dragon.png')
            man.skinType='Dragon'
        elif man.won=='Lion':
            man.skin = load_image('Resources\\Monster\\Lion.png')
            man.skinType = 'Lion'
        else:
            man.skin=load_image('Resources\\MainCharacter\\Original.png')
            man.skinType='Original'
        retval,man,type=run('run',map,man)
    elif retval=='battle':
        bmap=load_image('Resources\\Map\\Battle.png')
        map=Map(bmap,1008,689,'battle')
        if man.won=='Rocket':
            man.skin=load_image('Resources\\Monster\\rocket.png')
            man.skinType='Rocket'
        elif man.won=='Dragon':
            man.skin=load_image('Resources\\Monster\\Dragon.png')
            man.skinType='Dragon'
        elif man.won=='Lion':
            man.skin=load_image('Resources\\Monster\\Lion.png')
            man.skinType='Lion'
        else:
            man.skin=load_image('Resources\\MainCharacter\\Original.png')
            man.skinType='Original'
        retval,man = battle(man,map,type)
    elif retval=='quit':
        Run=False
