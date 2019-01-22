import csv
import statDefinition

def openAnalysis(analysisFile):
    with open(analysisFile, 'r') as fin:
        values = {}
        reader = csv.reader(fin)
        role = next(reader)[0]
        for row in reader:
            if row[0] in statDefinition.statDefinition:
                values[statDefinition.statDefinition[row[0]]] = row[1]
            else:
                values[row[0]] = row[1]

    return AnalysisFunction(role, values)

class AnalysisFunction:
    def __init__(self, role, values):
        self.values = values
        self.role = role
        self.valueSum = sum(map(float, values.values()))

    def __call__(self, player):
        rating = 0
        for value in self.values:
            if player[value] == "-":
                continue
            rating += float(self.values[value])/self.valueSum * int(player[value])
        return rating
