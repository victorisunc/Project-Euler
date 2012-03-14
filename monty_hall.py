from __future__ import division
from random import randint

#Number of games and game generation
ngames = 10000

prize = [randint(1,3)*x for x in ngames*[1]]
player = [randint(1,3)*x for x in ngames*[1]]

# Evaluating success
default = 0
monty = 0

for game in range(ngames):
    # Keeping decision
    if prize[game] == player[game]:
        default = default + 1
    # Taking chance with Monty
    if prize[game] == player[game]:
        # Switching means losing
        pass
    # Switching means winning
    else:
        monty = monty + 1
print 'Probability of winning (own door)', default/ngames
print 'Probability of winning (switching doors)', monty/ngames
