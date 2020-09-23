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
