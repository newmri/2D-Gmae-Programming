from MoveFunc import *
from map import Map

class battleProcess:
    def __init__(self):
        open_canvas(1280,720,sync=True)
        battlemap=load_image('Resources\\Map\\Battle.png')
        bmap=Map(battlemap,1280,720,'battle')
    def draw(self):
        self.bmap.draw(self.bmap.x/2,self.bmap.y/2)
        update_canvas()

