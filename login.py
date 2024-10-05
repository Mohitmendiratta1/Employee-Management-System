from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All field are required!!')
    elif usernameEntry.get()=='mohit' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful!!')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong credential!!')
        root.destroy()
        import ems

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
# login.py
image = CTkImage(Image.open('assets/cover.jpg'), size=(930, 478))

imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#cad6e2', text_color='black',font=('Goudy Old Style',20,'bold') )
headinglabel.place(x=20,y=100)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',fg_color='#f0f0f0',text_color='black',bg_color='#cad6e2',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password',fg_color='#f0f0f0',text_color='black',bg_color='#cad6e2',width=180,show='*')
passwordEntry.place(x=50,y=200)

loginbutton = CTkButton(root,text='Login',bg_color='#cad6e2',cursor='hand2', command=login)
loginbutton.place(x=70,y=250)

root.mainloop()

