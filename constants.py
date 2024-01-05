from enum import Enum

class Elo(Enum):
    IRON = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4
    PLATINUM = 5
    EMERALD = 6
    DIAMOND = 7
    MASTER = 8
    GRANDMASTER = 9
    CHALLENGER = 10


class Role(Enum):
    TOP = 1
    JUNGLE = 2
    MID = 3
    ADC = 4
    SUPPORT = 5