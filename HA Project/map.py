class Map:
    def __init__(self,map,x,y,name):
         self.map=map
         self.x=x
         self.y=y
         self.name=name
         self.chk=False
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


