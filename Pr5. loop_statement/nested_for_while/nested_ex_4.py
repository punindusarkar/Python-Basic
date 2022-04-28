# Program to print following pyramid:
""" 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

from itertools import count


count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end='')
        count=count+1
        if count>9:
            count=1
    print()