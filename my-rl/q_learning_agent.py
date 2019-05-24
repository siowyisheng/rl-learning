# Our goal in reinforcement learning is to learn an optimal policy.

# Q learning. Update a dictionary with state, action tuples mapped to
# expected present value of future rewards.

# observation => state
# space => set
# return => cumulative future reward
# value => discounted return => cumulative future discounted reward
# episodic => describing a task that eventually ends
# optimal policy => mapping states to their optimal actions
# policy => mapping state, action pairs to their probability of being taken
# markov decision process => directed graph with states for nodes and state transitions as edges
# action value function => Q(s,a), mapping of state-action pairs to value
# state value function => V(s), mapping of states to value
# stochastic => probabilistic
# bellman equation => expresses values of states using values of future states

from base_classes import Agent
import random
import numpy as np


class QLearningAgent(Agent):
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


# Agent
# init(alpha, gamma)
# _Q = {(s,a): v}
# learn()
#         old_value = q_table[state, action]
#         next_max = np.max(q_table[next_state])
#         # Update the new value
#         new_value = (1 - alpha) * old_value + alpha * \
#             (reward + gamma * next_max)
#         q_table[state, action] = new_value

#         action_ = maxAction(Q, observation_, env.possibleActions)
#         state = observation_
#     if EPS - 2 / numGames > 0:
#         EPS -= 2 / numGames
#     else:
#         EPS = 0
#     totalRewards[i] = epRewards

# plt.plot(totalRewards)
# plt.show()