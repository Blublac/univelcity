#GIVEN A STRING S1 AND S2 CREATE A NEW STRING BY APPENDING S2 IN THE MIDDLE OF S1 GIVEN S1 = AUIT S2 = KELLY
s1 = "Auit"
s2 = "Kelly"
print(s1[0]+s1[1]+s2+s1[2]+s1[3])

#GIVEN 2 STRINGS, S1 AND S2 RETURN A NEW STRING MADE OF THE FIRST AND LAST CHARACTER EACH INPUT STRING
a1 = "America"
a2 = "Japan"
a3 = a1[0]+a2[0]+a1[3]+a2[2]+a1[-1]+a2[-1]
print(a3)

#CREATE A THIRD STRING MADE OF THE FIRST CHARACTER OF S1 THEN THE LAST CHARACTER OF S2, NEXT THE SECOND CHARACTER OF S1 AND SECOND LAST CHARACTER OF S2 AND SO ON
q1 = "Abc"
q2 = "Xyz"
q3 = q1[0]+q2[-1]+q1[1]+q2[-2]+q1[2]+q2[0]
print(q3)

#corretion for assignment
r1 = "Auit"
r2 = "Kelly"
r3 = int(len(s1)/2)
solution = r1[0:r3]+s2 +r1[r3:]
print(solution)

i1 = "China"
i2 = "Japan"
b1 = i1[0]
b2 = i2[0]
c1 = i1[len(i1//2)]
d1 = i1