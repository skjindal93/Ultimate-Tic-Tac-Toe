def getMove(self,State,PlayerList=[]):
                I,J=State[1]
                if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
                        if(State[0][I][J][0][0]==self and State[0][I][J][0][1]==self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][1]==self and State[0][I][J][0][2]==self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][0]==self and State[0][I][J][0][2]==self):
                                if(State[0][I][J][0][1]==None):
                                        return I,J,0,1
                        if(State[0][I][J][1][0]==self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][1][2]==None):
                                        return I,J,1,2
                        if(State[0][I][J][1][1]==self and State[0][I][J][1][2]==self):
                                if(State[0][I][J][1][0]==None):
                                        return I,J,1,0
                        if(State[0][I][J][1][0]==self and State[0][I][J][1][2]==self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][2][0]==self and State[0][I][J][2][1]==self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][2][1]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][2][0]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][2][1]==None):
                                        return I,J,2,1
                        if(State[0][I][J][0][0]==self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][1][1]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][0]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][0][2]==self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][2][0]==self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][2]==self and State[0][I][J][2][0]==self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
        
                        if(State[0][I][J][0][0]==self and State[0][I][J][2][0]==self):
                                if(State[0][I][J][1][0]==None):
                                        return I,J,1,0
                        if(State[0][I][J][0][0]==self and State[0][I][J][1][0]==self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][1][0]==self and State[0][I][J][2][0]==self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][1]==self and State[0][I][J][2][1]==self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][0][1]==self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][2][1]==None):
                                        return I,J,2,1
                        if(State[0][I][J][1][1]==self and State[0][I][J][2][1]==self):
                                if(State[0][I][J][0][1]==None):
                                        return I,J,0,1
                        if(State[0][I][J][0][2]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][1][2]==None):
                                        return I,J,1,2
                        if(State[0][I][J][0][2]==self and State[0][I][J][1][2]==self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][1][2]==self and State[0][I][J][2][2]==self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][0]!=self and State[0][I][J][0][1]!=self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][1]!=self and State[0][I][J][0][2]!=self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][0]!=self and State[0][I][J][0][2]!=self):
                                if(State[0][I][J][0][1]==None):
                                        return I,J,0,1
                        if(State[0][I][J][1][0]!=self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][1][2]==None):
                                        return I,J,1,2
                        if(State[0][I][J][1][1]!=self and State[0][I][J][1][2]!=self):
                                if(State[0][I][J][1][0]==None):
                                        return I,J,1,0
                        if(State[0][I][J][1][0]!=self and State[0][I][J][1][2]!=self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][2][0]!=self and State[0][I][J][2][1]!=self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][2][1]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][2][0]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][2][1]==None):
                                        return I,J,2,1
                        if(State[0][I][J][0][0]!=self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][1][1]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][0]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][0][2]!=self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][2][0]!=self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][2]!=self and State[0][I][J][2][0]!=self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
            
                        if(State[0][I][J][0][0]!=self and State[0][I][J][2][0]!=self):
                                if(State[0][I][J][1][0]==None):
                                        return I,J,1,0
                        if(State[0][I][J][0][0]!=self and State[0][I][J][1][0]!=self):
                                if(State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][1][0]!=self and State[0][I][J][2][0]!=self):
                                if(State[0][I][J][0][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][0][1]!=self and State[0][I][J][2][1]!=self):
                                if(State[0][I][J][1][1]==None):
                                        return I,J,1,1
                        if(State[0][I][J][0][1]!=self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][2][1]==None):
                                        return I,J,2,1
                        if(State[0][I][J][1][1]!=self and State[0][I][J][2][1]!=self):
                                if(State[0][I][J][0][1]==None):
                                        return I,J,0,1
                        if(State[0][I][J][0][2]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][1][2]==None):
                                        return I,J,1,2
                        if(State[0][I][J][0][2]!=self and State[0][I][J][1][2]!=self):
                                if(State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][1][2]!=self and State[0][I][J][2][2]!=self):
                                if(State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][0]==self and State[0][I][J][2][2]==self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][0][1]==None and State[0][I][J][1][2]==None and State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][0]==self and State[0][I][J][2][2]==self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][1][0]==None and State[0][I][J][2][1]==None and State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][0][2]==self and State[0][I][J][2][0]==self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][1][2]==None and State[0][I][J][2][1]==None and State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        if(State[0][I][J][2][0]==self and State[0][I][J][0][2]==self and State[0][I][J][1][1]!=self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][0][1]==None and State[0][I][J][1][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][1][0]==self and State[0][I][J][2][1]==self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][2][2]==None and State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][0][1]==self and State[0][I][J][1][2]==self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][2][2]==None and State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][1]==self and State[0][I][J][1][0]==self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][0][2]==None and State[0][I][J][2][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][1][2]==self and State[0][I][J][2][1]==self):
                                if(State[0][I][J][0][2]==None and State[0][I][J][2][0]==None and State[0][I][J][2][2]==None):
                                        return I,J,2,2
        
                        if(State[0][I][J][0][0]!=self and State[0][I][J][2][2]!=self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][0][1]==None and State[0][I][J][1][2]==None and State[0][I][J][0][2]==None):
                                        return I,J,0,1
                        if(State[0][I][J][0][0]!=self and State[0][I][J][2][2]!=self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][1][0]==None and State[0][I][J][2][1]==None and State[0][I][J][2][0]==None):
                                        return I,J,2,1
                        if(State[0][I][J][0][2]!=self and State[0][I][J][2][0]!=self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][1][2]==None and State[0][I][J][2][1]==None and State[0][I][J][2][2]==None):
                                        return I,J,2,1
                        if(State[0][I][J][2][0]!=self and State[0][I][J][0][2]!=self and State[0][I][J][1][1]==self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][0][1]==None and State[0][I][J][1][0]==None):
                                        return I,J,0,1
                        if(State[0][I][J][1][0]!=self and State[0][I][J][2][1]!=self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][2][2]==None and State[0][I][J][2][0]==None):
                                        return I,J,2,0
                        if(State[0][I][J][0][1]!=self and State[0][I][J][1][2]!=self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][2][2]==None and State[0][I][J][0][2]==None):
                                        return I,J,0,2
                        if(State[0][I][J][0][1]!=self and State[0][I][J][1][0]!=self):
                                if(State[0][I][J][0][0]==None and State[0][I][J][0][2]==None and State[0][I][J][2][0]==None):
                                        return I,J,0,0
                        if(State[0][I][J][1][2]!=self and State[0][I][J][2][1]!=self):
                                if(State[0][I][J][0][2]==None and State[0][I][J][2][0]==None and State[0][I][J][2][2]==None):
                                        return I,J,2,2
                        flag=1
                        for i in range(0,3):
                                for j in range(0,3):
                                        if(State[0][I][J][i][j]!=None):
                                                flag=0
                        if(flag==1):
                                return I,J,0,0
                        if(State[0][I][J][0][0]==self and State[0][I][J][2][2]==None):
                                return I,J,2,2
                        if(State[0][I][J][2][2]==self and State[0][I][J][0][0]==None):
                                return I,J,0,0
                        if(State[0][I][J][2][0]==self and State[0][I][J][0][2]==None):
                                return I,J,0,2
                        if(State[0][I][J][0][2]==self and State[0][I][J][2][0]==None):
                                return I,J,2,0
        
                        if(State[0][I][J][0][0]!=self and State[0][I][J][2][2]==None):
                                return I,J,2,2
                        if(State[0][I][J][2][0]!=self and State[0][I][J][0][2]==None):
                                return I,J,0,2
                        if(State[0][I][J][2][2]!=self and State[0][I][J][0][0]==None):
                                return I,J,0,0
                        if(State[0][I][J][0][2]!=self and State[0][I][J][2][0]==None):
                                return I,J,2,0
                        if(State[0][I][J][0][0]==None):
                                return I,J,0,0
                        if(State[0][I][J][0][2]==None):
                                return I,J,0,2
                        if(State[0][I][J][2][0]==None):
                                return I,J,2,0
                        if(State[0][I][J][2][2]==None):
                                return I,J,2,2
                        for i in range(0,3):
                                if(State[0][I][J][1][i]==None):
                                        return I,J,1,i
                        for i in range(0,3):
                                if(State[0][I][J][i][1]==None):
                                        return I,J,1,i
                        for i in range(0,3):
                                if(State[0][I][J][i][i]==None):
                                        return I,J,i,i
                        for i in range(0,3):
                                if(State[0][I][J][i][2-i]==None):
                                        return I,J,i,2-i
                        while True:
                                i,j  = random.randint(0,2), random.randint(0,2)
                                if State[0][I][J][i][j]==None:
                                        return x,y,i,j
                
                else:
                        for x,y in [(I,J) for I in xrange(3) for J in xrange(3)]:
                                if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,x,y,player) else False for player in PlayerList]) and checkEmpty(State,x,y):
                                        while True:
                                                i,j  = random.randint(0,2), random.randint(0,2)
                                                if State[0][x][y][i][j] == None:
                                                        return x,y,i,j
    