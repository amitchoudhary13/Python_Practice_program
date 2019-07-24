'''

Using calendar module perform following operations.
a) Print the 2016 calendar with space between months as 10 characters.
b) How many leap days between the years 1980 to 2025.
c) Check given year is leap year or not. 
d) print calendar of any specified month of the year 2016.

'''
import calendar as calendar

print(cal.calendar(2016,0,0,10))

print(cal.leapdays(1980,2025))

year_input = input("enter year to check if its leap or not (yyyy)")

print(cal.isleap(year_input))

month_input = input("enter month (mm)")

print(cal.month(2016,month_input))