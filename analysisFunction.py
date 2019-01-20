class AnalysisFunction:
    def __init__(self, role, values):
        self.values = values
        self.role = role

    def __call__(self, player):
        rating = 0
        for value in self.values:
            rating += int(self.values[value]) * int(player[value])
        return rating
