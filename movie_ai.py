import numpy as np
import pandas as pd

movies_df=pd.read_csv("tmdb_5000_movies.csv")
credits_df=pd.read_csv("tmdb_5000_credits.csv")


#renaming
credits_renamed=credits_df.rename(index=str, columns={"movie_id":"id"})
movies_df_merge=movies_df.merge(credits_renamed,on="id")
print(movies_df_merge.head())
print("..............")
#droping unneeded columns from movies 
movies_cleaned_df=movies_df_merge.drop(columns=["homepage","title_x","title_y","status","production_countries"]) 
print(movies_df_merge.head())
print("..............")
print(movies_cleaned_df.info())

#we have to take movie name from user and 
#provide similar movies from the overview in data set

print(movies_cleaned_df.head(1)["overview"])

from sklearn.feature_extraction.text import TfidfVectorizer
tfv=TfidfVectorizer(min_df=3, max_features=None,
                    strip_accents="unicode",analyzer="word",token_pattern=r'\w{1,}',
                    ngram_range=(1,3),
                    stop_words='english')

#filling NaN values with string
movies_cleaned_df["overview"]=movies_cleaned_df['overview'].fillna('')

#fitting TF-IDF on overview text (basically making sparse matrix)

tfv_matrix=tfv.fit_transform(movies_cleaned_df["overview"])
print(tfv_matrix)
