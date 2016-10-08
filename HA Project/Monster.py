from CharClass import *
import math

def dist(man,monster):
    return math.sqrt( ((man.x-monster.x)*(man.x-monster.x))+((man.y-monster.y)*(man.y-monster.y)))
