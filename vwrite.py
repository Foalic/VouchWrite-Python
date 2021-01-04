from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Creating the root frame and window
ROOT = Tk()
ROOT.title("VouchWrite")
ROOT.minsize(150, 150)
ROOT.configure(background="white")


# Creating an input box - Maybe just leave the browse button
# input_box = Entry(ROOT, width=30, border=2)
# input_box.pack()
# input_box.insert(0, "Enter file name")

# Function to open selected file in a new window
def open_edit_win(filename):
    global edit_img
    FILEWIN = Toplevel()
    FILEWIN.title("VouchWrite - Editing")

    # Scrollbars for FILEWIN
    #scroll_vert = Scrollbar(img_label)
    #scroll_vert.pack(side=RIGHT, fill=Y)
    # # scroll_hori = Scrollbar(FILEWIN, orient=HORIZONTAL)
    # # scroll_hori.pack()

    edit_img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(FILEWIN, image=edit_img)
    img_label.pack()

# Function for browsing file explorer and opening image to be edited
def select_file():               ## Block user from opening a second Editing window
    input = input_box.get()
    if input == "Enter file name":
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Jpeg", "*.jpg*"), ("png", "*.png*"), ("all files", "*.*")))
        if filename != "":
            start_label.configure(text = "File opened: " + filename)
            open_edit_win(filename)

        else:
            pass
    #else:
        ## Need to be able to search for the file


# Creating label widget and packing it onto screen
start_label = Label(ROOT, text="Welcome to Vouchwrite!")
start_label.pack()

# Creating button widget
browse_button = Button(ROOT, text="Browse Files", padx=20, command=select_file)
browse_button.pack()

ROOT.mainloop()
