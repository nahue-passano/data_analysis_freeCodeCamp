# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 02:52:47 2021

@author: NPass
"""

import pandas as pd


# Read data from file
df = pd.read_csv('https://raw.githubusercontent.com/nahue-passano/data_analysis_freeCodeCamp/main/database/adult.data.csv')

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = race_count = df['race'].value_counts()

# What is the average age of men?
average_age_men = round(df.loc[ df['sex'] == 'Male' ]['age'].mean() ,1)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(df['education'].value_counts().loc['Bachelors'] / df.shape[0] * 100 ,1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
adv_ed_df = df[(df['education'] ==  'Masters') | (df['education'] ==  'Bachelors') | (df['education'] ==  'Doctorate')]
low_ed_df = df[~((df['education'] ==  'Masters') | (df['education'] ==  'Bachelors') | (df['education'] ==  'Doctorate'))]

# percentage with salary >50K
higher_education_rich = round(adv_ed_df[adv_ed_df['salary']=='>50K'].count()[0] / adv_ed_df.count()[0] * 100 ,1)
lower_education_rich = round(low_ed_df[low_ed_df['salary']=='>50K'].count()[0] / low_ed_df.count()[0] * 100 ,1)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()
# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = round(df[df['hours-per-week'] == min_work_hours] , 1)

rich_percentage = round(num_min_workers[num_min_workers['salary'] == '>50K'].count()[0] / num_min_workers.count()[0] * 100 ,1)

# What country has the highest percentage of people that earn >50K?
rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
count_per_country = df['native-country'].value_counts()
perc_per_country = rich_per_country / count_per_country * 100

highest_earning_country = perc_per_country.idxmax()
highest_earning_country_percentage = round(perc_per_country.max() ,1)

# Identify the most popular occupation for those who earn >50K in India.
rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()
