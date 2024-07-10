import pandas as pd

print(pd.__version__)

#dataframe
my_data={'cars':['bmw','mercedes','toyota'],'passings':[3,7,2]}
myvar=pd.DataFrame(my_data)
print(myvar)
print(myvar)

a=[1,12,15,17,20]
aVar=pd.Series(a)
print(aVar)
print(".......")

#labels
print(aVar[3])

#With the index argument, you can name your own labels
labelvar = pd.Series(a, index = ["u","v","x", "y", "z"])  #here x,y,z,u,v are labels
print(labelvar)

#When you have created labels, you can access an item by referring to the label
print(labelvar["v"])

# Key/Value Objects as Series 
calories={"day1":123,"day2":342,"day3":429} #Note: The keys of the dictionary become the labels.
cal_df=pd.Series(calories)
print(cal_df)
#Named Indexes
cal_df=pd.DataFrame(calories,index=["day1","day2","day3"])
print(cal_df["day2"])
#locate
print(cal_df.loc["day2"])
print("......................")

mydata={"bholu":[10,20,30],"dholu":[40,50,60]}
df=pd.DataFrame(mydata)
print(df)
print(type(df))

#Locate Row 
# loc
print(df.loc[1])
print(df.loc[[0,1]])
print("...................")

# Load Files Into a DataFrame
#read_csv
#read_json
bigdata=pd.read_csv("movies.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None) 
print(bigdata)

#head - default 5 lines
print(bigdata.head(10))
#tail - default 5 lines
print(bigdata.tail(10))

print(".....................")
#info
print(bigdata.info())