#single and multiline string
a="single line string"
b="""multi 
line
string"""
print(a)
print(b)

#access string
str="batman"
print(str[2])

print("...............................")
#looping string
str="spiderman"
for i in str:
    print(i)

x="superman"
print(len(x))

# check string 
txt="i love you my darling from the bottom of my heart"
print("love" in txt)
print("potato" in txt)

#checking using if 
txt2="i love python its the best"
if "best" in txt2:
    print("yes best is present in txt2")

#Check if NOT
txt3="i hate going to school"
print("love" not in txt3)

#checking not using if
txt4="hola bhar se bhola ander bkl"
if "asshole" not in txt4:
    print("yes it is not present")

