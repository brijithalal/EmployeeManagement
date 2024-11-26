class LibraryCRUD:
    def __init__(self):
        self.db_connection = db_connection
    
    def Add_employee(self, employee):
        try:
            cursor = self.db_connection.connection.cursor()
            query = """
                INSERT INTO employee (emp_name, age, doj, createdon, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (employee.name, employee.age, employee.doj, employee.created_on, employee.is_active))
            self.db_connection.connection.commit()
            return f"Employee {employee.name} added successfully."
        except Error as e:
            return f"Error while adding employee: {e}"