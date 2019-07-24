#Write a program to perform following file operations

#b) Open the file in write mode and enter 5 new lines of strings in to the new file.
fo=open("firstFile2.txt","w")
fo.writelines("so we have come to the end now\ni dont think this is\nyes very true\n still to go\n this is final now")
fo.close()

#a) Open the file in read mode and read all its contents on to STDOUT.
fo = open("firstFile2.txt","r")
print("Read String is : ",fo.read())
fo.close()




#c) Open file in Append mode and add 5 lines of text into it.
fo=open("firstFile2.txt","a")
fo.writelines("finally\nso we have come to the end now\n again and again\nsorry to keep you waiting\nFINAL ONE!!!!")
fo.close()


