#This Tkinter program is create an app for shorten an url:-
from tkinter import *
import pyshorteners
#Make a function for clearing copy-label
def delete_text():
        print('Delete run')
        copy_url.delete("0", "end")


#Make a Function For Running Button Command:-
def shorten():
    #Check is url-paste box is empty or not
    if paste_url.index("end") == 0:
        return
    else:
        #Make an object of Shortener Class
        Short_url = pyshorteners.Shortener()

        #Sort the url using prebuild function of class
        sorted_url = Short_url.tinyurl.short(paste_url.get())
        delete_text()
        #Insert into copy label
        copy_url.insert(0,sorted_url)

#Load Gui Window
root = Tk()
root.geometry('350x400')
root.resizable(0,0)
root.config(background='black')
#Set Title
root.title('Url Shorten')

#Set Label and button:-
#For paste-url
meesage = Label(root,text='Enter Url',bg='Black',fg='#FF4040')
meesage.pack(pady=(50,20))
meesage.config(font=('Helvetica',20,'bold'))
paste_url = Entry(root,width=50)
paste_url.pack(ipady=6,pady=(5,20))

#Create Button
Short_button = Button(root,text='Click For Short',fg='blue',width=20,command=shorten)
Short_button.pack(ipady=5,pady=(15,20))
Short_button.config(font=('verdana',10,'bold'))
#For copy-url
meesage = Label(root,text='Copy This Url',bg='Black',fg='#FF4040')
meesage.pack(pady=(10,20))
meesage.config(font=('Helvetica',20,'bold'))
copy_url = Entry(root,width=50)
copy_url.pack(ipady=6,pady=(5,20))
#Hold Gui Window
root.mainloop()