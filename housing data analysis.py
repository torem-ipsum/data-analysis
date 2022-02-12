import sys
import os
import csv
import pandas as pd 
sys.path.insert(1, '/Users/trac.k.y/Downloads/housing.csv')
'''
with open('housing.csv', 'r') as file:
    read_file = csv.reader(file)
    for row in read_file:
        print(row)

'''
housing = pd.read_csv("housing.csv")
#df_test = pd.read_csv("titanic_dset/test.csv")
print(housing)
'''
print(housing.head())
print(housing.describe())
'''
housing_isnull = housing.isnull()
print(housing_isnull.mean())
# only 1% of entries don't have data for total_bedrooms, so i deleted them

housing2 = housing.query("total_bedrooms == total_bedrooms")
print(housing2)
housing2_isnull = housing2.isnull()
print(housing2_isnull.mean())
# no null values :D
