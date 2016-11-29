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
        self.name=0
        self.skillList=[0,0,0,0]
        self.skillCool=[0,0,0,0]
        self.skillDmg=5
        self.myTurn=False
        self.skin=skin
        self.type=type
        self.skillX=0
        self.skillY=0
        self.hp,mp=20,30
        self.battle=0
        self.dp=0
        self.skillSound=None
    def drawFirst(self):
        if self.type=='Rocket':
            self.skin.clip_draw(0, 48 * 3, 42 - 12, 48,self.x,self.y)
        elif self.type=='Dragon':
            self.skin.clip_draw(0, 96, 96, 96, self.x, self.y)
        elif self.type=='Lion':
            self.skin.clip_draw(0, 75*2+5, 60, 70, self.x, self.y)
    def drawBattle(self):
        if self.type=='Rocket':
            self.skin.clip_draw(0, 48 * 2, 42 - 12, 48, self.x, self.y)
        elif self.type=='Dragon':
            self.skin.clip_draw(0, 96*2, 96, 96, self.x, self.y)
        elif self.type=='Lion':
            self.skin.clip_draw(0, 100, 55, 70, self.x, self.y)
        font = load_font('ENCR10B.TTF', 30)
        font.draw(self.x-100, self.y - 50, 'HP: %d' % self.hp)
    def setHitEffect(self,Effect):
        self.hitEffect=[Effect[0],Effect[1],Effect[2],Effect[3],Effect[4],Effect[5],Effect[6],Effect[7]]
    def giveItem(self,other):
        pass

    def giveGold(self,other):
        pass

    def calDamage(self, Dmg):
        self.hp -= (Dmg - self.dp)


    def Attack(self,other):
        pass
    def skillUpdate(self):
        self.frame = (self.frame + 1) % 6
    def setSkill(self, skill):
        self.skill = skill
    def setSkillEfect(self,skill):
        self.skillEffect=skill
    def drawSkillEfect(self,man,map):
        self.skillX=man.x
        self.skillY=man.y
        if self.type=='Rocket':
            if self.skillSound==None:
                self.skillSound = load_music('Resources\\SoundTrack\\Thunder.mp3')
                self.skillSound.set_volume(128)
            map.bgm.pause()
            self.skillSound.play()
            clear_canvas()
            map.draw()
            self.draw()
            man.drawBattle()
            man.update()
            delay(2)
            for i in range(6):
                   clear_canvas()
                   map.draw()
                   self.draw()
                   man.drawBattle()
                   self.skillEffect[i].draw(man.x,man.y)
                   #self.skillUpdate()
                   #self.skillX+=self.skillX
                   delay(0.05)
                   man.update()

            #self.skillSound.pause()


        elif self.type=='Dragon':
            if self.skillSound==None:
                self.skillSound = load_music('Resources\\SoundTrack\\Blizzard.mp3')
                self.skillSound.set_volume(128)
            map.bgm.pause()
            self.skillSound.play()
            clear_canvas()
            map.draw()
            self.draw()
            man.drawBattle()
            man.update()
            delay(4.5)
            for i in range(19):
                clear_canvas()
                map.draw()
                self.draw()
                man.drawBattle()
                self.skillEffect[i].draw(man.x, man.y)
                # self.skillUpdate()
                # self.skillX+=self.skillX
                delay(0.05)
                man.update()
        elif self.type=='Lion':
            if self.skillSound==None:
                self.skillSound = load_music('Resources\\SoundTrack\\Tornado.mp3')
                self.skillSound.set_volume(128)
            map.bgm.pause()
            self.skillSound.play()
            clear_canvas()
            map.draw()
            self.draw()
            man.drawBattle()
            man.update()
            delay(3)
            for i in range(6):
                   clear_canvas()
                   map.draw()
                   self.draw()
                   man.drawBattle()
                   self.skillEffect[i].draw(man.x,man.y)
                   #self.skillUpdate()
                   #self.skillX+=self.skillX
                   delay(0.05)
                   man.update()

        for i in range(7):
            clear_canvas()
            map.draw()
            self.draw()
            man.drawBattle()
            man.hitEffect[i].draw(man.x,man.y)
            delay(0.05)
            man.update()
        man.calDamage(self.skillDmg)
        print(man.hp)
        clear_canvas()
        map.draw()
        man.drawBattle()
        man.update()
        self.skillSound.stop()
        map.bgm = load_music('Resources\\SoundTrack\\BattleBGM.mp3')
        map.bgm.set_volume(64)
        map.bgm.repeat_play()


class User(Monster):
    PIXEL_PER_METER = (10/0.3)  # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    def __init__(self, skin, type):
        self.won=0
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
        self.hp,mp=100,30
        self.dp=0
        self. myTurn=True
        self.total_frames=0.0
        self.distance=0
        self.frame2=0
        self.skillSound=None
    def skillUpdate(self):
        self.frame = (self.frame + 1) % 6
    def setSkill(self, skill):
        self.skill = skill
    def setSkillEfect(self,skill):
        self.skillEffect=skill
    def drawSkill_Box(self,y):
        self.skill.draw(self.x+200,y+100)
    def drawSkillEfect(self,man,map):
        if self.skinType=='Original':
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
        elif self.skinType=='Rocket':
                self.skillX = map.monster.x
                self.skillY = map.monster.y
                self.skillSound = load_music('Resources\\SoundTrack\\Thunder.mp3')
                self.skillSound.set_volume(128)
                map.bgm.pause()
                self.skillSound.play()
                clear_canvas()
                map.draw()
                man.drawBattle()
                man.update()
                delay(2)
                for i in range(6):
                    clear_canvas()
                    map.draw()
                    man.drawBattle()
                    self.skillEffect[i].draw(map.monster.x,map.monster.y)
                    # self.skillUpdate()
                    # self.skillX+=self.skillX
                    delay(0.05)
                    man.update()
        elif self.skinType=='Dragon':
                self.skillX = map.monster.x
                self.skillY = map.monster.y
                self.skillSound = load_music('Resources\\SoundTrack\\Blizzard.mp3')
                self.skillSound.set_volume(128)
                map.bgm.pause()
                self.skillSound.play()
                delay(4.5)
                for i in range(19):
                    clear_canvas()
                    map.draw()
                    man.drawBattle()
                    self.skillEffect[i].draw(map.monster.x,map.monster.y)
                    # self.skillUpdate()
                    # self.skillX+=self.skillX
                    delay(0.05)
                    man.update()
        elif self.skinType=='Lion':
            self.skillX = map.monster.x
            self.skillY = map.monster.y
            self.skillSound = load_music('Resources\\SoundTrack\\Tornado.mp3')
            self.skillSound.set_volume(128)
            map.bgm.pause()
            self.skillSound.play()
            delay(3)
            for i in range(6):
                clear_canvas()
                map.draw()
                man.drawBattle()
                self.skillEffect[i].draw(map.monster.x, map.monster.y)
                # self.skillUpdate()
                # self.skillX+=self.skillX
                delay(0.05)
                man.update()

        for i in range(7):
            clear_canvas()
            map.draw()
            man.drawBattle()
            map.monster.hitEffect[i].draw(map.monster.x,map.monster.y)
            delay(0.05)
            man.update()
        if(self.skinType!='Original'):
            self.skillSound.stop()
        map.bgm = load_music('Resources\\SoundTrack\\BattleBGM.mp3')
        map.bgm.set_volume(64)
        map.bgm.repeat_play()
    def setBattleDialog(self,dialog):
        self.dialog=dialog
    def resetBattleDialog(self):
        self.drawDiaChk=False
    def drawBattleDialog(self):
         self.dialog.draw(self.x+200,self.y+100)

    def calDamage(self, Dmg):
        self.hp -= (Dmg - self.dp)


    def draw(self):
        if self.skinType == 'Original':
            self.frame=(self.frame+1)%4
            if self.movePosition[LEFT]==True:
                self.skin.clip_draw(self.frame*30,48*2,30,48,self.x,self.y)
            elif self.movePosition[RIGHT]==True:
                self.skin.clip_draw(self.frame * 30, 48, 30, 48, self.x, self.y)
            elif self.movePosition[UP] == True:
                self.skin.clip_draw(self.frame * 30+8, 0, 30, 48, self.x, self.y)
            elif  self.movePosition[DOWN] == True:
                self.skin.clip_draw(self.frame * 30+8, 48*3, 30, 48, self.x, self.y)
        elif self.skinType == 'Rocket':
            self.frame = (self.frame + 1) % 4
            # Images of UP
            if self.movePosition[UP] == True:
                self.skin.clip_draw(self.frame*32, 0, 30, 48, self.x, self.y)
            # Images of DOWN
            elif self.movePosition[DOWN] == True:
                self.skin.clip_draw(self.frame*32, 48 * 3, 30, 48, self.x, self.y)
            # Images of LEFT
            elif self.movePosition[LEFT] == True:
                self.skin.clip_draw(self.frame*32, 48 * 2, 30, 48, self.x, self.y)
            # Images of RIGHT
            elif self.movePosition[RIGHT] == True:
                self.skin.clip_draw(self.frame*32, 48, 30, 48, self.x, self.y)

        elif self.skinType == 'Dragon':
            self.frame = (self.frame + 1) % 4
            # Images of UP
            if self.movePosition[UP] == True:
                self.skin.clip_draw(self.frame*96, 0, 96, 96, self.x, self.y)

            # Images of DOWN
            elif self.movePosition[DOWN] == True:
                self.skin.clip_draw(self.frame * 96,96*3,96,96, self.x, self.y)

            # Images of LEFT
            elif self.movePosition[LEFT] == True:
                self.skin.clip_draw(self.frame * 96, 96 * 2, 96, 96, self.x, self.y)

            # Images of RIGHT
            elif self.movePosition[RIGHT] == True:
                self.skin.clip_draw(self.frame * 96, 96, 96, 96, self.x, self.y)
        elif self.skinType=='Lion':
            self.frame = (self.frame + 1) % 4
            # Images of UP
            if self.movePosition[UP] == True:
                self.skin.clip_draw(self.frame*57, 0, 60, 55, self.x, self.y)

            # Images of DOWN
            elif self.movePosition[DOWN] == True:
                self.skin.clip_draw(self.frame * 57,75 * 2 + 5,60,70, self.x, self.y)

            # Images of LEFT
            elif self.movePosition[LEFT] == True:
                self.skin.clip_draw(self.frame*57, 100, 55, 65, self.x, self.y)

            # Images of RIGHT
            elif self.movePosition[RIGHT] == True:
                self.skin.clip_draw(self.frame * 57, 58, 58, 55, self.x, self.y)

    def drawFirst(self):
        if self.skinType == 'Original':
            self.skin.clip_draw(0, 48 * 3, 42 - 12, 48, self.x, self.y)
        elif self.skinType=='Rocket':
            self.skin.clip_draw(0, 48 * 3, 42 - 12, 48, self.x, self.y)
        elif self.skinType=='Dragon':
            self.skin.clip_draw(0, 96*3, 96, 96, self.x, self.y)
        elif self.skinType=='Lion':
            self.skin.clip_draw(0, 75 * 2 + 5, 60, 70, self.x, self.y)
    def drawBattle(self):
        if self.skinType=='Original':
            self.skin.clip_draw(0, 48, 30, 48, self.x, self.y)
        elif self.skinType=='Rocket':
            self.skin.clip_draw(0, 48, 30, 48, self.x, self.y)
        elif self.skinType=='Dragon':
            self.skin.clip_draw(0, 96, 96, 96, self.x+30, self.y)
        elif self.skinType=='Lion':
            self.skin.clip_draw(0, 58, 58, 55, self.x, self.y)
        font=load_font('ENCR10B.TTF',30)
        font.draw(self.x,self.y-50,'HP: %d' % self.hp)
    def update(self):
        #self.distance=self.RUN_SPEED_PPS
        #self.total_frames+=self. FRAMES_PER_ACTION * self.ACTION_PER_TIME
        #self.frame2=int(self.total_frames)%4
        update_canvas()

class NPC(baseofCharacter):
    pass