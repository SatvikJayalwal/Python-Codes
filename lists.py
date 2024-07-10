#Lists are used to store multiple items in a single variable and can contain different data types:
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0]

l=["a","b","c","d","e",1,2,4.5,"a"]
print(l)

#list length and type
print(len(l))
print(type(l))

#acess
print(l[4])
print(l[-2])
print(l[-1])
print(l[-6:-1])
print(l[2:])
print(l[2:5]) #Note: index 2 (included) and index 5 (not included)

#check
print("z" in l)

#replace item value
l2=["dholu","bholu","satvik",1,2,3]
l2[2]="kutta"
print(l2)

l2[-3:-1]=[10,20,30,40]
print(l2)

#insert()
l2.insert(2,"mishra")
print(l2)

#append()
l2.append("dce")
print(l2)

#extend()
#you can extend any of these(list , tuples, sets, dictionaries etc.)
list1=[1,2,3,4]
list2=[5,6,7,8,9]
list1.extend(list2)
print(list1)

myL=["chattarpur","delhi","gurgaon","kutb minar","haus khas"]
myL.remove("kutb minar")
print(myL)

l3=[1,2,3,4,5,6]
l3.pop(3)
print(l3)

#del : deletes with index
l4=[1,2,3,4,5,6]
del l4[4]

#del can also del the whole list
del l4

#clear()
l5=[1,2,3,4,5,6,7]
l5.clear()
print(l5)

#for loop in list
l6=[1,2,3,4,5]
for i in l6:
    print(i)

print("...............")
#while loop in list
l7=["a","b","c","d"]
i=0
while i < len(l7):
    print(l7[i])
    i+=1

