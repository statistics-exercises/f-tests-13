# Histogram

You can now generate samples of the statistic:

![](https://render.githubusercontent.com/render/math?math=F=\frac{SS_T/(t-1)}{SS_E/\left[\sum_{j=1}^t(n_j-1)\right]})

As was briefly alluded to in the instructions for the previous task, if the expectations for all t distributions that were sampled are identical F is a sample from an f-distribution with ![](https://render.githubusercontent.com/render/math?math=(t-1, N-t))-degrees of freedom where N is the sum of all the ![](https://render.githubusercontent.com/render/math?math=n_j) values above.

__To complete this task I want you to write code to generate a histogram for F and to "prove" for yourself that this statement about the distribution that F is sampled from is true.__

The outline code that I have written calls on you to copy the function  (`generate_f_variable`) that you wrote for the previous task. This function will be used to generate the random variable that we are interested in.  I have then created and stored the midpoints for a series of histogram bins that start at `xmin` and that finish at `xmax` in a NumPy array called `xvals`.  Your task is to write a loop that generates 200 random variables using the  `generate_f_variable` function.  These should be samples of F above with `T=5` and all the ![](https://render.githubusercontent.com/render/math?math=n_j)=10.  Within this loop, you should use the NumPy array called `counts` to count how many of these random variables fall within each of the `nbins` histogram bins.  

Once you have generated all your random variables you will need to normalise the histogram that is stored in `counts`.   When your code is complete it should generate a graph showing the histogram that you have generated in red.  The black line illustrates the true distribution that should be sampled by this variable for comparison.     
