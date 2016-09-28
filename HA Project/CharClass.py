# define for using instead of number
first= 0
second= 1
third=2
forth=3
up=0
down=1
left=2
right=3


class baseofcharacter:

    # Initialization of the Character
    def __init__(self):
        
        self.skin='basic'
        self.sUp=[0,0,0,0]
        self.sUpChk=[True,0,0,0]
        self.sDown=[0,0,0,0]
        self.sDownChk=[True,0,0,0]
        self.sLeft=[0,0,0,0]
        self.sLeftChk=[True,0,0,0]
        self.sRight=[0,0,0,0]
        self.sRightChk=[True,0,0,0]
        self.movePosition=[False,False,False,False]
        self.nowMove=[False,False,False,False]
        self.myTurn=False
        self.haveItem=False
        self.angelVal=0
        self.devilVal=0
        self.attack=1
        self.defence=1
        self.x=0
        self.y=0
        self.hp=1



   
    
        
