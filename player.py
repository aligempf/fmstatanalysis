class Player:
    def __init__(self, playerRow):
        self.__dict__ = playerRow
        self.name = playerRow["Name"]

    def __repr__(self):
        return "Player: " + self.name + " - " + self.Club

