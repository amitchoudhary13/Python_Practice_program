
#!/usr/bin/python
'''
Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average.
'''
#variable declaration
num = 10;
total_sum = 0;
number = [];
numless = [];
nummore = [];
numequi = [];
#user input and total_sum
for x in range(num):
    number.append(float(input('enter number : ')))
    total_sum += number[x]
    
#Average
avg = total_sum/num
print 'Average of ', num, ' numbers is :', avg

#less,more,equal than average.
for x in range(num):
    if number[x] < avg:
        numless.append(number[x])
    if number[x] > avg:
        nummore.append(number[x])
    if number[x] == avg:
        numequi.append(number[x])

print 'list of numbers less than average ', numless
print 'list of numbers more than average ', nummore
print 'list of numbers equal than average ', numequi