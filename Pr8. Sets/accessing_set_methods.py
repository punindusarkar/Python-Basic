# Methods of set in Python

# 1) add()


furits={"apple","banana","cherry","mango"}
print(furits)
furits.add("orange")
print(furits)

# 2) clear()
furits1={"apple","banana","cherry","mango"}
print(furits1)
furits1.clear()
print(furits1)

# 3) copy()
furits2={"apple","banana","cherry","mango","pineapple"}
x=furits2.copy()
print(x)

# 4) difference()
furits3={"apple","banana","cherry","mango","pineapple"}
furits4={"apple","banana","cherry","mango"}
x=furits3.difference(furits4)
print(x)

# 4) difference_update()
furits5={"apple","banana","cherry","mango"}
furits6={"apple","banana","cherry","mango","pineapple"}
y=furits6.difference_update(furits5)
print(y)

# 5)  discard()
furits7={"apple","banana","pinapple"}
furits7.discard('apple')
print(furits7)

# 6) intersection()
furits8={'mango', 'cherry','banana'}
furits9={"apple","banana","cherry","mango","pineapple"}
w=furits.intersection(furits9)
print(w)


# 7) intersection_update()
number1={121,545,161,16,1621,1}
number2={4548,8454,8451,4845,78,78,84,841}
number1.intersection_update(number2)
print("number",number1)

# 9) isdisjoint()
x={"google","apple","microsoft"}
y={"mango","cherry","apple"}
u=x.intersection(y)
print("isdisjoint",u)


# 10) issubset()
k={1,2,3,4,5,6,4,6}
l={1,2,3,5,6,9,6,656,32,31,3}
d=k.issubset(l)
print(d,"issubset")

# 11) issuperset()
o={1,2,3,4,6,4}
p={1,2,3,4,6,4}
q=o.issuperset(p)
print("issuperset",q)

# 12) pop()
set1={1,25,4,6,6,8,2,6}
set1.pop()

# 13) remove()
set2={1,2,3,4,5,6,4,6}
set2.remove(5)
print("remove",set2)



# 14) symmetric_difference() 
set3={1,2,3,4,5,4,5,6,7,9,7}
set4={1,2,4,5,6,9,7}
se=set3.symmetric_difference(set4)
print("symmetric_difference",se)


# 15) symmetic_difference_update() 
set5={1,2,3,4,5,4,5,6,7,9,7}
set6={1,2,4,5,6,9,7}
z=set5.symmetric_difference(set6)
print( "symmetic_difference_update",z)



# 16) union()
set11={1,2,3,4,5,4,5,6,7,9,7}
set12={1,2,4,5,6,9,7}
set11.union()
set12.union()
print("union",set11)
print("union",set12)

# 17) update()
b={"google","apple","microsoft"}
e={"mango","cherry","apple"}
b.update("tesla")
print(b)