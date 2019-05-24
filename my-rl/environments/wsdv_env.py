from base_classes import Environment
import random

initial_state = {
    'prestige': 0,
    'wc': 0,
    'socialism': 0,
    'pink_cubes': {
        'supply': 11,
        'box': 1,
        'meck_vorp': 0,
        'brandenburg': 0,
        'anhalt': 0,
        'thuringen': 0,
        'sachsen': 0,
    },
    'west_hand': [],
    'east_hand': [],
    'red_police': 0,
    'pink_police': 0,
    'decade': 1,
    'decade_half': 1,
    'card_row': [],
    'special_card': None,
    'end_of_decade_step': None,
    'hamburg_in': 'schleswig',
    ''
    'w_provinces': {
        'schleswig': {
            
        }
    }
}
# how to record the state of the map?
# accurately?
# provinces - unrest, mp, LS, pink_cubes
# cities - factory(bool)
# infrastructure - city1.city2(bool)
# cssr_w, cssr_e, polska_w, polska_e

WEST_PROVINCES = [
    'SH',
    'NI',
    'HE',
    'RH',
    'BD',
    'BY',
    'WB',
    'NW',
]

class WestPlayer:
    pass

class EastPlayer:
    pass

PROVINCES = [
    Province('Schleswig-Holstein', []),

]

class Province:
    def __init__(self, name: str, cities: list, unrest: int, side: str):
        self.name = name
        self.cities = cities
        self.unrest = unrest
        self.side = side
        self.ls = 0

class City:
    def __init__(self, cities: list, index: int = 0):
        self.cities = cities

class Connection:
    def __init__(self, cities: list, index: int = 0):
        self.cities = cities
        self.index = index 

MAP = {
    'schleswig': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
    'nieder': {
        'cities': [],
        'connections': [],
    },
}

class WirSindDasVolkEnv(Environment):
    """
    The board game Wir Sind Das Volk! 
    https://boardgamegeek.com/boardgame/165401/wir-sind-das-volk
    """

    def __init__(self):
        # self.initial_state = 'start'
        # self.action_space = ['rock', 'paper', 'scissors']
        

    # how can game end?
    # 1. step 10 EOD 4 mass protests on either side
    # 2. step 9 EOD need to remove socialists but none left
    # 3. step 9 EOD need to add socialists but none left
    # 4. any step EOD east needs to dismantle but none left
    #
    # action_space depends on context
    # action_space can be a dictionary
    # context should be a part of state

    def step(self, state, action):
        context
        x = random.random()
        if x <= 1 / 2:
            oaction = 'rock'
        elif x <= 3 / 4:
            oaction = 'paper'
        else:
            oaction = 'scissors'
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
    
