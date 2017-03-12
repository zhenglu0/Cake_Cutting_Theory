'''
Created on Oct 25, 2012

@author: roncytron
'''
import random

'''

'''
        
class Prefs(object):
    '''
    classdocs
    '''
    @classmethod
    def random(cls, avgNumIntervals, seedValue=None):
        random.seed(seedValue)
        points = []
        curX = 0.0
        while curX < 1:
            curY = random.random()
            points.append((curX,curY))
            curX += random.random()/avgNumIntervals
        points.append((1.0, random.random()))
        return cls(points)
        
    @classmethod
    def fromFile(cls, fileName):
        points = []
        with open(fileName) as f:
            for line in f:
                x, y = [float(x) for x in line.split()]
                points.append((x,y))
        return cls(points)
    
    '''
    Primary constructor from a list of points
    NB:
        If points are missing at x == 0  or  x == 1
        then values are assumed at those points with y == 0
        
        The x values must appear in sorted order, strictly increasing
    '''
    def __init__(self, listOfPoints):
        '''
        Constructor
        '''
        self.intervals = []
        oldx = 0
        oldy = 0
        for (x,y) in listOfPoints:
            if x == 0:
                oldy = y
            else:
                interval = _PrefsInterval(oldx,oldy,x,y)
                self.intervals.append(interval)
                oldx = x
                oldy = y
        if oldx < 1.0:
            self.intervals.append(_PrefsInterval(oldx,oldy,1,0))

    '''
    Return the value according to preferences from a to b,
    scaled by the value of the entire cake.
    This is done by visiting every interval and accumulating value
    where applicable
    '''                    
    def valueOfPiece(self,param1,param2=None):
        if param2 == None:
            a,b = param1
        else:
            a = param1
            b = param2
        ans   = 0.0
        total = 0.0
        for interval in self.intervals:
            total += interval.area(0,1)
            ans   += interval.area(a,b)
        return ans / total
                    
    def __str__(self):
        ans = ""
        for interval in self.intervals:
            ans += str(interval) + " "
        return ans
    
'''
Class used internally by Prefs to hold an interval
'''
class _PrefsInterval(object):
    
    def __init__(self,x1,y1,x2,y2):
        if x1 >= x2:
            raise Exception("Bad interval specification")
        #
        # Store everything as float
        #
        self.x1 = 1.0*x1
        self.y1 = 1.0*y1
        self.x2 = 1.0*x2
        self.y2 = 1.0*y2
        #
        # constants for y = mx + b
        #
        self.m  = 1.0*(y2-y1)/(x2-x1)
        self.b  = 1.0*y1-self.m*x1

    '''
    Based on the integral of the linear equation
    y = mx + b
    '''        
    def _evalIntegral(self,x):
        return self.m*x*x/2.0 + self.b*x
    
    '''
    Return the area of this interval from a to b
    The area is valid only between the left and right boundaries of
    this interval.
    '''    
    def area(self, a, b):
        left  = max(self.x1, a)
        right = min(self.x2, b)
        
        if left > self.x2 or right < self.x1:
            return 0.0
        else:
            return self._evalIntegral(right) - self._evalIntegral(left)
        
    def __str__(self):
        return '(' + str(self.x1) + ',' + str(self.y1) + ')--(' + str(self.x2) + ',' + str(self.y2)+')'
            


        