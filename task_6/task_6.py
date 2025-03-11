import csv
# number,Question, Option A, Option B, Option C, Correct Answer
# def match_answer():
#     with open("exam_questions.csv", "r") as csvfile:
#         reader = csv.reader(csvfile)
#         global result1 
#         result1 = []
#         for row in reader:
#             if row[5] == "Correct Answer":
#                 pass
#             else:
#                 result1.append(row[5])
#         print(result1)
#     return True  
# column_index = 2
# column_name = 1
# def store_value(row_values, column_index):
#     file = open('user_data.csv', 'w', newline='')
#     # with open('user_data.csv', 'w', newline='') as file:
#     writer = csv.writer(csvfile)

#         # Write data rows
#     for value in row_values:
#             row = [''] * (column_index + 1)  
#             row[column_index] = value  
#             print(file.closed)      
#             writer.writerow(row)
column_index = 1
def append_to_column(column_index, data):
    rows = []
    with open("user_data.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    
    with open("user_data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for i, row in enumerate(rows):
            if i == 0:
                writer.writerow(row)
            else:
                if len(row) > column_index:
                        row[column_index] = data
                else:
                    while len(row) <= column_index:
                        row.append("")
                    row[column_index] = data
                writer.writerow(row)







# def store_name(column_name, name):
#     with open("user_data.csv", 'r+') as file:
#         reader = csv.reader(file)
#         rows = list(reader)

#         while len(rows[0]) <= column_name:
#             rows[0].append('')

#         rows[0][column_name] = name
#         file.seek(0)
#         writer = csv.writer(file)
#         writer.writerows(rows)

username = input("Enter your username: ")
# store_name(column_name, username)
with open("exam_questions.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    result = []
    for row in reader:
            number = row[0]
            question = row[1] 
            option_a = row[2]
            option_b = row[3]
            option_c = row[4]
            print(f"{number}.Question: {question}")
            print(f"""Options:
                    A {option_a}
                    B {option_b}
                    C {option_c}""")
            # import pdb; pdb.set_trace()
            # global answers
            
            answers = input("Enter your answer (A/B/C): ")
            if answers == "A" or answers == "B" or answers == "C":
                result += answers
            else:
                print("Invalid input. Please enter one uppercase character.")
            # import pdb; pdb.set_trace()
    append_to_column(column_index, result)
    
    
    
    
    # result = [] 
    # if len(answers) == 1 and answers.isupper():
    #         result += answers
    # if answers == "A" or answers == "B" or answers == "C":
    #     print(result)
    #     store_value(answers)
    # else:
    #     print("Invalid input. Please enter one uppercase character.")
    #     print_row()