from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Creating the root frame and window
ROOT = Tk()
ROOT.title("VouchWrite")
ROOT.minsize(300, 150)
ROOT.configure(background="black")

# Function to open selected file in a new window
def open_edit_win(filename):
    global edit_img
    FILEWIN = Toplevel()
    FILEWIN.title("VouchWrite - Editing")
    FILEWIN.maxsize(1000, 500)

    edit_img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(FILEWIN, image=edit_img)
    img_label.pack()

    # # Scrollbar for FILEWIN
    # scroll_vert = Scrollbar(FILEWIN)
    # scroll_vert.pack(side=RIGHT, fill=Y)

# Function for browsing file explorer and opening image to be edited
def select_file():               ## Block user from opening a second Editing window - Create modal window
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Jpeg", "*.jpg*"), ("png", "*.png*"), ("all files", "*.*")))
    if filename != "":
        start_label.configure(text = "File opened: " + filename)
        open_edit_win(filename)

    else:
        pass

def main():
    # Creating label widget and packing it onto screen
    global start_label
    start_label = Label(ROOT, text="Welcome to VouchWrite!", bg="black", fg="white", pady=30)
    start_label.pack()

    # Creating button widget
    browse_button = Button(ROOT, text="Find File to Edit", padx=20, command=select_file, bg="white")
    browse_button.pack()
    ROOT.mainloop()


if __name__ == "__main__":
    main()
