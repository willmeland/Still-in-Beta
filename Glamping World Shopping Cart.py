from tkinter import * # Import tkinter
import tkinter as ttk
from PIL import ImageTk, Image # Usage of PIL to import GW Logo

class ShoppingCart:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Glamping World Shopping Cart") # Set title of a window
        window.geometry("463x450") # Set dimensions of window
        window.configure(background = 'white') # Set color of window

        self.Yes = IntVar() # Assign int variable for 'Yes' checkbutton
       

        # Assign variables for drop down boxes
        tkvar = StringVar(window)
        tkvar2 = StringVar(window)
        

        # Set up labels for the shopping cart in the left column of the window, align labels left (Sticky=W)
        choices = {'Sleeping Bag - $15.00', "Lantern - $10.00", "Tent - $20.00", "Kayak - $25.00", "Hiking Boots - $12.00", "Rain Jacket - $11.00"}
        tkvar.set('Choose Product')
        popupMenu = OptionMenu(window, tkvar, *choices)
        Label(window, text = "Choose Product", bg='white').grid(row = 2, column = 1, sticky = W)
        popupMenu.grid(row = 2, column = 3)

        choices2 = {'Sleeping Bag - $15.00', "Lantern - $10.00", "Tent - $20.00", "Kayak - $25.00", "Hiking Boots - $12.00", "Rain Jacket - $11.00"}
        tkvar2.set('Choose Product 2')
        popupMenu = OptionMenu(window, tkvar2, *choices2)
        Label(window, text = "Choose Product 2", bg='white').grid(row = 5, column = 1, sticky = W)
        popupMenu.grid(row = 5, column = 3)

        Label(window, text = "Quantity", bg='white').grid(row = 3, column = 1, sticky = W)
        self.Quantity = IntVar()
        Entry(window, textvariable = self.Quantity, justify = RIGHT).grid(row = 3, column = 3, sticky = E)
        
        Label(window, text = "Customer ID", bg='white').grid(row = 1, column = 1, sticky = W)
        self.CustomerID = StringVar()
        Entry(window, textvariable = self.CustomerID, justify = RIGHT).grid(row = 1, column = 3, sticky = E)
        
        Label(window, text = "Price of Product ($)", bg='white').grid(row = 4, column = 1, sticky = W)
        self.Price = StringVar()
        Entry(window, textvariable = self.Price, justify = RIGHT).grid(row = 4, column = 3, sticky = E)


        Label(window, text = 'Quantity', bg='white').grid(row=6, column = 1, sticky = W)
        self.Quantity2 = IntVar()
        Entry(window, textvariable = self.Quantity2, justify = RIGHT).grid(row=6, column = 3, sticky = E )

        Label(window, text = "Price of Product ($)", bg='white').grid(row = 7, column = 1, sticky = W)
        self.Price2 = StringVar()
        Entry(window, textvariable = self.Price2, justify = RIGHT).grid(row = 7, column = 3, sticky = E)

        Label(window, text = "Discount (2% for item in stock over 120 days)", bg='white').grid(row = 8, column = 1, sticky = W)

        Label(window, text = "Sales Tax 13% ($)", bg='white').grid(row = 10 , column = 1, sticky = W)

        Label(window, text = "SubTotal ($)", bg='white').grid(row = 9, column = 1, sticky = W)

        Label(window, text = "Total Order Cost ($)", bg='white').grid(row = 11, column = 1, sticky = W)
        
        #set up the output area for the shopping cart, using three labels, a check button; the check button calls the function Yes which applies a 2% discount to the order, and a button; the button calls the function computePayment when it's clicked
        self.SalesTax = StringVar()
        Label(window, textvariable = self.SalesTax, bg='white').grid(row = 10, column = 3, sticky = E)
        self.SubTotal = StringVar()
        Label(window, textvariable = self.SubTotal, bg='white').grid(row = 9, column = 3, sticky = E)
        self.TotalCost = StringVar()
        Label(window, textvariable = self.TotalCost, bg='white').grid(row = 11, column = 3, sticky = E)

        Button(window, text="Help?", bg="Yellow").grid(row=12, column = 1, sticky= W)

        C1 = Checkbutton(window, text="Yes", command = self.Yes, onvalue = 1, offvalue = 0).grid(row = 8, column = 3, sticky = N)
        
        Button(window, text = "Compute Payment", bg="cornsilk1", command = self.computePayment).grid(row = 12, column = 3, sticky = E)
        photo = PhotoImage(file="C:\\Users\\Teddy Fotos\\Desktop\\python (1)\\GWlogo.gif")
        imglabel = Label(window, image=photo).grid(row = 0, column = 1)

        window.mainloop() # Create an event loop to display the window

    def computePayment(self):
        SalesTax = float(self.Price.get()) * int(self.Quantity.get()) * .13 + float(self.Price2.get()) * int(self.Quantity2.get()) * .13 #Calculate SalesTax
        self.SalesTax.set(format(SalesTax, '10.2f')) #Output SalesTax amount formatted to two decimal places
        SubTotal = float(self.Price.get()) * int(self.Quantity.get())  + float(self.Price2.get()) * int(self.Quantity2.get())  #Calculate SubTotal 
        self.SubTotal.set(format(SubTotal, '10.2f'))   #Output SubTotal formatted to two decimal places 
        TotalCost = float(self.Price.get()) * int(self.Quantity.get()) * .13 + float(self.Price.get()) * int(self.Quantity.get()) + float(self.Price2.get()) * int(self.Quantity2.get()) * .13 + float(self.Price2.get()) * int(self.Quantity2.get()) #Calculate TotalCost
        self.TotalCost.set(format(TotalCost, '10.2f')) #Output TotalCost formatted to two decimal places


    def Yes(self):
        if self.Yes.get() == 1:
            SubTotal = float(self.Price.get()) * int(self.Quantity.get()) + float(self.Price2.get()) * int(self.Quantity2.get()) - float(self.Price.get()) * int(self.Quantity.get())  + float(self.Price2.get()) * int(self.Quantity2.get()) * .02
            self.Subtotal.set(format(Subtotal, '10.2f'))
    
    
ShoppingCart()  # Create GUI 