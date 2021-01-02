from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import ImageTk, Image

# 1) Create a window

WIN = Tk()
WIN.title("VouchWrite")
WIN.minsize(300, 300)
WIN.configure(background="grey")

STARTLABEL = Label(WIN, text="Welcome to VouchWrite!")
STARTLABEL.pack()

# **Entry of template
# !! Change sequence of commands
INITIAL_CANVAS = Canvas(WIN)
INITIAL_CANVAS.pack()

entry1 = Entry(WIN)
INITIAL_CANVAS.create_window(200, 140, window=entry1)

## Function to browse file explorer -- And open image in window to be edited
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Pdf", "*.pdf*"), ("Jpeg", "*.jpg*"), ("png", "*.png*"), ("all files", "*.*")))
    #label_file_explorer.configure(text = "File opened: " + filename)                ## Change this line to adding path to button_open or opening file handle itself
    filehandle = open(filename, "r")

## !! Function that will print what is typed onto the opened file underneath, editing it
def send_to_img():
    path = entry1.get()             # Needs a file handle and open the file entered.
    return path

button_explore = Button(WIN, text = "Browse Files", command = browseFiles)
button_write = Button(WIN, text='Write', command=send_to_img)                   ## Need to use .drawString(x,y, text) to add string onto the pdf
INITIAL_CANVAS.create_window(200, 180, window=button_explore)

# 2) Upload a pdf (if image= would be great) and scale window to it
# !!!**** Add this to definition in input box
# path = 'Background.png'
# img = ImageTk.PhotoImage(Image.open(path))
# imgwin = Label(WIN, image = img)
# imgwin.pack()

# 3) Allow input boxes to be created and pulled into place (-> use text-input cursor)

# 4) Print input onto the pdf (canvas)

# 5) [Merge pdf with written input or] create a new pdf

# 6) Save configurations for easy reusability.


WIN.mainloop()
