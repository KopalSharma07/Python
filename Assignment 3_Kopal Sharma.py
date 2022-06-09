#Question 1

a=int(input("Enter a number you want to convert into binary: "))
print("Binary form of",a,"is: ",bin(a))

#Output 1

#Enter a number you want to convert into binary: 56
#Binary form of 56 is:  0b111000


#Question 2

exp=input("Enter the expression you want to solve: ")
calculation=eval(exp)
print(exp,"=",calculation)


#Output 2

#Enter the expression you want to solve: 65/5**2
#65/5**2 = 2.6


#Question 3

# 1. (3+4)(5)
import math
a = int((3+4)*(5))
print("(3+4)(5) = ",a)

# 2. n(n-1)/2
n= int(input("Enter the value of n:"))
c = n * (n-1)/2
print ("n(n-1)/2 = ",c)

# 3. 4πr^2
r = int(input("Enter the value of r: "))
d = 4 * math.pi * r**2
print ("4πr^2=",d)

# 4. [r(cos a)^2 + r(sin b)^2]^0.5
r= int(input("Enter the value of r:"))
a= int(input("Enter value of a:"))
b= int(input("Enter value of b:"))
c=math.sqrt(r * (math.cos(a))**2 + r * (math.sin(a))**2)
print ("√(r(cos a)^2 + r(sin b)^2) =",c)

# 5. (y2-y1)/(x2-x1)
y1= int(input("Enter y1:"))
y2= int(input("Enter y2:"))
x1= int(input("Enter x1:"))
x2= int(input("Enter x2:"))
a=(y2-y1)/(x2-x1)
print("(y2-y1)/(x2-x1) = ",a)


#Output 3

#(3+4)(5) =  35

#Enter the value of n:5
#n(n-1)/2 =  10.0

#Enter the value of r: 5
#4πr^2= 314.1592653589793

#Enter the value of r:5
#Enter value of a:5
#Enter value of b:6
#√(r(cos a)^2 + r(sin b)^2) = 2.2360679774997894

#Enter y1:1
#Enter y2:9
#Enter x1:4
#Enter x2:5
#(y2-y1)/(x2-x1) =  8.0


#Question 4

for i in range(5):
    print(i)

for i in range(3,10):
    print(i)

for i in range(4,13,3):
    print(i)

for i in range(15,5,-2):
    print(i)

for i in range(5,3):
    print(i)
    
#Output 4

#0
#1
#2
#3
#4

#3
#4
#5
#6
#7
#8
#9

#4
#7
#10

#15
#13
#11
#9
#7

    
#Question 5

a=int(input("Enter the number of hydrogen atoms:"))
b=int(input("Enter the number of carbon atoms:"))
c=int(input("Enter the number of oxygen atoms:"))
d=a*1.00794
e=b*12.0107
f=c*15.9994
print("Molecular weight of the carbohydrate molecule=",d+e+f)

#Output 5

#Enter the number of hydrogen atoms:6
#Enter the number of carbon atoms:3
#Enter the number of oxygen atoms:3
#Molecular weight of the carbohydrate molecule= 90.07794
