"""Read in the normalized expression data, the jetset and the list of hallmarks, than checking the output of the read-in.
Subsetting the jetset dataset based on hallmark gene names, than subsetting the normalized expression data based on hgu219 probe ids
in the subsetted data. Saving the annotated hallmark genes expression data into a csv file

Do not use dataframe with asigned subtissues due redundancies
"""

import pandas as pd
import numpy as np

norm_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/norm_exp_df.csv", sep=';')
jetset_df=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/jetset_genes.csv", sep=";")
hm_df=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark.csv")
norm_df.head()
jetset_df.head()
hm_df.head()

subset=pd.merge(jetset_df, hm_df)
full_merged=pd.merge(subset, norm_df)

full_merged.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/subseted_r.csv", sep=";")

"""Assigning the cell lines and tissues to the clustered hallmark probe sets"""
hm_clust_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/hm_clust.csv", sep=';')
hm_clust_df.head()

cell_lines_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/cell_lines.csv", sep=';')
cell_lines_df.head()

subset_hm_clust=pd.merge(cell_lines_df, hm_clust_df)
subset_hm_clust

subset_hm_clust.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=";")

"""Assigning subtissues"""
sub_tss_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/sub_tissues.csv", sep=';')
sub_tss_df.head()
sub_tss_df

clustered_df=pd.read_table("C:/Egyetem/Szakmai_gyak/Data_tables/clustered_r.csv", sep=';')
clustered_df.head()
clustered_df

subset_sub_tss=pd.merge(sub_tss_df, clustered_df)
subset_sub_tss

subset_sub_tss.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/final_clust_data.csv", sep=";")

subset_sub_tss.drop_duplicates(subset=None, inplace=True)
subset_sub_tss

"""Transpose matrix for variance analysis"""
norm_df=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/norm_exp_df.csv", sep=";")
trans_df=norm_df.transpose()
trans_df.head(5)
trans_df.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/trans_df.csv", sep=";")