import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def gen_f_variable( T, N ) : 
  # Your code to generate the variable that we introduced in the previous task goes here
  return

# This generates the midpoints of all your histogram bins
nbins, xmin, xmax = 10, 0, 6 
delx = (xmax - xmin ) / nbins
xvals, counts = np.zeros(nbins), np.zeros(nbins)
for i in range(nbins) : xvals[i] = xmin + i*delx

# Add code to generate the histogram here 




# You should not need to modify anything from here onwards
# This plots the histogram you have generated
plt.plot( xvals, counts, 'r-')
# This plots the f-distribution
xv = np.linspace( xmin, xmax, 200 )
yv = scipy.stats.f.pdf( xv, 4, 45 )
plt.plot( xv, yv, 'k-')
plt.savefig("histogram_t.png")
