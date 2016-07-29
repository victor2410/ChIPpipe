# Calculate_AUC.r
# =============
# Author: Gaborit Victor
# Date: Jul 18, 2016
# =============



args = commandArgs(trailingOnly=TRUE); # Lecture des arguments depuis la ligne de commande

#Code
library('ROCR')
if (grepl('^-i=',args[1])) { #-i=<scorefile>
		arg.split <- strsplit(args[1],'=',fixed=TRUE)[[1]] # on récupère ce qui est après le symbole "="
		if (! is.na(arg.split[2]) ) {
			result.file <- arg.split[2] # La seconde partie est le fichier attendu
		} else {
			cat('erreur\n')
			stop('Pas de fichier donné pour l\'option -i=')
		}
	}
data=read.table(result.file, header = FALSE, sep = "\t", dec = ".")
fr=data.frame(data)
pred <- prediction(fr$V1, fr$V2)
perf <- performance(pred, "auc")
outfile=args[2]
AUC=perf@y.values[[1]]
sink(outfile)
cat("Valeur d'AUC : ", AUC)
sink()


# FIN DU PROGRAMME
