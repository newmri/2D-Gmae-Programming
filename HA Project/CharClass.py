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
        self.hp,mp=100
        self.dp=5

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
        self.skillDamage=[0,0,0,0]
        self.myTurn=False
        self.skin=skin
        self.type=type
    def drawFirst(self):
        self.skin.clip_draw(0, 48 * 3, 42 - 12, 48,self.x,self.y)
    def drawBattle(self):
        self.skin.clip_draw(0, 48 * 2, 42 - 12, 48, self.x, self.y)

    def giveItem(self,other):
        pass

    def giveGold(self,other):
        pass

    def Attack(self,other):
        pass

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
    def skillUpdate(self):
        self.frame = (self.frame + 1) % 6
    def setSkill(self, skill):
        self.skill = skill
    def drawSkill_Box(self,y):
        self.skill.draw(self.x+200,y+100)
    def drawSkillEfect(self,x):
        self.skill.clip_draw(self.frame*42,0,42,30,self.x,self.y)
        self.x+=self.x
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