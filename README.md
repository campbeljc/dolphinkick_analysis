# dolphinkick_analysis

## Main Function

Analyzes differences in a swimmer's dolphin kick technique compared to elite swimmers.

Input is a data table of x,y-coordinates of key points on a swimmer performing dolpihin kick (created using [Tracker software](https://physlets.org/tracker/)), output is table of x,y-coordinates that are significantly different from the average of the x,y-coordinates of elite swimmers performing dolphin kick.

## Running the Software

To run the program type the following into terminal:
```
python3 dolphin.py
```

The software will ask you a series of questions about your gender, orientation while performing the dolphin kick, and the speed at which you were performing it. These questions are to select an equivelant subset of data from the database of elite swimmers to compare to.

Please have the following installed to run the program:

* sys
* numbers
* pandas
* numpy
* scipy

Use the following command to import these packages if you do not have them installed
```
pip3 install {package name}
```

## How the Software Works

### Creating the Input File

The input file is and excel file containing a data table with the y-coordinates of six key joints on the swimmer throughout one full cycle of dolphin kick. The designated beginning is when the ankles are at the farthest back position in the kick. Make sure the ankles are at least behind the hips at time 1. The program will automatically detect the farthest back position.

The data table should look as follows:

| t      | Finger | Shoulder | Hip | Knee | Ankle | Toe |
|--------|--------|----------|-----|------|-------|-----|
| time 1 |        |          |     |      |       |     |
| time 2 |        |          |     |      |       |     |
| time 3 |        |          |     |      |       |     |

The easiest way to create this table is using the free online software [Tracker](https://physlets.org/tracker/). 

In order to keep values relative to the swimmer's location in the frame, the hips are designated as the origin of the x,y-plane. The angle of the x-axis is designated as the straight line that represents the best fit to all points on the swimmers body when the swimmer is at her most straight position.

The height of the swimmer is used to scale measurements.

The image below represents the proper set-up.


![Swimmer](Tracker_swimmer.png)


### Elite Swimmer Library

The program contains a library of data representing dolphin kick technique from elite swimmers as pandas dataframe. This library was created using the processog.py file included in this repository. This script asks for an excel file (same format as above) as an input and outputs a printed version of the dataframe that can then be copy and pasted into Library.py to be referenced as a comparison.

Four key time points are computed for every elite swimmer's data, and only these timepoints are used in comparison and stored. See below for explanation of the key time points.

Use the following command to create an input for the Library dataframe:

```
python3 processog.py {swimmer name} {gender} {orientation} {speed} {swimmer's height}
```

### Program Logic

When run the program follows these processing steps:

1. The inputted parameters (gender, orientation and speed) are used to filter the elite swimmer data so only equivallent comparisons are made. 

2. The mean and variance of the filtered elite swimmer data is computed for each joint and each time point.

3. Four key time points based on specific positions during the dolphin kick are computed. The key time points are:

      Key 1: Ankles are at farthest backwards position during the kick
      Key 2: Ankles cross the midline in a forward direction
      Key 3: Ankles are at farthest forward position during the kick
      Key 4: Ankles cross the midline in a backward direction
      
4. All values are normalized to the height of the swimmer.

5. The values at each of the key time points are compared to the filtered elite swimmer data for each joint an p-values are computed.

6. A table containing these p-values is returned.


## Future Updates

1. Add feature that plots a graph for each key time point with "Joint" on the x-axis and y-value on the y-axis. Mark in red values that have p-values less than or equal to 0.05

2. Update plot feature to include averaged value of filtered elite swimmer data to compare.

3. Update input to include x-values so plot can include x-values as x-axis.



