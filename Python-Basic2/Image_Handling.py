#THIS PROGRAM IS ALSO SHOWING THE WORKING OF FILE HANDLING...
#CASE-4(Working On Images)
#(i)...
'''print('(i)...\n')
File1=open('dice-six-faces-five.png','rb')
print(File1.tell())
print(File1.read())
print(File1.tell())
'''
#(ii)...
print('(ii)...\n')
#File1=open("C:\Users\Harsh Vardhan Gupta\Downloads\IMAGE\Dodge.jpg",'rb')
File1=open("Dodge.jpg",'rb')
print(File1.tell())
print(File1.read())
print(File1.tell())
File2=open('File_image2.jpg','wb')
for i in File1:
    File2.write(i)
