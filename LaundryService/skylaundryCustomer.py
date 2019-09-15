# SkyLaundry 
# Customer Page

from tkinter import *
import tkinter.messagebox

# Creating the window
root = Tk()




#attributes
def writeText():
    outFile = open("OrderDetails.txt", "wt")
    outFile.write("" + tfCustomerID.get())
    outFile.write("\n" + tfFirst_Name.get())
    outFile.write("\n" + tfSurname.get())
    outFile.write("\n" + tfAddress_Line_1.get())
    outFile.write("\n" + tfAddress_Line_2.get())
    outFile.write("\n" + tfTown.get())
    outFile.write("\n" + tfCounty.get())
    outFile.write("\n" + tfPostcode.get())
    outFile.write("\n" + tfEmail.get())
    outFile.write("\n" + tfTelephone.get())
    outFile.write("\n" + tfBookingID.get())
    outFile.write("\n" + tfScheduled_Collection_Time.get())
    outFile.write("\n" + tfScheduled_Collection_Date.get())
    outFile.write("\n **************************")
    tkinter.messagebox.showinfo("Update", "Updating details for order")

def goBack():
    tkinter.messagebox.showinfo("LogOut", "Thank You for using Sky Laundry, Hope we see you again!")
    import skylaundryLogin

def makeOrder():
    tkinter.messagebox.showinfo("Ordering", "Redirecting to Order Page")
    import skylaundryOrder
    

    

# Creating attributes
lCustomer = Label(root, text="Customer")
labelfont = ('times', 25, "bold")
labelfont2 = ('times', 15, "italic")
lCustomer.config(font=labelfont)
lwelcomeCustomer = Label(root, text="Welcome Customer")
lwelcomeCustomer.config(font=labelfont2)
lCustomerID = Label(root, text="Customer ID:")
lFirst_Name= Label(root, text="First Name:")
lSurname = Label(root, text="Surname:")
lAddress_Line_1 = Label(root, text="Address Line 1:")
lAddress_Line_2 = Label(root, text="Address Line 2:")
lTown = Label(root, text="Town:")
lCounty = Label(root, text="County:")
lPostcode = Label(root, text="Postcode:")
lEmail = Label(root, text="Email:")
lTelephone = Label(root, text="Telephone:")
lBookingID = Label(root, text="Booking ID:")
lScheduled_Collection_Time = Label(root, text="Scheduled Collection Time:")
lScheduled_Collection_Date = Label(root, text="Scheduled Collection Date:")


#Obtaining Data

              
# Creating TextFields
tfCustomerID = Entry(root)
tfFirst_Name = Entry(root)
tfSurname = Entry(root)
tfAddress_Line_1 = Entry(root)
tfAddress_Line_2 = Entry(root)
tfTown = Entry(root)
tfCounty = Entry(root)
tfPostcode = Entry(root)
tfEmail = Entry(root)
tfTelephone = Entry(root)
tfBookingID = Entry(root)
tfScheduled_Collection_Time = Entry(root)
tfScheduled_Collection_Date = Entry(root)

# Inserting Information from textfield
with open('CustomerDetails.txt', 'r') as f:
    data = f.readlines()

tfCustomerID.insert(0, "C001")
tfFirst_Name.insert(0, data[0])
tfSurname.insert(0, data[1])
tfAddress_Line_1.insert(0, data[2])
tfAddress_Line_2.insert(0, data[3])
tfTown.insert(0, data[4])
tfCounty.insert(0, data[5])
tfPostcode.insert(0, data[6])
tfEmail.insert(0, data[7])
tfTelephone.insert(0, data[8])
tfBookingID.insert(0, "B001")




### Create Buttons
makeOrder = Button(root, text="Make Order", fg="red", command=makeOrder)
updateDetails = Button(root, text="Update Details", fg="red", command=writeText)
logOut = Button(root, text="Log Out", fg="red", command=goBack)

#Layout
lCustomer.grid(row=0)
lwelcomeCustomer.grid(row=1)
lCustomerID.grid(row=2)
lFirst_Name.grid(row=3)
lSurname.grid(row=4)
lAddress_Line_1.grid(row=5)
lAddress_Line_2.grid(row=6)
lTown.grid(row=7)
lCounty.grid(row=8)
lPostcode.grid(row=9)
lEmail.grid(row=10)
lTelephone.grid(row=11)
lBookingID.grid(row=12)
lScheduled_Collection_Time.grid(row=13)
lScheduled_Collection_Date.grid(row=14)

#GridLayout - TextFields 
tfCustomerID.grid(row=2, column=2)
tfFirst_Name.grid(row=3, column=2)
tfSurname.grid(row=4, column=2)
tfAddress_Line_1.grid(row=5, column=2)
tfAddress_Line_2.grid(row=6, column=2)
tfTown.grid(row=7, column=2)
tfCounty.grid(row=8, column=2)
tfPostcode.grid(row=9, column=2)
tfEmail.grid(row=10, column=2)
tfTelephone.grid(row=11, column=2)
tfBookingID.grid(row=12, column=2)
tfScheduled_Collection_Time.grid(row=13, column=2)
tfScheduled_Collection_Date.grid(row=14, column=2)


###GridLayout - Buttons
makeOrder.grid(row=15)
updateDetails.grid(row=15, column=2)
logOut.grid(row=16)


# Modify window features
root.title("Sky Laundry Driver - Customer")
root.geometry("300x400")

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


