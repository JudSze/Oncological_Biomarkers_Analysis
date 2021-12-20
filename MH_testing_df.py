import pandas as pd
import numpy as np

"""Group 8"""
df_8=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_8_FDR.csv", sep=";")
df_8.head()
df_8.loc[df_8.MWp_value<=0.082126, "FDR"]="1"
df_8.loc[df_8.MWp_value>0.082126, "FDR"]="0"

df_8.loc[df_8.auc_value>=0.7, "AUC_ROC"]="1"
df_8.loc[df_8.auc_value<0.7, "AUC_ROC"]="0"

df_8.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_8_FDR.csv", sep=";")

sub_8=df_8[(df_8['FDR']==1)&(df_8["AUC_ROC"]==1)]
sub_8.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_8.csv", sep=";")

"""Group 7"""
df_7=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_7_FDR.csv", sep=";")
df_7.head()
df_7.loc[df_7.MWp_value<=0.073789, "FDR"]="1"
df_7.loc[df_7.MWp_value>0.073789, "FDR"]="0"

df_7.loc[df_7.auc_value>=0.7, "AUC_ROC"]="1"
df_7.loc[df_7.auc_value<0.7, "AUC_ROC"]="0"

df_7.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_7_FDR.csv", sep=";")

sub_7=df_7[(df_7['FDR']==1)&(df_7["AUC_ROC"]==1)]
sub_7.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_7.csv", sep=";")

"""Group 6"""
df_6=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_6_FDR.csv", sep=";")
df_6.head()
df_6.loc[df_6.MWp_value<=0.067486, "FDR"]="1"
df_6.loc[df_6.MWp_value>0.067486, "FDR"]="0"

df_6.loc[df_6.auc_value>=0.7, "AUC_ROC"]="1"
df_6.loc[df_6.auc_value<0.7, "AUC_ROC"]="0"

df_6.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_6_FDR.csv", sep=";")

sub_6=df_6[(df_6['FDR']==1)&(df_6["AUC_ROC"]==1)]
sub_6.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_6.csv", sep=";")

"""Group 5"""
df_5=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_5_FDR.csv", sep=";")
df_5.head()
df_5.loc[df_5.MWp_value<=0.071768, "FDR"]="1"
df_5.loc[df_5.MWp_value>0.071768, "FDR"]="0"

df_5.loc[df_5.auc_value>=0.7, "AUC_ROC"]="1"
df_5.loc[df_5.auc_value<0.7, "AUC_ROC"]="0"

df_5.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_5_FDR.csv", sep=";")

sub_5=df_5[(df_5['FDR']==1)&(df_5["AUC_ROC"]==1)]
sub_5.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_5.csv", sep=";")

"""Group 4"""
df_4=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_4_FDR.csv", sep=";")
df_4.head()
df_4.loc[df_4.MWp_value<=0.06833, "FDR"]="1"
df_4.loc[df_4.MWp_value>0.06833, "FDR"]="0"

df_4.loc[df_4.auc_value>=0.7, "AUC_ROC"]="1"
df_4.loc[df_4.auc_value<0.7, "AUC_ROC"]="0"

df_4.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_4_FDR.csv", sep=";")

sub_4=df_4[(df_4['FDR']==1)&(df_4["AUC_ROC"]==1)]
sub_4.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_4.csv", sep=";")

"""Group 3"""
df_3=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_3_FDR.csv", sep=";")
df_3.head()
df_3.loc[df_3.MWp_value<=0.065705, "FDR"]="1"
df_3.loc[df_3.MWp_value>0.065705, "FDR"]="0"

df_3.loc[df_3.auc_value>=0.7, "AUC_ROC"]="1"
df_3.loc[df_3.auc_value<0.7, "AUC_ROC"]="0"

df_3.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_3_FDR.csv", sep=";")

sub_3=df_3[(df_3['FDR']==1)&(df_3["AUC_ROC"]==1)]
sub_3.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_3.csv", sep=";")

"""Group 2"""
df_2=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_2_FDR.csv", sep=";")
df_2.head()
df_2.loc[df_2.MWp_value<=0.070688, "FDR"]="1"
df_2.loc[df_2.MWp_value>0.070688, "FDR"]="0"

df_2.loc[df_2.auc_value>=0.7, "AUC_ROC"]="1"
df_2.loc[df_2.auc_value<0.7, "AUC_ROC"]="0"

df_2.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_2_FDR.csv", sep=";")

sub_2=df_2[(df_2['FDR']==1)&(df_2["AUC_ROC"]==1)]
sub_2.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_2.csv", sep=";")

"""Group 1"""
df_1=pd.read_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_1_FDR.csv", sep=";")
df_1.head()
df_1.loc[df_1.MWp_value<=0.069769, "FDR"]="1"
df_1.loc[df_1.MWp_value>0.069769, "FDR"]="0"

df_1.loc[df_1.auc_value>=0.7, "AUC_ROC"]="1"
df_1.loc[df_1.auc_value<0.7, "AUC_ROC"]="0"

df_1.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/hallmark_auc_eredmenyek/df_1_FDR.csv", sep=";")

sub_1=df_1[(df_1['FDR']==1)&(df_1["AUC_ROC"]==1)]
sub_1.head()
sub_1.to_csv("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/FDR_auc_1.csv", sep=";")