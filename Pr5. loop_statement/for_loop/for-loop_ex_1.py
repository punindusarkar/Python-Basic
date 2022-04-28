
# Program to print prime numbers in between a range.

start=int(input("Enter Starting Number:"))
end=int(input("Entrer Ending Number:"))

for n in range(start,end + 1):
    if(n>1):
        for i in range(2,n):
            if(n%i)==0:
                break
            else:
                print(n)