#Question 1
a=input("Enter the string to be reversed: ")
print("Reversed string:",a[::-1])

#Output 1

#Enter the string to be reversed:
#Hello, python is an interpreted language
#Reversed string: egaugnal deterpretni na si nohtyp ,olleH


#Question 2
a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
c=int(input("Enter the number to check divisibility with: "))
for i in range(a,b):
    if i%c==0:
        print(i,"is divisible by",c)
    i=i+1

#Output 2
    
#Enter the lower limit: 1
#Enter the upper limit: 100
#Enter the number to check divisibility with: 5
#5 is divisible by 5
#10 is divisible by 5
#15 is divisible by 5
#20 is divisible by 5
#25 is divisible by 5
#30 is divisible by 5
#35 is divisible by 5
#40 is divisible by 5
#45 is divisible by 5
#50 is divisible by 5
#55 is divisible by 5
#60 is divisible by 5
#65 is divisible by 5
#70 is divisible by 5
#75 is divisible by 5
#80 is divisible by 5
#85 is divisible by 5
#90 is divisible by 5
#95 is divisible by 5

#Question 3

a=int(input("Enter the 1st side of triangle: "))
b=int(input("Enter the 2nd side of triangle: "))
c=int(input("Enter the 3rd side of triangle: "))
#Checking if the triangle exists or not
d=max(a,b,c)
e=a+b+c
f=e-d
if(f>d):
    print("Triangle can be formed")
    s=(a+b+c)/2
    area= ((s)*(s-a)*(s-b)*(s-c))**0.5
    print("Area of the triangle: ",area)
else:
    print("Triangle can not be formed")

#Output 3

#Enter the 1st side of triangle: 3
#Enter the 2nd side of triangle: 4
#Enter the 3rd side of triangle: 5
#Triangle can be formed
#Area of the triangle:  6.0


#Question 4

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end ='')
    print("")

for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end ='')
    print("")


#Output 4

#*
#**
#***
#****
#*****
#****
#***
#**
#*


#Question 5

a= int(input("Enter the number of rows you want: "))
ascii_no=65
for i in range(0,a):
    for j in range(0,i+1):
        b=chr(ascii_no)
        print(b,end="")
        ascii_no+=1
        if ascii_no>90:
            ascii_no=65
    print("")

#Output 5

#Enter the number of rows you want: 10
#A
#BC
#DEF
#GHIJ
#KLMNO
#PQRSTU
#VWXYZAB
#CDEFGHIJ
#KLMNOPQRS
#TUVWXYZABC


#Question 6

a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
x=0
while(a<=b):
    count=0
    i=2
    while(i<=a//2):
        if(a%i==0):
            count=count+1
        i=i+1
    if(count==0 and a!=1):
        print(a,"is a prime number")
        x=x+1
    a=a+1
print("Total prime numbers: ",x)

#Output 6

#Enter the lower limit:1
#Enter the upper limit:10
#2 is a prime number
#3 is a prime number
#5 is a prime number
#7 is a prime number
#Total prime numbers:  4


#Question 7

for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i,"is multiple of 7 and divisible by 11")

#Output 7

#77 is multiple of 7 and divisible by 11
#154 is multiple of 7 and divisible by 11
#231 is multiple of 7 and divisible by 11
#308 is multiple of 7 and divisible by 11
#385 is multiple of 7 and divisible by 11
#462 is multiple of 7 and divisible by 11


#Question 8

list1=[]
for i in range(0,10):
    a=int(input("Enter the number: "))
    if a>0:
        print(a,"is a positive number")
    if a<0:
        print(a,"is a negative number")
    if a%2==0:
        print(a,"is an even number")
    if a%2!=0:
        print(a,"is an odd number")
    list1.append(a)
res={}
for i in list1:
    res[i]=list1.count(i)
print(res)

#Output 8

#Enter the number: 1
#1 is a positive number
#1 is an odd number
#Enter the number: 3
#3 is a positive number
#3 is an odd number
#Enter the number: 5
#5 is a positive number
#5 is an odd number
#Enter the number: -6
#-6 is a negative number
#-6 is an even number
#Enter the number: 5
#5 is a positive number
#5 is an odd number
#Enter the number: 3
#3 is a positive number
#3 is an odd number
#Enter the number: -8
#-8 is a negative number
#-8 is an even number
#Enter the number: -6
#-6 is a negative number
#-6 is an even number
#Enter the number: 5
#5 is a positive number
#5 is an odd number
#Enter the number: 1
#1 is a positive number
#1 is an odd number
#{1: 2, 3: 2, 5: 3, -6: 2, -8: 1}


#Quesstion 9

a=input("Enter a string: ")
b=dict()
list1=a.split(' ')
for i in list1:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

#Output 9

#Enter a string: hi how are you i am good you are looking good as well
#{'hi': 1, 'how': 1, 'are': 2, 'you': 2, 'i': 1, 'am': 1, 'good': 2, 'looking': 1, 'as': 1, 'well': 1}
