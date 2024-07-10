import numpy as np
import pandas as pd

#defining data frames

credits_df=pd.read_csv("credits.csv")
movies_df=pd.read_csv("movies.csv")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print(credits_df)
print(movies_df)


# #print only top 5
# # head()
# print(credits_df.head())
# print(movies_df.head())

# #print only last 5
# # tail()
# print(credits_df.tail())
# print(movies_df.tail())

# #merge the credit dataframe into movies dataframe
# movies_df=movies_df.merge(credits_df,on = 'title')

# print("..............................................................")
# #dimensionality of data frame
# movies_df.shape
# credits_df.shape

# #info of data in dataframe like data type and memory usage
# movies_df.info()
# credits_df.info()

# #select some main columns in which we are working on
# movies_df=movies_df[["movie_id","title","overview","genres","keywords","cast","crew"]]
# print(movies_df.head())

# movies_df.info()

# print(movies_df.isnull().sum())
# print(movies_df.dropna(inplace=True)) 

# print(movies_df.duplicated().sum())

# #retriving any perticular rows or columns by using index value from value 
# #by iloc function
# print(movies_df.iloc[0].genres)

# #tree representation
# import ast
# def convert(obj):
#     L=[]
#     for i in ast.literal_eval(obj):
#         L.append(i['name'])
#     return L

# movies_df['genres'] = movies_df['genres'].apply(convert)
# movies_df['keywords']=movies_df['keywords'].apply(convert)
# print(movies_df.head())