# SkyLaundry 
# Driver Page

from tkinter import *
import tkinter.messagebox

# Creating the window
root = Tk()


#attributes
def completeJob():
    outFile = open("DriverDetails.txt", "wt")
    outFile.write("" + tfDriverID.get())
    outFile.write("\n" + tfBookingID.get())
    outFile.write("\n" + tfPickUpAddress1.get())
    outFile.write("\n" + tfPickUpTown.get())
    outFile.write("\n" + tfPickUpCounty.get())
    outFile.write("\n" + tfPickUpPostcode.get())
    outFile.write("\n" + tfPickUpDate.get())
    outFile.write("\n" + tfPickUpTime.get())
    outFile.write("\n" + tfJobStatus.get())
    outFile.write("\n **************************")
    tkinter.messagebox.showinfo("Job Complete" , "Job set to complete")

def logOut():
    import skylaundryLogin.py
    

# Creating labels
lDriver = Label(root, text="Driver")
driverfont = ('times', 25 , "bold")
driverfont2 = ('times', 15, "italic")
lDriver.config(font=driverfont)
lwelcomeDriver = Label(root, text="Welcome Driver")
lwelcomeDriver.config(font=driverfont2)
lDriverID = Label(root, text="Driver ID:")
lBookingID = Label(root, text="Booking ID:")
lPickUpAddress1 = Label(root, text="Pick Up Address:")
lPickUpTown = Label(root, text="Town:")
lPickUpCounty = Label(root, text="County:")
lPickUpPostcode= Label(root, text="Postcode:")
lPickUpDate = Label(root, text="Pick up Date:")
lPickUpTime = Label(root, text="Pick up Time:")
lJobStatus = Label(root, text="Job Status:")

# Creating TextFields
tfDriverID = Entry(root)
tfBookingID = Entry(root)
tfPickUpAddress1 = Entry(root)
tfPickUpTown = Entry(root)
tfPickUpCounty = Entry(root)
tfPickUpPostcode = Entry(root)
tfPickUpDate = Entry(root)
tfPickUpTime = Entry(root)
tfJobStatus = Entry(root)

# Obtaining data for TextFields
with open('OrderDetails.txt', 'r') as f:
    data = f.readlines()

tfDriverID.insert(0, "D001")
tfBookingID.insert(0, "B001")
tfPickUpAddress1.insert(0, data[5])
tfPickUpTown.insert(0, data[9])
tfPickUpCounty.insert(0, data[11])
tfPickUpPostcode.insert(0, data[13])
tfPickUpTime.insert(0, data[20])
tfPickUpDate.insert(0, data[21])
tfJobStatus.insert(0, "In Progress")

# Create Buttons
viewJobs = Button(root, text="View Jobs", fg="red")
setJobAsComplete = Button(root, text="Set Job as Complete", fg="red", command=completeJob)
logOut = Button(root, text="Log Out", fg="red", command=logOut)

#Layout
lDriver.grid(row=0)
lwelcomeDriver.grid(row=1)#, column=2)
lDriverID.grid(row=2)
lBookingID.grid(row=3)
lPickUpAddress1.grid(row=4)
lPickUpTown.grid(row=5)
lPickUpCounty.grid(row=6)
lPickUpPostcode.grid(row=7)
lPickUpDate.grid(row=8)
lPickUpTime.grid(row=9)
lJobStatus.grid(row=10)

#GridLayout - TextFields 
tfDriverID.grid(row=2, column=2)
tfBookingID.grid(row=3, column=2)
tfPickUpAddress1.grid(row=4, column=2)
tfPickUpTown.grid(row=5, column=2)
tfPickUpCounty.grid(row=6, column=2)
tfPickUpPostcode.grid(row=7, column=2)
tfPickUpDate.grid(row=8, column=2)
tfPickUpTime.grid(row=9, column=2)
tfJobStatus.grid(row=10, column=2)

#GridLayout - Buttons
viewJobs.grid(row=18)
setJobAsComplete.grid(row=18, column=2)
logOut.grid(row=19)


# Modify window features
root.title("Sky Laundry Driver - Driver")
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


