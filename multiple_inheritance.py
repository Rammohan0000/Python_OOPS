class Contact:
    def __init__(self, email):
        self.email = email

    def get_email(self):
        return self.email

class Employee(Person, Contact):
    def __init__(self, name, employee_id, email):
        Person.__init__(self, name)
        Contact.__init__(self, email)
        self.employee_id = employee_id

    def work(self):
        print(f"{self.name} is working.")

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Email: {self.email}"

class Manager(Employee):
    def __init__(self, name, employee_id, email, department):
        super().__init__(name, employee_id, email)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing the {self.department} department.")

# Creating an instance of Manager
manager = Manager("Bob", "M001", "bob@example.com", "Sales")
print(manager.get_details())  # Output: Name: Bob, ID: M001, Email: bob@example.com
manager.work()  # Output: Bob is working. (Inherited from Employee)
manager.manage()  # Output: Bob is managing the Sales department.
