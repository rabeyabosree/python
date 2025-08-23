# import cv2
# from tkinter import *
# from tkinter import filedialog
# from PIL import Image, ImageTk

# # main window
# root = Tk()
# root.title("Sketch App")
# root.geometry("1000x800")

# # label placeholder for sketch
# sketch_label = Label(root)
# sketch_label.pack()


# def select_image():
#     # open dialog when button clicked
#     img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

#     if img_path:
#         # read image
#         img = cv2.imread(img_path)

#         # convert to gray
#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # invert the image
#         inverted_img = 255 - gray_img
#         blur = cv2.GaussianBlur(inverted_img, (21, 21), 0)
#         inverted_blur = 255 - blur
#         sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

#         # convert sketch back to Tkinter-compatible image
#         sketch_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
#         im_pil = Image.fromarray(sketch_rgb)
#         imgTk = ImageTk.PhotoImage(im_pil)

#         # update label
#         sketch_label.config(image=imgTk)
#         sketch_label.image = imgTk  # keep reference


# # button to open image
# btn = Button(root, text="Select Image", command=select_image)
# btn.pack(pady=10)



# root.mainloop()


import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


#main window
root = Tk()
root.title("Sketch app")
root.geometry("1000x800")

# open image function
def open_image():
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png; *.jpg; *.jpeg")])
    if img_path:
        img = cv2.imread(img_path)

        # convert to gray 
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # show original img
        cv2.imshow("Original image", img)

# button to open image
btn = Button(root, text="Select Image", command=open_image)
btn.pack(pady=10)

root.mainloop()