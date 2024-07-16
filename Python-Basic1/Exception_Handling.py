#THIS PROGRAM IS SHOWING THE WORKING OF EXCEPTION-HANDLING...
'''#CASE-1:-
a=1
b=0
print(a/b)'''
#CASE-2(Use of Try,Except and finaly keyword)
a=1
b=0
try:
    print("Hello")
    print(a/b)
    #print("Bye")
#except Exception:
except Exception as e:
    #print("Don't Divide by Zero")
    print(e)
    print("Bye")
finally:
    print("Ram Ram Bhai")