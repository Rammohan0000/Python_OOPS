class Cricket():
    def __init__(self,name,role):
        self.__name = name
        self._role = role
    def player_info(self):
        print(f"the player name is {self.__name} and his role is {self._role}")

class Team(Cricket):
    def __init__(self, name, role,team):
        super().__init__(name, role)
        self._team = team
    def team_info(self):
        print(f"the player name is {self._Cricket__name} and his role is {self._role} and he plays for the team {self._team}")

class Game(Team):
    def __init__(self,name,role,team,result):
        super().__init__(name,role,team)
        self.result = result
    def result_info(self):
        print(f"the player name is {self._Cricket__name} and his role is {self._role} and he plays for the team {self._team} and match result is {self.result}")


cricket = Cricket("kl_rahul","batsmen")
cricket.player_info()

team = Team("kl_rahul","batsmen","DC")
team.team_info()

game = Game("kl_rahul","batsmen","DC","won")
game.result_info()