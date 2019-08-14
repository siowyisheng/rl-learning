import random


class BiasedRockPaperScissorsEnv:
    """
    A simple mock game of rock paper scissors against an opponent
    who most often plays rock.
    """

    def __init__(self):
        self.initial_state = 'start'
        self.action_space = ['rock', 'paper', 'scissors']

    def step(self, state, action):
        x = random.random()
        if x <= 1 / 2:
            oaction = 'rock'
        elif x <= 3 / 4:
            oaction = 'paper'
        else:
            oaction = 'scissors'
        ACTION_OACTION_TO_RESULT = {
            ('rock', 'rock'): 'draw',
            ('rock', 'paper'): 'lose',
            ('rock', 'scissors'): 'win',
            ('paper', 'rock'): 'win',
            ('paper', 'paper'): 'draw',
            ('paper', 'scissors'): 'lose',
            ('scissors', 'rock'): 'lose',
            ('scissors', 'paper'): 'win',
            ('scissors', 'scissors'): 'draw',
        }
        result = ACTION_OACTION_TO_RESULT[action, oaction]
        if result == 'lose':
            reward = -1
        elif result == 'draw':
            reward = 0
        else:
            reward = 1
        next_state = 'ended'
        done = True
        info = None
        return next_state, reward, done, info