#Question 1

a="Python is a case sensitive language"
print(a)
print("Length of the string:",len(a))
print("Reverse of the string:",a[::-1])
b=a[10:-9]
print("The specified part:",b)
print("String after replacement",a.replace("a case sensitive","object oriented"))
print("The index of 'a' is",a.index('a'))
print("String without space",a.replace(" ",""))

#Solution 1

#Python is a case sensitive language
#Length of the string: 35
#Reverse of the string: egaugnal evitisnes esac a si nohtyP
#The specified part: a case sensitive
#String after replacement Python is object oriented language
#The index of 'a' is 10
#String without space Pythonisacasesensitivelanguage



#Question 2

a=input("Enter your name: ")
b=int(input("Enter your SID: "))
c=input("Enter the name of the department: ")
d=float(input("Enter your CGPA: "))
print("Hey,",a,"Here!\nMy SID is",b,"\nI am from",c,"department and my CGPA is",d)

#Solution 2

#Enter your name: Kopal Sharma
#Enter your SID: 21102019
#Enter the name of the department: Civil
#Enter your CGPA: 9.6
#Hey, Kopal Sharma Here!
#My SID is 21102019
#I am from Civil department and my CGPA is 9.6



#Question 3

a=56
b=10
print("a=",a)
print("b=",b)
print("Result of a&b=",a&b)
print("Result of a|b=",a|b)
print("Result of a^b=",a^b)
print("Result of left shift of a with 2 bits=",a<<2)
print("Result of left shift of b with 2 bits=",b<<2)
print("Result of right shift of a with 2 bits=",a>>2)
print("Result of right shift of b with 4 bits=",b>>4)

#Solution

#a= 56
#b= 10
#Result of a&b= 8
#Result of a|b= 58
#Result of a^b= 50
#Result of left shift of a with 2 bits= 224
#Result of left shift of b with 2 bits= 40
#Result of right shift of a with 2 bits= 14
#Result of right shift of b with 4 bits= 0



#Question 4

a=input("Enter the string:")
if "name" in a:
    print("Yes")
else:
    print("No")

#Solution

#Enter the string:Hello my name is Kopal
#Yes
#Enter the string:Hello world, we live in a free world.
#No


#Question 5

a=int(input("Enter the 1st side of triangle: "))
b=int(input("Enter the 2nd side of triangle: "))
c=int(input("Enter the 3rd side of triangle: "))
d=max(a,b,c)
e=a+b+c
f=e-d
while(f>d):
    print("Triangle can be formed")
    break
while(f<=d):
    print("Triangle can not be formed")
    break

#Solution

#Enter the 1st side of triangle: 5
#Enter the 2nd side of triangle: 4
#Enter the 3rd side of triangle: 8
#Triangle can be formed

#Enter the 1st side of triangle: 7
#Enter the 2nd side of triangle: 9
#Enter the 3rd side of triangle: 1
#Triangle can not be formed

#Enter the 1st side of triangle: 2
#Enter the 2nd side of triangle: 3
#Enter the 3rd side of triangle: 5
#Triangle can not be formed


#Question 6

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=a^b
d=0
while(c!=0):
    c=c&(c-1)
    d+=1
print("Number of bits to be fliped: ",d)

#Solution

#Enter the 1st number: 6
#Enter the 2nd number: 9
#Number of bits to be fliped:  4
