# stdev_effect_on_returns

I'm currently enrolled in an MBA program. During our Capital Markets class, we discussed the importance of taking an investment's risk (i.e. the standard deviation of its annual returns) into account when considering how to optimize a portfolio. 

This made me wonder: if our investment horizon is long enough, do we need to care about the risk of an investment? After all, we might expect the positive and negative effects of risk to cancel out.

However, I remembered from my Business Analytics class last semester that, when dealing with random events (such as the fluctuations in an investment's return), we need to be careful about making assumptions about the long-term effects of those events. Since I'm also enrolled in a Python course this semester, I decided to create a Python program that would simulate the return of a 50-year investment in a security at 50 different levels of risk (from a 0% standard deviation to a 50% standard deviation, in increments of 1%). The program performs 1,000 simulaton trials for each risk level; outputs several descriptive statistics on those returns into a DataFrame; and then converts those results into a CSV file.

I found the results of this program to be interesting, since they suggest that higher levels of risk may result in lower median returns. This makes sense: if an investment plunges 50% in a year, and there's no correlation between one year's returns and the next, it would be hard for the investment to regain that ground. However, I imagine that in the real world, major drops in an investment's value are often followed by major increases, which means that this program may greatly overstate the negative impacts of higher risk levels on investors' median returns. This is just one reason why I absolutely do not recommend that you use this program for investing advice or research. 

I had fun making this program, and may modify it to include a graphical plot of the results using matplotlib. 
