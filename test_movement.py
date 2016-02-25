import dk1
import pytest
number = 10
class movement:
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

    def test_move(self):
	while(number>0):
    		for i in range(24):
        		for j in range(80):
               			 if( self.board[i][j] == 'D'):
				     assert (self.board[i+1][j]=='X' or self.board[i+1][j]=='H')
				 elif ( self.board[i][j] == 'P'):    
				     assert (self.board[i+1][j]=='X' or self.board[i+1][j]=='H')
				 elif ( self.board[i][j] == 'O'):    
				     assert (self.board[i+1][j]=='X' or self.board[i+1][j]=='H')
		return True
 
def test_coin_returnval():
 	T = movement()
     	assert T.test_move() == True

