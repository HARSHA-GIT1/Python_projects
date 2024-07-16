#THIS PROGRAM SHOW THE WORKING RESULT...
Student_Marks={
    'Harsh':76,
    'Raman':75,
    'Sunil':89,
    'Ganesh':78,
    'Abhimanyu':87,
    'Rajat Dalal':43,
    'Akshay':56,
    'Punit':89,
}
Student_Grade=dict({})#Declare a Dictornary
for Name in Student_Marks:
    marks=Student_Marks[Name]
    if marks >= 90 and marks <= 100:
        Student_Marks[Name] = 'A+'
        print(Student_Grade)
    elif marks >= 80 and marks <= 89:
        Student_Grade[Name] = 'A'
        print(Student_Grade)
    elif marks >= 65 and marks <= 79:
        Student_Grade[Name]= 'B'
        print(Student_Grade)
    elif marks >= 50 and marks <= 65:
        Student_Grade[Name] = 'C'
        print(Student_Grade)
    elif marks >= 40 and marks <= 50:
        Student_Grade[Name] = 'D'
        print(Student_Grade)
    elif marks < 40:
        Student_Grade[Name] = 'E'
        print(Student_Grade)
print('Student Data With Grade:')
for i in Student_Grade:
    print(i," :-",Student_Grade[i])