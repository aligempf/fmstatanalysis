import csv

class Player:
    def __init__(self, playerRow, funs=None):
        self.__dict__ = playerRow
        self.name = playerRow["Name"]
        if funs:
            self.values = {fun.role: fun(self) for fun in funs}
        else:
            self.values = {}

    def __repr__(self):
        return "Player: " + self.name + " - " + self.Club

    def __getitem__(self, key):
        return self.__dict__[key]

    def apply(self, fun):
        self.values.update({fun.role: fun(self)})

    def outputPlayer(self):
        output = {"Name": self.Name, "Club": self.Club, "Position": self.Position}
        output.update(self.values.items())
        return output

class PlayerReader:
    def __init__(self, statFile):
        self.statFile = statFile

    def __call__(self, analyses):
        pass

class PlayerReaderCSV(PlayerReader):
    def __call__(self, analyses):
        with open(self.statFile, 'r') as fin:
            stats = set()
            for row in csv.DictReader(fin):
                stats.add(Player(row, analyses))
        return stats

class PlayerWriter:
    def __init__(self, outFile):
        self.outFile = outFile

    def __call__(self, players):
        pass

class PlayerWriterCSV(PlayerWriter):
    def __call__(self, players):
        with open("target/out.csv", "w") as fout:
            writer = csv.DictWriter(fout, list(players)[0].outputPlayer().keys())
            writer.writeheader()
            for player in players:
                writer.writerow(player.outputPlayer())

