from tkinter import *
from reportlab.pdfgen import canvas
from PIL import ImageTk, Image

# 1) Create a window

WIN = Tk()
WIN.title("VouchWrite")
WIN.minsize(300, 300)
WIN.configure(background="grey")

startlabel = Label(WIN, text="Welcome to VouchWrite!")
startlabel.pack()

# **Entry of template
# !! Change sequence of commands
canvas1 = Canvas(WIN)
canvas1.pack()

entry1 = Entry(WIN)
canvas1.create_window(200, 140, window=entry1)

def send_img():
    entry = entry1.get()
    path = entry
    return path

button1 = Button(text='Add template', command=send_img)
canvas1.create_window(200, 180, window=button1)

# 2) Upload a pdf (if image= would be great) and scale window to it
# !!!**** Add this to definition in input box
path = 'Background.png'
img = ImageTk.PhotoImage(Image.open(path))
imgwin = Label(WIN, image = img)
imgwin.pack()

# 3) Allow input boxes to be created and pulled into place (-> use text-input cursor)

# 4) Print input onto the pdf (canvas)

# 5) [Merge pdf with written input or] create a new pdf

# 6) Save configurations for easy reusability.


WIN.mainloop()
