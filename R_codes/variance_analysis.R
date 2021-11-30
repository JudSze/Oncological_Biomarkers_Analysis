#Hosszú génlista transzpoz
n <- beforecluster$Gene
expression <- as.data.frame(t(beforecluster[,-1]))
colnames(expression) <- n

sample <- rownames(expression)
rownames(expression) <- NULL
expression <- cbind(sample,expression)

#ezekre a csomagokra keress rá légyszi és előtte telepítsd
library(ROC)
library(ROCR)
library(hash)
MyAUC <- function(c, x){
  n <- length(c)
  n1 <- length(which(c == 1))
  n0 <- n - n1
  S1 <- cbind(x[which(c == 1)], 1)
  S0 <- cbind(x[which(c == 0)], 1)
  U <- 0
  for( i in 1 : n1){
    for(j in 1 : n0){
      if(S1[i, 1] > S0[j, 1]) {U <- U + 1}
      if(S1[i, 1] == S0[j, 1]) {U <- U + .5}
    }
  }
  auc <- U/(n1 * n0)
  vpj <- vector(length=n1)
  vqk <- vector(length=n0)
  U1 <- 0
  for(i in 1 : n1){
    for(j in 1 : n0){
      if(S1[i, 1] > S0[j, 1]) {U1 <- U1 + 1}
      else {if(S1[i, 1] == S0[j, 1]) {U1 <- U1 + 0.50 }}
    }
    division <- U1 / n0
    resta <- (division - auc)^2
    vpj[i] <- resta
    U1 <- 0
  }
  U2 <- 0
  resta <- 0
  for(j in 1 : n0){
    for(i in 1 : n1){
      if(S1[i, 1] > S0[j, 1]) {U2 <- U2 + 1}
      else {if(S1[i, 1] == S0[j, 1]) {U2 <- U2 + 0.50 }}
    }
    division <- U2 / n1
    resta <- (division - auc)^2
    vqk[j] <- resta
    U2 <- 0
  }
  vpj <- vpj/(n1 * (n1 - 1))
  vqk <- vqk/(n0 * (n0 - 1))
  var <- sum(vpj) + sum(vqk)
  s <- sqrt(var)
  p <- 1 - pnorm((auc - 0.5) / s)
  return(c(AUC = auc, lower.95 = qnorm(0.025, mean = auc, sd = s), upper.95 = qnorm(0.975, mean = auc, sd = s), p = p))
}
#Futtatásonként itt cserélgeted az első tagot
merged <- merge(response_6_months, R_54e_base_for_run, by="AffyID")
merged1 <- merged

state_vector <- merged1$response

gene_names = colnames(merged1)
index1 = 1:dim(merged1)[2]
index <- 3:dim(merged1)[2]
gene_list <- hash( keys= gene_names, values= index1)
for (j in index) {

  marker_vector <- merged1[[j]]
  roc<-rocdemo.sca(truth = state_vector,data = marker_vector,rule = dxrule.sca)
  auc_value<-AUC(roc)
 
  result <- MyAUC(state_vector, marker_vector);
  p_value = result[['p']]
 
 if (auc_value < 0.50){
    auc_value = 1 - auc_value
    p_value = 1 - p_value
    negator = c(rep(1, length(state_vector)))
    state_vector = negator - state_vector
    roc <- rocdemo.sca( truth=state_vector, data=marker_vector, rule=dxrule.sca)
    auc_value <- AUC(roc)
    result <- MyAUC(state_vector, marker_vector)
  }
    auc_value = format(auc_value, digits = 3)
    if (p_value < 0.05) {
      p_value = format(p_value, digits = 2, scientific = TRUE)
    }
    else{
      p_value = format(p_value, digits = 2, scientific = FALSE)
    }
   
    #fold change calculation
  mm_non_response<-subset(merged1,merged1$response==0)
  mm_response<-subset(merged1,merged1$response==1)
  mm_non_response_mean<-mean(mm_non_response[,j])
  mm_response_mean<-mean(mm_response[,j])
  if (mm_response_mean>mm_non_response_mean) {
  mm_foldchange<-mm_response_mean/mm_non_response_mean
  } else { mm_foldchange<-mm_non_response_mean/mm_response_mean }
  mm_foldchange = format(mm_foldchange, digits = 3)
  mm_foldchange_with<-mm_non_response_mean/mm_response_mean
 
  resMW<-wilcox.test(marker_vector ~ state_vector)
  restemp2<-unlist(resMW)
  MWp_value<-as.numeric(unlist(restemp2[[2]]))
  MWp_value<-format(MWp_value,digits = 5)
 
  #Az eredménybe beteszi a fájlnevet, a relatív és abszolút fold change-t, a Mann-Whitney teszt eredményét, az AUC-t és a p értékét
  res1 = c(as.name(gene_names[j]), mm_response_mean, mm_non_response_mean, mm_foldchange, mm_foldchange_with,MWp_value,auc_value, p_value)
 
 
  unlist(res1)
  res = t(res1);
  # Először elkészíti az eredményeket. Itt futtatásonként írd át, hogy melyik munkalapról származik.
  write.table(res, "ov6_2_new.txt", append = TRUE, row.names = TRUE, col.name=TRUE)
  }

#Készít egy táblát, amiből majd ki tudunk még szedni dolgokat, ha szükség lesz rá.
write.table(merged1, "ov6_2_new_TABLE.txt", append = TRUE, row.names = TRUE, col.name=TRUE)