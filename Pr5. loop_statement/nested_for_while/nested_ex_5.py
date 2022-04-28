# Program to print Pyramid:

""" 
                1
              1 2 1
            1 2 3 2 1
          1 2 3 4 3 2 1
        1 2 3 4 5 4 3 2 1 

"""

for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end=' ')
    for a in range(1,i+1):
        print(a,end=' ')
    for x in range(a-1,0,-1):
        print(x,end=' ')
    print()