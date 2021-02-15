# Program that simulates effect of different standard deviations of return on a portfolio
# Kenneth Burchfiel, MIT license
# First edition uploaded on 2/15/2021
# Note: This program is absolutely NOT recommended for investing advice or research!


import numpy as np
import pandas as pd

initial_value = 1000 # The amount we initially invest
mu = 0.07 # The annual return (0.07 = 7%) 
years = 50 # The years for which we will be investing this money 
simulation_trials = 1000 # The number of times the program will calculate our return for each standard deviation 

results_table = {}
for i in range(0,51,1):
    sigma = i/100 # The annual standard deviation of our portfolio return. i/100 converts i to 0.01, 0.02, etc. (reflecting standard deviations of 1%, 2%, etc.)
    final_value_list = [] # We will store our results from each simulation trial for each standard deviation in this list.
    print(f"Now calculating returns when sigma = {sigma}") # Since the program can take a little while to run, it helps to have a print statement run for each instance of sigma so that you can track its progress
    for i in range (simulation_trials): # i.e. for each of our simulation trials
        final_value = initial_value
        for i in range(years): # i.e. for each year that we're investing our money
            final_value *= max(0,(1+np.random.normal(mu,sigma,1))) # This line updates the value of our investment on an annual basis. The annual change in the investment is random, but based on a normal curve with a mean equal to our average annual return and the standard deviation we are evaluating in the current for loop. For instance, if we start with 1000 and np.random.normal returns 0.5, our investment will be worth 1,050 at the end of the year.
            # The max (0, normal distribution) statement is used so that the amount returned cannot be negative. Since you won't lose more than you invest in a stock (provided you're not shorting it), it wouldn't make sense for (1+np.random.normal(mu,sigma,1)) to return a negative amount, but our program doesn't know that, hence the addition of the max() statement.
        final_value_list.append(final_value)
        # print(final_value) # Debugging
        # print(final_value_list) # Debugging
    final_value_row = {} # For each standard deviation, we will create a dictionary (final_value_row) that will store summary statistics about the list of results that we calculated over all our simulation trials. 
    final_value_row['1st percentile'] = np.percentile(final_value_list,1)
    final_value_row['5th percentile'] = np.percentile(final_value_list,5)
    final_value_row['median'] = np.median(final_value_list)
    final_value_row['95th percentile'] = np.percentile(final_value_list,95)
    final_value_row['99th percentile'] = np.percentile(final_value_list,99)
    final_value_row['average'] = np.average(final_value_list)
    results_table[sigma] = final_value_row # This dictionary stores each of our final_value_row dictionaries with the sigma being examined in the for loop as the key.
    # print(f"Given an annual return of {mu}, a standard deviation of {sigma}, a starting investment amount of {initial_value} and an investment horizon of {years} years, The median ending investment amount after {simulation_trials} simulations is {median} and the average is {average}.") # Can be used for debugging
    
# print(results_table) # for debugging
df_results = pd.DataFrame.from_dict(results_table).transpose() # Turns our results_table dictionary into a DataFrame
df_results.rename_axis('sigma',inplace=True)
print(df_results)
df_results.to_csv('effect_of_stdev_on_returns.csv')












