#16-SEPT-2021
#list
# a list is ordered and its changeble and can be indexed 
a = [0,1,5,20,1,2,0,False]
a[3] = 6000
a[7]= True
b = [4,1,5,"hi",False]
#c = [a+b]
a.extend(b)
print(a)


#create a new list of usernames.
#  Then write a program to get input from the user requesting his first name and last name
#  genetate a username for him. the username should comprise of the first 3 words of his last name and the last 2 words of his first name
#Add his usere name to the list of username and print an output telling him his account has been created.
#hello, user's firstname thank you for signind up your account has sucessfully been created cheers admin
usernames = ["Frank3","Henro","blacky3"]
First_name = input("Enter your first name\n>")
Last_name = input("Enter your last name\n>")
userid = Last_name[0:3]+First_name[-2:]
usernames.append(userid)
print(usernames)
print(f"Hello, {First_name.title()}:.\n\tThank you for signing up. Your account has successfully been created.\n\tYour account ID is {userid}.\n\t\tCHEERS....\n\t\tAdmin")

#GIVEN THE LIST BELOW
#[500,200,[200,500,700,[250,800],250][1000]]

NUMBERS = [500,200,[200,500,700,[250,800],250],[1000]]
X = NUMBERS[2][2]+NUMBERS[2][3][1]
print(X)
NUMBERS[3].append(X)
print(NUMBERS)

str1= "Emma is a Data scientist who knows python. Emma works at google."
str2 = str1.rindex("Emma")
print(f"Last occurrance of Emma starts at index {str2}")

a=["hello","h","gg"]
b= a
ist=a.copy()
a[0]="jjj"
print(a)
print(b)
print(ist)
removed_element =a.remove("jjj")
popped_element = a.pop(-1)
a.pop(-1)
print(a)
print(popped_element)
print(removed_element)
new_list = [3136]
new_list.insert(0,4546)
print(new_list)
new_list.sort()

print(new_list)
import random