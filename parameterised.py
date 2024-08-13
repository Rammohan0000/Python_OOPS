class Cricket:
    def __init__(self, batsmen, bowler):
        self.batsmen = batsmen
        self.bowler = bowler
        
    def get_batsmeninfo(self):
        print(f"Batsmen info: Best Batsmen are :{self.batsmen}, Best Bowlers are {self.bowler}")
        
batsmen = str(input("Enter batsmen name: "))
bowler = str(input("Enter Bowler name: "))

cricket = Cricket(batsmen, bowler)

cricket.get_batsmeninfo()      
            