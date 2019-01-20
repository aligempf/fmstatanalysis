import csv
import sys
import player

statFile = sys.argv[1]

with open(statFile, 'r') as fin:
    stats = set()
    for row in csv.DictReader(fin):
        stats.add(player.Player(row))

print(stats)

