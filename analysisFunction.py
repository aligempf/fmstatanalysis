import csv

def openAnalysis(analysisFile):
    with open(analysisFile, 'r') as fin:
        values = {}
        reader = csv.reader(fin)
        role = next(reader)[0]
        for row in reader:
            values[row[0]] = row[1]

    return AnalysisFunction(role, values)

class AnalysisFunction:
    def __init__(self, role, values):
        self.values = values
        self.role = role
        self.valueSum = sum(map(int, values.values()))

    def __call__(self, player):
        rating = 0
        for value in self.values:
            rating += float(self.values[value])/self.valueSum * int(player[value])
        return rating
