
#Program to check whether the input Armstrong number

n=int(input("Enter a Number:"))
num=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=int(n/10)
if num==sum:
    print(num, "is armstrong")
    print(num, "is not armstrong")