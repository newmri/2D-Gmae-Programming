import os
os.chdir('P:\\3-2\\2D\\Resources')
from pico2d import *
from CharClass import *
open_canvas(800,566)
startBack=load_image('BackGround.png')
House=load_image('House.png')

startBack.draw_now(400,283)
delay(1)
close_canvas()
open_canvas(375,397)
House=load_image('House.png')
House.draw_now(375/2,397/2)
os.chdir('P:\\3-2\\2D\\Resources\\MainCharacter')
man=baseofcharacter()
# up
man.sUp[first]=load_image('OriginalUp01.png')
man.sUp[second]=load_image('OriginalUp02.png')
man.sUp[third]=load_image('OriginalUp03.png')
man.sUp[forth]=load_image('OriginalUp04.png')
# down
man.sDown[first]=load_image('OriginalDown01.png')
man.sDown[second]=load_image('OriginalDown02.png')
man.sDown[third]=load_image('OriginalDown03.png')
man.sDown[forth]=load_image('OriginalDown04.png')
# left
man.sLeft[first]=load_image('OriginalLeft01.png')
man.sLeft[second]=load_image('OriginalLeft02.png')
man.sLeft[third]=load_image('OriginalLeft03.png')
man.sLeft[forth]=load_image('OriginalLeft04.png')
# right
man.sRight[first]=load_image('OriginalRight01.png')
man.sRight[second]=load_image('OriginalRight02.png')
man.sRight[third]=load_image('OriginalRight03.png')
man.sRight[forth]=load_image('OriginalRight04.png')


def handle_events(char):


    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
           if event.key == SDLK_UP:
               char.movePosition[up]=True
               char.nowMove[up]=True
           elif event.key == SDLK_DOWN:
              char.movePosition[down]=True
           elif event.key == SDLK_RIGHT:
              char.movePosition[right]=True
           elif event.key == SDLK_LEFT:
              char.movePosition[left]=True
            
            
            
            
        if event.type==SDL_KEYUP:
            if event.key == SDLK_UP:
              char.movePosition[up]=False
              char.nowMove[up]=False
            elif event.key == SDLK_DOWN:
              char.movePosition[down]=False
            elif event.key == SDLK_RIGHT:
              char.movePosition[right]=False
            elif event.key == SDLK_LEFT:
              char.movePosition[left]=False
        
            


def run(chk):
    if chk=='run':
       x=375/2
       y=397/2
       man.sDown[first].draw_now(x,y)
       while(True):
            handle_events(man)
            get_events()
   
            if man.movePosition[up]:
                clear_canvas()
                House.draw_now(375/2,397/2)
                y+=5

                if(man.sUpChk[first]==True):
                    man.sUp[first].draw_now(x,y)
                    man.sUpChk[first]=False
                    man.sUpChk[second]=True
                elif(man.sUpChk[second]==True):
                    man.sUp[second].draw_now(x,y)
                    man.sUpChk[second]=False
                    man.sUpChk[third]=True
                elif(man.sUpChk[third]==True):
                    man.sUp[third].draw_now(x,y)
                    man.sUpChk[third]=False
                    man.sUpChk[forth]=True
                elif(man.sUpChk[forth]==True):
                    man.sUp[forth].draw_now(x,y)
                    man.sUpChk[forth]=False
                    man.sUpChk[first]=True
                
                man.nowMove[up]=True
                delay(0.1)
            if man.movePosition[down]:
                y-=5
                clear_canvas()
                House.draw_now(375/2,397/2)
                if(man.sDownChk[first]==True):
                     man.sDown[first].draw_now(x,y)
                     man.sDownChk[first]=False
                     man.sDownChk[second]=True
                elif(man.sDownChk[second]==True):
                       man.sDown[second].draw_now(x,y)
                       man.sDownChk[second]=False
                       man.sDownChk[third]=True
                elif(man.sDownChk[third]==True):
                        man.sDown[third].draw_now(x,y)
                        man.sDownChk[third]=False
                        man.sDownChk[forth]=True
                elif(man.sDownChk[forth]==True):
                        man.sDown[forth].draw_now(x,y)
                        man.sDownChk[forth]=False
                        man.sDownChk[first]=True
                
                man.nowMove[down]=True
                if man.nowMove[down]==True and man.movePosition[down]==False:
                        clear_canvas()
                        House.draw_now(375/2,397/2)
                        man.sDown[first].draw_now(x,y)
                        man.nowMove[down]=False
                delay(0.1)
            if man.movePosition[right]:
                x+=5
                clear_canvas()
                House.draw_now(375/2,397/2)
                if(man.sRightChk[first]==True):
                    man.sRight[first].draw_now(x,y)
                    man.sRightChk[first]=False
                    man.sRightChk[second]=True
                elif(man.sRightChk[second]==True):
                    man.sRight[second].draw_now(x,y)
                    man.sRightChk[second]=False
                    man.sRightChk[third]=True
                elif(man.sRightChk[third]==True):
                    man.sRight[third].draw_now(x,y)
                    man.sRightChk[third]=False
                    man.sRightChk[forth]=True
                elif(man.sRightChk[forth]==True):
                    man.sRight[forth].draw_now(x,y)
                    man.sRightChk[forth]=False
                    man.sRightChk[first]=True
                
                man.nowMove[right]=True
                if man.nowMove[right]==True and man.movePosition[right]==False:
                    clear_canvas()
                    House.draw_now(375/2,397/2)
                    man.sRight[first].draw_now(x,y)
                    man.nowMove[right]=False
                delay(0.1)
            if man.movePosition[left]:
                x-=5
                clear_canvas()
                House.draw_now(375/2,397/2)
                if(man.sLeftChk[first]==True):
                    man.sLeft[first].draw_now(x,y)
                    man.sLeftChk[first]=False
                    man.sLeftChk[second]=True
                elif(man.sLeftChk[second]==True):
                    man.sLeft[second].draw_now(x,y)
                    man.sLeftChk[second]=False
                    man.sLeftChk[third]=True
                elif(man.sLeftChk[third]==True):
                    man.sLeft[third].draw_now(x,y)
                    man.sLeftChk[third]=False
                    man.sLeftChk[forth]=True
                elif(man.sLeftChk[forth]==True):
                    man.sLeft[forth].draw_now(x,y)
                    man.sLeftChk[forth]=False
                    man.sLeftChk[first]=True
                
                man.nowMove[left]=True
                if man.nowMove[left]==True and man.movePosition[left]==False:
                    clear_canvas()
                    House.draw_now(375/2,397/2)
                    man.sLeft[first].draw_now(x,y)
                    man.nowMove[left]=False
                delay(0.1)
        
        
    


    




 












