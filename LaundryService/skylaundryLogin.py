# SkyLaundry - On Demand Laundry Service
# Login Page
# This page will allow the user to login if their username and password is correct
# @ Author Shahbaz

from tkinter import *
import tkinter.messagebox

# Create window
root = Tk()


#Functions
def logIn():
    # For loop 1 for Customer login
    username = tfUsername.get()
    password = tfPassword.get()
    customer = open("CustomerLogin.txt", "r")
    admin = open("AdminLogin.txt", "r")
    driver = open("DriverLogin.txt", "r")
    for line in customer.readlines():
        un, pw = line.strip().split("|")
        if username == un and password == pw:
            tkinter.messagebox.showinfo("Login", "Login: Customer")
            import skylaundryCustomer.py

    # For loop 2 for Admin login       
    for line in admin.readlines():
        un, pw = line.strip().split("|")
        if username == un and password == pw:
            tkinter.messagebox.showinfo("Login", "Login: Admin")
            import skylaundryAdmin.py
            
    # For loop 3 for Driver login
    for line in driver.readlines():
        un, pw = line.strip().split("|")
        if username == un and password == pw:
            tkinter.messagebox.showinfo("Login", "Login: Driver")
            import skylaundryDriver.py
      
 
def bRegisterMessage():
    tkinter.messagebox.showinfo("Login", "Redirecting you to Register Page")
    import skylaundryRegister
    

########################

# Create Labels
lWelcome = Label(root, text="Welcome! Please Sign In...")
lUsername = Label(root, text="Username:")
lPassword = Label(root, text="Password:")

# Create TextFields
tfUsername = Entry(root)
tfPassword = Entry(root)

# Create Buttons
bRegister = Button(root, text="Register", fg="red", command=bRegisterMessage)
bSubmit = Button(root, text="Login", fg="red", command=logIn)

###########################

# Assign components to GridLayout
#GridLayout - Labels
lWelcome.grid(row=0)
lUsername.grid(row=1)
lPassword.grid(row=2)

#GridLayout - TextFields
tfUsername.grid(row=1, column=2)
tfPassword.grid(row=2, column=2)

#GridLayout - Buttons
bRegister.grid(row=4)
bSubmit.grid(row=4, column=2)

#############################

# Modify window features
root.title("Sky Laundry Service - Login")
root.geometry("300x125")

# Start main event
root.mainloop()







####### NOTES #######


# Create Frame
#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

# Create buttons and set positions
#Register = Button(bottomFrame, text="Register", fg="red")
#bSubmit = Button(bottomFrame, text="Submit", fg="red")
#bRegister.pack(side=LEFT)
#bSubmit.pack(side=RIGHT)

# Widgets
#ne = Label(root, text="One", bg="red", fg="white")
#one.pack()
#two = Label(root, text="Two", bg="green", fg="black")
#two.pack(fill=X)
#three = Label(root, text="Two", bg="blue", fg="white")
#three.pack(side=LEFT, fill=Y)

# Modify window features
#root.title("Sky Laundry Service - Login")
#root.geometry("300x200")


