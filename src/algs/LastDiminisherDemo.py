'''
Created on Nov 23, 2012

@author: John Fang, Sreeharsha Sistla, Zheng Luo
'''
from LastDiminisher import LastDiminisher

if __name__ == '__main__':
    pass

resolution = 0.001
epsilon = 0.01 # define epsilon to indicate whether double numbers are equal
demo = LastDiminisher(resolution,epsilon)

# add the players with Prefs.random(avgNumIntervals)
numberOfPlayers = 10
avgNumIntervals = 20 
for i in range(numberOfPlayers):
    demo.addPlayerRadomPrefs(avgNumIntervals)
    
print ("Run Last Diminisher among " + str(numberOfPlayers) +  " players with resolution = " + str(resolution) + " \n")    
# run the demo
demo.run()