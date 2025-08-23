import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Globals
img_path = None
img = None
gray_img = None

def open_image():
    global img_path, img, gray_img
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.png; *.jpeg")])

    if img_path:
        img = cv2.imread(img_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        update_sketch()

def update_sketch(val=None):
    global img, gray_img

    if img is None:
        return

    ksize = blur_slider.get()
    if ksize % 2 == 0:
        ksize += 1

    inverted_img = 255 - gray_img
    blur = cv2.GaussianBlur(inverted_img, (ksize, ksize), 0)
    inverted_blur = 255 - blur
    sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

    sketch_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)

    im_pil = Image.fromarray(sketch_rgb)
    imgTk = ImageTk.PhotoImage(im_pil)

    sketch_label.imgtk = imgTk
    sketch_label.configure(image=imgTk)

# Main Window
root = Tk()
root.title("Pencil Sketch App")
root.geometry("800x600")

open_btn = Button(root, text="Open Image", command=open_image)
open_btn.pack(pady=10)

blur_slider = Scale(root, from_=1, to=51, orient=HORIZONTAL, label="Blur Kernel Size", command=update_sketch)
blur_slider.set(21)
blur_slider.pack(pady=10)

sketch_label = Label(root)
sketch_label.pack()

root.mainloop()


