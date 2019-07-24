#Write a program to open the existing file in read mode and perform following tasks,

#a) Read 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
fo=open("file.txt","r")
position=0
#print(fo.read())
while True:
    a=fo.read(10)
    if not a:
        break
    else:
        print(a)
        position+=10
        print("position=",position)




#b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
fo=open("file.txt","r")
position=0
while position<100:
    a=fo.read(10)
    if not a:
        break
    else:
        print(a)
        position+=10
        print("position=",position)
fo.seek(0,0)
print(fo.read(10))




#c) Open the file in read mode and start printing the contents from 5th line onwards.
fo = open("file.txt","r")
for i in range(5):
    fo.readline()
for line in fo:
    print("line=",line)
fo.close()


