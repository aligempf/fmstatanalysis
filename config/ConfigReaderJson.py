import json

import config

class ConfigReaderJson(config.ConfigReader):
    def __init__(self, configFile):
        self.configFile = configFile

    def readConfig(self):
        with open(self.configFile, "r") as fin:
            configJson = json.load(fin)
        return config.Config(configJson["statFile"], configJson["analysisFiles"], configJson["targetFile"])
