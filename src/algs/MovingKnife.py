'''
Created on Nov 21, 2012

@author: John Fang, Sreeharsha Sistla, Zheng Luo
'''
from prefs.Prefs import Prefs
import random

class MovingKnife(object):
    '''
    classdocs
    '''

    def __init__(self, totalSteps):
        self.totalPlayers = 0
        self.playerList = []
        self.totalSteps = totalSteps
        self.suppressOutput = 0
    
    def addPlayer(self, playerPref):
        self.totalPlayers += 1
        self.playerList.append(playerPref)
 
    def addPlayerFromFile(self, filename):
        playerPref = Prefs.fromFile(filename)
        self.totalPlayers += 1
        self.playerList.append(playerPref)
    
        
    def addRandomPlayer(self, avgNumIntervals,startingseed):
        self.randomseed = startingseed
        newplayer = Prefs.random(avgNumIntervals, self.randomseed)
        self.playerList.append(newplayer)    
        self.totalPlayers += 1
        self.randomseed += 1    
        return newplayer
        
    def run(self):
        lastCut = 0;
        n = 1
        self.resultList = []
        for i in range(self.totalPlayers):
            self.resultList.append(0)
        for i in range(self.totalSteps):
            for j in range(len(self.playerList)):
                pref = self.playerList[j]
                if(self.resultList[j] > 0):
                    continue
                ' If only 1 player remains, he gets all the cake that is left over'
                if(len(self.playerList) == 1 or n == self.totalPlayers):
                    playerIndex = self.playerList.index(pref)
                    self.resultList[playerIndex] = pref.valueOfPiece(lastCut,1)
                    if self.suppressOutput == 0:
                        print("Player " + str(playerIndex) + " got a piece with value " + str(pref.valueOfPiece(lastCut,1)))
                    return
                
                'Otherwise check to see if anyone would call stop.'
                if(pref.valueOfPiece(lastCut,i*1.0/self.totalSteps) >= 1.0/self.totalPlayers):
                    playerIndex = j
                    self.resultList[playerIndex] = pref.valueOfPiece(lastCut,i*1.0/self.totalSteps)
                    if self.suppressOutput == 0:
                        print("Player " + str(playerIndex) + " got a piece with value " + str(pref.valueOfPiece(lastCut,i*1.0/self.totalSteps)))
                    lastCut = i*1.0/self.totalSteps
                    n += 1
                    break
        for i in range(len(self.resultList)):
            if(self.resultList[i] == 0 and self.suppressOutput == 0):
                '''print("Player " + str(i) + " didnt get a piece :(")'''
    
    
                    
                