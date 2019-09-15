# SkyLaundry - On Demand Laundry Service
# Register Page
# This page will allow the user to register and will output the data to a text file
# @ Author James

from tkinter import *
import tkinter.messagebox

# Create window
root = Tk()


#Functions
# Gets text from Entry widgets and outputs to textfile
def writeText():
    outFile = open("CustomerLogin.txt", "wt")
    outFile.write("" + tfUsername.get())
    outFile.write("|" + tfPassword.get())

    outFile = open("CustomerDetails.txt", "wt")
    outFile.write("" + tfFirstName.get())
    outFile.write("\n" + tfSurname.get())
    outFile.write("\n" + tfAddress1.get())
    outFile.write("\n" + tfAddress2.get())
    outFile.write("\n" + tfTown.get())
    outFile.write("\n" + tfCounty.get())
    outFile.write("\n" + tfPostcode.get())
    outFile.write("\n" + tfEmail.get())
    outFile.write("\n" + tfTelephone.get())
    outFile.write("\n **************************")

    tkinter.messagebox.showinfo("Login", "Thank You, Please now Sign In")

def goBack():
    import skylaundryLogin
    

# Create Labels
lRegister = Label(root, text="Please Register...")
lFirstName = Label(root, text="First Name:")
lSurname = Label(root, text="Surname:")
lAddress1 = Label(root, text="Address Line 1:")
lAddress2 = Label(root, text="Address Line 2:")
lTown = Label(root, text="Town:")
lCounty= Label(root, text="County:")
lPostcode = Label(root, text="Postcode:")
lEmail = Label(root, text="Email:")
lTelephone = Label(root, text="Telephone:")
lUsername = Label(root, text="Username:")
lPassword = Label(root, text="Password:")

# Create TextFields
tfFirstName = Entry(root)
tfSurname = Entry(root)
tfAddress1 = Entry(root)
tfAddress2 = Entry(root)
tfTown = Entry(root)
tfCounty = Entry(root)
tfPostcode = Entry(root)
tfEmail = Entry(root)
tfTelephone = Entry(root)
tfUsername = Entry(root)
tfPassword = Entry(root)

# Create Buttons
bGoBack = Button(root, text="Go Back", fg="red", command=goBack)
bSubmit = Button(root, text="Submit", fg="red", command=writeText)

# Assign components to GridLayout
#GridLayout - Labels
lRegister.grid(row=0)
lFirstName.grid(row=1)
lSurname.grid(row=2)
lAddress1.grid(row=3)
lAddress2.grid(row=4)
lTown.grid(row=5)
lCounty.grid(row=6)
lPostcode.grid(row=7)
lEmail.grid(row=8)
lTelephone.grid(row=9)
lUsername.grid(row=10)
lPassword.grid(row=11)

#GridLayout - TextFields
tfFirstName.grid(row=1, column=2)
tfSurname.grid(row=2, column=2)
tfAddress1.grid(row=3, column=2)
tfAddress2.grid(row=4, column=2)
tfTown.grid(row=5, column=2)
tfCounty.grid(row=6, column=2)
tfPostcode.grid(row=7, column=2)
tfEmail.grid(row=8, column=2)
tfTelephone.grid(row=9, column=2)
tfUsername.grid(row=10, column=2)
tfPassword.grid(row=11, column=2)

#GridLayout - Buttons
bGoBack.grid(row=12)
bSubmit.grid(row=12, column=2)


# Modify window features
root.title("Sky Laundry Service - Login")
root.geometry("300x300")

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


