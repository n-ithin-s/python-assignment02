

#Write a program to create a list of fruits and copy only 'e' letter fruits to the new list
fruits=[]
new_fruits=[]


while(True):
    fruit=input("enter fruits or stop to exit ")
    if(fruit=="exit"):
        break
    fruits.append(fruit)

    
for x in fruits:
    for y in x:
        if(y=='e'):
            new_fruits.append(x)
            break

print(new_fruits)

#write a program to find prime number or not
n=int(input("enter the number"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("number is prime")
else:
    print("number is composite")


