#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average.
#Enter file:mbox.txt
#38444.0323119
import re
bate = raw_input ("Enter file:")
fhand = open(bate)
tot = 0
avj = 0
num_list = []
for line in fhand :
    line = line.rstrip()
    y = re.findall('^New Revision: ([0-9]+)',line)

    if len(y) > 0 :
        float(y[0])
        num_list.append(y[0])
for num in num_list :
    tot = tot +float(num)
avj = tot / len(num_list)
print (avj)
