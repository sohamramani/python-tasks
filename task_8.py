from datetime import datetime, timedelta

def add_times(time_str1, time_str2):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    combined_time_delta = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
    new_time = time1 + combined_time_delta
    return new_time.strftime(time_format)
while True:
    try:
        user_time = input("Enter time in HH:MM:SS format: ")
        time_object = datetime.strptime(user_time, "%H:%M:%S").time()
        print("Entered time:", time_object)
        break
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")

select_option = input("""1 for Increase a Time by (seconds/minutes/hours)
                        2 for Addition of two time values
                        3 for Diﬀrence of two time values
                        Enter your choice (1/2/3): """)
if select_option == "1":
    increase_time = input("Enter which time to increase (s/m/h): ")
    if increase_time == "h":
        increase_time = 1
    elif increase_time == "m":
        increase_time = 60
    elif increase_time == "s":
        increase_time = 3600
    else:
        print("Invalid input. Please enter s/m/h.")
    time_object = datetime.strptime(increase_time, "%H:%M:%S").time()
    print("Entered time:", time_object)
    result = add_times(user_time, increase_time)
    print("The new time is:", result)
elif select_option == "2":
    while True:
        try:
            increase_time = input("Enter time to increase in HH:MM:SS format: ")
            result = add_times(user_time, increase_time)
            print("The new time is:", result)
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")
