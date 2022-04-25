#Question 1

a1=int(input("Enter 1st number : "))
a2=int(input("Enter 2nd number : "))
a3=int(input("Enter 3rd number : "))
print("Average of the numbers : ",(a1+a2+a3)/3)


#output

#Enter 1st number : 7
#Enter 2nd number : 7
#Enter 3rd number : 7
#Average of the numbers :  7.0




#Question 2

a1=int(input("Enter Gross Income : "))
a2=int(input("Enter the number of dependents :"))
a3=a1-10000-(3000*a2)
a4=a3*0.2
print("Tax to be paid : ",a4)


#output

#Enter Gross Income : 500000
#Enter the number of dependents :3
#Tax to be paid :  96200.0



#Question 3

a1=input("Enter the name of the person : ")
a2=int(input("Enter the age of the person : "))
a3=float(input("Enter the marks obatined by the person : "))
a4=input("Enter the name of the course peson wants to take : ")
a5=int(input("Enter the SID of the students : "))
a6=[a1,a2,a3,a4,a5]
print("Information about the person :",a6)



#output

#Enter the name of the person : abc
#Enter the age of the person : 16
#Enter the marks obatined by the person : 89.8
#Enter the name of the course peson wants to take : civil
#Enter the SID of the students : 2110215675
#Information about the person : ['abc', 16, 89.8, 'civil', 2110215675]



#Question 4


a1=int(input("Enter the marks of 1st student : "))
a2=int(input("Enter the marks of 2nd student : "))
a3=int(input("Enter the marks of 3rd student : "))
a4=int(input("Enter the marks of 4th student : "))
a5=int(input("Enter the marks of 5th student : "))
a6=[a1,a2,a3,a4,a5]
print("Marks of the students : ",a6)
a6.sort()
print("Marks of the students in the sorted manner : ",a6)




#output

#Enter the marks of 1st student : 94
#Enter the marks of 2nd student : 75
#Enter the marks of 3rd student : 78
#Enter the marks of 4th student : 35
#Enter the marks of 5th student : 41
#Marks of the students :  [94, 75, 78, 35, 41]
#Marks of the students in the sorted manner :  [35, 41, 75, 78, 94]



#Question 5


a1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a1.pop(3)
print(a1)


#output

#['Red', 'Green', 'White', 'Pink', 'Yellow']


b1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b1=["Purple" if(i=="Black")or(i=="Pink")else i for i in b1]
print(b1)


#Output

#['Red', 'Green', 'White', 'Purple', 'Purple', 'Yellow']



