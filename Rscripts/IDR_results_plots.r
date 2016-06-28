# IDR_results_plots.r
# =============
# Author: Gaborit Victor
# Date: Mar 30, 2016
# Update : Apr 1, 2016
# =============



args = commandArgs(trailingOnly=TRUE); # Lecture des arguments depuis la ligne de commande


#FONCTION D'USAGE
print.usage <- function() {
	cat('Erreur, un ou plusieurs arguments sont manquants\n',file=stderr())
	cat('Usage: Rscript IDR_results_plots.r <options>\n',file=stderr())
	cat('ARGUMENTS OBLIGATOIRES:\n',file=stderr())
	cat('-r=<consistency_outputFile>, Chemin et nom complet du fichier de sortie du script "batch-consistency-analysis.r" (Extention de fichier : -overlapped-peaks.txt) \n',file=stderr())
	cat('-o=<scatter_prefix>, Chemin et préfixe du nom à donner aux graphes à réaliser \n',file=stderr())
}

#FONCTION SCATTER log(signal)
scatter.log <- function(table,name_out) {
	png(name_out)
	plot(log(table[,4]),log(table[,8]),col=table[,11], pch=".", xlab="log(signal) Rep1", ylab="log(signal) Rep2")
	legend("topleft", c("IDR=>0.01","IDR<=0.01"), col=c("red","black"), pch=19, bty="n", lty=c(1,1), lwd=c(2,2))
	dev.off();
}
#FONCTION SCATTER rank(signal)
scatter.rank <- function(table,name_out) {
	png(name_out)
	plot(rank(-table[,4]),rank(-table[,8]),col=table[,11], pch=".", xlab="Peak rank Rep1", ylab="Peak rank Rep2")
	legend("topleft", c("IDR=>0.01","IDR<=0.01"), col=c("red","black"), pch=19, bty="n", lty=c(1,1), lwd=c(1,1))
	dev.off();
}
#FONCTION SCATTER rank(signal)
if (length(args)<=1) {
	print.usage()
} else {
	if (grepl('^-r=',args[1])) { #-r=<consistency_outputFile>
		arg.split <- strsplit(args[1],'=',fixed=TRUE)[[1]] # on récupère ce qui est après le symbole "="
		if (! is.na(arg.split[2]) ) {
			result.file <- arg.split[2] # La seconde partie est le fichier attendu
		} else {
			cat('erreur\n')
			stop('Pas de fichier donné pour l\'option -r=')
		}
	}
	if (grepl('^-o=',args[2])) { #-o=<scatter_prefix>
		arg.split <- strsplit(args[2],'=',fixed=TRUE)[[1]] # on récupère ce qui est après le symbole "="
		if (! is.na(arg.split[2]) ) {
			out.file <- arg.split[2] # La seconde partie est le fichier attendu
		} else {
			cat('erreur\n')
			stop('Pas de préfix donné pour le nom de l\'output -o=')
		}
	}
	data = read.table(result.file, header = TRUE, sep = " ", dec = ".") # Lecture du fichier et création d'une table pour récupérer les données du fichier
	#Création d'une nouvelle colonne	
	data$col[data[,10]<=0.01]="black" # si la valeur d'IDR (colonne 10) est inférieure à 1%, on donne la balise "black" 
	data$col[data[,10]>=0.01]="red" # si la valeur d'IDR (colonne 10) est supérieure à 1%, on donne la balise "red"
	output_log=paste(out.file, "logsignal.png", sep = "_") # Ajout de l'extension au prefixe d'output donné
	output_rank=paste(out.file, "ranksignal.png", sep = "_") # Ajout de l'extension au prefixe d'output donné
	# Appel aux fonctions pour réaliser les plots
	scatter.log(data,output_log)
	scatter.rank(data,output_rank)
}

# FIN DU PROGRAMME
