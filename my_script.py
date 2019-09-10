import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#============Data Manipulation===========#
#load data into DataFrame using pandas read_csv function
members = pd.read_csv('home_ownership_data.csv')
loans = pd.read_csv('loan_data.csv')

#splice relevant data
loans = loans[['member_id','loan_amnt']]

#merge the DataFrames using one to one merging
merged_data = pd.merge(members, loans, on='member_id')

#splice out member_id as no longer needed
merged_data = merged_data[['home_ownership','loan_amnt']]

#find the mean loan_amnt grouping by home_ownership status
results = merged_data.groupby(['home_ownership']).mean()

#===========Plotting results============#
#split up into two subplots
fig, (tble,graph) = plt.subplots(1,2)

#turn off graph axis for the table and show table with data rounded to two decimals
tble.axis("off")
table = pd.plotting.table(tble,np.round(results, 2),loc='center')
table.auto_set_column_width([-1,0])

#plot the results in a bar graph
results.plot(ax=graph,y='loan_amnt',kind='bar')
graph.title.set_text('Average loan amounts per home ownership')
graph.set_ylabel('Average loan amount ($)')

plt.tight_layout()
plt.show()
