import random


class TicTacToeEnv:
    """
    A game of tic tac toe.
    """

    initial_state = (0, 0, 0, 0, 0, 0, 0, 0, 0)

    def __init__(self):
        self.state = self.initial_state

    @property
    def action_space(self):
        return [i for i, x in enumerate(self.state) if x == 0]

    def step(self, state, action):
        # resolve player's move
        new_state = list(self.state)
        new_state[action] = 1
        self.state = tuple(new_state)
        reward, done = self.check_game_end()

        if done:
            next_state = self.state
            info = None
            return next_state, reward, done, info

        # resolve opponent's move
        opp_action = random.choice(self.action_space)
        new_state = list(self.state)
        new_state[opp_action] = -1
        self.state = tuple(new_state)
        reward, done = self.check_game_end()

        next_state = self.state
        info = None
        return next_state, reward, done, info

    def check_game_end(self):
        if sum([self.state[i] for i in [0,1,2]]) == 3 or sum([self.state[i] for i in [3,4,5]]) == 3 or sum([self.state[i] for i in [6,7,8]]) == 3 or sum([self.state[i] for i in [0,3,6]]) == 3 or sum([self.state[i] for i in [1,4,7]]) == 3 or sum([self.state[i] for i in [2,5,8]]) == 3 or sum([self.state[i] for i in [0,4,8]]) == 3 or sum([self.state[i] for i in [2,4,6]]) == 3:
            reward = 1
            done = True
        elif sum([self.state[i] for i in [0,1,2]]) == -3 or sum([self.state[i] for i in [3,4,5]]) == -3 or sum([self.state[i] for i in [6,7,8]]) == -3 or sum([self.state[i] for i in [0,3,6]]) == -3 or sum([self.state[i] for i in [1,4,7]]) == -3 or sum([self.state[i] for i in [2,5,8]]) == -3 or sum([self.state[i] for i in [0,4,8]]) == -3 or sum([self.state[i] for i in [2,4,6]]) == -3:
            reward = -1
            done = True
        elif 0 not in self.state:
            reward = 0 
            done = True
        else:
            reward = 0
            done = False
        return reward, done
