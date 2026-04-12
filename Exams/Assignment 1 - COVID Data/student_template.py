import sys

def parse_nyt_data(file_path='us-counties.csv'):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    
    # Function that answers the first assignment question using the dataset "data"
    
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?    

    # Create a list of entries where:
    # entry[1] is "Harrisonburg city" AND the number of cases (entry[4]) is greater than 0
    harrisonburg_COVID_cases = [entry for entry in data if entry[1] == 'Harrisonburg city' and entry[4] > 0]

    # Check if the list contains any entries
    if harrisonburg_COVID_cases:

        # Sort the Harrisonburg entries by date (entry[0]) and take the earliest one
        first_case = sorted(harrisonburg_COVID_cases, key=lambda x: x[0])[0]

        # Print the date and number of cases for the first positive case
        print(f"First positive COVID case in Harrisonburg city: {first_case[0]} (Cases: {first_case[4]})")   

    else:        
        # If no cases were found, print a message
        print("No COVID cases found in Harrisonburg city.")

    # Create a list of entries where:
    # entry[1] is "Rockingham" AND the number of cases (entry[4]) is greater than 0
    rockingham_COVID_cases = [entry for entry in data if entry[1] == 'Rockingham' and entry[2] == 'Virginia' and entry[4] > 0]

    # Check if the list contains any entries
    if rockingham_COVID_cases:

        # Sort the Rockingham entries by date and select the earliest one
        first_case = sorted(rockingham_COVID_cases, key=lambda x: x[0])[0]

        # Print the date and number of cases for the first positive case
        print(f"First positive COVID case in Rockingham County: {first_case[0]} (Cases: {first_case[4]})")

    else:
        # If no cases were found, print a message
        print("No COVID cases found in Rockingham County.")



def second_question(data):
    
    # Function that answers the second assignment question
    
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    
    # Create a list of Harrisonburg entries where daily cases are greater than 0
    harrisonburg_COVID_cases2 = [entry for entry in data if entry[1] == 'Harrisonburg city' and entry[4] > 0]

    # Check if the list contains any entries
    if harrisonburg_COVID_cases2:

        # Find the entry with the maximum number of new cases (entry[4])
        most_new_cases = max(harrisonburg_COVID_cases2, key=lambda x: x[4])

        # Print the date and number of cases with the highest daily increase
        print(f"Greatest number of new daily cases in Harrisonburg city: {most_new_cases[0]} (Cases: {most_new_cases[4]})")

    else:
        # If no cases were found, print a message
        print("No COVID cases found in Harrisonburg city.")

    # Create a list of Rockingham entries where daily cases are greater than 0
    rockingham_COVID_cases2 = [entry for entry in data if entry[1] == 'Rockingham' and entry[2] == 'Virginia' and entry[4] > 0]

    # Check if the list contains any entries
    if rockingham_COVID_cases2:

        # Find the entry with the maximum number of new cases
        most_new_cases = max(rockingham_COVID_cases2, key=lambda x: x[4])

        # Print the date and number of cases with the highest daily increase
        print(f"Greatest number of new daily cases in Rockingham County: {most_new_cases[0]} (Cases: {most_new_cases[4]})")

    else:
        # If no cases were found, print a message
        print("No COVID cases found in Rockingham County.")



def third_question(data):
    
    # Function that answers the third assignment question
    
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    
    # Create a list of Harrisonburg entries where daily cases are greater than 0
    harrisonburg_COVID_cases3 = [entry for entry in data if entry[1] == 'Harrisonburg city' and entry[4] > 0]

    # Check if the list contains any entries
    if harrisonburg_COVID_cases3:

        # Sort the entries by date so the 7-day window works correctly
        harrisonburg_COVID_cases3.sort(key=lambda x: x[0]) 

        # Variable to track the maximum number of cases found in any 7-day window
        max_cases = 0

        # Variable to store the start and end dates of the worst period
        worst_period = None

        # Loop through the list while leaving space for a full 7-day window
        for i in range(len(harrisonburg_COVID_cases3) - 6):

            # Calculate the total number of cases for the current 7-day slice
            seven_day_cases = sum(entry[4] for entry in harrisonburg_COVID_cases3[i:i+7])

            # Check if this 7-day total is greater than the previous maximum
            if seven_day_cases > max_cases:

                # Update the maximum case count
                max_cases = seven_day_cases

                # Store the start and end dates of this worst 7-day period
                worst_period = (harrisonburg_COVID_cases3[i][0], harrisonburg_COVID_cases3[i+6][0])

        # Print the worst 7-day period and total cases
        print(f"Worst 7-day period in Harrisonburg city: {worst_period[0]} to {worst_period[1]} (Cases: {max_cases})")

    else: 
        # If no cases were found, print a message
        print("No COVID cases found in Harrisonburg city.")

    # Create a list of Rockingham entries where daily cases are greater than 0
    rockingham_COVID_cases3 = [entry for entry in data if entry[1] == 'Rockingham' and entry[2] == 'Virginia' and entry[4] > 0]

    # Check if the list contains any entries
    if rockingham_COVID_cases3:

        # Sort entries by date
        rockingham_COVID_cases3.sort(key=lambda x: x[0]) 

        # Variable to track the maximum 7-day case total
        max_cases = 0

        # Variable to store the worst 7-day period
        worst_period = None

        # Loop through the dataset checking every 7-day window
        for i in range(len(rockingham_COVID_cases3) - 6):

            # Sum the number of cases across the 7-day slice
            seven_day_cases = sum(entry[4] for entry in rockingham_COVID_cases3[i:i+7])

            # If this total is larger than the previous maximum
            if seven_day_cases > max_cases:

                # Update the maximum case total
                max_cases = seven_day_cases

                # Save the start and end dates of this period
                worst_period = (rockingham_COVID_cases3[i][0], rockingham_COVID_cases3[i+6][0])

        # Print the worst 7-day period and number of cases
        print(f"Worst 7-day period in Rockingham County: {worst_period[0]} to {worst_period[1]} (Cases: {max_cases})")

    else:
        # If no cases were found, print a message
        print("No COVID cases found in Rockingham County.")


if __name__ == '__main__':
    data = parse_nyt_data()

    first_question(data)
    second_question(data)
    third_question(data)


