# my_dict = {"name":"jerry", 
#         "courses":["data science","backend"],
#         "scores":{"data science":20,"backend":15-7}}
# var = my_dict.pop("scores")
# my_dict.update({"result": var})
# my_dict["result"] = var
# print(my_dict)


# a= my_dict["result"]
# print(type(a))
# print(type(list(my_dict.keys())))

smapledict = {"emp1" : {"name":"jhon","salary":7500},
              "emp2" : {"name": "Emma","salary":8000},
              "emp3" : {"name": "Brad","salary":6500}
              }
smapledict ["emp3"]["salary"] = 8500
print(smapledict)


# #a program that takes in user details and saves it un the user dict

# users = {}
# first_name =input("enter first name\n")
# last_name = input("enter last name\n")
# username = first_name[:3]+last_name[:-3]
# users[username]= {}
# users[username]["first_name"] = first_name
# users[username]["last_name"] = last_name
# print(users)

# list1 = [2,2,4,6,7,2,4,4,3,6,2,1]
# list2 = list(set(list1))
# print(list2)

# multipe_nos = ["11","55","33"]
# mult = "".join(multipe_nos)
# print(int(mult))

# x,y,w,r = ("hi","how","are","you")
# print(x)
# print(y)
# print(w)
# print(r)

# tuplez = ("u","n","i","v","e","l","c","i","t","y")
# uni = "".join(list(tuplez))
# print(uni)

total_no_en  = input("No of english students")
list_no_en = input("list of english students")
total_no_fr = input("No of french students")
list_no_fr = input("lisy of french students")

english = set(list_no_en.split())
french = set(list_no_fr.split())
no = english.symmetric_difference(french)
print(no)
print(len(no))

