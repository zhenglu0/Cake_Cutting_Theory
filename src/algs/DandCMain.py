'''
Created on Oct 29, 2012

@author: cytron
'''

'''
This is the file Kevin will call from the web page.
It is listed in the algs file at the top level of the repo,
  saying that it takes 2 prefs file names as input
'''
import sys
import os
if __name__ == '__main__':
    pass
'''
Make sure Kevin's web page can get to the python packages
'''
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))

from DivideAndChoose import DivideAndChoose
from prefs.Prefs import Prefs

'''
Kevin supplies the filenames to us, chosen from the web page
'''
f1 = sys.argv[1]
f2 = sys.argv[2]

'''
Now do what you want
'''
dc = DivideAndChoose(Prefs.fromFile(f1), Prefs.fromFile(f2))
pi1, pi2 = dc.run()
print ("answer is pi1 = " + str(pi1) + " and pi2 = " + str(pi2))
