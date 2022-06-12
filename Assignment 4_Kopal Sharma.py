#Question 1:

a=int(input("Enter marks of the students:"))
if a>80:
    print("Grade scored:A")
elif 60<a<80:
    print("Grade scored:B")
elif 50<a<60: 
    print("Grade scored:C")
elif 45<a<50:
    print("Grade scored:D")
elif 25<a<45:
    print ("Grade scored:E")
else:
    print("Grade scored:F")

#Output 1:
    
#Enter marks of the students:85
#Grade scored:A
    
#Enter marks of the students:67
#Grade scored:B

#Enter marks of the students:53
#Grade scored:C
    
#Enter marks of the students:49
#Grade scored:D
    
#Enter marks of the students:44
#Grade scored:E
    
#Enter marks of the students:15
#Grade scored:F


#Question 2:
    
year=int(input("Enter year: "))
if year%4==0 or year%400==0:
    print(year,"is a leap year")
else:
    print(year," is not a leap year")

#Output 2:
    
#Enter year: 2016
#2016 is a leap year
    
#Enter year: 2200
#2200 is a leap year
    
#Enter year: 2019
#2019  is not a leap year


#Question 3:
    
import random
i=1
while i<=10:
    a=random.randint(1,30)
    b=random.randint(1,30)
    print(a, "X",b,"=")
    c=int (input ("Enter your answer: "))
    d=int(a*b)
    if c==d:
        print ("correct answer")
    else:
        print("wrong answer")
    i=1+i
print ("end")

#Output 3

#19 X 24 =
#Enter your answer: 262
#wrong answer
#1 X 5 =
#Enter your answer: 5
#correct answer
#1 X 5 =
#Enter your answer: 5
#correct answer
#18 X 9 =
#Enter your answer: 162
#correct answer
#14 X 18 =
#Enter your answer: 546
#wrong answer
#30 X 30 =
#Enter your answer: 900
#correct answer
#10 X 1 =
#Enter your answer: 10
#correct answer
#28 X 1 =
#Enter your answer: 28
#correct answer
#15 X 26 =
#Enter your answer: 390
#correct answer
#3 X 28 =
#Enter your answer: 84
#correct answer
#end


#Question 4:

x=200
for i in range(x):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i,"candies are in the bowl.")
                
#Output 4:
                
#177 candies are in the bowl.



