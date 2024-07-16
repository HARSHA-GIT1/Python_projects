#THIS PROGRAM IS CREATE AN APPLICATION FOR ENTER THE DATA:-
from tkinter import *
from  tkinter import ttk,messagebox
import openpyxl
import os
#A Function Which Show The Name of All City:-
def ShowCity():
    List =['Agra','Aligarh','Amroha','Ayodhya','Azamgarh','Bahraich','Ballia','Banda','Bara Banki','Bareil']
    return List

#A Function Which Show The Name of All City:-
def ShowState():
    List =[ "Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
            "Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
            "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand",
            "West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu", "Lakshadweep",
            "New Delhi","Puducherry"]
    return List

#A Function Which Show The Name of All City:-
def ShowEducation():
    List =['Primary','Secondary','Graduate','Post Graduate','Phd']
    return List

#A Function Which Save The Data:-
def SaveData():
    #First We check user accept term & conditions
    check = accept_var.get()
    if  check == "Accepted":
        First_name = firstname_entry.get()
        Last_name = lastname_entry.get()

        if First_name and Last_name:
            Sex = sex_label_combobox.get()
            Age = Age_spinbox.get()
            city = City_combobox.get()
            state = State_combobox.get()
            check_registered = check_var.get()
            education = Education_box.get()
            sem = Semester_spin.get()
            print(f'First-Name: {First_name} Last-Name: {Last_name}')
            print(f'Sex: {Sex} Age: {Age}')
            print(f'Address: {city}, {state}')
            print(f'Registration Status:{check_registered}')

            #Save Data Into Excel Sheet
            Filepath = "E:\Python-tkinter\data.xlsx"
            if not os.path.exists(Filepath):
                #First Create a sheet
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading =["First-Name","Last-Name","Sex","Age","City","State","Reg-Status"]
                sheet.append(heading)
                workbook.save(Filepath)
            #Now Load The Data To Excel File
            workbook = openpyxl.load_workbook(Filepath)
            sheet = workbook.active
            sheet.append([First_name,Last_name,Sex,Age,city,state,check_registered])
            workbook.save(Filepath)
        else:
            messagebox.showerror(title='Error', message="First And Last Name Is Required ")

    else:
        messagebox.showerror(title='Error',message="Please Accept Term's Conditions")

#Make a Gui Window:-
root = Tk()
root.geometry('560x450')
root.resizable(0,0)
root.config(background='white')
root.title('Data Entry Form')
#Make a Window frame:-
window = Frame(root)
window.pack()
#Make a Label frame:-
user_info_frame = LabelFrame(window,text='User Information')
user_info_frame.grid(row=0,column=0,padx=20,pady=20)
user_info_frame.config(font=('descent',10,'bold'))

#CODE FOR ENTRY OF DATA:-
#FIRST PART:-
firstname = Label(user_info_frame,text='Firstname')
firstname.grid(row=0,column=0)
firstname.config(font=('verdana',10,'bold'))
lastname = Label(user_info_frame,text='Lastname')
lastname.grid(row=0,column=1,)
lastname.config(font=('verdana',10,'bold'))
sex_label = Label(user_info_frame,text='Sex')
sex_label.grid(row=0,column=2)
sex_label.config(font=('verdana',10,'bold'))


firstname_entry = Entry(user_info_frame)
lastname_entry = Entry(user_info_frame)
firstname_entry.grid(row=1,column=0)
lastname_entry.grid(row=1,column=1)
sex_label_combobox = ttk.Combobox(user_info_frame,values=["Male","Female","Other"])
sex_label_combobox.grid(row=1,column=2)

Age_label = Label(user_info_frame,text='Age')
Age_label.grid(row=2,column=0)
Age_label.config(font=('verdana',10,'bold'))
Age_spinbox = Spinbox(user_info_frame,from_= 12 ,to=100)
Age_spinbox.grid(row=3,column=0)

#Address
City = Label(user_info_frame,text='City')
City.grid(row=2,column=1)
City.config(font=('verdana',10,'bold'))
City_combobox = ttk.Combobox(user_info_frame,values=ShowCity())
City_combobox.grid(row=3,column=1)
State= Label(user_info_frame,text='State')
State.grid(row=2,column=2)
State.config(font=('verdana',10,'bold'))
State_combobox = ttk.Combobox(user_info_frame,values=ShowState())
State_combobox.grid(row=3,column=2)

#Set Padding for all labels:-
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Second Part:-
#make a Second label frame
course_name = LabelFrame(window)
course_name.grid(row=1,column=0,sticky='news',padx=20,pady=20)

#make a label for registration check
check_registration = Label(course_name,text='Registration Status')
check_registration.grid(row=0,column=0)
check_registration.config(font=('verdana',10,'bold'))
#make a checkbutton
"""check_button = Checkbutton(course_name,text='Currently Registered')"""
check_var = StringVar(value='Not Registered')
#Here We use StringVar Because Checkbutton not support get functions
check_button = Checkbutton(course_name,text='Currently Registered',variable=check_var,
                           onvalue='Registered',offvalue='Not Registered')
check_button.grid(row=1,column=0)
check_button.config(font=('verdana',10,'bold'))

#make a label for Education:-
Education = Label(course_name,text='Education')
Education.grid(row=0,column=1)
Education.config(font=('verdana',10,'bold'))
Education_box = ttk.Combobox(course_name,values=ShowEducation())
Education_box.grid(row=1,column=1)

#make a label for Semester:-
Semester = Label(course_name,text='Semester')
Semester.grid(row=0,column=3)
Semester.config(font=('verdana',10,'bold'))
Semester_spin = Spinbox(course_name,from_=1,to=8)
Semester_spin.grid(row=1,column=3)
#Set Padding for all labels:-
for widget in course_name.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Third Part:-
#make a Third label frame
term_condition = LabelFrame(window,text="Terms & Conditions")
term_condition.grid(row=2,column=0,sticky='news',padx=20,pady=20)
term_condition.config(font=('descent',10,'bold'))

#make a checkbutton
#check_button = Checkbutton(term_condition,text='I accept all the terms & conditions')
accept_var = StringVar(value='Not Accepted')
#Here We use StringVar Because Checkbutton not support get functions
accept_button = Checkbutton(term_condition,text='I accept all the terms & conditions',variable=accept_var,onvalue='Accepted',
                            offvalue='Not Accepted')
accept_button.grid(row=0,column=0)
accept_button.config(font=('verdana',10,'bold'))

#make a Data_entry_button
Data_enter = Button(window,text='Enter',command=lambda :SaveData())
Data_enter.grid(row=3,column=0,sticky='news',padx=20,pady=20)
Data_enter.config(font=('verdana',10,'bold'))
#Hold The Gui Window:-
root.mainloop()