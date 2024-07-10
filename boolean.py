print(10>5)

a=10
b=100
if a>b:
    print("a is greater")
elif a==b:
    print("a is equal to b")
else :
    print("b is greater")

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool(""))
print(bool(None))
print(bool("any string"))
print(bool(15))
print(bool(0))
print(bool([]))
bool(["apple","banana"])

# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# The following will return False: 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#functions can return a boolean
def myfun():
    return True
print(myfun())