import dk1
import pytest
import os
class testplayer:
    def __init__(self):
         screen=dk1.Screen()
   	 i=24    
   	 j=2
   	 i1=4
   	 j1=1
   	 pm=dk1.player(i,j)
   	 screen.printpm(i,j,'P')
   	 dk=dk1.donkey(4,2)
   	 screen.printdk(4,2,'D',dk)
   	 fi=dk1.fireball(4,3)
   	 screen.printfi(4,3,'O',fi)
   	 os.system("clear")
   	 screen.genCoins()
   	 screen.printScreen()
   	 self.board = screen.a

    def test_player(self):
	number = 0
    	for i in range(25):
        	for j in range(80):
               	 if( self.board[i][j] == 'P'):
                 	number=number+1

	if ( number == 1):
	    return True
 
	return False

def test_player_returnval():
 	T = testplayer()
     	assert T.test_player() == True

