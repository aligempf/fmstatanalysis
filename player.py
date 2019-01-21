import csv

def openStatsFile(statFile, analyses):
    with open(statFile, 'r') as fin:
        stats = set()
        for row in csv.DictReader(fin):
            stats.add(Player(row, analyses))
    return stats

class Player:
    def __init__(self, playerRow, funs):
        self.__dict__ = playerRow
        self.name = playerRow["Name"]
        self.values = {fun.role: fun(self) for fun in funs}

    def __repr__(self):
        return "Player: " + self.name + " - " + self.Club

    def __getitem__(self, key):
        return self.__dict__[key]

    def outputPlayer(self):
        output = {"Name": self.Name, "Club": self.Club, "Position": self.Position}
        output.update(self.values.items())
        return output

def writePlayer(players):
    with open("target/out.csv", "w") as fout:
        writer = csv.DictWriter(fout, list(players)[0].outputPlayer().keys())
        writer.writeheader()
        for player in players:
            writer.writerow(player.outputPlayer())

