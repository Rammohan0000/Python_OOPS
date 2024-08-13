class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def work(self):
        print(f"{self.name} is working.")

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing the {self.department} department.")

# Creating an instance of Manager
manager = Manager("Bob", "M001", "Sales")
print(manager.get_details())  # Output: Name: Bob, ID: M001
manager.work()  # Output: Bob is working. (Inherited from Employee)
manager.manage()  # Output: Bob is managing the Sales department.
