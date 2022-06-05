- Bike Share Data:
In this project, I make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 
The project provides computing descriptive statistics and creating interactive experience in the terminal to present these statistics.

- The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Datasets examples:
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
Gender
Birth Year

- Statistics Computed:
In this project, I wrote a code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day

#2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration
total travel time
average travel time

#4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

All project data files:
[washington.zip](https://github.com/ManuelHany/BikeShare_Analysis/files/8839703/washington.zip)
[chicago.zip](https://github.com/ManuelHany/BikeShare_Analysis/files/8839704/chicago.zip)
[new_york_city.zip](https://github.com/ManuelHany/BikeShare_Analysis/files/8839705/new_york_city.zip)



- Steps to run project:
1- Download/Clone project data as ZIP then extract all data.
2- In the readme file(the current file), scroll down to the "All poject data files" section.
3- Download all 3 data sets as zip. 
4- Browse to the main profect directory and extract all data files inside it. 
5- From any terminal, Browse to the project directory and type the command -> python .\bikeshare_2.py
6- Next, the project will auto navigate you through the analysis filters and outputs based on your requests
