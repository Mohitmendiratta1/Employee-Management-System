import pyodbc
from tkinter import messagebox

# Global connection and cursor
conn = None
mycursor = None

def connect_database():
    global conn, mycursor
    try:
        # Connect to 'employee_data' database
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server=LAPTOP-06A48PU7;'   
                              'Database=employee_data;'   
                              'UID=admin;'                
                              'PWD=Admin@2024;')          
        mycursor = conn.cursor()
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong. Please check the SQL Server connection.\nError: {str(e)}')

    # Create table if it doesn't exist
    try:
        mycursor.execute('''
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'data')
            CREATE TABLE data (
                Id VARCHAR(20),
                name VARCHAR(50),
                phone VARCHAR(15),
                Role VARCHAR(50),
                Gender VARCHAR(20),
                Salary VARCHAR(10)
            )
        ''')
        conn.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to create or check the table.\nError: {str(e)}')

def insert(id, name, phone, role, gender, salary):
    global mycursor, conn
    try:
        if conn is None or mycursor is None:
            connect_database()  # Ensure connection is established
        mycursor.execute('INSERT INTO data (Id, name, phone, Role, Gender, Salary) VALUES (?, ?, ?, ?, ?, ?)', 
                         (id, name, phone, role, gender, salary))
        conn.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to insert data.\nError: {str(e)}')

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE Id = ?', (id,))
    result = mycursor.fetchone()
    return result[0] > 0  # Returning True if ID exists, else False

def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    global mycursor, conn  # Ensure we're using the correct cursor
    try:
        if conn is None or mycursor is None:
            connect_database()  # Ensure connection is established
        mycursor.execute('UPDATE data SET name=?, phone=?, Role=?, Gender=?, Salary=? WHERE Id=?', 
                         (new_name, new_phone, new_role, new_gender, new_salary, id))
        conn.commit()  # Commit the transaction
        print(f"Successfully updated employee with ID: {id}")
    except Exception as e:
        messagebox.showerror('Error', f'Failed to update data.\nError: {str(e)}')

def delete(id):
    try:
        mycursor.execute('DELETE FROM data WHERE Id = ?', (id,))  # Use tuple for parameters
        conn.commit()  # Commit the transaction
        print(f"Successfully deleted employee with ID: {id}")  # Optional for debugging
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete data.\nError: {str(e)}')  # Show error message if any issue occurs

def search(option, value):
    try:
        mycursor.execute(f'SELECT * FROM data WHERE {option} = ?', (value.strip("'"),))  # Use a tuple
        result = mycursor.fetchall()
        return result
    except Exception as e:
        messagebox.showerror('Error', f'Failed to search data.\nError: {str(e)}')

def deleteall_record():
    try:
        mycursor.execute('TRUNCATE TABLE data')  # Truncate to remove all records
        conn.commit()  # Commit the changes to the database
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete all records.\nError: {str(e)}')


# Connect directly to the database
connect_database()
