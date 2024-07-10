import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))

print(np.__version__)

# 0D array
a=np.array(43)
print(a)


# 1D array
b=np.array([1,2,3,4,5])
print(b)

# 2D array
c=np.array([[10,20,30],[40,50,60]])
print(c)


d=np.array([[[11,22,33],[33,44,55]],[[66,77,88],[99,10,11]]])
print(d)

#printing dimensions

print(b.ndim)
print(c.ndim)
print(d.ndim)

#specify dimensions
e=np.array([111,222,333,444,555,666],ndmin=3)
print(e)

#accessing
print(b[2])
print(c[0,2])
print(d[1,0,1])

#arithmetic operations on arrays + - * / ** %
print(b[0]+b[3])
print(c[0,0]+c[0,1])
print(d[0,0,0]+d[1,1,0])

print("...........")
#step sclicing
arr1 = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr1[1:4:2])

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr2[-3:-1])

arr3= np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])
print(arr3[0:2, 1:4])


#numpy datatypes
a=np.array([1,2,3,4])
print(a.dtype)

b=np.array(['a','b','c','c'])
print(b.dtype)

#iterating 1D array 
x=np.array([1,2,3,4,5,6,7,8,9])
for i in x:
    print(i)
print(".................................")

#iterating 2D array
y=np.array([[1,2,3,4],[5,6,7,8]])
for i in y:
    print(i)

print(".................................")

#iterating 3D array
m=np.array([[[1,2,3],[5,6,7]],[[8,9,10],[11,12,13]]])
for g in m:
   print(g)

print(".................................")

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

#joining numpy arrays
name=np.array(["dholu","bholu","satvik"])
age=np.array([5,6,10])
joint_arr=np.concatenate((name,age))
print(joint_arr)
print(type(joint_arr))
print(type(name))

# split numpy arrays
a=np.array([1,2,3,4,5,6,7,8,9]) 
new_a=np.array_split(a,3)
print(new_a)

#searching_array
x=np.array([134,457,56324,745,78,5,2,778,54,35,2,62,6345756,78,6,562,5,8,968,3,65,])
s=np.where(x==6345756) #gives the index of this number
print(s)

# Find the indexes where the values are even: 
d=np.array([1,2,3,4,5,6,7,8,9,9,10])
j=np.where(d%2==0)
print(j)

# Find the indexes where the values are odd: 
d=np.array([1,2,3,4,5,6,7,8,9,9,10])
j=np.where(d%2==1)
print(j)

# Find the indexes where the value 7 should be inserted according to accending order
x=np.array([1,2,3,4])
y=np.searchsorted(x,5)
print(y)

# Find the indexes where the value 7 should be inserted from right according to accending order
x=np.array([1,2,3,4,5,6,7])
k=np.searchsorted(x,10,side='right')
print(k)

#multiple sorting
x=np.array([1,2,4,5,7,8,10,12])
u=np.searchsorted(x,[3,6,9,11])
print(u)

#numpy sorting array
arr=np.array([5,3,7,3,6,3,0,1,3,4,5,8,2])
print(np.sort(arr))

arr2= np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr2))

arr3=np.array([False,True,True,False,False,True])
print(np.sort(arr3))

# filtering numpy array
a=np.array([1,2,3,4,5])
b=np.array([True,False,False,True,True])
new_a=a[b]
print(new_a)
