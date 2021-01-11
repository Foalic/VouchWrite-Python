from tkinter import *
from tkinter.tix import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import os

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


def get_destroy():
    global added_text
    global font_size

    added_text = input_box.get()
    font_size = int(font_size_input.get())

    text_window.destroy()


def write_new_file():

    file_name = file_path.split('/')[-1]

    if os.path.isfile(os.environ['USERPROFILE'] + '\Desktop\{}'.format('edited_' + file_name)):
        output = open(os.path.join(os.environ['USERPROFILE'], 'Desktop\{}'.format('edited_again_' + file_name)), mode='w')
        final_img.save(output)
    else:
        output = open(os.path.join(os.environ['USERPROFILE'], 'Desktop\{}'.format('edited_' + file_name)), mode='w')
        final_img.save(output)

    edit_window.destroy()


def draw_text():
    global final_img

    get_destroy()

    try:
        base_img = Image.open(image).convert("RGBA")
    except:
        base_img = image.convert("RGBA")

    txt_img = Image.new("RGBA", base_img.size, (255, 255, 255, 0))

    font_obj = ImageFont.truetype('arial.ttf', size=font_size)
    draw_obj = ImageDraw.Draw(txt_img)

    print_text = added_text
    text_colour = (0, 0, 0, 255)

    draw_obj.text((coordinates[0], coordinates[1]), print_text, fill=text_colour, font=font_obj)
    final_img = Image.alpha_composite(base_img, txt_img)
    final_img = final_img.convert("RGB")

    open_edit_win(final_img)


# Function to add text to the image where you double click
def add_text(vector):
    global input_box
    global font_size_input
    global text_window
    global coordinates

    coordinates = vector.x, vector.y

    text_window = Toplevel()
    text_window.title("Enter text")
    text_window.minsize(200, 125)
    centre_window(text_window, 200, 125)
    text_window.transient(edit_window)
    text_window.grab_set()

    text_label = Label(text_window, text="Text:")
    text_label.pack()
    input_box = Entry(text_window, bd=5)
    input_box.pack()

    font_label = Label(text_window, text="Font size:")
    font_label.pack()
    font_size_input = Entry(text_window, bd=5)
    font_size_input.insert(0, "10")
    font_size_input.pack()

    ok_button = Button(text_window, text="Ok", padx=20, command=draw_text)
    ok_button.pack()



# Function to open selected file in a new window and block root, or open
# already edited image instead of original
def open_edit_win(worked_image):
    global edit_img
    global edit_window
    global image

    image = worked_image

    try:
        edit_window.destroy()
    except:
        pass

    edit_window = Toplevel()
    edit_window.title("VouchWrite - Editing")
    edit_window.maxsize(1000, 500)
    centre_window(edit_window, 1000, 500)
    edit_window.grab_set()

    scroll = ScrolledWindow(edit_window)
    scroll.pack()
    scroll_win = scroll.window

    try:
        edit_img = ImageTk.PhotoImage(Image.open(image))
    except:
        edit_img = ImageTk.PhotoImage(image)

    img_label = Label(scroll_win, image=edit_img)
    img_label.pack()

    save_button = Button(scroll_win, text="Save", padx=20, bg="white", command=write_new_file)
    save_button.pack()

    img_label.bind('<Double 1>', add_text)


def select_file():
    global file_path

    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a file",
                                            filetypes = (("all files", "*.*"), ("Jpg", "*.jpg*"), ("Jpeg", "*.jpeg*"), ("png", "*.png*")))
    if file_path != "":
        start_label.configure(text = "File opened: " + file_path)
        open_edit_win(file_path)

    else:
        pass


def main():
    centre_window(root, WIDTH, HEIGHT)

    global start_label
    start_label = Label(root, text="Welcome to VouchWrite!", bg="black", fg="white", pady=30)
    start_label.pack()

    browse_button = Button(root, text="Find File to Edit", padx=20, bg="white", command=select_file)
    browse_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
