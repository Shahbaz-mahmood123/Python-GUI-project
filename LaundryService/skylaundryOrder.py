#Emil Sofrone Customer GUI
from tkinter import *
import tkinter.messagebox

##root = Tk()

#image

root = tkinter.Toplevel()

img = PhotoImage(file = ("laundry.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "none", expand = "no")
panel.grid(row=6,column=0)

#

file = open("Customer.txt", "w")
def textW():
    outFile = open("Customer.txt", "wt")


def CancelOrder():
    outFile=open("Customer.txt", "w")
    outFile.write("")
    tkinter.messagebox.showinfo("Cancel Order", "Your order has been canceled")

def ViewOrder():
    outFile = open('Customer.txt', 'r')
    v = outFile.read()
    print (v)
   
    
def MakeOrder():
    outFile=open("Customer.txt", "w")
    outFile.write("" + tMakeOrder.get())
    tkinter.messagebox.showinfo("Make Order", "Order has been placed. Thank you!")

#Labels
lMakeOrder = Label(root, text="Make an order")
lfont=('times', 15, 'bold')
font=('times',15,'bold')
lMakeOrder.config(font=lfont)
#TextFields
tMakeOrder = Entry(root,width=31)

#Buttons
bMakeOrder = Button(root, text="Make order",bg="black",width=15,fg="green", command=MakeOrder)
bCancelOrder = Button(root, text="Cancel order",width=15,bg="black",fg="green", command=CancelOrder)
bViewOrder = Button(root, text="View orders",width=15,bg="black",fg="green", command=ViewOrder)
bMakeOrder.config(font=font)
bCancelOrder.config(font=font)
bViewOrder.config(font=font)
#Position
lMakeOrder.grid(row=0,column=0)


tMakeOrder.grid(row=1, column=0)


bMakeOrder.grid(row=2)
bViewOrder.grid(row=3)
bCancelOrder.grid(row=4)

#Window stuff
root.title("Sky Laundry Service - Order")
root.geometry("770x530")

root.mainloop()


