class Cricket:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def profile(self):
        print(f"Player name is: {self.name}, He was working on: {self.role}")
        
class Football:
    def __init__(self, organisation, coach):
        self.organisation = organisation
        self.coach = coach
        
    def coach_details(self):
        print(f"He was working in: {self.organisation}, and his coach was: {self.coach}")

class Event(Cricket, Football):
    def __init__(self, name, role, organisation, coach):
        Cricket.__init__(self, name, role)
        Football.__init__(self, organisation, coach)
        
    def details(self):
        print(f"Complete details: Player Name: {self.name}, Role: {self.role}, Organisation: {self.organisation}, Coach: {self.coach}")

# Input data
name = input("Enter the player name: ")
role = input("Enter the role of the player: ")
organisation = input("Enter the organisation details: ")
coach = input("Enter the coach details: ")

# Create instances of the classes
cricket = Cricket(name, role)
football = Football(organisation, coach)
event = Event(name, role, organisation, coach)

# Display details
cricket.profile()
football.coach_details()
event.details()
