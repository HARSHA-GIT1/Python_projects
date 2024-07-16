#THIS PROGRAM CREATE AN CALCULATOR:-
from tkinter import *
#Make Three Variable for Mathmatics operations:-
first_no = second_no = operator = None
#Makes Methods for Functionality

#Method for get-digit
def get_digit(value):
    current = result['text']
    new = current + str(value)
    result.config(text=new)
#Method for clear
def clear():
    result.config(text='')

#Make Methods for Mathmatically operations:-

#Make a Method for add,multiple,etc
def operation(op):
    global first_no,operator
    first_no = int(result['text'])
    result.config(text='')
    operator = op
#Make a Method for equal
def equal():
    global  second_no,first_no,operator
    second_no = int(result['text'])
    if operator == '+':
        Result = first_no + second_no
    elif operator == '-':
        Result = first_no - second_no
    elif operator == '*':
        Result = first_no * second_no
    elif operator == '/':
        if second_no == 0:
            result.config(text='can not divide')
            return
        else:
            Result = round(first_no / second_no,5)
    result.config(text=Result)
#Make a Gui Window
root = Tk()
root.geometry('280x400')
root.resizable(0,0)
root.config(bg='Black')

#Change Title and image
root.title('Calculator')
root.iconbitmap('Calculator.ico')

# Dispaly Result
result = Label(root,text='',fg= 'White',bg= 'Black')
result.grid(row =0,column =0,columnspan =5, pady =(50,40),sticky = 'w')
result.config(font=('verdana',30,'bold'))

#Creates Buttons
#Row-1
Btn7 = Button(text= 7,fg= 'Black',bg= 'grey64',width=5,height=2,command= lambda:get_digit(7))
Btn7.grid(row = 1,column = 0,pady=(10,0))
Btn7.config(font= ('verdana',14,'bold'))

Btn8 = Button(text= 8,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(8))
Btn8.grid(row = 1,column = 1,pady=(10,0))
Btn8.config(font= ('verdana',14,'bold'))

Btn9 = Button(text= 9,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(9))
Btn9.grid(row = 1,column = 2,pady=(10,0))
Btn9.config(font= ('verdana',14,'bold'))

Btn_divide = Button(text= '/',fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :operation('/'))
Btn_divide.grid(row = 1,column = 3,pady=(10,0))
Btn_divide.config(font= ('verdana',14,'bold'))
command=get_digit(7)
#Row-2
Btn4 = Button(text= 4,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(4))
Btn4.grid(row = 2,column = 0)
Btn4.config(font= ('verdana',14,'bold'))

Btn5 = Button(text= 5,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(5))
Btn5.grid(row = 2,column = 1)
Btn5.config(font= ('verdana',14,'bold'))

Btn6 = Button(text= 6,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(6))
Btn6.grid(row = 2,column = 2)
Btn6.config(font= ('verdana',14,'bold'))

Btn_mul = Button(text= '*',fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :operation('*'))
Btn_mul.grid(row = 2,column = 3)
Btn_mul.config(font= ('verdana',14,'bold'))

#Row-3
Btn1 = Button(text= 1,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(1))
Btn1.grid(row = 3,column = 0)
Btn1.config(font= ('verdana',14,'bold'))

Btn2 = Button(text= 2,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(2))
Btn2.grid(row = 3,column = 1)
Btn2.config(font= ('verdana',14,'bold'))

Btn3 = Button(text= 3,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(3))
Btn3.grid(row = 3,column = 2)
Btn3.config(font= ('verdana',14,'bold'))

Btn_sub = Button(text= '-',fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :operation('-'))
Btn_sub.grid(row = 3,column = 3)
Btn_sub.config(font= ('verdana',14,'bold'))

#Row-4
Btn_clear = Button(text= 'C',fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :clear())
Btn_clear.grid(row = 4,column = 0)
Btn_clear.config(font= ('verdana',14,'bold'))

Btn_zero = Button(text= 0,fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :get_digit(0))
Btn_zero.grid(row = 4,column = 1)
Btn_zero.config(font= ('verdana',14,'bold'))

Btn_equal = Button(text= '=',fg= 'Black',bg= 'grey64',width=5,height=2,command= lambda :equal())
Btn_equal.grid(row = 4,column = 2)
Btn_equal.config(font= ('verdana',14,'bold'))

Btn_add = Button(text= '+',fg= 'Black',bg= 'grey64',width=5,height=2,command=lambda :operation('+'))
Btn_add.grid(row = 4,column = 3)
Btn_add.config(font= ('verdana',14,'bold'))

#Hold Gui Window
root.mainloop()
