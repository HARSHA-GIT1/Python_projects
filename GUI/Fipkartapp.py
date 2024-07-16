from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#Create a function for checking email and password
def check():
    #print('check')
    email = email_input.get()
    password = password_input.get()
    #print(email,password)
    if email == 'Kinggupta@gmail.com' and password == 'Sukuna@(0101)':
        messagebox.showinfo('Login Sucessfuly')
    else:
        messagebox.showerror('Login failed')
root = Tk()
#Take width x height
root.geometry("400x500")
#Set Minimum size
root.minsize(200,200)
#Set Max size
root.maxsize(700,700)
# Use Label and pack function for displaying text on window
#show = Label(text= "Ram Ram Bhai Sarayna")
#show.pack()

root.title("Login-Page")#Change the title of window
root.iconbitmap('FlipkartLogo.ico')#Change The Icon
root.config(background='blue')

#Set an image on window
img = Image.open('FlipkartLogo.jpg')
resize_img = img.resize((80,80))
img = ImageTk.PhotoImage(resize_img)
Image_display = Label(root,image=img)
Image_display.pack(pady=(10,10))

#Show a text on window
text_label = Label(root,text='Flipkart',fg='white',bg='blue')
text_label.pack()
text_label.config(font=('verdana',24))

#Create a login label
#For Email
email_label = Label(root,text='Enter Email',fg='white',bg='blue')
email_label.pack(pady=(30,10))
email_label.config(font=('bold',14))
email_input = Entry(root,width=40)
email_input.pack(ipady = 6,pady = (5,5))
#For Pasword
password_label = Label(root,text='Enter Password',fg='white',bg='blue')
password_label.pack(pady=(30,10))
password_label.config(font=('bold',14))
password_input = Entry(root,width=40)
password_input.pack(ipady = 6,pady = (5,5))

#Create a login button
login= Button(root,text='Login',bg='white',fg='black',width=5,command=check)
login.config(font=('bold',10))
login.pack(pady=(10,5))

root.mainloop()#Hold GUI Window