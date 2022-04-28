
#Program to check whether the entered number is prinme or not

n=int(input("Enter your Number:"))
for i in range(2,n+1):
    if n%1==0:
        break
if i==n:
    print(n," Is prime Number.")
else:
    print(n,"is not a prime Number.")