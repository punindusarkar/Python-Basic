# Program to print following pyramid:
""" 
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 

"""

a=6
for i in range(a):
    for j in range(1,i+1):
        print(i,end='')
    print()