'''
Created on Oct 28, 2012

@author: cytron
'''
import sys
sys.path.insert(0,'../..')

from DivideAndChoose import DivideAndChoose
from prefs.Prefs import Prefs

if __name__ == '__main__':
    pass


def runOneTest(name,p1,p2,resolution=0.01):
    print("\n"+name)    
    dc = DivideAndChoose(p1, p2, resolution)
    result = dc.run()
    print("   Answer is " + str(result))
    pi1, pi2 = result
    print("   P1 got " + str(pi1) + " with value " + str(p1.valueOfPiece(pi1)))
    print("   P2 got " + str(pi2) + " with value " + str(p2.valueOfPiece(pi2)))
    
runOneTest("Files ascending and descending",Prefs.fromFile("../../data/ascending"), Prefs.fromFile("../../data/descending"))

for i in range(0,5):
    runOneTest("Random run " + str(i),Prefs.random(10), Prefs.random(10))
    
p1 = Prefs.random(100)
p2 = Prefs.random(100)

for r in range(0,5):
    resolution = 1.0/10**r
    runOneTest("Resolution " + str(resolution),p1,p2,resolution)

    
if len(sys.argv) == 3:
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    print("File for first person's prefs is " + str(f1))
    print("File for second person's prefs is " + str(f2))
    runOneTest("File run",Prefs.fromFile(f1),Prefs.fromFile(f2))