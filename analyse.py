import sys
import player
from analysisFunction import openAnalysis

statFile = sys.argv[1]
funFiles = sys.argv[2:]

analyses = [openAnalysis(funFile) for funFile in funFiles]

stats = player.PlayerReaderRaw(statFile).read()
for stat in stats:
    for analysis in analyses:
        stat.apply(analysis)

player.PlayerWriterCSV("target/out.csv")(stats)

