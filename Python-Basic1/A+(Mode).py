#THIS PROGRAM IS ALSO SHOWING THE WORKING OF FILE HANDLING...
#CASE-4( a+ MODE)
#In a+ Mode If File Is Exists Then It Start to Write the Data at Ending.
#If Not Exists Then First Create and after use..
#(i)...
print('(i)...\n')
File1=open('File1.txt','a+')
print(File1.tell())
print(File1.tell())

#(ii)...
print('(ii)...\n')
File2=open('File1.txt','a+')
print(File2.tell())
print(File2.read())
File2.write('Python Deveops')
print(File2.tell())
print(File2.read())
print(File2.tell())

#(iii)....
print('(iii)...\n')
#File3=open('File5.txt','a+')#Here I Get a new File
File3=open('File2.txt','a+')
print(File3.tell())
File3.write('sita')
File3.seek(0)
print(File3.tell())
print(File3.read())
print(File3.tell())