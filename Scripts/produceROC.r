# Calculate_AUC.r
# =============
# Author: Gaborit Victor
# Date: Jul 26, 2016
# =============

args = commandArgs(trailingOnly=TRUE); # Lecture des arguments depuis la ligne de commande

#Code
library('ROCR')
if (grepl('^-i=',args[1])) { #-r=<consistency_outputFile>
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
perf <- performance(pred, "tpr", "fpr")
outfile=args[2]
png(outfile)
plot(perf, colorize = TRUE, main = "courbe ROC")
dev.off()
perf2 <- performance(pred, "auc")
perf2@y.values[[1]]


# FIN DU PROGRAMME
