from connection.DBconnect import DBConnect
from model.employee import Employee
from Library.LibraryCRUD import LibraryCRUD

def menu():
    db = DBConnect(host="localhost", user="root", password="root", database="employeemanagement")
    db.connect()
    crud = LibraryCRUD(db)

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            doj = input("Enter date of joining (YYYY-MM-DD): ")
            # created_on = "2024-11-25"  # Example created_on date
            employee = Employee(name, int(age), doj)
            print(crud.Add_employee(employee))

        # elif choice == "2":
        #     employees = crud.read_employees()
        #     print(employees)

        # elif choice == "3":
        #     name = input("Enter the name of the employee to update: ")
        #     updated_info = {}
        #     age = input("Enter new age (leave blank to skip): ")
        #     doj = input("Enter new DOJ (leave blank to skip): ")

        #     if age:
        #         updated_info["age"] = int(age)
        #     if doj:
        #         updated_info["doj"] = doj

        #     print(crud.update_employee(name, updated_info))

        # elif choice == "4":
        #     name = input("Enter the name of the employee to delete: ")
        #     print(crud.delete_employee(name))

        # elif choice == "5":
        #     print("Exiting application.")
        #     db.disconnect()
        #     break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
