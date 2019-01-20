class AnalysisFunction:
    def __init__(self, role, values):
        self.values = values
        self.role = role
        self.valueSum = sum(map(int, values.values()))

    def __call__(self, player):
        rating = 0
        for value in self.values:
            rating += int(self.values[value])/self.valueSum * int(player[value])
        return rating
