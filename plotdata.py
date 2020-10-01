import numpy as np

def plot_data(data, only_keys, mean, p_values):

    #Bug that crashes python when Tk instance 
    import matplotlib.pyplot as plt  


    fig1, ax1 = plt.subplots(nrows = 1, ncols=1, figsize=(5,4)) 

    # Plot Standard Imported Data
    data_toplot = data.drop(['Hip'], axis=1)
    data_toplot.index = data_toplot['t']
    ax1.set_prop_cycle(color=['#714bff','#15087b','#217bfc','#7aed85','#21f3fc'])
    data_toplot.iloc[:,1:].plot(ax=ax1)
    ax1.set_ylabel("Vertical Displacement (m)", fontsize=12)
    ax1.set_xlabel("time (s)", fontsize=12)

    #Plot Time Intervals

    fig3, axtime = plt.subplots(nrows = 1, ncols =1, figsize= (8,5.5))
    mean_times = mean['Time'].round(decimals=2)
    data_times = only_keys['Time'].round(decimals=2)

    time_labels = ['Point 4 to 1', 'Point 1 to 2', 'Point 2 to 3', 'Point 3 to 4']
    x = np.arange(len(time_labels))
    width = 0.35

    rects1 = axtime.bar(x - width/2, data_times, width, label='Your Data',color=(0, 0.1, 0.2, 0.8))
    rects2 = axtime.bar(x + width/2, mean_times, width, label='Professional Swimmer Averages',color=(0, 0, 0, 0.2))

    axtime.set_ylabel('Time (s)',fontsize=12)
    axtime.set_xticks(x)
    axtime.set_yticks([0,0.05,0.1,0.15,0.2,0.25])
    axtime.set_xticklabels(time_labels,fontsize=12)
    axtime.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            axtime.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

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

    #Create Comparison Plot

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

    outliers = p_values.iloc[:,1:7]
    outliers.columns = proportions

    def get_scatterpoints(p_values, data, n):
        row = p_values.iloc[n]
        x_values = []
        y_values = []
        for index, value in row.items():
            if value < 0.1:
                something = data.iloc[n]
                # print(something[index])
                x_values.append(something[index])
                y_values.append(index)
        return x_values, y_values

    plot_data.iloc[0,:].plot(ax=ax2, label="Your Data",color=(0, 0.1, 0.9,1))
    plot_mean.iloc[0,:].plot(ax=ax2, label="Elite Swimmer Average",color=(0, 0, 0, 0.7))
    ax2.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
    ax2.set_xlim(-10,120)
    ax2.set_xticks([])
    ax2.set_ylabel('Vertical Displacement (normalized)', fontsize=11)
    ax2.yaxis.grid()
    
    ys, xs = get_scatterpoints(outliers, plot_data, 0)
    ax2.scatter(xs,ys, color='red')
    
    for i, txt in enumerate(labels):
        ax2.annotate(txt, (proportions[i], plot_data.iloc[0,i]))

    fig2.legend()

    plot_data.iloc[1,:].plot(ax=ax3,color=(0, 0.1, 0.9,1))
    plot_mean.iloc[1,:].plot(ax=ax3,color=(0, 0, 0, 0.7))
    ax3.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
    ax3.set_xlim(-10,120)
    ax3.set_xticks([])
    ax3.yaxis.grid()

    ys, xs = get_scatterpoints(outliers, plot_data, 1)
    ax3.scatter(xs,ys, color='red')

    plot_data.iloc[2,:].plot(ax=ax4,color=(0, 0.1, 0.9,1))
    plot_mean.iloc[2,:].plot(ax=ax4,color=(0, 0, 0, 0.7))
    ax4.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
    ax4.set_xlim(-10,120)
    ax4.set_xticks([])
    ax4.set_ylabel('Vertical Displacement (normalized)', fontsize=10)
    ax4.yaxis.grid()

    ys, xs = get_scatterpoints(outliers, plot_data, 2)
    ax4.scatter(xs,ys, color='red')

    plot_data.iloc[3,:].plot(ax=ax5,color=(0, 0.1, 0.9,1))
    plot_mean.iloc[3,:].plot(ax=ax5,color=(0, 0, 0, 0.7))
    ax5.set_ylim(total_min+(0.05*total_min),total_max+(0.05*total_max))
    ax5.set_xlim(-10,120)
    ax5.set_xticks([])
    ax5.yaxis.grid()

    ys, xs = get_scatterpoints(outliers, plot_data, 3)
    ax5.scatter(xs,ys, color='red')

    return fig1, fig2, fig3