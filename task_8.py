from datetime import datetime, timedelta

# USER INPUT TIME
while True:
    try:
        user_time = input("Enter time in HH:MM:SS format: ")
        time_object = datetime.strptime(user_time, "%H:%M:%S").time()
        print("Entered time:", time_object)
        break
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")

# FUNCTION TO ADD TIME
def add_times(time_str1, time_str2):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    combined_time_delta = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
    new_time = time1 + combined_time_delta
    return new_time.strftime(time_format)

# FUNCTION TO DIFFERENCE TIME
def diff_times(time_str1, time_str2):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    time_diff = time1 - time2
    return time_diff

# FUNCTION TO INCREASE SECONDS
def add_sec(time_str1, time_str2):
    time_format = "%H:%M:%S"
    new_sec_format = "%S"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, new_sec_format)
    combined_time_delta = timedelta(seconds=time2.second)
    new_time = time1 + combined_time_delta
    return new_time.strftime(time_format)

# FUNCTION TO INCREASE MINUTES
def add_min(time_str1, time_str2):
    time_format = "%H:%M:%S"
    new_min_format = "%M"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, new_min_format)
    combined_time_delta = timedelta(minutes=time2.minute)
    new_time = time1 + combined_time_delta
    return new_time.strftime(time_format)

# FUNCTION TO INCREASE HOURS
def add_hour(time_str1, time_str2):
    time_format = "%H:%M:%S"
    new_hour_format = "%H"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, new_hour_format)
    combined_time_delta = timedelta(hours=time2.hour)
    new_time = time1 + combined_time_delta
    return new_time.strftime(time_format)

# SELECT OPTION
select_option = input("""1 for Increase a Time by (seconds/minutes/hours)
                        2 for Addition of two time values
                        3 for Diﬀrence of two time values
                        Enter your choice (1/2/3): """)

if select_option == "1":
    # INCREASE TIME
    increase_time_input = input("Enter which time to increase (s/m/h): ")
    if increase_time_input == "s":
        try:
            add_seconds_input = input("Enter seconds: ")
            result = add_sec(user_time, add_seconds_input)
            print("The new time is:", result)
        except ValueError:
            print("Invalid input. Please enter seconds.")
    elif increase_time_input == "m":
        try:
            add_minutes_input = input("Enter minutes: ")
            result = add_min(user_time, add_minutes_input)
            print("The new time is:", result)
        except ValueError:
            print("Invalid input. Please enter minutes.")
    elif increase_time_input == "h":
        try:
            add_hours_input = input("Enter hours: ")
            result = add_hour(user_time, add_hours_input)
            print("The new time is:", result)
        except ValueError:
            print("Invalid input. Please enter hours.")
    else:
        print("Invalid input. Please enter s/m/h.")
elif select_option == "2":
    # ADD TIME
    while True:
        try:
            add_time_input = input("Enter time to add in HH:MM:SS format: ")
            result = add_times(user_time, add_time_input)
            print("The new time is:", result)
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")
elif select_option == "3":
    # DIFF TIME
    while True:
        try:
            diff_time_input = input("Enter time to subtract in HH:MM:SS format: ")
            result = diff_times(user_time, diff_time_input)
            print("The time difference is:", result)
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")
else:
    print("Invalid input. Please enter 1/2/3.")