# Libraries
from customtkinter import *
import qrcode as qr
from PIL import Image
from tkinter import PhotoImage
import os
#  QR Code Generator Function
def Generate():
    URL = LinkEntry.get()# Get Link From The Entry
    qrcodeimg = qr.make(URL) # Generate QrCode
    qrcodeimg.save("Generated.png") # Save Image
    FinalImage = CTkImage(dark_image=Image.open("Generated.png"),size=(200,200)) # Resize Image
    QrCode.configure(image=FinalImage) # Configure Image To Label
    os.remove("Generated.png") # Remove,Saved Image
# GUI
primarycolor = "#30323D"
secodarycolor = "#4D5061"
win = CTk() # Make A Window
win.title("QR Code Generator") # Set A Title For Window
win.resizable(0,0)
win.geometry("400x600") # Window Size
win.config(bg = primarycolor) #Change Window Background To Primarycolor
Header = CTkLabel(win,text="QR Code Generator",font=("Roboto Slab",40),fg_color=primarycolor)
Header.place(relx=0.5,rely=0.1,anchor=CENTER)
MainFrame = CTkFrame(win,bg_color= primarycolor,border_color=primarycolor,fg_color=secodarycolor,corner_radius=20,border_width=2,height=450,width=300)
MainFrame.place(relx=0.5,rely=0.55,anchor=CENTER)
EntryLabel = CTkLabel(win,text="Enter Your Website Url :",fg_color=secodarycolor,bg_color=secodarycolor,text_color="White",font=("Robot Slab",18))
EntryLabel.place(relx=0.5,rely=0.25,anchor=CENTER)
LinkEntry = CTkEntry(win,fg_color=primarycolor,bg_color=secodarycolor,width=250,placeholder_text="Enter You Website Url :",placeholder_text_color="White")
LinkEntry.place(relx = 0.5,rely = 0.31,anchor=CENTER)
GenerateButton = CTkButton(win,text="Generate",fg_color="#cdd1c4",text_color=primarycolor,hover_color="#cdd1c4",bg_color=secodarycolor,command=Generate)
GenerateButton.place(relx=0.5,rely=0.38,anchor=CENTER)
QrCode = CTkLabel(win,text=None,bg_color=secodarycolor,fg_color=secodarycolor)
QrCode.place(relx=0.5,rely=0.6,anchor = CENTER)
win.mainloop()
