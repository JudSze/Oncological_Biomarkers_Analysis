if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("BiocManager")
BiocManager::install("multiClust")

install.packages("factoextra")
install.packages("NbClust")
install.packages("cluster")

library(factoextra)
library(NbClust)
library(multiClust)
library(cluster)

#C:\Program Files\R\R-4.1.2

setwd("C:/Egyetem/Szakmai_gyak/Data_tables")
path<-file.path("C:/Egyetem/Szakmai_gyak/Data_tables/clust_r.txt")

ann_data<-input_file("clust_r.txt") #input only with probe set ID and expression data
ranked.exprs <- probe_ranking(input=path,  #dir path
                              probe_number=300, 
                              probe_num_selection="Fixed_Probe_Num",
                              data.exp=ann_data,  #expression matrix input
                              method="SD_Rank")

ranked.exprs[1:4, 1:4]

#integer output indicates the optimal number of clusters, takes tremendeous amount of time to run 
cluster_num<-number_clusters(data.exp = ann_data, Fixed = NULL, gap_statistic = TRUE) #output is 8

#finally the real deal
hclust_analysis <- cluster_analysis(sel.exp=ranked.exprs,  #output of probe_ranking
                                    cluster_type="HClust", #type of clustering method
                                    distance="euclidean",  #distance metrics: euclidean-default, maximum, manhattan, canberra, binary, minkowski
                                    linkage_type="ward.D2",#ward.D2-default, average, complete, median, centroid, single, mcquitty
                                    gene_distance="correlation", #distance measure, can be set to NULL by Kmeans, correlation, abspearson, spearman, kendall, maximum, manhattan, eucledian
                                    num_clusters=8,              #number of clusters defined by number_clusters() function
                                    data_name="Hallmarks",  #title of dataset
                                    probe_rank="SD_Rank",        #feautre selection method CV_Rank, CV_Guided SD_Rank, Poly
                                    probe_num_selection="Fixed_Probe_Num",   #way in which probes were selected, Fixed/Percent/Poly/Adaptive_Probe_Num
                                    cluster_num_selection="Predefined_Clust_Num") #Fixed_Clust_Num, gap_Statistic

head(hclust_analysis)
#C:\Users\Judit\Downloads\TreeView-1.2.0-win (2)\TreeView-1.2.0-win

#Elbow method
fviz_nbclust(ann_data, kmeans, method = "wss", k.max=24) +
    geom_vline(xintercept=1, linetype = 2)+
  labs(subtitle = "Elbow method") #suggested 2

#Silhouette method
fviz_nbclust(ann_data, kmeans, method="silhouette")+
labs(subtitle="Silhouette method") #suggested 2

#Gap method
ann_data
gap_stat <- clusGap(ann_data, FUN = kmeans, nstart = 30, K.max = 24, B = 50)
fviz_gap_stat(gap_stat) + theme_minimal() + ggtitle("fviz_gap_stat: Gap Statistic")