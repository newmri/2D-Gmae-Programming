class Map:
    def __init__(self,map,x,y,name):
         self.map=map
         self.x=x
         self.y=y
         self.name=name
         self.chk=False
    def setMonster(self,monster):
        self.monster=monster
        self.chk=True

    def draw(self):
         self.map.draw(self.x/2,self.y/2)
         if self.chk ==True:
             if self.name != 'battle':
                self.monster.drawFirst()
             else:
                 self.monster.drawBattle()

