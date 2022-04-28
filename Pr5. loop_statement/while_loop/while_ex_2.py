
#Program to find sum of digit of a given number.

n=int(input("Enter A Number"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=int(n/10)
print("Sum of Number:", sum)
