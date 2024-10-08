class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.bonus = 0

# Sample list of employees
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("Charlie", 70000)
]

# Calculate bonuses
for employee in employees:
    employee.bonus = employee.salary * 0.1

# Print out the results
for employee in employees:
    print(f"{employee.name}: Bonus = {employee.bonus}")
