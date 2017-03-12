'''
Created on Dec 11, 2012

@author: John Fang
'''
from MovingKnife import MovingKnife
from MovingKnifeExact import MovingKnifeExact
import random

if __name__ == '__main__':
    pass

step = 1000

sim = MovingKnife(step)
simExact = MovingKnifeExact()

for i in range(10):
    seed = random.randint(-10000000,10000000)
    newplayer = sim.addRandomPlayer(20,seed)
    simExact.addPlayer(newplayer)
print("Running Moving Knife with step resolution of 1/" + str(step))
sim.run()
print("\nRunning Exact Moving Knife on same set of preferences")
simExact.run()