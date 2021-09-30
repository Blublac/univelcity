#write a program that takes in input from the user , asking him for a list of the total  prices of items bought in 7days separated by a comma.
#calclate the sum
#calculate the average.
#return a stdout(standard output) telling him how much he has spent and the average amount.






# list_of_items = input("total price per day").split(",")
# num_list = list(map(lambda i : int(i),list_of_items))
# print(sum(num_list))

# print(sum(num_list)/len(num_list))

# my_math = lambda x,y,z : x**2+y+z
# print(my_math(6,7,6))
# li = [1,2,3,4,5]


# l2 = list(map(lambda i : i**2,li))
# print(l2)

# c = ["002","014","029"]
# p = [2000,4000,2015]
# d = dict(zip(c,p))
# print(d)

# print(list(enumerate(c)))

# my_list =[2,3,4,5,7,5,4,6,87,9]
# filtered = list(filter (lambda x: x%2 != 0,my_list))
# print(filtered)

import time
# user = input("Enter your name")
# print ("creating your account please wait")
# time.sleep(5)
# print("Hey there! kindly wait...")
# time.sleep(5)
# print("still there?")
# time.sleep(5)
# print(f"Hey, {user} yor account has been created")

import random
# mmm= [3,45,6,8,89,9,7,5,4,3,4,5]
# random.shuffle(mmm)
# print(mmm)
# import datetime
# from datetime import datetime
# print(datetime.now())

# print ("Welcome to this guess game")
# list_of_ran = [10,3,4,6,7,8,6,4,4,3,5]
# choice = int(input(f"Guess a number from {list_of_ran}\n>"))
# random.shuffle(list_of_ran)
# com_choice = random.choice(list_of_ran)
# if choice==com_choice:
#     print("YOU WIN!!!!!!")
# else:
#     print("try again")

# print("WELCOME TO GAME")
# if input("press S to start").upper() == S:
#     print("Game started")
#     games = ["R","P","S"]
#     your_turn = input(f"ENTER ANY OF THE LETTERS{games}\n>").upper()
#     random.shuffle(games)
#     comp_turn = random.choice(games).upper()
#     if your_turn == games[0] and comp_turn == games[2]:
#         winner = games[0]
#         print("YOU WIN")
#     elif your_turn == games[1] and comp_turn == games[0]:
#         winner = games[1]
#         print("you win")
#     elif your_turn == games[2] and comp_turn == games[1]:
#         winner = games[2]
#         print("you win")
#     elif comp_turn == games[0] and your_turn == games[2]:
#         winner = games[0]
#         print("COMP WIN")
#     elif comp_turn == games[1] and your_turn == games[0]:
#         winner = games[1]
#         print("COMP WIN")
#     elif  comp_turn == games[2] and your_turn == games[1]:
#         winner = games[2]
#         print("COMP WIN")
#     elif your_turn == comp_turn:
#         print("PICK AGAIN")
    

#ROCK,PAPER,SCISSORS.
print("Welcom to the game")
print("Rock Paper Scissors")
clue = """This is a simple game that follows the rule below
Rock wins scissors
Scissors wins Paper
Paper wins Rock
Choices are R for rock, P for paper and S for scissors.
You have only one chance."""
print(clue)
player_name = input("Enter your name")
choices = ["r","p","s"]
player_choice = input("What do you choose?\n").lower()
random.shuffle(choices)
comp_choice = random.choice(choices)
if  player_choice in choices:
    if (player_choice == "r" and comp_choice == "s") or (player_choice == "p" and comp_choice == "r") or (player_choice == "s" and comp_choice == "p"):
        print("HEY {player_name}!, YOU WIN")
    elif (comp_choice == "r" and player_choice == "s") or (comp_choice == "p" and player_choice == "r") or (comp_choice == "s" and player_choice == "p"):
        print("COMPUTER WINS")
    else:
        print("ITS A TIE")
else:
    print("INVALID INPUT.")
 


