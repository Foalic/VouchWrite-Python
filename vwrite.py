from tkinter import *
from tkinter.tix import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Creating the root frame and window
ROOT = Tk()
ROOT.title("VouchWrite")
WIDTH, HEIGHT = 400, 150
ROOT.minsize(WIDTH, HEIGHT)
ROOT.configure(background="black")

def centre_window(window, width, height):
    # Finding screen size
    WIDTH_SCREEN = window.winfo_screenwidth()
    HEIGHT_SCREEN = window.winfo_screenheight()

    # Using screen size to place root in the middle
    winx = (WIDTH_SCREEN/2) - (width/2)
    winy = (HEIGHT_SCREEN/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, winx, winy))

# Function to open selected file in a new window
def open_edit_win(filename):
    global edit_img
    FILEWIN = Toplevel()
    FILEWIN.title("VouchWrite - Editing")
    FILEWIN.maxsize(1000, 500)
    centre_window(FILEWIN, 1000, 500)

    # Adding scrollbar
    scroll = ScrolledWindow(FILEWIN)
    scroll.pack()
    scrollwin = scroll.window

    edit_img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(scrollwin, image=edit_img)
    img_label.pack()

# Function for browsing file explorer and opening image to be edited
def select_file():               ## Block user from opening a second Editing window - Create modal window
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Jpeg", "*.jpg*"), ("png", "*.png*"), ("all files", "*.*")))
    if filename != "":
        start_label.configure(text = "File opened: " + filename)
        open_edit_win(filename)

    else:
        pass

def main():
    centre_window(ROOT, WIDTH, HEIGHT)

    # Creating label widget and packing it onto screen
    global start_label
    start_label = Label(ROOT, text="Welcome to VouchWrite!", bg="black", fg="white", pady=30)
    start_label.pack()

    # Creating button widget
    browse_button = Button(ROOT, text="Find File to Edit", padx=20, bg="white", command=select_file)
    browse_button.pack()
    ROOT.mainloop()


if __name__ == "__main__":
    main()
