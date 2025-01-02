class Cricket:
    def __init__(self, player_name, role):
        self.__player_name = player_name
        self._role = role
    def __str__(self):
        return f"The player name is {self._Cricket__player_name} and his role is {self._role}"
class Team(Cricket):
    def __init__(self,player_name,role,captain):
        super().__init__(player_name, role)
        self.__captain = captain
    def __str__(self):
        return f"The Player name is {self._Cricket__player_name} , his role is {self._role}  and his captain is {self._Team__captain}"
class Match(Team):
    def __init__(self, player_name, role, captain, result):
        super().__init__(player_name, role, captain)
        self.result = result
    def __str__(self):
        return f"The Player name is {self._Cricket__player_name} , his role is {self._role} and his captain is {self._Team__captain} and result of the match is {self.result}"

team = Team("Kl_rahul", "Batsmen", "Rohit")
print(team)

match = Match("Kl_rahul", "Batsmen", "Rohit", "India won")
print(match)
