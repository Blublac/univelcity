# #Name = input("what is your name ")
# #Favourite_colour = input("what is your Favourite colour ")
# #print (Name +" likes " + Favourite_colour)
# price_of_house = 1000000
# good_credit = 500000
# bad_credit = 1000

# bank_account = int(input("how much does he have:\n>"))
# if bank_account >= good_credit and bank_account < price_of_house :
#    Down_payment = price_of_house * 0.1
# elif bank_account <=bad_credit:
#     Down_payment=("Not Eligible")
# else:
#     Down_payment = price_of_house * 0.2
# print(f"Down payment is :$ {Down_payment}")
# if bank_account==price_of_house:
#     print("SOLD")

# Name = input("Enter your name\n>")
# if len(Name) < 3:
#     print("Name must be atleast 3 characters")
# elif len(Name) > 50:
#     print("Name cannot be more than 50 characters")
# else:
#     print(Name)
#     print(len(Name))
#     print("Name looks good")

# #weight measurement program
# weight= int(input("Weight\n>"))
# unit = input("(L)bs or (K)g\n>").upper()
# if unit == "L":
#     converted = weight*0.45
#     print(f"Weight is {converted} in Kg" )
# else:
#     converted = weight//0.45
#     print(f"weight is {converted} in pounds")


#while loop
#car game
# help = """start - To start the car.\nstop - To stop the car.\nquit- To exit """.title().lower()

# started = False
# ask_for_help = input("Ask for HELP\n")
# while True:
#     command = input("command here please\n>").lower()
#     if command == "start":
#         if started:
#             print("car already started")
#         else:
#             started=True   
#             print("car started")
#     elif command == "stop":
#         if not started:
#             print("car already stopped")
#         else:
#             started=False    
#             print("car stopped")
#     elif command == "quit":
#         break
#     else:
#         print("oops invalid command")
#for loop
# item_prices= [200,300,300]
# total = 0
# for item in item_prices:
#     total += item
# print(total)

# NUMS = [2,2,2,2,5]
# for cout in NUMS:
#     out = ""
#     for items in range(cout):
#         out += "x"
#     print(out)

# list_of_colours = ["Red","Green","White","Blac", "Pink", "Yellow"]
# print(list_of_colours)
# for coloz in list_of_colours:
#     User_favorite_colour = input("enter your favourite colour\n>").lower()
#     for selected in coloz:
#          user_favorite_colour = selected
#          print("COLOUR ALREADY EXIST")
#          break
#     if user_favorite_colour == coloz:
#         print(list_of_colours.append(User_favorite_colour))
    
        
# list_of_colours.append(User_favourite_colour)
# print(list_of_colours)
# numbas = [100,20,300,500,1000,123,54,654,345,987,87,65,44,56,76]
# a = numbas[0]
# for item in numbas:
#     if item > a:
#         a = item
# print(a)
# numbas.sort()
# numbas.reverse()
# print(numbas[0])

# noss = [1,2,3,1,2,4,5,3,54,6,2,4,6,8,9,6,5,43,4,5,3,23,4,3,23,2,2,1,21,2,43,5,3,2,12,4]
# uniques = []
# # for noz in noss:
# #     if noz not in uniques:
# #         uniques.append(noz)
# # print(uniques)


# # phone=input("enter digits\n>")
# # values ={
# #     "1":"one" ,"2":"two", "3":"three","4":"four",
# #      "5":"five", "6":"six","7":"seven","8":"eight",
# #      "9":"nine", "0": "zero"
# # }

# # ooo = ""
# # for no in phone:
# #     ooo += values.get(no, " ")+" "
# # print(ooo)


# # def emoji_eonverter(message):
# #     word=message.split(" ")
# #     emoji = {
# #         ":)" :"5678",
# #         ":(" :"9875"
# #     }
# #     output= " "
# #     for words in word:
# #         output+= emoji.get(words,words)+" "
# #     return(output)
# # message = input("text here")
# # emoji_eonverter(message)
# # print(emoji_eonverter(message))


# # class Person:
# #     def __init__(self, name):
# #         self.name =name
# #     def talk(self):
# #         print("talk")
# # Person1 = Person("Kene")
# # print(Person1.name)
# # Person1.talk()
        


# #
# # Complete the 'plusMinus' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# # n = int(input().strip())
# # arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
# # print("{0:.6f}".format(arr.count(1)/n))
# # print("{0:.6f}".format(arr.count(-1)/n))
# # print("{0:.6f}".format(arr.count(0)/n))
# # print(type(arr))


# list_0f_no = [23,4,-5,6,5,7,-8,9,0,0,-7,5,-5,9,0,-5,0,0,7]
# positve = []
# negative = []
# zero = []
# for i in list_0f_no:
#     if i > 0:
#         positve.append(i)
#     elif i < 0:
#         negative.append(i)
#     else:
#         zero.append(i)
# print(positve)
# print(negative)
# print(zero)

# ratio1 =len(positve)/(len(list_0f_no))
# ratio2 =len(negative)/(len(list_0f_no))
# ratio3 =len(zero)/(len(list_0f_no))
# print("{:.6f}".format(ratio1))
# print("{:.6f}".format(ratio2))
# print("{:.6f}".format(ratio3))



# print(list(range(1,100)))
# multiples3 = 0
# multiples5 = 0
# for elems in range(1,100):
#     if elems % 3 == 0:
#         multiples3 += elems
#     elif elems % 5 == 0:
#         multiples5 += elems
        
# print(multiples3)
# print(multiples5)


# tot_for_3 = 0
# tot_for_5 = 0
# tot = 0
# arrq = list(range(1,100))
# xx = []
# xy = []
# xz = []
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         xx.append(i)
#         tot+= i
#     if i % 3 == 0:
#         xy.append(i)
#         tot_for_3 +=i
#     if i % 5 == 0:
#         xz.append(i)
#         tot_for_5 += i
# print(tot)
# print(tot_for_3)
# print(tot_for_5) 
# print(xx)
# print(xy)
# print(xz)
# print(arrq)


winno = 9
trial = 0
while trial < 3:
    guess = int(input("guess oo\n>"))
    trial += 1
    if guess == winno:
        print("you win")
        break
    else:
        if trial <= 2:
            print("try again")
else:
    print("failed")
