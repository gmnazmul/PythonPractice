print('Hello')
name = 'mery'
grade = 81.7993
record = '%s: %.2f' % (name, grade)
print(record)


#input
name = input()
print(name)


#output to file
import sys
sys.stdout = open('text.txt', 'a')
record = '%s: %.2f' % (name, grade)
print(record)
