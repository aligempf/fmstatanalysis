import sys
import player
from analysisFunction import openAnalysis
from config import Config

config = Config(sys.argv[1], sys.argv[2:], "target/out.csv")

statFile = config.statFile
funFiles = config.analysisFiles

analyses = [openAnalysis(funFile) for funFile in funFiles]

stats = player.PlayerReaderRaw(statFile).read()
for stat in stats:
    for analysis in analyses:
        stat.apply(analysis)

player.PlayerWriterCSV("target/out.csv")(stats)

