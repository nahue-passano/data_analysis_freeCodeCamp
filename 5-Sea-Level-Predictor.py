# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 05:27:04 2021

@author: NPass
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('https://raw.githubusercontent.com/nahue-passano/data_analysis_freeCodeCamp/main/database/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (12,8),dpi=500)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'] )

    # Create first line of best fit
    a_1 , b_1 , r_1 , p_1, std_1 = linregress( df['Year'] , df['CSIRO Adjusted Sea Level'])
    x_1 = np.arange(df['Year'].min(),2051)
    y_1 = a_1*x_1 + b_1
    plt.plot(x_1 , y_1, linewidth = 2 , color = 'orange', label = 'since {year}'.format(year = df['Year'].min()))

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    a_2 , b_2 , r_2 , p_2, std_2 = linregress( df_2000['Year'] , df_2000['CSIRO Adjusted Sea Level'])
    x_2 = np.arange(2000,2051)
    y_2 = a_2*x_2 + b_2
    plt.plot(x_2 , y_2, linewidth = 2 , color = 'red', label = 'since 2000')
    
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    plt.legend(title = 'Prediction', )
    plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
