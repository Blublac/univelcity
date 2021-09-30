#tuples
t1 = (False, "true", 100)
t2 =(1,4,9)
t3 = t1+t2
print(t3)

# #sets
# s = {"True","Born",45,100,"Water",45,}
# z = {"Mary","Favour", "Tunde", 20, 100}
# s.pop()
# print(s)
# s.discard(100)
# s.add("cool")
# print(s)
# q = s.union(z)
# w = s.difference(z)
# e = s.intersection(z)
# r = s.symmetric_difference(z)
# s.update(z)
# print(q)
# print(w)
# print(e)

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print(set1.intersection(set2))
print(set1.union(set2))

set11 = {10,20,30}
set22 = {20,40,50}
set11.difference_update(set22)
print(set11)

#set1.difference_update({10,20,30})
#print(set1)
set3 = set1.symmetric_difference(set2)
print(set3)
set1.intersection_update(set2)
print(set1)