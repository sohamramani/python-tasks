import csv

def authenticate_user(username, password, csv_file = "user_data.csv"):
    try:
        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            credentials = {}
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    username_csv = row[0].strip()
                    password_csv = row[1].strip()
                    credentials[username_csv] = password_csv 
            if username in credentials and credentials[username] == password:
                print("log in successful")
                quiz_from_csv(csv_file_path)
                return True
            else:
                print("log in failed")
                return False
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_file}")
        return False
    except Exception as e:
            print(f"An error occurred: {e}")
            return False
    return False

def quiz_from_csv(csv_file):
    correct_count = 0
    total_questions = 0
    while True:
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    total_questions += 1
                    question, *options, answer = row  
                    print(f"\n{question}")
                    for i, option in enumerate(options):
                        print(f"{chr(65 + i)}. {option}") 
                    user_answer = input("Your Answer: ").upper()
                    if user_answer == answer.strip().upper():
                        correct_count += 1
            print(f"\nResults: You answered {correct_count} out of {total_questions} questions correctly.")
            break
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file}")
            return False
        except Exception as e:
                print(f"An error occurred: {e}")
                return False
    return False
csv_file_path = "exam_questions.csv"  
while True:
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authenticate_user(username, password)
    except Exception as e:
        print(f"An error occurred: {e}")