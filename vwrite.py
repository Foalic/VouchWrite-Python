from tkinter import *
from tkinter.tix import *
from tkinter import filedialog, messagebox
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
    edit_window.destroy()


def write_new_file():

    file_name = file_path.split('/')[-1]

    if 'final_img' not in globals():
        messagebox.showinfo("Original file", "This is still the original file. \nPlease make a change and save.")
        return
    else:
        if os.path.isfile(os.environ['USERPROFILE'] + '\Desktop\{}'.format('edited_' + file_name)):
            output = open(os.path.join(os.environ['USERPROFILE'], 'Desktop\{}'.format('edited_again_' + file_name)), mode='w')
            final_img.save(output)
        else:
            output = open(os.path.join(os.environ['USERPROFILE'], 'Desktop\{}'.format('edited_' + file_name)), mode='w')
            final_img.save(output)

    edit_window.destroy()


# Function to draw the entered text to image, either originial or last edited.
def draw_text():
    global final_img
    global edits
    global added_text

    if 'edits' in globals():
        print("********EDITS IN GLOBAL***************************")
        pass
    else:
        print("************EDITS CREATED*************")
        edits = []

    try:
        get_destroy()
    except:
        pass

    base_img = Image.open(file_path).convert("RGBA")
    print("BASE IS FILE PATH!!!!!!!!!!!!!!!!!!!!!!")

    if added_text != "":
        edits.append((added_text, (coordinates)))
    text_colour = (0, 0, 0, 255)

    if edits != []:
        for index, edit in enumerate(edits, start=0):
            print("[[[[[[[[[]]]]]]]]]STARTING FOR LOOP[[[[[[[[[[]]]]]]]]]]")
            txt_img = Image.new("RGBA", base_img.size, (255, 255, 255, 0))
            font_obj = ImageFont.truetype('arial.ttf', size=font_size)
            draw_obj = ImageDraw.Draw(txt_img)
            draw_obj.text((edits[index][1][0], edits[index][1][1]), edits[index][0], fill=text_colour, font=font_obj)
            inter_img = Image.alpha_composite(base_img, txt_img)
            if edit != edits[-1]:
                base_img = inter_img.convert("RGBA")
            else:
                final_img = inter_img.convert("RGB")
                break
    else:
        print("***********NO EDITS IMAGE**************")
        final_img = base_img.convert("RGB")

    print(edits)
    print(type(edits))
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
    font_size_input.insert(0, "15")
    font_size_input.pack()

    ok_button = Button(text_window, text="Ok", padx=20, command=draw_text)
    ok_button.pack()


# Feature to enable deleting changes. Create an optionmenu or Radio buttons
# def delete_chosen():
#     if edits == []:
#         messagebox.showinfo("No changes", "No changes have been made.")
#     else:
#         popup = tk.Toplevel()
#         PUWIDTH, PUHEIGHT = (200, 65)
#         popup.minsize(PUWIDTH, PUHEIGHT)
#         popupx = (WIDTH_SCREEN/2) - (PUWIDTH/2)
#         popupy = (HEIGHT_SCREEN/2) - (PUHEIGHT/2)
#         popup.geometry('%dx%d+%d+%d' % (PUWIDTH, PUHEIGHT, popupx, popupy))
#
#         enter_label = tk.Label(popup, text="Please enter index of file to delete:")
#         enter_label.pack()
#
#         input_box = tk.Entry(popup, textvariable=tk.IntVar())
#         input_box.pack()
#
#         destroypu = tk.Button(popup, text="Enter", command=get_destroy)
#         destroypu.pack()


# Feature to allow deleting last made change - faster than delete_chosen
def delete_last():
    global edits
    global added_text
    global image

    print("EDITS BEFORE POP: ", edits)
    if 'edits' not in globals():
        messagebox.showinfo("No changes", "No changes have been made that could be deleted.")
    elif edits == []:
        messagebox.showinfo("No changes", "No changes exist that could be deleted.")
        image = Image.open(file_path)
    else:
        print("EDITS RIGHT BEFORE POP: ", edits)
        edits.pop()
        #image = Image.open(file_path)
        added_text = ""
        print("******************", edits, "*******************")
        edit_window.destroy()
        draw_text()


# Function to open selected file in a new window and block root, or open
# already edited image instead of original
def open_edit_win(worked_image):
    global edit_img
    global edit_window
    global image

    image = worked_image
    print("(((((((((((((())))))))))))))", image, "((((((((((((((()))))))))))))))")

    edit_window = Toplevel()
    edit_window.title("VouchWrite - Editing")
    try:
        img_wdth, img_hght = Image.open(image).size
    except:
        img_wdth, img_hght = image.size
    wn_wdth, wn_hght = img_wdth+50, img_hght+80
    centre_window(edit_window, wn_wdth, wn_hght)
    edit_window.grab_set()

    scroll = ScrolledWindow(edit_window, width=wn_wdth, height=wn_hght)
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

    del_last_button = Button(scroll_win, text="Delete Last Change", padx=20, bg="white", command=delete_last)
    del_last_button.pack()

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
