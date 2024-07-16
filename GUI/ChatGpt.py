"""
(i).In This Program We Make A Small Chat-Gpt For Getting Projects-ideas using Api
(ii). This Api Get From Openai PlateForm.
"""
import os
import openai
from customtkinter import *

#Function For Generating code
def generate():
    try:
        print(os.getenv('OPENAI_API_KEY'))
        prompt = "Generate 10 Unique Projects Ideas "
        language = Chose_language.get()
        prompt += "for " + language + ", "
        difficulty = level.get()
        prompt += "and difficulty level is " + difficulty + ". "
        if Check_box1.get():
            prompt += "Include in Project database. "
        if Check_box2.get():
            prompt += "Use API as well."
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            message=[
                {"role":"user","content":prompt}
            ]
        )

        answer = response.choices[0].message.content
        Text_box.delete(1.0, END)
        Text_box.insert(END, answer)
    except Exception as e:
        print(f"Error occurred: {str(e)}")


#Make a Function for Return The Languages:-
def language():
    List =["Python","C","C++","Java","Kotlin","Php","Html","React"]
    return List
#Create a Visual Window
root = CTk()
root.geometry("800x650")
root.resizable(0,0)
#Here By default window take appearance-mode by desktop
set_appearance_mode("Dark")
root.title("Chat-Gpt for Project Idea")
root.iconbitmap("images.ico")

#Write Visual Content For Window:-
First_label = CTkLabel(root,text="Project Idea Generator",font=CTkFont(size=50,weight='bold'))
First_label.pack(padx=10, pady=(20,20))
#Create First Frame
select_data = CTkFrame(root)
select_data.pack(fill='x',padx=100)
#Make Insider Frame
#First-Frame
Language = CTkFrame(select_data)
Language.pack(padx=100,pady=(20,5),fill="both")
Language_label = CTkLabel(Language,text="Programing Language",font=CTkFont(size=17,weight="bold"))
Language_label.pack()
Chose_language = CTkComboBox(Language,values=language())
Chose_language.pack(padx=10,pady=5)
#Second-Frame
Project = CTkFrame(select_data)
Project.pack(padx=100,pady=5,fill="both")
Project_label = CTkLabel(Project,text="Project Difficulty ",font=CTkFont(size=17,weight="bold"))
Project_label.pack()
level = StringVar(value='Easy')
Chose_1 = CTkRadioButton(Project,text='Easy',variable=level,value='Easy')
Chose_1.pack(side='left',padx=(20,10),pady=10)

Chose_2 = CTkRadioButton(Project,text='Medium',variable=level,value='Medium')
Chose_2.pack(side='left',padx=10,pady=10)

Chose_3 = CTkRadioButton(Project,text='Difficult',variable=level,value='Difficult')
Chose_3.pack(side='left',padx=10,pady=10)

#Third-Frame
Feature = CTkFrame(select_data)
Feature.pack(padx=100,pady=5,fill="both")
Feature_label = CTkLabel(Feature,text="Features ",font=CTkFont(size=17,weight="bold"))
Feature_label.pack()
#Makes-Checkboxes
Check_box1 = CTkCheckBox(Feature,text='Database')
Check_box1.pack(side='left',padx=50,pady=5)
Check_box2 = CTkCheckBox(Feature,text='API')
Check_box2.pack(side='left',padx=70,pady=5)

#Create Enter Button
Enter = CTkButton(select_data,text="Generate",command=generate)
Enter.pack(padx=20,pady=10)

#Text-Box
Text_box = CTkTextbox(root,font=CTkFont(size=20))
Text_box.pack(padx=100,fill='x',pady=10)
#Hold Gui Window
root.mainloop()