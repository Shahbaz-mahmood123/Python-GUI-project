# SkyLaundry - On Demand Laundry Service
# Admin Page
# This page will allow the admin to view the orders and assign the orders to the drivers
# @ Author Shahbaz 

from tkinter import *
import tkinter.messagebox

#Create window
root = Tk()


# Create Labels
lWelcome = Label(root, text="Welcome Administrator!")
labelfont = ('times', 25, "bold")
labelfont2 = ('times', 15, "italic")
lHeading = Label(root, text="Admin")
lHeading.config(font=labelfont)
lCustomer = Label(root, text="Customer")
lCustomer.config(font=labelfont2)
lBooking_ID = Label(root, text="Booking ID:")
lCustomer_ID = Label(root, text="Customer ID:")
lPickUpAddress = Label(root, text="PickUp Address:")
lDropOffAddress = Label(root, text="DropOff Address:")
lPickUp_Time = Label(root, text="PickUp Time:")
lPickUp_Date= Label(root, text="PickUp Date:")

lDriver = Label(root, text="Driver")
lDriver.config(font=labelfont2)
lDriver_ID = Label(root, text="Driver ID:")
lTelephone = Label(root, text="Telephone:")
lStatus = Label(root, text="Status:")

# Create Textfields
tfBooking_ID = Entry(root)
tfCustomer_ID = Entry(root)
tfPickUpAddress = Entry(root)
tfDropOffAddress = Entry(root)
tfPickUp_Time = Entry(root)
tfPickUp_Date = Entry(root)

tfDriver_ID = Entry(root)
tfTelephone = Entry(root)
tfStatus = Entry(root)

#Inserting Data into Textfields
with open('OrderDetails.txt', 'r') as f:
    data = f.readlines()
tfCustomer_ID.insert(0, data[0])

with open('CustomerDetails.txt', 'r') as f:
    data = f.readlines()

tfTelephone.insert(0, data[8])

with open('DriverDetails.txt', 'r') as f:
    data = f.readlines()

tfDriver_ID.insert(0, data[0])
tfBooking_ID.insert(0, data[1])
tfPickUpAddress.insert(0, data[2])
tfDropOffAddress.insert(0, data[2])
tfPickUp_Time.insert(0, data[12])
tfPickUp_Date.insert(0, data[10])
tfStatus.insert(0, data[14])


def LogOut():
    tkinter.messagebox.showinfo("LogOut", "Thank You for using Sky Laundry, Hope to see you again!")
    import skylaundryLogin


# Create Buttons
bFirstOrder = Button(root, text="First Order", fg="red", width = 15)
bNextOrder = Button(root, text="Next Order", fg="red", width = 15)
bAssignJob = Button(root, text="Assign Job to Driver", fg="red", width = 15)
bLogOut = Button(root, text="LogOut", fg="red", width = 15, command=LogOut)

###########################

###########################

#Assign components to GridLayout
#GridLayout - Labels
lHeading.grid(row=0)
lWelcome.grid(row=1)
lCustomer.grid(row=2)
lBooking_ID.grid(row=3)
lCustomer_ID.grid(row=4)
lPickUpAddress.grid(row=5)
lDropOffAddress.grid(row=6)
lPickUp_Time.grid(row=7)
lPickUp_Date.grid(row=8)
lDriver.grid(row=2, column=3)
lDriver_ID.grid(row=3, column=3)
lTelephone.grid(row=4, column=3)
lStatus.grid(row=5, column=3)

# GridLayout - TextFields
tfBooking_ID.grid(row=3, column=2)
tfCustomer_ID.grid(row=4, column=2)
tfPickUpAddress.grid(row=5, column=2)
tfDropOffAddress.grid(row=6, column=2)
tfPickUp_Time.grid(row=7, column=2)
tfPickUp_Date.grid(row=8, column=2)

tfDriver_ID.grid(row=3, column=4)
tfTelephone.grid(row=4, column=4)
tfStatus.grid(row=5, column=4)


#GridLayout - Buttons
bFirstOrder.grid(row=9)
bNextOrder.grid(row=9, column=2)
bAssignJob.grid(row=10) 
bLogOut.grid(row=10, column=2)


#############################

# Modify window features
root.title("Sky Laundry Service - Admin")
root.geometry("500x300")

# Start main event
root.mainloop()

# Notes
##Changing Header Properties - Heading = Label(text="Admin", fg="white", bg="blue")
# Assign background colour
##root.configure(background='blue')
