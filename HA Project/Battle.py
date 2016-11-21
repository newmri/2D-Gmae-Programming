from CharClass import *
from map import *

# Easter Egga
# When user tires to go north zone, then game will be over.

def handle_events(man,map):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            close_canvas()
        else:
            if event.type==SDL_KEYDOWN:
                if event.key==SDLK_ESCAPE:
                    close_canvas()
                elif man.fightRun==True:
                    if event.key == SDLK_SPACE:
                        print("skill")
                        if man.skinType=='Original':
                            skillEfect = load_image('Resources\\SkillEffect\\Fire.png')
                        elif man.skinType=='Rocket':
                            skillEfect = [load_image('Resources\\SkillEffect\\Thunder1.png'),
                                          load_image('Resources\\SkillEffect\\Thunder2.png'),
                                          load_image('Resources\\SkillEffect\\Thunder3.png'),
                                          load_image('Resources\\SkillEffect\\Thunder4.png'),
                                          load_image('Resources\\SkillEffect\\Thunder5.png'),
                                          load_image('Resources\\SkillEffect\\Thunder6.png')
                                          ]
                        hitEffect = [load_image('Resources\\BloodEffect\\bloodtrail0.png'),load_image('Resources\\BloodEffect\\bloodtrail_1.png'),
                                     load_image('Resources\\BloodEffect\\bloodtrail_2.png'),load_image('Resources\\BloodEffect\\bloodtrail_3.png')
                                     ,load_image('Resources\\BloodEffect\\bloodtrail_4.png'),load_image('Resources\\BloodEffect\\bloodtrail_5.png')
                                     ,load_image('Resources\\BloodEffect\\bloodtrail_6.png'),load_image('Resources\\BloodEffect\\bloodtrail_7.png')]

                        man.setSkillEfect(skillEfect)
                        map.monster.setHitEffect(hitEffect)
                        man.drawSkillEfect(man,map)
                        map.monster.calDamage(man.skillDmg)
                        map.monster.myTurn = True
                        print(map.monster.hp)

                elif man.fight==True:
                     if event.key == SDLK_SPACE:
                        if man.skinType=='Original':
                            skill=load_image('Resources\\SelectOfSkills\\FireBallSel.png')
                        man.setSkill(skill)
                        man.fightRun=True
                        man.resetBattleDialog()
                        clear_canvas()
                        map.draw()
                        man.drawBattle()
                        man.myTurn = False



                     if event.key == SDLK_UP:
                        man.fight=True
                     if event.key==SDLK_DOWN:
                         man.fight=False
                elif man.fight==False:
                      if event.key==SDLK_SPACE:
                          man.fight = 'outhouse'
                      if event.key==SDLK_UP:
                          man.fight = True
                      if event.key==SDLK_DOWN:
                          man.fight = False
                elif event.key == SDLK_RIGHT:
                      pass
                elif event.key == SDLK_LEFT:
                      pass



def battle(man,map,type):

    clear_canvas()
    if type=='Rocket':
        skin = load_image('Resources\\Monster\\rocket.png')
        rocket = Monster(skin, 'Rocket')
        map.setBattleMonster(rocket,'Rocket')
        map.monster.x = map.x-30
        map.monster.y = map.y / 2
    elif type=='Dragon':
        skin = load_image('Resources\\Monster\\Dragon.png')
        dragon = Monster(skin, 'Dragon')
        map.setBattleMonster(dragon,'Dragon')
        map.monster.x = map.x-100
        map.monster.y = map.y / 2
    map.draw()
    man.x=30
    man.y=map.y/2
    man.drawBattle()
    dialogFight = load_image('Resources\\DialogBox\\DialogFight.png')
    dialogRunAway = load_image('Resources\\DialogBox\\DialogRunAway.png')
    man.setBattleDialog(dialogFight)
    man.drawBattleDialog()
    man.update()
    onBattle=True
    while(onBattle==True):
        if(map.monster.myTurn==False):
            handle_events(man,map)
            get_events()
        if map.monster.hp<=0 or man.hp<=0:
            man.hp=100
            map.monster.hp=100
            man.fight='outhouse'
            print(map.monster.type)
            man.won=type
            man.skillDmg=map.monster.skillDmg
        if man.fight=='outhouse':
            man.fight=True
            return 'outhouse',man
        elif man.fight==True:
            if man.fightRun==False:
                man.setBattleDialog(dialogFight)
                if man.drawDiaChk==True:
                   man.drawBattleDialog()

            else:
                man.drawSkill_Box(man.y)
        elif man.fight==False:
            if man.fightRun == False:
               man.setBattleDialog(dialogRunAway)
               if man.drawDiaChk == True:
                   man.drawBattleDialog()
            else:
                man.drawSkill_Box(man.y)
        man.update()
        if map.monster.myTurn==True:
            if type=='Rocket':
                skillEfect = [load_image('Resources\\SkillEffect\\Thunder1.png'),
                          load_image('Resources\\SkillEffect\\Thunder2.png'),
                          load_image('Resources\\SkillEffect\\Thunder3.png'),
                          load_image('Resources\\SkillEffect\\Thunder4.png'),
                          load_image('Resources\\SkillEffect\\Thunder5.png'),
                          load_image('Resources\\SkillEffect\\Thunder6.png')
                          ]
            elif type=='Dragon':
                skillEfect=[load_image('Resources\\SkillEffect\\Blizard1.png'),
                          load_image('Resources\\SkillEffect\\Blizard2.png'),
                          load_image('Resources\\SkillEffect\\Blizard3.png'),
                           load_image('Resources\\SkillEffect\\Blizard4.png'),
                            load_image('Resources\\SkillEffect\\Blizard5.png'),
                            load_image('Resources\\SkillEffect\\Blizard6.png'),
                            load_image('Resources\\SkillEffect\\Blizard7.png'),
                            load_image('Resources\\SkillEffect\\Blizard8.png'),
                            load_image('Resources\\SkillEffect\\Blizard9.png'),
                            load_image('Resources\\SkillEffect\\Blizard10.png'),
                            load_image('Resources\\SkillEffect\\Blizard11.png'),
                            load_image('Resources\\SkillEffect\\Blizard12.png'),
                            load_image('Resources\\SkillEffect\\Blizard13.png'),
                            load_image('Resources\\SkillEffect\\Blizard14.png'),
                            load_image('Resources\\SkillEffect\\Blizard15.png'),
                            load_image('Resources\\SkillEffect\\Blizard16.png'),
                            load_image('Resources\\SkillEffect\\Blizard17.png'),
                            load_image('Resources\\SkillEffect\\Blizard18.png'),
                            load_image('Resources\\SkillEffect\\Blizard19.png')
                          ]
            hitEffect = [load_image('Resources\\BloodEffect\\bloodtrail0.png'),
                     load_image('Resources\\BloodEffect\\bloodtrail_1.png'),
                     load_image('Resources\\BloodEffect\\bloodtrail_2.png'),
                     load_image('Resources\\BloodEffect\\bloodtrail_3.png')
            , load_image('Resources\\BloodEffect\\bloodtrail_4.png'),
                     load_image('Resources\\BloodEffect\\bloodtrail_5.png')
            , load_image('Resources\\BloodEffect\\bloodtrail_6.png'),
                     load_image('Resources\\BloodEffect\\bloodtrail_7.png')]

            map.monster.setSkillEfect(skillEfect)
            man.setHitEffect(hitEffect)
            map.monster.drawSkillEfect(man,map)
            print(map.monster.skillDmg)
            map.monster.myTurn = False




