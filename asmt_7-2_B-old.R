#poisson spike distribution

r = 100 #success rate, firing rate
dt = 0.001 #1ms
rdt = r * dt
x = seq(60,140) # N trials displayed
y = runif(length(x)) # initialization of y

for (i in 1:length(x)){
  #y[i] = ((rdt**x[i]) * exp(-rdt) / factorial(x[i])) * 100
  y[i] = ((r**x[i]) * exp(-r) / factorial(x[i])) * 100
  #y[i] = dpois(x[i], r) * 100
}

plot(x,y, "h")

