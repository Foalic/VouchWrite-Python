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


# Place window in the middle of screen
def centre_window(window, width, height):
    WIDTH_SCREEN = window.winfo_screenwidth()
    HEIGHT_SCREEN = window.winfo_screenheight()

    winx = (WIDTH_SCREEN/2) - (width/2)
    winy = (HEIGHT_SCREEN/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, winx, winy))


# Store the input and destroy input window
def get_input_destroy():
    global added_text
    global font_size

    added_text = input_box.get()
    font_size = int(font_size_input.get())

    text_window.destroy()
    edit_window.destroy()


# Removing chosen radio-button from 'edits' list and destroying pop-up
# Sends to 'draw_text' to create image without chosen option
def get_chosen_destroy():
    global added_text

    chosen_value = chosen.get()

    if chosen_value == -1 or chosen_value == "":
        radio_wn.destroy()
        return
    else:
        to_remove = edits[chosen_value]
        edits.remove(to_remove)
        radio_wn.destroy()
        edit_window.destroy()
        added_text = ""
        print()
        draw_text()


# Write the newly created file to desktop on clicking 'save'
def write_new_file():

    file_name = file_path.split('/')[-1]

    if 'final_img' not in globals():
        messagebox.showinfo(
            "Original file", "This is still the original file. \nPlease make a change and save.")
        return
    else:
        if os.path.isfile(os.environ['USERPROFILE'] + '\Desktop\{}'.format('edited_' + file_name)):
            output = open(os.path.join(os.environ['USERPROFILE'], 'Desktop\{}'.format(
                'edited_again_' + file_name)), mode='w')
            final_img.save(output)
        else:
            output = open(os.path.join(os.environ['USERPROFILE'],
                          'Desktop\{}'.format('edited_' + file_name)), mode='w')
            final_img.save(output)

    edit_window.destroy()


# Draw the input text to image
def draw_text():
    global final_img
    global edits
    global added_text

    if 'edits' in globals():
        pass
    else:
        edits = []

    try:
        get_input_destroy()
    except:
        pass

    base_img = Image.open(file_path).convert("RGBA")

    if added_text != "":
        edits.append((added_text, (coordinates)))
    text_colour = (0, 0, 0, 255)

    if edits != []:
        for index, edit in enumerate(edits, start=0):
            txt_img = Image.new("RGBA", base_img.size, (255, 255, 255, 0))
            font_obj = ImageFont.truetype('arial.ttf', size=font_size)
            draw_obj = ImageDraw.Draw(txt_img)
            draw_obj.text((edits[index][1][0], edits[index][1][1]),
                          edits[index][0], fill=text_colour, font=font_obj)
            inter_img = Image.alpha_composite(base_img, txt_img)
            if edit != edits[-1]:
                base_img = inter_img.convert("RGBA")
            else:
                final_img = inter_img.convert("RGB")
                break
    else:
        final_img = base_img.convert("RGB")

    open_edit_win(final_img)


# Pop-up window to get input. Activated by double click and
# passes vector of click to 'draw_text' function
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


# Pop-up for radio-button list - chosen option passed on to 'get_chosen_destroy'
def delete_chosen():
    global chosen
    global radio_wn

    if 'edits' not in globals():
        messagebox.showinfo("No changes", "No changes have been made that could be deleted.")
    elif edits == []:
        messagebox.showinfo("No changes", "No changes exist that could be deleted.")
    else:
        radio_wn = Toplevel()
        RADWIDTH, RADHEIGHT = (300, 300)
        centre_window(radio_wn, RADWIDTH, RADHEIGHT)
        radio_wn.grab_set()

        radio_label = Label(radio_wn, text="Please choose a change to delete: ")
        radio_label.pack()

        chosen = IntVar()
        none_radio = Radiobutton(radio_wn, variable=chosen, text="None", value=-1)
        none_radio.pack()
        none_radio.select()
        for i, edit in enumerate(edits, start=0):
            option_radio = Radiobutton(radio_wn, variable=chosen,
                                       text=f"Change {i+1}:\n'{edit[0]}'", value=i)
            option_radio.pack()
            option_radio.deselect()

        destroy_radio_wn = Button(radio_wn, text="Ok", bg="white", command=get_chosen_destroy)
        destroy_radio_wn.pack()


# Deletes item last added to 'edits' list and sends to 'draw_text' for new image
def delete_last():
    global edits
    global added_text
    global image

    if 'edits' not in globals():
        messagebox.showinfo("No changes", "No changes have been made that could be deleted.")
    elif edits == []:
        messagebox.showinfo("No changes", "No changes exist that could be deleted.")
        image = Image.open(file_path)
    else:
        edits.pop()
        added_text = ""
        edit_window.destroy()
        draw_text()


# Open selected file/file being edited in a new window and block root
def open_edit_win(worked_image):
    global edit_img
    global edit_window
    global image

    image = worked_image

    edit_window = Toplevel()
    edit_window.title("VouchWrite - Editing")
    edit_window.state('zoomed')
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

    del_last_button = Button(scroll_win, text="Delete Last Change",
                             padx=20, bg="white", command=delete_last)
    del_last_button.pack()

    del_last_button = Button(scroll_win, text="Choose a Change to Delete",
                             padx=20, bg="white", command=delete_chosen)
    del_last_button.pack()

    img_label.bind('<Double 1>', add_text)


def select_file():
    global file_path

    file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                           filetypes=(("all files", "*.*"), ("Jpg", "*.jpg*"), ("Jpeg", "*.jpeg*"), ("png", "*.png*")))

    if file_path == "":
        pass
    elif ".jpg" not in file_path and ".jpeg" not in file_path and ".png" not in file_path:
        messagebox.showerror("Invalid file type",
                             "Sorry this file type is not compatible with VouchWrite.")
    elif file_path != "":
        start_label.configure(text="File opened: " + file_path)
        open_edit_win(file_path)


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
