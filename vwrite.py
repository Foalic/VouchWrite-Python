from tkinter import *
from tkinter.tix import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Creating the root frame and window
root = Tk()
root.title("VouchWrite")
WIDTH, HEIGHT = 400, 150
root.minsize(WIDTH, HEIGHT)
root.configure(background="black")


def centre_window(window, width, height):
    # Finding screen size
    WIDTH_SCREEN = window.winfo_screenwidth()
    HEIGHT_SCREEN = window.winfo_screenheight()

    # Using screen size to place root in the middle
    winx = (WIDTH_SCREEN/2) - (width/2)
    winy = (HEIGHT_SCREEN/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, winx, winy))


# Adding function to add text to the image where you click (need to add another
# window in which to input the text and use the mouseclick vector to place it)
def add_text(x, y):
    text_window = Toplevel()
    text_window.title("Enter text")

    ## Mouse click event to open text_window -- Has to be in open_edit_window

    ## Text Box Label with button --- Get code from Run Apps


    save_button = Button(text_window, text="Save", padx=20, bg="white", command=lambda: edit_img.save('voucher.jpg'))
    save_button.pack()

    draw_obj = ImageDraw.Draw(edit_img)
    font_obj = ImageFont.truetype('arial.ttf', size=10)

    print_text = "Input from text window"
    text_colour = 'rgb(0, 0, 0)'

    # draw the message on the image
    draw_obj.text((x, y), print_text, fill=text_colour, font=font_obj)



# Function to open selected file in a new window and block root
def open_edit_win(filename):
    global edit_img
    edit_window = Toplevel()
    edit_window.title("VouchWrite - Editing")
    edit_window.maxsize(1000, 500)
    centre_window(edit_window, 1000, 500)
    edit_window.grab_set()

    # Adding scrollbar
    scroll = ScrolledWindow(edit_window)
    scroll.pack()
    scrollwin = scroll.window

    edit_img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(scrollwin, image=edit_img)
    img_label.pack()

    # Listen for mouseclick event and open add_text(x,y)


# Function for browsing file explorer and opening image to be edited
def select_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Jpeg", "*.jpg*"), ("png", "*.png*"), ("all files", "*.*")))
    if filename != "":
        start_label.configure(text = "File opened: " + filename)
        open_edit_win(filename)

    else:
        pass


def main():
    centre_window(root, WIDTH, HEIGHT)

    # Creating label widget and packing it onto screen
    global start_label
    start_label = Label(root, text="Welcome to VouchWrite!", bg="black", fg="white", pady=30)
    start_label.pack()

    # Creating button widget
    browse_button = Button(root, text="Find File to Edit", padx=20, bg="white", command=select_file)
    browse_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
