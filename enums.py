class Attribute(Enum):
        STR = 'str'
        INT = 'int'
        PER = 'per'
        CON = 'con'

class Priority(Enum):
        TRIVIAL = 0.1
        EASY = 1
        MEDIUM = 1.5
        HARD = 2

class Frequency(Enum):
        DAILY = 'daily'
        WEEKLY = 'weekly'
        MONTHLY = 'monthly'
        YEARLY = 'yearly'
