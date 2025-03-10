import csv
# with open('exam_questions.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)
# number,Question, Option A, Option B, Option C, Correct Answer
def answer_question(question):
    # Your logic to answer the question based on the input
    # Replace this with your actual answer generation process
    pass

with open("exam_questions.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        question = row[1] 
        option_a = row[2]
        option_b = row[3]
        option_c = row[4]
        answer = answer_question(question)
        print(f"Question: {question}")
        print(f"""Options:
                A {option_a}
                B {option_b}
                C {option_c}""")
        answers = input("Enter your answer: ")         