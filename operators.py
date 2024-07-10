#arithmetic
# + - * / % **
print(5+5)
print(5-5)
print(5*5)
print(10/5)
print(5%1) #modulus 
print(2**5) #exponent


#assignment
# = +=  -=  *=  /=  %=  **=
a=10
a+=10
a-=5
a*=5
a/=5
a%=5
a**=5

#comparison
# ==  !=  >  <  >=  <=
a=100
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical
#and or not
x=100
if x>3 and x>18: #both should be true
    print("x is big")

if x<10 or x==100:
    print("x is 100")

print(not(x>1000))

#identity
#Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#is   is not
x=["apple","mango"]
y=["apple","mango"]
z=x
print(z is x)
print(z is not x)

print(x is y)
print(x is not y)

print(x==y)

#membership
#test if a sequence is presented in an object:
#in   not in
x=["a","b","c","d","e"]
print("g" in x)
print("e" in x)
print("z" not in x)
print("z" in x)

#bitwise 
#i didnt understand