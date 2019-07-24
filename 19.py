#!/usr/bin/python
'''
19.Using loop structures print even numbers between 1 to 100. 
a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 50 
ii) Use continue for the values 10,20,30,40,50

b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 90 
ii) Use continue for the values 60,70,80,90
'''

#Using for loop structure to print even numbers between 1 to 100
print "The even numbers from 1 to 100 using for loop is below:" 
for i in range(1,101):
  if i%2==0:
    print i
print "\n\n"


#.a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
print "The numbers from 1 to 100 skipping odd numbers using for loop is below:" 
for i in range (1,101):
  if i%2!=0:
    continue
  print i
print "\n\n"


#.i) break the loop if the value is 50 
print "Breaking the for loop i ==50"
for i in range(1,101):
    if i==50:
      break
    print i
print "\n\n"    


#.ii) Use continue for the values 10,20,30,40,50
print "using continue for the values 10,20,30,40,50"    
for i in range (1,101):
  if i==10 or i==20 or i==30 or i==40 or i==50:
    continue
  print i
print "\n"    



#Using while loop structure to print even numbers between 1 to 100
print "The even numbers from 1 to 100 using while loop is below:" 
i=1
while i<=100:
  if i%2==0:
    print i
  i+=1
print "\n\n"


#.a) By using while loop , use continue/ break/ pass statement to skip odd numbers.
print "The numbers from 1 to 100 skipping odd numbers using while loop is below:" 
i=1
while i<=100:
  if i%2!=0:
    i+=1
    continue
  print i
  i+=1
print "\n\n"


#.i) break the loop if the value is 50 
print "Breaking the for loop i ==50"
i=1
while i<=100:
  if i==50:
    break
  print i
  i=i+1    


#.ii) Use continue for the values 10,20,30,40,50
print "using continue for the values 10,20,30,40,50"    
i=1
while i<=100:
  if i==10 or i==20 or i==30 or i==40 or i==50:
    i=i+1
    continue
  print i
  i=i+1
print "\n"