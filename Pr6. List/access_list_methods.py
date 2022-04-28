
from itertools import count

#   Creating list

list_number=[1,2,3,4,5,6,7,8,9,0]

list_animals=['cat','dog','rabbit']



list_currencies=['Dollar','Euro','Pound']
print(list_currencies)



    # Methods

# 1) append()

list_currencies.append('rupees')
print(list_currencies)


# 2) extend()

list_number2=[11,12,13]

list_number.extend(list_number2)
print (list_number)

# 3) insert()

list_animals.insert(3,'Tiger')
print(list_animals)

list_animals.insert(4,'lion')
print(list_animals)

# 4) remove()

list_prime_number=[2,3,5,7,9,11]
print(list_prime_number)

list_prime_number.remove(9)
print(list_prime_number)

# 5) pop()

list_prim1=[2,3,5,7]
print(list_prim1)
removed_element=list_prim1.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', list_prim1)

# 6) clear()

list2=[1,2,3,5,4,6,8,5,4,2]
print(list2)
list2.clear()
print(list2)

# 7) index()

animal=['cat','dog','rabbit']
print(animal)
index = animal.index('rabbit')
print(index)

# 8) count()

list_of_number=[2,2,3,4,5,6,6,6,6,6,7]
count=list_of_number.count(6)
print('Count of 2:',count)

# 9) sort()

sort_list=[1,5,8,7,2,6,4,2,1,35,424,36]
sort_list.sort()
print(sort_list)

# 10) reverse()

re_list=[1,596,52,36,42,985,6356,56,]
re_list.reverse()
print(re_list)

# 11) copy()

for_copy_list=[64,565,646,46,56,565,62656,64]
number_list=for_copy_list.copy()
print(number_list)


