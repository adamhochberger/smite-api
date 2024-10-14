import enum

class Role(enum.Enum):
    SOLO = 1
    JUNGLE = 2
    MIDDLE = 3
    CARRY = 4
    SUPPORT = 5

    def all_roles(self):
        return list(self.names)
