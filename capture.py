from tkinter import *
from PIL import Image, ImageTk
import cv2

from main import read_image
from service import ifRegistered


def send_to_image_read(filename):
    number = read_image(filename)
    if number == '':
        raise ValueError("Please try again.")
    ifRegistered(number)


root = Tk()
root.geometry("700x700")

label = Label(root)
label.frame_num = 0
label.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


def show_frames():
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.frame_num += 1.
    label.configure(image=imgtk)
    label.after(20, show_frames)


def key_pressed():
    take_pic()


button1 = Button(root, text="Take Photo", command=key_pressed)
button1.grid(row=1, column=0)


def take_pic():
    file_name = "raw.png"
    imagetk = label.imgtk
    imgpil = ImageTk.getimage(imagetk)
    imgpil.save("taken/" + file_name, "PNG")
    imgpil.close()
    send_to_image_read('taken/raw.png')


show_frames()
root.mainloop()


