'''
Created on Oct 25, 2012

@author: roncytron
'''

class TwoPrefs(object):
    '''
    classdocs
    '''

    def __init__(self, p1, p2):
        '''
        Constructor
        '''
        self.p1 = p1
        self.p2 = p2
        print("Two-prefs algorithm with prefs:")
        print("p1   " + str(p1))
        print("p2   " + str(p2))