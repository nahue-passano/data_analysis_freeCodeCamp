# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 02:51:44 2021

@author: NPass
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('https://raw.githubusercontent.com/nahue-passano/data_analysis_freeCodeCamp/main/database/fcc-forum-pageviews.csv',
                 sep = ',', index_col = 'date', parse_dates = ['date'])

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) &
        (df['value'] >= df['value'].quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig , ax = plt.subplots(figsize = (21,7))
    ax.plot(df.index , df['value'] , color = 'red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig , ax = plt.subplots(figsize = (10,10)) 
    df_bar.plot(kind = 'bar',
                xlabel = 'Years',
                ylabel = 'Average Page Views',
                ax = ax)

    plt.legend(title = 'Months', labels = ['January', 'February', 'March',
                                           'April', 'May', 'June', 
                                           'July', 'August', 'September', 
                                           'October','November', 'December'] )

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig , (ax1, ax2) = plt.subplots(1,2,figsize = (20,10))
    ax1 = sns.boxplot(x = df_box['year'],
                      y = df_box['value'],
                      ax = ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    ax2 = sns.boxplot(x = df_box['month'],
                      y = df_box['value'],
                      ax = ax2,
                      order = ['Jan', 'Feb', 'Mar',
                               'Apr', 'May', 'Jun',
                               'Jul', 'Aug', 'Sep',
                               'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
