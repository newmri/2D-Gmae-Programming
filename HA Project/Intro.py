import os
os.chdir('P:\\3-2\\2D\\Resources')
from pico2d import *

def draw_intro():
        open_canvas(800,566)
        startBack=load_image('BackGround.png')
        House=load_image('House.png')

        startBack.draw_now(400,283)
        delay(1)
        close_canvas()
        open_canvas(375,397)
        House=load_image('House.png')
        House.draw_now(375/2,397/2)


