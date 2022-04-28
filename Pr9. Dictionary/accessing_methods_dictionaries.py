

# 1)  clear() Removes all the elements from the dictionary
dic={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1996
}
print(dic)
dic.clear()

print(dic)


# 2)  copy()	Returns a copy of the dictionary
dic1={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(dic1)
d=dic1.copy()

print(d)


# 3)  fromkeys()	Returns a dictionary with the specified keys and value
x=('key1','key2','key3')
y=0

dics=dict.fromkeys(x,y)

print(dics)


# 4)  get()	Returns the value of the specified key
dic3={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(dic3)
d=dic3.get("Model")

print(d)


# 5)  items()	Returns a list containing a tuple for each key value pair
dic4={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(dic4)
d=dic4.items()

print(d)



# 6)  keys()	Returns a list containing the dictionary's keys
dic5={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(dic5)
t=dic5.keys()

print("keys()",t)


# 7)  pop()	Removes the element with the specified key
d={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(d)
d.pop("Model")

print("pop()",d)


# 8)  popitem()	Removes the last inserted key-value pair
a={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(a)
a.popitem()

print("popitem()",a)


#9)  setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
b={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(b)
b.setdefault("Model","Bronco")

print(b)


# 10)  update()	Updates the dictionary with the specified key-value pairs
i={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(i)
i.update({"Modem":"Bronco"})

print("update",i)


# 11) values()	Returns a list of all the values in the dictionary
s={
    "Brand":"Ford",
    "Model":"Mustang",
    "year":1945
}
print(s)
v=s.values()

print("values",s)
