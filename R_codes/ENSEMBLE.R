if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("clusterProfiler")

library(clusterProfiler)
#ez tartalmazza mondjuk az x darab szignifikás gén ENSEMBLE ID-t
ranked <- read.table("C:/Egyetem/Szakmai_gyak/Data_tables/ontology/df_8_ann_ensembl.csv")
# karakter vektorrá alakítás
de<-as.list.Vector(ranked)
ed<-unlist(de)
edd<-as.character(ed)

ego_CC <- enrichGO(gene         = edd,
                 OrgDb         = org.Hs.eg.db,
                 keyType       = 'ENSEMBL',
                 ont           = "CC",
                 pAdjustMethod = "BH",
                 pvalueCutoff  = 0.01,
                 qvalueCutoff  = 0.05)
head(ego_CC, 10)
CC<-head(ego_CC, 10)
write.table(CC, "df8_CC.txt", append = TRUE, row.names = TRUE, col.name=TRUE)
getwd()

ego_MF <- enrichGO(gene         = edd,
                 OrgDb         = org.Hs.eg.db,
                 keyType       = 'ENSEMBL',
                 ont           = "MF",
                 pAdjustMethod = "BH",
                 pvalueCutoff  = 0.01,
                 qvalueCutoff  = 0.05)
MF<-head(ego_MF, 10)
write.table(MF, "df8_MF.txt", append = TRUE, row.names = TRUE, col.name=TRUE)

ego_BP <- enrichGO(gene         = edd,
                   OrgDb         = org.Hs.eg.db,
                   keyType       = 'ENSEMBL',
                   ont           = "BP",
                   pAdjustMethod = "BH",
                   pvalueCutoff  = 0.01,
                   qvalueCutoff  = 0.05)
BP<-head(ego_BP, 10)
write.table(BP, "df8_BP.txt", append = TRUE, row.names = TRUE, col.name=TRUE)

#bárplottok készítése
barplot(ego_MF, drop = TRUE, showCategory = 10)
barplot(ego_CC, drop = TRUE, showCategory = 10)
barplot(ego_BP, drop = TRUE, showCategory = 10)

