#!/usr/bin/env python

if __name__ == '__main__':

    import sys
    from distutils.util import strtobool
    import numbers
    import pandas as pd
    import numpy as np
    from scipy import stats

    from CreateDataFrame import To_DataFrame

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

    destination, swimmer, data = To_DataFrame(orientation)

    # Step 2: Analyze Stored Data. Analyze data frames from all videos corresponding to parameters of new data. Load in data and calculate mean and variance for key points.

    from Library import import_library
    ogdata = import_library()
    filtered_data = ogdata[(ogdata['Gender'] == gender) & (ogdata['Side'] == orientation)]
    # Add this when we have enough data to include speed as a filter.
    # & (ogdata['Speed'] == speed

    filtered_data = filtered_data.reset_index()

    if len(filtered_data.index) == 0:
        print("No data for your inputs. Cannot calculate comparison values.")
    else:

        # Calculate Mean
        # first = filtered_data.iloc[0]['Data Frame']
        first = filtered_data.loc[0,'Data Frame']
        mean = first
        remaining = filtered_data.drop(0, axis=0).reset_index()
        for index in remaining.index:
            # mean = mean + remaining.iloc[index]['Data Frame']
            mean = mean + remaining.loc[index,'Data Frame']

        mean = mean/(len(filtered_data.index))

        # Calculate Variance 
        variance = (first - mean) **2

        for index in remaining.index:
            # variance = variance + ((remaining.iloc[index]['Data Frame'] - mean)**2)
            variance = variance + ((remaining.loc[index, 'Data Frame'] - mean)**2)

        variance = variance/(len(filtered_data.index)-1)
        std = np.sqrt(variance)

        # Step 3: Analyze New Data. Calculate four key points for new data. 

        from keys import find_keys

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

        import matplotlib.pyplot as plt

        fig1, ax1 = plt.subplots(nrows = 1, ncols=1, figsize=(8,4)) 

        ax1.set_title("Raw Data")

        # Plot Standard Imported Data
        data_toplot = data
        data_toplot.index = data_toplot['t']
        data_toplot.iloc[:,1:].plot(ax=ax1)

        #Plot All Key Points

        #Find min and max for y-axis
        data_max = only_keys.iloc[:,1:7].to_numpy().max()
        data_min = only_keys.iloc[:,1:7].to_numpy().min()

        mean_max = mean.iloc[:,1:7].to_numpy().max()
        mean_min = mean.iloc[:,1:7].to_numpy().min()

        if data_max > mean_max:
            total_max = data_max
        else:
            total_max = mean_max

        if data_min < mean_min:
            total_min = data_min
        else:
            total_min = mean_min

        #Create Plot

        fig2, ((ax2, ax3),(ax4,ax5)) = plt.subplots(nrows = 2, ncols=2, figsize=(12,8)) 

        ax2.set_title("Time Point 1: Ankles Farthest Back")
        ax3.set_title("Time Point 2: Ankles Cross Hip Line (Forward Direction)")
        ax4.set_title("Time Point 3: Ankles Farthest Forward")
        ax5.set_title("Time Point 4: Ankles Cross Hip Line (Backward Direction)")

        proportions = [0,40,70,90,105,110]
        labels = only_keys.columns[1:7]

        plot_data = only_keys.iloc[:,1:7]
        plot_data.columns = proportions
        plot_mean = mean.iloc[:,1:7]
        plot_mean.columns = proportions

        plot_data.iloc[0,:].plot(ax=ax2, label="Your Data")
        plot_mean.iloc[0,:].plot(ax=ax2, label="Elite Swimmer Average")
        ax2.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
        ax2.set_xlim(-10,120)
        ax2.set_xticks([])
        

        for i, txt in enumerate(labels):
            ax2.annotate(txt, (proportions[i], plot_data.iloc[0,i]))

        fig2.legend()

        plot_data.iloc[1,:].plot(ax=ax3)
        plot_mean.iloc[1,:].plot(ax=ax3)
        ax3.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
        ax3.set_xlim(-10,120)
        ax3.set_xticks([])

        plot_data.iloc[2,:].plot(ax=ax4)
        plot_mean.iloc[2,:].plot(ax=ax4)
        ax4.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
        ax4.set_xlim(-10,120)
        ax4.set_xticks([])

        plot_data.iloc[3,:].plot(ax=ax5)
        plot_mean.iloc[3,:].plot(ax=ax5)
        ax5.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
        ax5.set_xlim(-10,120)
        ax5.set_xticks([])

        plt.show()

