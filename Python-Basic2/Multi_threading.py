#THIS PROGRAM IS SHOWING THE WORKING OF MULTI-THREADING...
#THREAD:-Basically Threads are Smallest Part Or Unit Of A Process.
#We use Thread module for execution of function using multithread.
#CASE-1(Simple)
'''class Hello():
    def run(self):
        for i in range(5):
            print("Hii")
class Ram():
    def run(self):
        for i in range(5):
            print("Ram Ram")
#Making Objects
T1=Hello()
T2=Ram()
#Calling
T1.run()
T2.run()
'''
#CASE-2(Using Multi-Threading)
import threading
from time import sleep

class Hello(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)

class Ram(threading.Thread):
    def run(self):
        for i in range(5):
            print("Ram Ram")
            sleep(1)

#Making Objects
T1=Hello()
T2=Ram()
#Calling
#T1.run()
#T2.run()
#Calling the function using Multi-Threading
T1.start()
T2.start()