"""Read in the normalized expression data, the jetset and the list of hallmarks, than checking the output of the read-in.
Subsetting the jetset dataset based on hallmark gene names, than subsetting the normalized expression data based on hgu219 probe ids
in the subsetted data. Saving the annotated hallmark genes expression data into a csv file
"""

import pandas as pd
import numpy as np

norm_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/norm_expression_data.csv", sep=';')
jetset_df=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/jetset_genes.csv", sep=";")
hm_df=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark.csv")
norm_df.head()
jetset_df.head()
hm_df.head()

subset=pd.merge(jetset_df, hm_df)
full_merged=pd.merge(subset, norm_df)

full_merged.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/proba_r.csv", sep=";")

