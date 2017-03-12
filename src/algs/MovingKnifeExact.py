from prefs.Prefs import Prefs
import math

class MovingKnifeExact(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.totalPlayers = 0
        self.playerList = []
        self.suppressOutput = 0
        self.envyChart = []
    
    def addPlayer(self, playerPref):
        self.totalPlayers += 1
        self.playerList.append(playerPref)
        
    def addPlayerFromFile(self, filename):
        playerPref = Prefs.fromFile(filename)
        self.totalPlayers += 1
        self.playerList.append(playerPref)
        return playerPref
        
    def addRandomPlayer(self, avgNumIntervals):
        newplayer = Prefs.random(avgNumIntervals)
        self.playerList.append(newplayer)    
        self.totalPlayers += 1    
        return newplayer
    
    def solveForCut(self,x1,x2,y1,y2, requiredValue):
        m = (y2-y1)/(x2-x1)
        b = y1-m*x1
        a = m/2
        c = -(a*(x1**2)+b*x1+requiredValue)
        
        return self.solveQuadFormula(a, b, c, x1, x2)
    
    def run(self):
        # chart that will tell us what each player thinks of the other players' pieces
        for i in range(self.totalPlayers):
            self.envyChart.append([0]*self.totalPlayers)
        
        lastCut = 0;
        playersLeft = []
        for player in self.playerList:
            playersLeft.append(self.playerList.index(player))
        proportion = 1.0/self.totalPlayers
        self.resultList = []
        for i in range(self.totalPlayers):
            self.resultList.append(0);
        
        for i in range(self.totalPlayers):
            lowestCut = 2
            lowestPlayer = -1
            
            for playernum in playersLeft:
                if(len(playersLeft) == 1):
                    nextCut = 1;
                else:
                    nextCut = self.findNextCut(self.playerList[playernum], lastCut, proportion)
                
                if(nextCut < lowestCut):
                    lowestPlayer = playernum
                    lowestCut = nextCut
            self.resultList[lowestPlayer] = self.playerList[lowestPlayer].valueOfPiece(lastCut,lowestCut)
            for k in range(self.totalPlayers):
                self.envyChart[k][lowestPlayer] = self.playerList[k].valueOfPiece(lastCut, lowestCut)
            if(self.suppressOutput == 0):
                print("Player " + str(lowestPlayer) + " got a piece of value: " + str(self.resultList[lowestPlayer]))
            playersLeft.remove(lowestPlayer)
            lastCut = lowestCut
        for i in range(len(self.resultList)):
            if(self.resultList[i] == 0 and self.suppressOutput == 0):
                print("Player " + str(i) + " didnt get a piece :(")
                
    
    def findNextCut(self, prefFile, xStart, proportion):
        total = 0
        for i in prefFile.intervals:
            total += i.area(0,1)
            
        for interval in prefFile.intervals:
            if(interval.x2 < xStart):
                continue
            '''
                Find the interval where the summed value of all intervals between the last cut and the end of the current
                interval is bigger than proportional value. 
            '''

           
            if(prefFile.valueOfPiece(xStart, interval.x2) < proportion):
                continue
            else:
                '''Sanity check'''
                if(prefFile.valueOfPiece(xStart, interval.x1) > proportion):
                    print ("WAT?!")
                    print("Current interval:" + str(interval))
                    print("proportion: " + str(proportion))
                    for intd in prefFile.intervals:
                        print(str(intd))
                        if(xStart < intd.x1):
                            print("interval.x1:" + str(prefFile.valueOfPiece(xStart,intd.x1)))
                            print("interval.x2:" + str(prefFile.valueOfPiece(xStart,intd.x2)))

                    exit()
                valueSoFar = prefFile.valueOfPiece(xStart, interval.x1)

                    
                targetValue = (proportion - valueSoFar)*(total)
                nextXcut = self.solveForRequiredValue(interval.x1, interval.x2, interval.y1, interval.y2, targetValue)
                return nextXcut
                break
                
                
    def solveForRequiredValue(self,x1,x2,y1,y2, requiredValue):
        m = (y2-y1)/(x2-x1)
        b = y1-m*x1
        a = m/2
        c = -(a*(x1**2)+b*x1+requiredValue)
        xcut = self.solveQuadFormula(a, b, c, x1, x2)
        return xcut 

    def solveQuadFormula(self, a, b, c, x1, x2):
        root = (b**2)-4*a*c
        '''print root'''
        # Root MUST be positive here (or something is wrong)
        x_1 = (-b+math.sqrt(root))/(2*a)
        x_2 = (-b-math.sqrt(root))/(2*a)
        
        if (x_1 >= x1 and x_1 <= x2):
            return x_1
        elif (x_2 >= x1 and x_2 <= x2):
            return x_2
        else:
            print("SOMETHING IS WRONG - GETTING A ROOT THATS NOT IN RANGE")
            return x_1
        
        