import player
from analysisFunction import openAnalysis
from config.ConfigReaderJson import ConfigReaderJson

config = ConfigReaderJson("analysisFunctions/config.json").readConfig()

statFile = config.statFile
funFiles = config.analysisFiles

analyses = [openAnalysis(funFile) for funFile in funFiles]

stats = player.PlayerReaderRaw(statFile).read()
for stat in stats:
    for analysis in analyses:
        stat.apply(analysis)

player.PlayerWriterCSV("target/out.csv")(stats)

