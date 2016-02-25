import dk1
import pytest
class testdonkey:
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
# os.system("clear")
   	 screen.genCoins()
   	 screen.printScreen()
   	 self.board = screen.a

    def test_donkey(self):
	number = 0
    	for i in range(24):
        	for j in range(80):
               	 if( self.board[i][j] == 'D'):
                 	number=number+1

	if ( number == 1):
	    return True
 
	return False

def test_donkey_returnval():
 	T = testdonkey()
     	assert T.test_donkey() == True

