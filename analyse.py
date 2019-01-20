import csv
import sys
import player
from analysisFunction import AnalysisFunction

statFile = sys.argv[1]

with open(statFile, 'r') as fin:
    stats = set()
    goalkeeper = AnalysisFunction("GK", {"Aer": 1}) 
    for row in csv.DictReader(fin):
        stats.add(player.Player(row, [goalkeeper]))

print(stats)
print([player.values for player in stats])

