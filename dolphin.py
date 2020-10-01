#!/usr/bin/env python

if __name__ == '__main__':

    import sys
    from distutils.util import strtobool
    import numbers
    import pandas as pd
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt
    import os

    from Library import import_library
    from CreateDataFrame import To_DataFrame
    from plotdata import plot_data
    from keys import find_keys
    from createpdf import create_pdf

    #Set up parameters
    input_values = strtobool(sys.argv[1])

    if input_values:
        name = input("What is your name? ")
        gender = input("What is your gender? Enter Female or Male: ")
        while (gender != 'Female') & (gender != 'Male'):
            gender = input("Please enter Female or Male: ")
        orientation = input("Are you kicking on your front or back? Enter Front or Back: ")
        while (orientation != 'Front') & (orientation != 'Back'):
            orientation = input("Please enter Front or Back: ")
        speed = input("Are you kicking fast or slow? Enter Fast or Slow: ")
        while (speed != 'Fast') & (speed != 'Slow'):
            speed = input("Please enter Fast or Slow: ")
        # height = input("What is your height in meters? ")
        while True:
            try:
                height = float(input("Enter your height in meters: "))
                break
            except ValueError:
                print("Please enter only a number: ")
    else:
        name = 'Jenna'
        gender = 'Male'
        orientation = 'Front'
        speed = 'Fast'
        height = 1.74

    print("Processing...one moment please")

    # Step 1: Inport data to be analyzed and convert it to Data Frame

    destination, data = To_DataFrame(orientation)

    # Step 2: Analyze Stored Data. Analyze data frames from all videos corresponding to parameters of new data. Load in data and calculate mean and variance for key points.

    ogdata = import_library()
    filtered_data = ogdata[(ogdata['Gender'] == gender) & (ogdata['Side'] == orientation)]
    # Add this when we have enough data to include speed as a filter.
    # & (ogdata['Speed'] == speed

    filtered_data = filtered_data.reset_index()

    if len(filtered_data.index) == 0:
        print("No data for your inputs. Cannot calculate comparison values.")
    else:

        # Calculate Mean
        first = filtered_data.loc[0,'Data Frame']
        mean = first
        remaining = filtered_data.drop(0, axis=0).reset_index()
        for index in remaining.index:
            mean = mean + remaining.loc[index,'Data Frame']

        mean = mean/(len(filtered_data.index))

        # Calculate Variance 
        variance = (first - mean) **2

        for index in remaining.index:
            variance = variance + ((remaining.loc[index, 'Data Frame'] - mean)**2)

        variance = variance/(len(filtered_data.index)-1)
        std = np.sqrt(variance)

        # Step 3: Analyze New Data. Calculate four key points for new data. 

        key_1, key_2, key_3, key_4, time_1, time_2, time_3, time_4, time_total = find_keys(data)

        only_keys = data.iloc[[key_1, key_2, key_3, key_4]]
        only_keys['Time'] = [time_1, time_2, time_3, time_4]
        only_keys = only_keys.reset_index().drop(['index'], axis='columns')

        only_keys.loc[:,['Finger','Shoulder','Hip','Knee','Ankle','Toe']] = only_keys.loc[:,['Finger','Shoulder','Hip','Knee','Ankle','Toe']]/height

        # Step 4: Compare Stored Data with New Data. Compare all points and angles from Stored Data and New Data to look for significant difference. Output spreadsheet with significant differences highlighted.
        z_scores = (only_keys - mean)/std

        rows = z_scores.shape[0]
        columns = z_scores.shape[1]

        p_values = z_scores

        for column in np.arange(columns):
            for row in np.arange(rows):
                p_values.iloc[row,column] = stats.norm.cdf(z_scores.iloc[row,column])

        # Step 5: Plot Stored Data against new Data.

        fig1, fig2, fig3 = plot_data(data, only_keys, mean, p_values)

        fig1.savefig('fig1.png',bbox_inches='tight')
        fig2.savefig('fig2.png',bbox_inches='tight')
        fig3.savefig('fig3.png',bbox_inches='tight')

        curr_dir = os.getcwd()
        fig1_dest = os.path.join(curr_dir, 'fig1.png')
        fig2_dest = os.path.join(curr_dir, 'fig2.png')
        fig3_dest = os.path.join(curr_dir, 'fig3.png')

        # Step 6: Create PDF

        create_pdf(name, orientation, gender, speed, fig1_dest, fig2_dest, fig3_dest)


