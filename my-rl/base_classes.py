# Our goal in reinforcement learning is to,
# given an environment,
# learn an optimal policy.

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
# episode => initial state to terminal state
# epoch => initial state to terminal state, including learning/updating of values
# alpha => learning rate = factor by which weights are adjusted
# gamma => discount factor = factor by which future rewards are discounted to present value
# epsilon => curiosity vs greed, explore vs exploit = chance that the agent will explore instead of exploit

import numpy as np
import matplotlib.pyplot as plt
import time
from collections import defaultdict


class Session:
    """A session which can control many episodes of an agent in an environment."""

    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent

    def run(
            self, episodes=None, duration=None, epsilon='explore_then_exploit'
    ):  # duration input not working yet, other epsilon styles not working yet
        if episodes is None and duration is None:
            raise ValueError
        logs = []
        start = time.time()
        for i in range(episodes):
            elapsed = time.time() - start
            if duration and elapsed > duration:
                break
            epsilon = _adjust_epsilon(episodes, i + 1)
            log = self._run_episode(epsilon)
            logs.append(log)
        return logs

    def _run_episode(self, epsilon):
        steps, score, done = 0, 0, False
        log = {}
        state_action_pairs = []
        total_info = []
        state = self.environment.initial_state
        action_space = self.environment.action_space
        while not done:
            action = self.agent.decide(state, action_space, epsilon)
            next_state, reward, done, info = self.environment.step(
                state, action)
            self.agent.learn(state, action, next_state, reward, action_space)
            state = next_state
            score += reward
            steps += 1
            state_action_pairs.append((state, action))
            if info:
                total_info.append(info)
        return {
            'state-action pairs': state_action_pairs,
            'steps': steps,
            'score': score,
            'info': total_info,
        }


def _adjust_epsilon(episodes, current_episode):
    return max(0, 1 - current_episode / episodes)


class Environment:
    """An environment for an agent to act in."""

    def __init__(self):
        pass

    def step(self, state, action):
        raise NotImplementedError


class Agent:
    """An agent which learns to seek reward in an environment."""

    def __init__(self):
        pass

    def decide(self, state, action_space):
        raise NotImplementedError
        # should return action

    def learn(self):
        raise NotImplementedError


class ActionSpace:
    """A set of possible actions."""

    def __init__(self):
        pass

    def sample(self):
        """Uniformly randomly sample a random element of this space. """
        raise NotImplementedError

    def __contains__(self, x):
        """Implements `if action in space:`"""
        raise NotImplementedError


# END GOAL

# env = CartPoleEnv()
# agent = QLearningAgent(alpha=0.9, gamma=0.9)
# session = Session(env, agent)
# logs = session.run(n=10000, time=60, epsilon='explore_then_exploit')

# session has environment, agent, run
# session.run takes n, duration, epsilon, returns logs and changes agent._Q inplace
# session.run gets env.initial_state, calls agent.decide(), env.step(), agent.learn()
# episode is an internal implementation which has environment, agent, run
# it takes the job of calling agent.decide(), env.step(), agent.learn() and just
# leaves session in charge of controlling the episodes
# environment has initial_state, action_space, step
# step takes state and action and returns next_state, reward, done, info
# action_space has sample
# agent has decide, learn

# Session
# init(env, agent)
# run(env, agent, n, duration, epsilon) => trained_agent, logs
# logs = []
# start = time.time()
# for i in range(n):
#     elapsed = time.time() - start
#     if elapsed > duration:
#         break
#     episode = Episode(env, agent)
#     log = episode.run()
#     logs.append(log)
# return logs

# run_episode()
#     steps, score, done = 0, 0, False
#     state = env.initial_state
#     while not done:
#         action = agent.decide(state)
#         next_state, reward, done, info = env.step(state, action)
#         agent.learn(state, action, next_state, reward)
#         state = next_state
#         score += reward
#
# state: State

# run_without_learning(env, agent, n, time) => logs # BONUS, basically overrides alpha to 0
# logs: List[List[Tuple[State, Action]]]

# Agent
# init(alpha, gamma)
# _Q = {(s,a): v}
# alpha: float
# discount_rate: float
# epsilon: function => float
# decide(epsilon)
#         if random.uniform(0, 1) < epsilon:
#             # Check the action space
#             action = env.action_space.sample()
#         else:
#             # Check the learned values
#             action = np.argmax(q_table[state])
# learn()
#         old_value = q_table[state, action]
#         next_max = np.max(q_table[next_state])
#         # Update the new value
#         new_value = (1 - alpha) * old_value + alpha * \
#             (reward + gamma * next_max)
#         q_table[state, action] = new_value

# Environment
# action_space: ActionSpace
# initial_state: State
# step(s, a) => state, reward, done, info

# ActionSpace
# n - size
# sample() => action