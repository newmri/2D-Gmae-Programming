from pico2d import *

def setBack():
    open_canvas(800,566)
    startBack=load_image('Resources\\BackGround\\BackGround.png')
    startBack.draw_now(800/2,566/2)
    delay(3)
    close_canvas()
