a="sattu"
_b=3
c=4.5
d=True
e=None
f=5j
g=("apple","banana","cherry")
h=range(6)
i=frozenset({"apple","banana","mango"})
j=dict(name="rahul",age=24)
k=[5,3,55.3,10.4,"a","b","abcd",5j]

#print type of variables
print(type(a))
print(type(_b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))

#print variables
print(a)
print(_b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

#casting
a=str(34)
print(type(a))
print(a)

b=float(55)
print(type(b))
print(b)

#Many Values to Multiple Variables
a,b,c,d=10,20,30,"rahul",
print(a)
print(b)
print(c)
print(d)

#One Value to Multiple Variables
x=y=z=1000
print(x)
print(y)
print(z)

#Unpack a Collection
fruits=["orange","apple","mango"]
p,q,r=fruits
print(p)
print(q)
print(r)

#output in once
x="python"
y="is"
z="cool"
print(x,y,z)
print(x+y+z)

#global var
x="global var"
def myfun():
    print(x)

myfun()

#local var
def myfun2():
    y="local var"
    print(y)

myfun2()

#global keyword
def myfun3():
    global x
    x=300
    print(x)

myfun3()


