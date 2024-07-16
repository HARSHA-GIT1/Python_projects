#THIS PROGRAM IS ALSO SHOWING THE WORKING OF FILE HANDLING...
#CASE-4( r+ MODE)
#In r+ Mode If File Is Exists It Give File_Pointer To Poistion 1.
#If Not Exists Then You Get error..
#(i)...
'''print('(i)...\n')
File1=open('File1.txt','r+')
print(File1.tell())
print(File1.read())
print(File1.tell())
'''
#(ii)...
'''print('(ii)...\n')
File2=open('File1.txt','r+')
print(File2.tell())
print(File2.read())
print(File2.tell())
File2.write(' Python Deveops')
print(File2.tell())
print(File2.read())
print(File2.tell())'''
#(iii)....
print('(iii)...\n')
#File3=open('File5.txt','r+')#Here I Get Error Of File Is Not Exists.
File3=open('File1.txt','r+')
print(File3.tell())
File3.write('sita')
print(File3.tell())
print(File3.read())
print(File3.tell())

