'''
Created on Nov 23, 2012

@author: John Fang, Sreeharsha Sistla, Zheng Luo
'''

from prefs.Prefs import Prefs
from Player import Player

class LastDiminisher(object):
    '''
    classdocs
    '''

    def __init__(self, resolution, epsilon):
        # number of players
        self.totalPlayers = 0
        # list to store the players
        self.playerList = []
        # resolution to let knife move on the cake
        self.resolution = resolution
        # list to store the result
        self.resultList = []
        # define epsilon to indicate whether double numbers are equal
        self.epsilon = epsilon
    
    def addPlayer(self, playerPref):
        # create a player with id and playerPref
        player = Player(self.totalPlayers,playerPref)
        # add it to the list
        self.playerList.append(player)
        # increase the counter
        self.totalPlayers += 1
        
    def addPlayerRadomPrefs(self, avgNumIntervals):
        # create a player with id and random playerPref
        player = Player(self.totalPlayers,Prefs.random(avgNumIntervals))
        # add it to the list
        self.playerList.append(player)
        # increase the counter    
        self.totalPlayers += 1
        
    def run(self):
        # the marker of last cut
        lastCut = 0
        nowCut = 0
        # store the id of the player who cut the cake
        pCutter = -1
        index = -1
        
        # set all the element in the result list 0 first
        for i in range(0,self.totalPlayers):
            self.resultList.append(0)
            
        n = 0 # loop should run total number of player times
        while n < self.totalPlayers:    
            # if only 1 player remains, he gets all the cake that is left over
            if(len(self.playerList) == 1):
                print ("When everyone except the last one finishes the cutting, ")
                print ("the id of the last player in the list is " + str(self.playerList[0].playerId) + "\n")
                self.resultList[self.playerList[0].playerId] = self.playerList[0].playerPref.valueOfPiece(lastCut,1)
                # remove the player from the list
                self.playerList.pop(0)
                break
            
            # if we have more than one player left, the first player left in the list trim the cake first, actually mark the cake
            for i in range(1,int(1.0/self.resolution)):
                x = i * self.resolution
                v = self.playerList[0].playerPref.valueOfPiece(lastCut,lastCut + x)
                # here we think that self.p1.valueOfPiece(0,x) == 1.0/self.totalPlayers in the range of e
                if v - 1.0/self.totalPlayers <= self.epsilon and v - 1.0/self.totalPlayers >= 0 :
                    #  Player first 1 cuts
                    nowCut = lastCut + x
                    pCutter = self.playerList[0].playerId
                    index = 0
                    break
            
            # pass the cake to the rest of the player
            for i in range(1,len(self.playerList)):
                # here we think that self.pi.valueOfPiece(0,x) <= 1.0/self.totalPlayers in the range of e
                v = self.playerList[i].playerPref.valueOfPiece(lastCut,nowCut)
                if v - 1.0/self.totalPlayers <= 0:
                    continue
                # when a player thinks the piece of cake is larger than 1/n
                else:
                    # move the marker left and find the 1/n to player i
                    for j in range(1,int(1.0/self.resolution)):
                        x = j * self.resolution
                        v = self.playerList[i].playerPref.valueOfPiece(lastCut,nowCut - x)
                        # here we think that self.p1.valueOfPiece(0,x) == 1.0/self.totalPlayers in the range of e
                        if v - 1.0/self.totalPlayers <= self.epsilon and v - 1.0/self.totalPlayers >= 0 :
                            nowCut = nowCut - x
                            pCutter = self.playerList[i].playerId
                            index = i
                            break
                            
            # after everyone trims the cake
            self.resultList[pCutter] = self.playerList[index].playerPref.valueOfPiece(lastCut,nowCut)
            # remove the player who gets the cake
            self.playerList.pop(index)
            # update the last cut
            lastCut = nowCut
            # update the index   
            n += 1
          
        # check if the player did not get the cake        
        for i in range(0,self.totalPlayers):
            if(self.resultList[i] == 0):
                print("Player " + str(i) + " didnt get a piece :(")
            else:
                # print out the cake player index get
                print("Player " + str(i) + " got a piece with value " + str(self.resultList[i]))  