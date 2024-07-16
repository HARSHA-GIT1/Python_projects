#THIS PROGRAM IS SHOWING HOW FILE-HANDLING WORK...
#CASE-1(Read Mode)
File1=open("File1.txt",'r')#Here If File Is Not Exits its Give Error
print(File1.read())

#CASE-2(Write Mode)
#In Write Mode If File Exits it Over write The Content From Starting.
#If File Does`t Exits First File Create And After Data Insert.
File2=open("File2.txt",'w')
File2.write('JAI')

File3=open('File3.txt','w')
File3.write('Hello')
#print(File3.read())#Here I Get Error Because We Can`t Be Use Read() in Write Mode.

#CASE-3(Append Mode)
#In Append Mode If File Exits it Start to write The Content at Ending.
#If File Does`t Exits First File Create And After Data Insert.
File4=open('File4.txt','a')
File4.write('Ram Ram')

print(type(File1))
print(type(File2))
print(type(File3))
print(type(File4))