from tkinter import *
import os
from PIL import ImageTk,Image
def next_image():
    global Counter
    image_label.config(image=img_array[Counter%len(img_array)])
    Counter = Counter+1
#Make a GUI window
Counter = 1
root = Tk()
root.geometry('300x400')
root.minsize(100,100)
root.maxsize(500,500)
root.title("Wallpaper-Window")
root.config(background='black')
#Take image list
files = os.listdir('IMAGE')
print(files)

img_array =[]
for file in files:
    img = Image.open(os.path.join('IMAGE',file))
    resize_img = img.resize((250,300))
    img_array.append(ImageTk.PhotoImage(resize_img))

#Make an image label for showing image:-
image_label = Label(root,image= img_array[0])
image_label.pack(pady=(10,5))

#Make a button :-
next = Button(text='Next',bg='White',fg='Black',width=10,height=-1,font='bold',command=next_image)
next.pack(pady=(10,5))
#Hold the GUI window
root.mainloop()