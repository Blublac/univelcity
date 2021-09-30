noba = int(input("VALUE HERE\n>"))
if noba % 2 == 0 and noba in range(2,5):
    print("NOT WEIRD")
if noba % 2 == 0 and noba > 20:
    print("NOT WEIRD")
elif noba % 2 ==0 and  noba in range(6,20):
    print("WEIRD")
else:
    print("WEIRD")


