#poisson spike generator

r = 100 #success rate, firing rate
dt = 0.001 #1ms
rdt = 100 * 0.001
x = seq(1,100) # N trials displayed
y = runif(100) # random initialization of y

for (i in x){
  if (rdt > y[i])
    y[i]=1.0
  else
    y[i]=0.0
}

plot(x,y, "h")

