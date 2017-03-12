'''
Created on Oct 27, 2012

@author: roncytron
'''

from TwoPrefs import TwoPrefs

class DivideAndChoose(TwoPrefs):
    '''
    classdocs
    '''


    def __init__(self, p1, p2, resolution=0.01):
        '''
        Constructor
        '''
        TwoPrefs.__init__(self, p1, p2)
        self.resolution = resolution
        
    '''
    Run the Divide and Choose algorithm,
       returning a list [pi1, pi2]
       for the pieces assigned to players 1 and 2,
       respectively
       
    The resolution of the algorithm is specified, which
       is the increment at which the value of the cut is
       evaluated for Player 1 to make his/her cut.
    '''
    def run(self):
        cut = 0
        for v1 in range(0,int(1.0/self.resolution)):
            x = v1 * self.resolution
            if self.p1.valueOfPiece(0,x) >= 0.5:
                #
                #  Player 1 cuts
                #
                cut = x
                break
        #
        #  Now Player 2 chooses
        #
        pi_x = (0,cut)
        pi_y = (cut,1)
        if self.p2.valueOfPiece(pi_x) >= 0.5:
            #
            #  Player 2 prefers pi_x
            #
            return [pi_y, pi_x]
        else:
            #
            #  Player 2 prefers pi_y
            #
            return [pi_x, pi_y]
    
