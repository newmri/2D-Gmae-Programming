from pico2d import *
class Map:
    def __init__(self,map,x,y,name):
         self.map=map
         self.x=x
         self.y=y
         self.name=name
         self.chk=False
         self.bgm=load_music('Resources\\SoundTrack\\HomeBGM.mp3')
         self.bgm.set_volume(64)
         self.bgm.repeat_play()
    def setMonster(self,monster,dragon,lion):
        self.monster=monster
        self.dragon=dragon
        self.lion=lion
        self.chk=True

    def setBattleMonster(self, monster,type):
        self.monster = monster
        self.type=type
        self.chk = True

    #t
    def draw(self):
         self.map.draw(self.x/2,self.y/2)
         if self.chk ==True:
             if self.name != 'battle':
                self.monster.drawFirst()
                self.dragon.drawFirst()
                self.lion.drawFirst()
             else:

                self.monster.drawBattle()


