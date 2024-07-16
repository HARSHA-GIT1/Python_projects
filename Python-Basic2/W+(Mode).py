#THIS PROGRAM IS ALSO SHOWING THE WORKING OF FILE HANDLING...
#CASE-4( w+ MODE)
#In w+ Mode If File Is Exists Then It Over Write The Data.
#If Not Exists Then First Create and after use..
#(i)...
'''print('(i)...\n')
File1=open('File1.txt','w+')
print(File1.tell())
print(File1.tell())
'''
'''#(ii)...
print('(ii)...\n')
File2=open('File1.txt','w+')
print(File2.tell())
File2.write( 'Python Deveops')
print(File2.tell())
print(File2.read())
print(File2.tell())
'''
#(iii)....
print('(iii)...\n')
#File3=open('File5.txt','w+')#Here I Get a new File
File3=open('File1.txt','w+')
print(File3.tell())
File3.write('sita')
File3.seek(0)
print(File3.tell())
print(File3.read())
print(File3.tell())