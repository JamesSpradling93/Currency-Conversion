import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import os
import sys
from tkinter import ttk


#create root and settings for app
root = tk.Tk()
root.title('Cryptourrency Converter')
root.geometry('500x780')
bgimage = Image.open("D:\\School\\SDEV 140\\Final\\bg3.jpg")
bg= ImageTk.PhotoImage(bgimage)
label = Label(root, image=bg)
label.place(x = 0,y = 0)

#Adding custom fonts
font_one = Font(
        family="Arial",
        size=16,
        underline=0,
        overstrike=0)

font_two = Font(
        family="Arial",
        size=12,
        underline=0,
        overstrike=0)



#define function to reset the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#define currency converter
def cry_val():
    cry_val = cry_text.get("1.0",END)
    print (cry_val)

    #currency conversion algorithm
    curr = [['Bitcoin',39173],['Ethereum',2645],['Tether',1.00],['BNB',380.02]]
    for c in curr:
        crypto = int(cry_val)/int(c[1])
        cryoutput.insert(END, 'USD = ' + str(crypto) + ' ' + c[0] + '\n')



#add custom image at top of page
img = ImageTk.PhotoImage(Image.open("cryptophoto2.jpg"))

#Instert image as label
crypanel = Label(root, image = img)
crypanel.pack(pady=10)

#Enter amount in USD label
cry_label = Label(root, highlightthickness=0,  text="Enter amount in USD", font=font_one)
cry_label.pack(pady=6)

#customize text in output
cry_text = Text(root, font=font_one,height = 1.1, width = 30)
cry_text.pack(pady=2)

#button to initiate conversion
cry_convert_button = Button(root, height = 1, width = 30,
                    text = "Convert", font=font_one, command = cry_val)
cry_convert_button.pack(pady=25)


#output conversion to cryptocurrency
cryoutput = Text(root, font=font_two, height = 5, width = 44)
cryoutput.pack(pady=5)

#button to reset the application
reset_button = Button(root, text="Reset", height = 1, width = 30, font=font_two, command=restart_program)
reset_button.pack(pady=3)

#button to close the application
exit_button = Button(root, text="Exit", height = 1, width = 30, font=font_two, command=root.destroy)
exit_button.pack(pady=3)


root.mainloop()
