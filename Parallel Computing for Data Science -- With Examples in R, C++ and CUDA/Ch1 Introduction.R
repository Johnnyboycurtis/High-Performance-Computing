## this file contains examples for Chapter 1 in R

## Example 1.4.1
mutoutser <- function(links){
	## links is a nxm matrix
	nr = nrow(links)
	nc = ncol(links)
	tot = 0
	for(i in 1:(nr-1)){
		for(j in (i+1):nr){
			for(k in 1:nc){
				tot = tot + links[i,k] * links[j,k]
			}
		}
	
	}
	tot / (nr*(nr-1) / 2)
}


sim <- function(nr, nc){
	link = matrix(sample(0.1, (nr*nc), replace=TRUE), nrow = nr, ncol = nc)
	return(system.time(mutoutser(link)))
}





mutoutser1 <- function(links){
	nr = nrow(links)
	nc = ncol(links)
	tot = 0
	
	for(i in 1:(nr-1)){
		tmp = links[(i+1):nr, ] %*% links[i,]
		tot = tot + sum(tmp)
		}
	return(tot/nr)

}




sim1 <- function(nr, nc){
	link = matrix(sample(0.1, (nr*nc), replace=TRUE), nrow = nr, ncol = nc)
	return(system.time(mutoutser1(link)))
}






## Parallel 
library(parallel)
doichunk <- function(ichunk){
	tot = 0
	nr = nrow(links)
	for(i in ichunk){
		tmp = links[(i+1):nr, ] %*% links[i,]
		tot = tot + sum(tmp)
	}
	return(tot)
}


mutoutpar <- function(cls, links){
	nr = nrow(links)
	clusterExport(cls, "links")
	# each "chunk" has only 1 value of i for now
	ichunks = 1:(nr-1)
	tots = clusterApply(cls, ichunks, doichunk)
	Reduce(sum, tots) / nr
}



snowSim <- function(nr, nc, cls){
	links <<- matrix(sample(0:1, (nr*nc), replace=TRUE), nrow=nr, ncol=nc)
	return(system.time(mutoutpar(cls, links)))
}


## set up a cluster of n-workers, workers on a multicore machine
initmc <- function(nworkers){
	makeCluster(nworkers)
}


## set up a cluster on machines specified,
## one worker per machine
initcls <- function(workers){
	makeCluster(spec=workers)
}



























