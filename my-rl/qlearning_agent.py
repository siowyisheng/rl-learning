# my implementation of a q-learning agent

import random
import numpy as np


class QLearningAgent:
    """An agent which uses Q learning to optimize actions in an environment."""

    def __init__(self, alpha, gamma):
        self._Q = {}
        self.alpha = alpha
        self.gamma = gamma

    def decide(self, state, action_space, epsilon):
        if np.random.random() < epsilon:
            return random.choice(action_space)
        else:
            return _best_action(self._Q, state, action_space)
        action = self.agent.decide(state, action_space, epsilon)

    def learn(self, state, action, next_state, reward, action_space):
        alpha = self.alpha
        old_value = self._Q.get((state, action), 0)
        next_best_action = _best_action(self._Q, next_state, action_space)
        next_value = self._Q.get((next_state, next_best_action), 0)
        discounted_return = reward + self.gamma * next_value
        self._Q[state, action] = (1 - alpha) * old_value + (
            alpha * discounted_return)  # yapf: ignore


def _best_action(Q, state, action_space):
    values = np.array([Q.get((state, a), 0) for a in action_space])
    return action_space[np.argmax(values)]
