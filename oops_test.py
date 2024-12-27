class Cricket:
    def __init__(self,player_name, player_role):
        self.__player_name = player_name
        self.__player_role = player_role
    def __str__(self):
        return f'{self.__player_name} is a {self.__player_role}'

class Team(Cricket):
    def __init__(self,team_name, player_name, player_role):
        super().__init__(player_name, player_role)
        self.__team_name = team_name
    def __str__(self):
        return f'{self.__team_name} has {self._Cricket__player_name} as a {self._Cricket__player_role}'
    
c = Team('India','Dhoni','Captain')
print(c)    

c1 = Cricket('Dhoni','Captain')
print(c1)

