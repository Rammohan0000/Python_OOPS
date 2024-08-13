class Employee:
    def __init__(self, name, employee_id):
        self.name = name
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
        
        # Creating an instance of Employee
employee = Employee("Alice", "E001")
print(employee.get_details())  # Output: Name: Alice, ID: E001
employee.work()  # Output: Alice is working.

# Creating an instance of Manager
manager = Manager("Bob", "M001", "Sales")
print(manager.get_details())  # Output: Name: Bob, ID: M001
manager.work()  # Output: Bob is working. (Inherited method)
manager.manage()  # Output: Bob is managing the Sales department.

