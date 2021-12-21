if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("BiocFileCache")
library(BiocFileCache)
bfc = BiocFileCache(".")

base="http://www.cancerrxgene.org/gdsc1000//Data/preprocessed/Cell_line_RMA_proc_basalExp.txt.zip"
paths = bfcrpath(bfc, paste0(base, c("suppData/TableS4A.xlsx",
            "preprocessed/Cell_line_RMA_proc_basalExp.txt.zip")))

drug_table = readxl::read_excel(paths[1], skip=5)
gene_table = readr::read_tsv(paths[2])
