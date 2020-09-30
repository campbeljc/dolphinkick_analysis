#!/usr/bin/env python
import sys

from CreateDataFrame import To_DataFrame
from keys import find_keys

if __name__ == '__main__':

    # Set up parameters
    name = sys.argv[1]
    gender = sys.argv[2]
    orientation = sys.argv[3]
    speed = sys.argv[4]
    height = float(sys.argv[5])

    # Step 1: Inport data to be analyzed and convert it to Data Frame.

    destination, swimmer, data = To_DataFrame(orientation)

    print("loaded as data frame")

    # Step 2: Analyze Stored Data. Analyze data frames from all videos corresponding to parameters of new data. Calculate four key points and calculate mean and variance for those key points.
    

    key_1, key_2, key_3, key_4, time_1, time_2, time_3, time_4, time_total = find_keys(data)

    print(key_1, key_2, key_3, key_4, time_1, time_2, time_3, time_4, time_total)
    print("keys found")

    # Step 3: Format into data frame that can be loaded into another data frame and stored in a library to be called whenever needed

    only_keys = data.iloc[[key_1, key_2, key_3, key_4]]
    only_keys['Time'] = [time_1, time_2, time_3, time_4]

    print(height)
    print(only_keys)

    only_keys.loc[:,['Finger','Shoulder','Hip','Knee','Ankle','Toe']] = only_keys.loc[:,['Finger','Shoulder','Hip','Knee','Ankle','Toe']]/height

    series_1 = only_keys.iloc[0].tolist()
    series_2 = only_keys.iloc[1].tolist()
    series_3 = only_keys.iloc[2].tolist()
    series_4 = only_keys.iloc[3].tolist()

    # series_5 = [time_1, time_2, time_3, time_4]

    print('''
        ['{name}', '{gender}', '{orientation}', '{speed}', {time}, {height}, pd.DataFrame([
            {data1},
            {data2},
            {data3},
            {data4}],
            columns = ['t','Finger','Shoulder','Hip','Knee','Ankle','Toe','Time']
            )
        ]
        '''.format(name=name, gender=gender, orientation=orientation, speed=speed, time=time_total, height=height, data1 = series_1, data2= series_2, data3=series_3, data4 =series_4))
