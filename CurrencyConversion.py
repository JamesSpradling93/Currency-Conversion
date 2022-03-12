import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import os


root = tk.Tk()
root.title('Cryptourrency Converter')
root.geometry('440x720')
root.config(bg='#58d67a')

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


def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
    return None


def cry_val():
    cry_val = cry_text.get("1.0",END)
    print (cry_val)


    curr = [['Bitcoin',39173],['Ethereum',2645],['Tether',1.00],['BNB',380.02]]
    for c in curr:
        crypto = int(cry_val)/int(c[1])
        cryoutput.insert(END, 'USD = ' + str(crypto) + ' ' + c[0] + '\n')

img = ImageTk.PhotoImage(Image.open("cryptophoto2.jpg"))


crypanel = Label(root, image = img)
crypanel.pack()


cry_label = Label(root, bg='#58d67a', text="Enter amount in USD", font=font_one)
cry_label.pack(pady=7)


cry_text = Text(root, font=font_one,height = 1.1, width = 30)
cry_text.pack(pady=7)


cry_convert_button = Button(root, height = 1, width = 10,
                    text = "Convert", font=font_one, command = cry_val)
cry_convert_button.pack(pady=10)

cryoutput = Text(root, font=font_two, height = 5, width = 44)
cryoutput.pack()



root.mainloop()
