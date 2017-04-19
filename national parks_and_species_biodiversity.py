# This exercise uses the Biodiversity in National Parks dataset from Kaggle.
# Look at number of different organism categories in each parks.
# The goal is to practice using data frames and plotting in Python.


import pandas as pd
import matplotlib.pyplot as plt
#help('modules')

# To make the plots easier to read.
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 9)

# Import the data from the csv files.
# Note that in species.csv, some columns after 13 have mixed data types.
species = pd.read_csv('species.csv', usecols=range(1,13))
parks = pd.read_csv('parks.csv')

#print species.values
#print parks.values

# Form a group with 'Park Name' and 'Category'.
typecount = species[['Park Name', 'Category']].groupby(['Park Name', 'Category']).size()

# Convert statustype to a data frame and reset the indices.
type_df = typecount.to_frame().reset_index()
type_df.columns = ['Park Name', 'Category', 'Count']

# Have an array of the various categories of organism type.
columnplot_type = ['Algae', 'Amphibian', 'Bird', 'Crab/Lobster/Shrimp', 'Fish', 'Fungi', 'Insect', 'Invertebrate', 'Mammal', 'Nonvascular Plant', 'Reptile', 'Slug/Snail', 'Spider/Scorpion', 'Vascular Plant']

# Have a different graph for each category that ranks the parks by greatest absolute number first.
for i in columnplot_type:
    subgroup_type = type_df[type_df['Category'] == i]
    subgroup_type.sort_values(by='Count', ascending=False).plot(x='Park Name', y='Count', kind='bar', legend='None')
    plt.title('Type category: %s' % (i))
    plt.ylabel('Number of species')
    plt.tight_layout()
    
plt.show()
#print type_df