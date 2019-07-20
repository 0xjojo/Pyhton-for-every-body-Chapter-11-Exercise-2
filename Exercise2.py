#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average.
#Enter file:mbox.txt
#38444.0323119
fhand = open (input("Enter file:"),'r')
tot = 0
avj = 0
num_list = []
for line in fhand :
    line = line.rstrip()
    y = findall('^New Revision: ([0-9]+)',line)
    if len(y) > 0 :
        num_list = num_list.append(y)
for num in num_list :
    tot = tot + float(num)
avj = tot / len(num_list)
print (avj)
