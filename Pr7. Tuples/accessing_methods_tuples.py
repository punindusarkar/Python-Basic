
# Accessing Methods 

#  1) count()

tuple1=(1,2,2,2,2,2,3,3,23,3,3,3,3,4,6,4,6,75,16,82,8,2,852,85,965,962,58)
x=tuple1.count(2)

print(x)



#  2) index()

tuple2=(12,1,25,2,41,63,22,12,6,2,1,265222,52,122,2,12,221212,1,21,21,2,12,12,12,1)
y=tuple2.index(21)
print(y)

#  3) deleting_tuple()

tuple3=(451,56,565,65,62656,56,526,5)
print(tuple3)
del tuple3
print(tuple3)

#  4) Updating Tuple

up_tuple=(20,62,56,56,562656,265)
list1=list(up_tuple)
list1[2]=20
b=tuple(up_tuple)
print(b)
