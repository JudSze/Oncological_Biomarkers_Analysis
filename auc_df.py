import pandas as pd

"""Changing status values"""
#Looking at cluster group 6
df_6=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_6.head(5)
df_6.loc[df_6.ClustGroup == 6, "Status"]="1"
df_6.loc[df_6.ClustGroup != 6 , "Status"]= "0"

df_6.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_6.csv", sep=";")

#Looking at cluster group 5
df_5=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_5.head(5)
df_5.loc[df_6.ClustGroup == 5, "Status"]="1"
df_5.loc[df_6.ClustGroup != 5 , "Status"]= "0"

df_5.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_5.csv", sep=";")

#Looking at cluster group 4
df_4=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_4.head(5)
df_4.loc[df_4.ClustGroup == 4, "Status"]="1"
df_4.loc[df_4.ClustGroup != 4 , "Status"]= "0"

df_4.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_4.csv", sep=";")

#Looking at cluster group 3
df_3=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_3.head(5)
df_3.loc[df_3.ClustGroup == 3, "Status"]="1"
df_3.loc[df_3.ClustGroup != 3 , "Status"]= "0"

df_3.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_3.csv", sep=";")

#Looking at cluster group 2
df_2=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_2.head(5)
df_2.loc[df_2.ClustGroup == 2, "Status"]="1"
df_2.loc[df_2.ClustGroup != 2 , "Status"]= "0"

df_2.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_2.csv", sep=";")

#Looking at cluster group 1
df_1=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")
df_1.head(5)
df_1.loc[df_1.ClustGroup == 1, "Status"]="1"
df_1.loc[df_1.ClustGroup != 1 , "Status"]= "0"

df_1.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/df_1.csv", sep=";")