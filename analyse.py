import csv
import sys
import player
from analysisFunction import AnalysisFunction

statFile = sys.argv[1]
funFile = sys.argv[2]

with open(funFile, 'r') as fin:
    values = {}
    reader = csv.reader(fin)
    role = next(reader)[0]
    for row in reader:
        values[row[0]] = row[1]

analysis = AnalysisFunction(role, values)
print(analysis.role, ":", analysis.values)

with open(statFile, 'r') as fin:
    stats = set()
    for row in csv.DictReader(fin):
        stats.add(player.Player(row, [analysis]))

print(stats)
print([player.values for player in stats])

