"""
1.Here we write a program for making a live-news app using api.
2.Here we use multiple modules.
"""
from tkinter import *
import requests

#Make a class for app
class News:
    def __init__(self):
        # Fetch Data
        self.data = requests.get( 'https://newsapi.org/v2/top-headlines?country=in&apiKey=eb577d082ead4c0bb6ccd0c2d1022e7a').json()
        print(self.data)
        #Load Gui Window
        self.loadGui()
        #Showing First News
        self.loadNews(0)

    #Make a Method for clear the screen:-
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    #Make a Method for Loading Gui:-
    def loadGui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.config(bg='black')
        self.root.mainloop()
    #Make a Method for Loading News:-
    def loadNews(self,index):
        #Clear Screen
        self.clear()
        #Create Heading label
        heading = Label(self.root,text= self.data['articles'][index]['title'],bg='black',fg='white',wraplength=100,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))
        # Create details label
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='blue', fg='white', wraplength=100,
                        justify='center')
        details.pack(pady=(10, 20))
        details.config(font=('verdana', 15))
obj = News()