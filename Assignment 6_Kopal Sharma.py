#Question 1

list1=[]
def div(n):
    i=1
    while i<=n:
        if(n%i==0):
            list1.append(i)
        i=i+1
    print("List of divisors: ",list1)


n=int(input("Enter the number: "))
div(n)

total=0
for i in range(0,len(list1)):
    total=total+list1[i]

total=total-n

if (total==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
    
    
#Output1
    
#Enter the number: 6
#List of divisors:  [1, 2, 3, 6]
#6 is a perfect number

#Enter the number: 9
#List of divisors:  [1, 3, 9]
#9 is not a perfect number


#Question 2

a=input("Enter the string you want to check is palindrome: ")
b=a.lower()
c=b.replace(" ","")
d=c[::-1]
if c==d:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

#Output 2
    
#Enter the string you want to check is palindrome: Nurses Run
#String is a palindrome

#Enter the string you want to check is palindrome: Hi how are you
#String is not a palindrome
    

#Question 3

from math import factorial
n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
  
    print()

#Output 3
    
#Enter the number of rows=8
#        1 
#       1 1 
#      1 2 1 
#     1 3 3 1 
#    1 4 6 4 1 
#   1 5 10 10 5 1 
#  1 6 15 20 15 6 1 
# 1 7 21 35 35 21 7 1


#Question 4

def ispangram(str):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for char in alphabet:
		if char not in str.lower():
			return False
	return True
	
s=input("Enter a String: ")
if(ispangram(s) == True):
    print(f"Yes, '{s}' is a panagram")
else:
    print(f"No, '{s}' is not a panagram")
print()

#Output 4

#Enter a String: qwertyuioplkjhgfdsazxcvbnm.
#Yes, 'qwertyuioplkjhgfdsazxcvbnm.' is a panagram

#Enter a String: Hi how are you
#No, 'Hi how are you' is not a panagram


#Question 5

a=input("Enter a string:")
list1=[]
list1=a.split("-")
list1.sort()
str1=""
for i in list1:
    if str1=="":
        str1=str1+i
    else:
        str1=str1+"-"+i
print("Sorted list:",list1)
print("Sorted string:",str1)

#Output 5

#Enter a string:rtyu-asd-jhgf-bvc-cvb-ytr-zxbn-dfgh
#Sorted list: ['asd', 'bvc', 'cvb', 'dfgh', 'jhgf', 'rtyu', 'ytr', 'zxbn']
#Sorted string: asd-bvc-cvb-dfgh-jhgf-rtyu-ytr-zxbn


#Question 6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")

 
student_data(student_id='21105048', student_name='Aakash')

student_data(student_id='21109052', student_name='Adarsh', student_class ='XII')

#Output 6

#Student ID: 21105048
#Student Name: Aakash

#Student ID: 21109052
#Student Name: Adarsh

#Student Name: Adarsh
#Student Class: XII


#Question 7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Output 7

#True
#False
#True
#False
#Check whether the said classes are subclasses of the built-in object class or not.
#True
#True

#Question 8

def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print([arr[i], arr[j], arr[k]])
					found = True
	if found == False:
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input("Enter the element:"))
	lst.append(ele) 
print(findTriplets(lst,n))  

#Output 8
#Enter number of elements : 9
#Enter the element:-3
#Enter the element:2
#Enter the element:1
#Enter the element:-6
#Enter the element:-5
#Enter the element:11
#Enter the element:-9
#Enter the element:-8
#Enter the element:17
#[-3, 2, 1]
#[-3, 11, -8]
#[-6, -5, 11]
#[-9, -8, 17]
#None

#Question 9

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")

#Output 9

#Enter the sequence of parantheses : []()
#[]() - is balanced

#Enter the sequence of parantheses : []{{][}{{}
#[]{{][}{{} - is unbalanced
