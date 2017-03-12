'''
Created on Oct 26, 2012

@author: cytron
'''
from Prefs import Prefs

if __name__ == '__main__':
    pass

def demoPrefs(name,p):
    print("Demo of " + name +" with prefs " + str(p))
    # print("Total area is " + str(p.valueOfPiece(0,1)))
    for e in [0.25, 0.5, 0.75, 1.0]:
        print("  Value from 0.0 to " + "{0:.4f}".format(e) + " is " + "{0:.6f}".format(p.valueOfPiece(0,e)))
    print("Value of first half is  " + str(p.valueOfPiece(0.0,0.5)))
    print("Value of second half is " + str(p.valueOfPiece(0.5,1.0)))
    print("\n")

def demoOne(name, points):
    print("Demo of " +  name + " using points " + str(points))
    p = Prefs(points)
    demoPrefs(name,p)

demoOne("uniform list", [(0,1), (1,1)])
demoOne("ascending list", [(0,0), (1,1)])
demoOne("descending list", [(0,1),(1,0)])
demoPrefs("prefs from a file ascending", Prefs.fromFile("../../data/ascending"))
for i in range(0,3):
    demoPrefs("random, ~5 intervals", Prefs.random(5))
for i in range(0,3):
    demoPrefs("random, ~5 intervals, always same seed", Prefs.random(5,0))
