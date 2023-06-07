from tkinter import *
from PIL import ImageTk,Image
import glob

win=Tk()
win.title("Image Watermarking")
win.minsize(width=500,height=500)
win.config(padx=200,pady=150)


logo_img = (Image.open("watermark.png")).resize((30, 25), Image.ANTIALIAS)
watermarked_image=[]

for image in glob.glob("images/*.jpg"):
    img=(Image.open(image)).resize((100, 100), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(img)
    new_img.paste(logo_img)
    watermarked_image.append(new_img)
for i in range(len(watermarked_image)):
    label = Label(win, width=100, height=100)
    if i>=5:
        label.grid(row=i-5, column=1)
        label.config(image=watermarked_image[i])
    else:

        label.grid(row=i, column=0)
        label.config(image=watermarked_image[i])

win.mainloop()