from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

#Functions

def delete_all():
    result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
    if result:
        try:
            database.deleteall_record()  # Call the function to delete all records
            treeview_data()  # Refresh the treeview to reflect changes
            messagebox.showinfo('Success', 'All records deleted successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete records.\nError: {str(e)}')


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')


def insert(id, name, phone, role, gender, salary):
    global mycursor, conn
    try:
        if conn is None or mycursor is None:
            database()  # Ensure connection is established
        mycursor.execute('INSERT INTO data (Id, name, phone, Role, Gender, Salary) VALUES (?, ?, ?, ?, ?, ?)', 
                         (id.strip("'"), name.strip("'"), phone.strip("'"), role.strip("'"), gender.strip("'"), salary.strip("'")))
        conn.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to insert data.\nError: {str(e)}')


def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error', 'Please select an option')
    else:
        searched_data = database.search(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children())  # Clear the treeview
        
        for employee in searched_data:
            # Ensure that no single quotes are displayed
            formatted_employee = tuple(str(field).replace("'", "") for field in employee)
            tree.insert('', 'end', values=formatted_employee)  # Use 'end' for insertion



def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear_fields()
        messagebox.showinfo('Success','Data is deleted')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update!')
    else:
        # Get the selected item's values
        item = tree.item(selected_item)
        employee_id = item['values'][0]  # Assuming the first column is ID

        # Retrieve updated values from the input fields
        new_name = nameEntry.get()
        new_phone = phoneEntry.get()
        new_role = roleBox.get()
        new_gender = genderBox.get()  # Use get() method here
        new_salary = salaryEntry.get()

        # Call the update function in the database module
        try:
            database.update(employee_id, new_name, new_phone, new_role, new_gender, new_salary)
            messagebox.showinfo('Success', 'Data is updated')
            treeview_data()  # Refresh the treeview
            clear_fields()  # Clear the input fields
        except Exception as e:
            messagebox.showerror('Error', f'Failed to update data: {str(e)}')



def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear_fields()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def treeview_data():
    for item in tree.get_children():
        tree.delete(item)
    employees = database.fetch_employees()  # Fetch employee data
    for employee in employees:
        formatted_employee = tuple(str(field).strip("'") for field in employee)
        tree.insert('', 'end', values=formatted_employee)



def clear_fields(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, 'end')
    nameEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    salaryEntry.delete(0, 'end')
    roleBox.set('')
    genderBox.set('')


def add_employee():
    # Check if any fields are empty
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required!!')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id Already Exists')
    else:
        try:
            # Call the insert function from the database module
            database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
            messagebox.showinfo('Success', 'Employee added successfully!')
            clear_fields()  # Clear input fields after successful addition
            treeview_data()  # Refresh treeview data after adding employee
        except Exception as e:
            messagebox.showerror('Error', f'Failed to add employee: {str(e)}')



     

#GUI Part
root=CTk()
root.geometry('930x580+100+100')
root.resizable(False,False)
root.title('Employee Management System')
root.configure(fg_color='#161c30')
# ems.py
logo = CTkImage(Image.open('assets/bg.jpg'), size=(930, 158))

logoLabel=CTkLabel(root,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(root,fg_color='#161c30') 
leftFrame.grid(row=1, column=0)

idLabel=CTkLabel(leftFrame,text='Id', font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='W')
idEntry=CTkEntry(leftFrame, font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name', font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='W')
nameEntry=CTkEntry(leftFrame, font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone', font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='W')
phoneEntry=CTkEntry(leftFrame, font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role', font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='W')
roleEntry=CTkEntry(leftFrame, font=('arial',15,'bold'),width=180)
roleEntry.grid(row=3,column=1)

role_options=['Web Developer','Cloud Architect', 'Technical Writer', 'Network Engineer', 'DevOps Engineer', 'Data Scientist', 'Business Analyst', 'IT Consultant', 'UI/UX Designer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',18,'bold'),state='readonly')
roleBox.grid(row=3,column=1)

genderLabel=CTkLabel(leftFrame,text='Gender', font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='W')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',18,'bold'),state='readonly')
genderBox.grid(row=4,column=1)

salaryLabel=CTkLabel(leftFrame,text='Salary', font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='W')
salaryEntry=CTkEntry(leftFrame, font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(root,fg_color='#dadada')
rightFrame.grid(row=1, column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

scrollbar = ttk.Scrollbar(rightFrame, orient='vertical')  # Initialize scrollbar
scrollbar.grid(row=1, column=4, sticky='ns')  # Place scrollbar in grid


tree = ttk.Treeview(rightFrame, height=13, yscrollcommand=scrollbar.set)  # Set the yscrollcommand
tree.grid(row=1, column=0, columnspan=4, sticky='nsew')  # Add sticky options for proper resizing

# ... tree configuration ...
tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')

tree.column('Id', width=100, anchor='center')
tree.column('Name', width=160, anchor='center')
tree.column('Phone', width=160, anchor='center')
tree.column('Role', width=200, anchor='center')
tree.column('Gender', width=100, anchor='center')
tree.column('Salary', width=140, anchor='center')

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'), bg='#161c30', fg='white')
style.configure('Treeview', font=('Arial', 15, 'bold'), rowheight=30, background='#161c30', foreground='white')

# Create the scrollbar
scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)  # Set the command
scrollbar.grid(row=1, column=4, sticky='ns')  # Position the scrollbar

# Configure the treeview to use the scrollbar
tree.configure(yscrollcommand=scrollbar.set)  # Link scrollbar and treeview


buttonFrame=CTkFrame(root,fg_color='#161c30')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',18,'bold'),width=160,corner_radius=15,command=lambda: clear_fields(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',18,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5, padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',18,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',18,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5)

deleteallButton=CTkButton(buttonFrame,text='DeleteAll Employee',font=('arial',18,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5)

treeview_data()

root.bind('<ButtonRelease>',selection)

root.mainloop()