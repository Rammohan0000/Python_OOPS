class Cricket:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def cricket_details(self):
        print(f"The player details are: {self.name}, {self.role}")
        
class Football(Cricket):
    def __init__(self, name, role, organisation):
        super().__init__(name, role)
        self.organisation = organisation
        
    def football_details(self):
        print(f"The details regarding football players are: ")
        
class Event(Football):
    def __init__(self, name, role, organisation, coach):
        super().__init__(name, role, organisation)
        self.coach = coach
        
    def event_details(self):
        print(f"The event details are {self.name}, {self.role}, {self.organisation}, {self.coach}")
        
name = input("Enter the player name: ")
role = input("Enter the role of the player: ")
organisation = input("Enter the organisation details: ")
coach = input("Enter the coach name: ")

event = Event(name, role, organisation, coach)  

event.cricket_details()
event.football_details()
event.event_details()                           
        
