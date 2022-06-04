import time
import pandas as pd
import numpy as np

############################################
## This code was developed by Manuel Hany ##
############################################

#please refer to read_me file
pd.options.mode.chained_assignment = None  # default='warn'

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
DAY_DATA = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

original_df = pd.DataFrame()
month_filtered = False
day_filtered = False

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello!\n    Let\'s explore some US bikeshare data!\nThe acquired data are for one of the 3 cities, Washington, New York City and Chicago.\nThe data are collected for the first 6 months of 2017.\nNow let\'s begin ...\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Please choose the city: Chicago, New York City or Washington\n"))
            city = city.lower()
            if city in CITY_DATA:
                break
            else:
                print("That is not a valid choice.\nPlease make sure to choose one of the cities stated")
        except:
            print("That is not valid.\nPlease make sure to enter words only")
    print('\n')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Please choose the month: January, February, March, April, May, June or type \"all\" if you want to apply no month filter\n"))
            month = month.lower()
            if (month in MONTH_DATA.values()) or (month == 'all'):
                break
            else:
                print("That is not a valid choice.\nPlease make sure to choose one of the stated months")
        except:
            print("That is not valid.\nPlease make sure to enter words only")
    print('\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("Please choose the day: Monday, Tuesday, Wednesday, Thursday, Friday, Sunday or type \"all\" if you want to apply no day filter\n"))
            day = day.lower()
            if (day in DAY_DATA) or (day == 'all'):
                break
            else:
                print("That is not a valid choice.\nPlease make sure to choose one of the stated days")
        except:
            print("That is not valid.\nPlease make sure to enter words only")
    print('\n')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #this global variable is used to load the initial raw data without any applied filters and have the ability to access it anywhere inside the code
    global original_df

    #these 2 global variables are used to clarify what type of filter was applied to demonstrate the printed outputs accordingly in "time_stats" function
    global month_filtered
    global day_filtered

    #Loading the full dataset inside a dataframe to be filtered accordingly
    data_filname = (city + '.csv').replace(" ", "_")
    df = pd.read_csv(data_filname)

    #Loading the original raw data inside original_df
    original_df = df
    
    #Converting start time object to datetime and adding 2 extra columns in the dataframe for 'month' and 'day'
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    #If month was used as a filter (could also be if month_filtered == True:)
    if month != 'all':
        month = list(MONTH_DATA.values()).index(month) + 1
        df = df[df['month'] == month]
        month_filtered = True

    #If day was used as a filter (could also be if day_filtered == True:)
    if day != 'all':
        day = day.title()
        df = df[df['day'] == day]
        day_filtered = True

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    global month_filtered
    global day_filtered

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # get the most common month
    most_common_month = MONTH_DATA[df['month'].mode()[0]]

    # get the most common day of week
    most_common_day = df['day'].mode()[0]

    #Depending on user's filter, display corresponding month and day
    if (month_filtered == False) and (day_filtered == False):
        print('Most common month is:           ', most_common_month.title())
        print('Most common day of the week is: ', most_common_day)
    elif (month_filtered == True) and (day_filtered == False):
        print('For "{}" month applied as filter: '.format(most_common_month.title()))
        print('Most common day of the week is: ', most_common_day)
    elif (month_filtered == False) and (day_filtered == True):
        print('For "{}" day applied as filter: '.format(most_common_day))
        print('Occurs mostly in th month:      ', most_common_month.title())
    else:
        print('For "{}" month, and "{}" day applied as filter: '.format(most_common_month.title(), most_common_day))

    print('\nDay_filtered ==> {}\nMonth_filtered ==> {}'.format(day_filtered, month_filtered))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Tho most common start hour is:  ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mcu_start_station = df['Start Station'].mode()[0]
    mcu_start_station_count = len(df[df['Start Station'] == mcu_start_station])
    print('Most commonly used start station is:                   "{}" of total count {} times'.format(mcu_start_station, mcu_start_station_count))

    # display most commonly used end station
    mcu_end_station = df['End Station'].mode()[0]
    mcu_end_station_count = len(df[df['End Station'] == mcu_end_station])
    print('Most commonly used end station is:                     "{}" of total count {} times'.format(mcu_end_station, mcu_end_station_count))

    # display most frequent combination of start station and end station trip
    mcu_start_end_station = (df['Start Station'] + '==>' + df['End Station']).mode()[0].split("==>")
    print('Most frequent combination of start ==> end station is: "{}" ==> "{}".'.format(mcu_start_end_station[0], mcu_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {} in seconds'.format(int(total_travel_time)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is:  {} in seconds'.format(int(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_usertype = df['User Type'].value_counts()
    print('Counts of users type is\n{}\n'.format(count_of_usertype))

    # Display counts of gender (if available!)
    if 'Gender' in df.columns:
        count_of_gender = df['Gender'].value_counts()
        print('Counts of users type is\n{}\n'.format(count_of_gender))

    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def finalize(original_df):
    """ This function is to print iterative 5 raws of the raw data input and handles the output when the file reaches the maximum row index"""

    #initializing the start index and end index of each 5 rows of the raw data
    starti, endi = 0, 5

    print('Showing the first 5 rows of the data here. If you would like to show more data just press yes in the prompt question.\n\n')
    #print first 5 lines
    print(original_df.iloc[starti: endi])
    while True:
        try:
            repeat = str(input('Would you like to print more date? Enter yes or no.\n'))
            repeat = repeat.lower()
            if (repeat != 'yes') and (repeat != 'no'):
                print('This is not a valid choice. Please type either "yes or "no')
            elif repeat == 'yes':
                #print the next 5 lines and make sure it's not the end of the file
                print('\n')
                if (endi+5) <= (original_df.shape[0] + 1):
                    starti+=5
                    endi+=5
                    print(original_df.iloc[starti: endi])
                else:
                    print('This was the end of the data')
                    break
            elif repeat == 'no':
                break
            else:
                pass
        except:
            print('Please make sure to enter a valid input')

def main():
    restart = 'yes'
    while restart == 'yes':
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        finalize(original_df)
        while True:
            try:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                restart = restart.lower()
                if (restart != 'yes') and (restart != 'no'):
                    print('This is not a valid choice. Please type either "yes or "no')
                else:
                    break
            except:
                print('Please make sure to enter a valid input')

if __name__ == "__main__":
	main()
