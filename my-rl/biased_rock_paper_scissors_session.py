from environments.biased_rock_paper_scissors_env import BiasedRockPaperScissorsEnv
from qlearning_agent import QLearningAgent
from session import Session
from collections import Counter

env = BiasedRockPaperScissorsEnv()
agent = QLearningAgent(alpha=0.1, gamma=0.9)
session = Session(env, agent)
logs = session.run(episodes=10000, epsilon='explore_then_exploit')
print(Counter([log['state-action pairs'][0][1] for log in logs]))

# the more randomness in the environment, the lower the alpha should be
