class Criket:
    totalScore = 0
    def __init__(self,batter,pscore):
        self.batter = batter
        self.pscore = pscore
        Criket.totalScore = Criket.totalScore+pscore
    def showbatterinfo(self):
        print(f'Player Name : {self.batter}')
        print(f'Player score : {self.pscore}')
        print(f'Total Score  : {Criket.totalScore}')
print("==================Player - 1 Information===========")
p1 = Criket("Virat Kohli",50)
p1.showbatterinfo()
print("==================Player - 1 Information===========")
p2 = Criket("Rohit sharma",70)
p2.showbatterinfo()
        