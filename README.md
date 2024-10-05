# Employee-Management-System
The Employee Management System (EMS) is a desktop application designed to streamline and simplify the process of managing employee records within an organization. Built with Python's CustomTkinter for a modern and intuitive graphical user interface (GUI), the system allows users to add, view, update, search, and delete employee records efficiently.

# Core Features:
Add Employee: Allows the user to input details like employee ID, name, phone number, role, gender, and salary. The system ensures that all fields are filled and prevents duplicate employee IDs by querying the MSSQL database.

Update Employee: Enables the user to modify employee details such as contact information, role, or salary, with real-time updates to the MSSQL database.

Delete Employee: Provides functionality to remove a single employee record or all records at once, with proper confirmation dialogs and deletion reflected in the database.

Search Employee: Users can search for employees based on multiple criteria, including ID, name, phone number, role, gender, and salary, using optimized SQL queries for fast retrieval.

View All Employees: Displays all employee records in a structured table format using Treeview, with the ability to scroll through a large dataset easily.

Responsive and Modern UI: The use of CustomTkinter ensures a sleek and user-friendly interface, optimized for both performance and usability.

# Technologies Used:
Python: The primary programming language for the application logic.

CustomTkinter: Used for building a modern, customizable GUI with responsive design elements.

Microsoft SQL Server (MSSQL): The relational database system for managing employee data, with SQL queries handling operations like insertion, updates, deletions, and searches.

PIL (Pillow): Utilized for image handling, allowing the display of images within the application (e.g., background or logos).

ttk Treeview: To present employee data in a tabular format with sortable columns and integrated scrollbar functionality.

# Required Python Modules:
customtkinter: For building the modern, customizable user interface.
Install using: pip install customtkinter

Pillow (PIL): For handling image loading and manipulation (e.g., loading background images or logos).
Install using: pip install Pillow

tkinter: Part of the standard Python library, used to create the main GUI framework.

pyodbc: Required for connecting to Microsoft SQL Server (MSSQL) databases and executing SQL queries.
Install using: pip install pyodbc

tkinter.ttk: For using the Treeview widget, which allows you to display data in a table-like format. This is part of the standard tkinter library.

messagebox: Also part of the tkinter library, used to display error, warning, and information pop-up dialogs.

