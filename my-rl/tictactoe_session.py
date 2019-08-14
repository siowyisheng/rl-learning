from environments.tictactoe_env import TicTacToeEnv
from qlearning_agent import QLearningAgent
from session import Session
from collections import Counter

env = TicTacToeEnv()
agent = QLearningAgent(alpha=0.1, gamma=0.9)
session = Session(env, agent)
logs = session.run(episodes=10000, epsilon='explore_then_exploit')
print(Counter([log['score'] for log in logs]))

# the more randomness in the environment, the lower the alpha should be
