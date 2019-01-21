import sys
import player
from analysisFunction import openAnalysis

statFile = sys.argv[1]
funFiles = sys.argv[2:]

analyses = [openAnalysis(funFile) for funFile in funFiles]

stats = player.openStatsFile(statFile, analyses)

player.writePlayer(stats)

