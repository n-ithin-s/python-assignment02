1#write a program to check wheather a number is odd or even
n=int(input("enter the number"))
if n%2==0:
    print("the number is even")
else:
    print("the number is odd")

2#find the largest of 3 numbers
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
if a>b:
    if a>c:
        print("the greatest number is:",a)
    else:
        print("the greatest number is:",c)
elif b>a:
    if b>c:
         print("the greatest number is:",b)
    else:
        print("the greatest number is:",c)

3#check wheather a given year is leap year or not
n=int(input("enter the year"))
if n%4==0:
    if n%400==0 or n%100!=0:
        print("the year is  a leap year")
    else:
        print("the year is not a leap year")
else:
    print("the year is not a leap year")

4#find summing numbers using while loop
sum=0
while True:
    n=input("Enter a number (or 'exit' to stop): ")
    if n=="exit":
        break
    else:
        sum=sum+int(n)
print("the sum of numbers is:",sum)  

5#print countdown of a number
n=int(input("enter the number"))
for i in range(n,0,-1):
    print(i)
