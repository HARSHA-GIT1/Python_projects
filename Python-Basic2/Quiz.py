#THIS PROGRAM IS SHOWING THE WORKING OF A QUIZ...
Questions=[
    {1:'No Of Vowels In English Alfabhets','ans':'A'},
    {2:'Next Prime Minister Of Bharat','ans':'A'},
    {3:'After BCA You Getting A job','ans':'D'},
    {4:'In Your College What You Have Learned','ans':'D'},
    {5:'In Programming Garbage a Valid Word To Said Anyone','ans':'D'},
    {6:'What Is A Term Of Keyword IN Programming','ans':'D'},
    {7:'In Ipl RCB Will Be Won','ans':'B'},
    {8:'In Future Ai Rush on Tech Jobs','ans':'B'},
    {9:'What Is the Future of Curret Generation:','ans':'C'},
    {10:'Now Days What You Think About Social Media Plateforms','ans':'D'},
]
Options=[
    ["A. 5","B. 4","C. 7","D. 9"],
    ['A. Narendra Das Modi','B. Sudhansu Trevedi','C. Ashwini Vashinaw','D. Amit Shah'],
    ['A. Upar Wala Ki Dua Ha','B. Ye Bhi Ho Sakata Ha Kya','C. 50-50 % Chance','D. I Think 100% '],
    ['A. Kabhi Zeevan Ko Kisi Ke Upar Mat Chodo','B. Never Left From Exam If Parents Is Present','C. College Walo Ki Aukat','D. All Above'],
    ['A. As A Fresher Yes','B. But When You Work in it No',' C. 50-50 % Chance','D. Debated Word '],
    ['A. Predefine But Have No Defination','B. Contain Especially Defination And Predefine ','C. Reserve Word','D. Both B And C '],
    ['A. Upar Wala Ki Dua Ha', 'B. Ye Bhi Ho Sakata Ha Kya', 'C. 50-50 % Chance', 'D. I Think 100% '],
    ['A. No', 'B. If People Not Work on Skills', 'C. 50-50 % Chance', 'D. I Think 100% '],
    ['A. Upar Wala He Zana', 'B. Destory The World ', 'C. Next Level Inovations and Inventions', 'D. I Think Face Very Difficults Days '],
    ['A. Give Learning and Important Informations', 'B. New Porn Site', 'C. Digital Weapon', 'D. All Above']
]
#Start
Count=0
for Ques_num in range(len(Questions)):
    print(Questions[Ques_num][Ques_num+1])
    for i in Options[Ques_num]:
     print(i)
    Choice=input('Enter Your Choice')
    if Choice.upper()==Questions[Ques_num]['ans']:
        Count+=1
        print('You Answer is Right Your Score is',Count)
    else:
        if Count==0:
            Count=0
            print('Your Answer Is Wrong You Lose One Point')
            print('Your Current Score is ', Count)
        else:
            Count-=1
            print('Your Answer Is Wrong You Lose One Point')
            print('Your Current Score is ',Count)