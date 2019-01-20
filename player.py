class Player:
    def __init__(self, playerRow, funs):
        self.__dict__ = playerRow
        self.name = playerRow["Name"]
        self.values = {fun.role: fun(self) for fun in funs}

    def __repr__(self):
        return "Player: " + self.name + " - " + self.Club

    def __getitem__(self, key):
        return self.__dict__[key]

