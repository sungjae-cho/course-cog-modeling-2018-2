# poisson spike distribution

r = 100 # success rate, firing rate
dt = 0.001 #1ms
rdt = r * dt
n_cells = 1 / dt

n_experiements = 5000
y_sum = seq(1,n_experiements)

for (j in 1:n_experiements) {
  x = seq(1,n_cells) # N trials displayed
  y = runif(length(x)) # random initialization of y
  
  for (i in x){
    if (rdt > y[i]) {
      y[i]=1.0
    } else {
      y[i]=0.0
    }
  }
  y_sum[j] = sum(y)
}

breaks = max(y_sum) - min(y_sum) + 1
hist(y_sum, breaks=breaks, freq=FALSE,
     main = 'Distribution of Spikes in a Second',
     xlab = 'Spikes in a second',
     ylab = 'Probability')

