class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age_operator, target_age):
        results = []
        for emp in self.employees:
            if age_operator == '<' and emp.age < target_age:
                results.append(emp)
            elif age_operator == '>' and emp.age > target_age:
                results.append(emp)
            elif age_operator == '<=' and emp.age <= target_age:
                results.append(emp)
            elif age_operator == '>=' and emp.age >= target_age:
                results.append(emp)
        return results

    def search_by_name(self, target_name):
        results = []
        for emp in self.employees:
            if target_name.lower() in emp.name.lower():
                results.append(emp)
        return results

    def search_by_salary(self, salary_operator, target_salary):
        results = []
        for emp in self.employees:
            if salary_operator == '<' and emp.salary < target_salary:
                results.append(emp)
            elif salary_operator == '>' and emp.salary > target_salary:
                results.append(emp)
            elif salary_operator == '<=' and emp.salary <= target_salary:
                results.append(emp)
            elif salary_operator == '>=' and emp.salary >= target_salary:
                results.append(emp)
        return results

def main():
    database = EmployeeDatabase()

    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    search_option = int(input("Enter your choice: "))

    if search_option == 1:
        age_operator = input("Enter age operator (<, >, <=, >=): ")
        target_age = int(input("Enter target age: "))
        results = database.search_by_age(age_operator, target_age)
    elif search_option == 2:
        target_name = input("Enter target name: ")
        results = database.search_by_name(target_name)
    elif search_option == 3:
        salary_operator = input("Enter salary operator (<, >, <=, >=): ")
        target_salary = int(input("Enter target salary: "))
        results = database.search_by_salary(salary_operator, target_salary)
    else:
        print("Invalid choice!")
        return

    if results:
        print("\nSearch Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("\nNo results found.")

if __name__ == "__main__":
    main()
