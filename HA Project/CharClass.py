# define for using instead of number
from pico2d import *
FIRST,SECOND,THIRD,FORTH=0,1,2,3
UP,DOWN,LEFT,RIGHT=0,1,2,3


#              clip_draw(이미지 전체에서x좌표,y좌표, x표현범위,y표현범위,출력x좌표,출력y좌표)
class baseofCharacter:

    # Initialization of the Character
    def __init__(self,skin,type):
        self.skin = skin
        self.skinType = type
        self.ItemList=[0,0]
        self.gold=0
        self.x,y=0

    def update(self):
        update_canvas()

    def draw(self):
         pass

    def drawFirst(self):
         pass


class Monster(baseofCharacter):
    def __init__(self, skin, type):

        self.skillList=[0,0,0,0]
        self.skillCool=[0,0,0,0]
        self.skillDmg=5
        self.myTurn=False
        self.skin=skin
        self.type=type
        self.skillX=0
        self.skillY=0
        self.hp,mp=30,30
        self.dp=0
    def drawFirst(self):
        self.skin.clip_draw(0, 48 * 3, 42 - 12, 48,self.x,self.y)
    def drawBattle(self):
        self.skin.clip_draw(0, 48 * 2, 42 - 12, 48, self.x, self.y)
    def setHitEffect(self,Effect):
        self.hitEffect=[Effect[0],Effect[1],Effect[2],Effect[3],Effect[4],Effect[5],Effect[6],Effect[7]]
    def giveItem(self,other):
        pass

    def giveGold(self,other):
        pass
    def calDamage(self,Dmg):
        self.hp-=(Dmg-self.dp)
    def Attack(self,other):
        pass
    def skillUpdate(self):
        self.frame = (self.frame + 1) % 6
    def setSkill(self, skill):
        self.skill = skill
    def setSkillEfect(self,skill):
        self.skillEffect=skill
    def drawSkillEfect(self,man):
        self.skillX=man.x
        self.skillY=man.y
        for i in range(6):
               clear_canvas()
               self.draw()
               man.drawBattle()
               self.skillEffect[i].draw(man.x,man.y)
               #self.skillUpdate()
               #self.skillX+=self.skillX
               delay(0.05)
               man.update()
        for i in range(7):
            clear_canvas()
            self.draw()
            man.drawBattle()
            man.hitEffect[i].draw(man.x,man.y)
            delay(0.05)
            man.update()

class User(Monster):
    def __init__(self, skin, type):
        self.skin = skin
        self.skinType = type
        self.movePosition=[False,False,False,False]
        self.moveChk=[False,False,False,False]
        self.rotate=FIRST
        self.frame=0
        self.fight=True
        self.fightRun=False
        self.drawDiaChk=True
        self.drawSkillChk=False
        self.skillDmg=10
        self.hp,mp=30,30
        self.dp=5
        self. myTurn=True
    def skillUpdate(self):
        self.frame = (self.frame + 1) % 6
    def setSkill(self, skill):
        self.skill = skill
    def setSkillEfect(self,skill):
        self.skillEffect=skill
    def drawSkill_Box(self,y):
        self.skill.draw(self.x+200,y+100)
    def drawSkillEfect(self,man,map):
        self.skillX=man.x
        self.skillY=man.y
        while self.skillX <map.monster.x:
               clear_canvas()
               map.draw()
               man.drawBattle()
               self.skillEffect.clip_draw(self.frame*42,0,42,30,self.skillX+20,self.skillY)
               self.skillUpdate()
               self.skillX+=self.skillX
               delay(0.05)
               man.update()
        for i in range(7):
            clear_canvas()
            map.draw()
            man.drawBattle()
            map.monster.hitEffect[i].draw(map.monster.x,map.monster.y)
            delay(0.05)
            man.update()
    def setBattleDialog(self,dialog):
        self.dialog=dialog
    def resetBattleDialog(self):
        self.drawDiaChk=False
    def drawBattleDialog(self):
         self.dialog.draw(self.x+200,self.y+100)


    def draw(self):
        if self.skinType == 'Original':
            # Images of UP
            if self.movePosition[UP] == True:
                if self.rotate == FIRST:
                    self.skin.clip_draw(0, 0, 30, 48, self.x, self.y)
                elif self.rotate == SECOND:
                    self.skin.clip_draw(30, 0, 30, 48, self.x, self.y)
                elif self.rotate == THIRD:
                    self.skin.clip_draw(30 * 2, 0, 30, 48, self.x, self.y)
                elif self.rotate == FORTH:
                    self.skin.clip_draw(30 * 3 + 8, 0, 30, 48, self.x, self.y)
                self.rotate += 1
                if self.rotate > FORTH:
                    self.rotate = FIRST
                self.moveChk[UP]=True
            elif (self.movePosition[UP] == False) & (self.moveChk[UP]==True):
                  self.rotate = FIRST
                  self.moveChk[UP]=False

            # Images of DOWN
            if self.movePosition[DOWN]==True:
                if self.rotate == FIRST:
                    self.skin.clip_draw(0, 48*3, 30, 48, self.x, self.y)
                elif self.rotate == SECOND:
                    self.skin.clip_draw(30, 48*3, 30, 48, self.x, self.y)
                elif self.rotate == THIRD:
                    self.skin.clip_draw(30 * 2, 48*3, 30, 48, self.x, self.y)
                elif self.rotate == FORTH:
                    self.skin.clip_draw(30 * 3 + 8, 48*3, 30, 48, self.x, self.y)
                self.rotate += 1
                if self.rotate > FORTH:
                    self.rotate = FIRST
                self.moveChk[DOWN]=True
            elif (self.movePosition[DOWN] == False) & (self.moveChk[DOWN]==True):
                   self.roate=FIRST
                   self.moveChk[DOWN]=False

            # Images of LEFT
            if self.movePosition[LEFT]==True:
                if self.rotate == FIRST:
                    self.skin.clip_draw(0, 48*2, 30, 48, self.x, self.y)
                elif self.rotate == SECOND:
                    self.skin.clip_draw(30, 48*2, 30, 48, self.x, self.y)
                elif self.rotate == THIRD:
                    self.skin.clip_draw(30 * 2, 48*2, 30, 48, self.x, self.y)
                elif self.rotate == FORTH:
                    self.skin.clip_draw(30 * 3 + 8, 48*2, 30, 48, self.x, self.y)
                self.rotate += 1
                if self.rotate > FORTH:
                    self.rotate = FIRST
                self.moveChk[LEFT]=True
            elif (self.movePosition[LEFT] == False) & (self.moveChk[LEFT]==True):
                   self.roate=FIRST
                   self.moveChk[LEFT]=False

            # Images of RIGHT
            if self.movePosition[RIGHT]==True:
                if self.rotate == FIRST:
                    self.skin.clip_draw(0, 48, 30, 48, self.x, self.y)
                elif self.rotate == SECOND:
                    self.skin.clip_draw(30, 48, 30, 48, self.x, self.y)
                elif self.rotate == THIRD:
                    self.skin.clip_draw(30 * 2, 48, 30, 48, self.x, self.y)
                elif self.rotate == FORTH:
                    self.skin.clip_draw(30 * 3 + 8, 48, 30, 48, self.x, self.y)
                self.rotate += 1
                if self.rotate > FORTH:
                    self.rotate = FIRST
                self.moveChk[RIGHT]=True
            elif (self.movePosition[RIGHT] == False) & (self.moveChk[RIGHT]==True):
                   self.roate=FIRST
                   self.moveChk[RIGHT]=False


    def drawFirst(self):
        if self.skinType == 'Original':
            self.skin.clip_draw(0, 48 * 3, 42 - 12, 48, self.x, self.y)
    def drawBattle(self):
        if self.skinType=='Original':
            self.skin.clip_draw(0, 48, 30, 48, self.x, self.y)


class NPC(baseofCharacter):
       pass