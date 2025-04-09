import random

file_path = r"C:\OOP\simple-number-programs\quiz_maker\confidential_quiz_bank.txt"

questions = []
options = []
answers = []

while True:
    question = input("Enter your question: ")
    opt_a = input("A. ")
    opt_b = input("B. ")
    opt_c = input("C. ")
    opt_d = input("D. ")
    correct = input("Enter the correct answer (A, B, C, or D): ").upper()

    while correct not in ['A', 'B', 'C', 'D']:
        correct = input("Enter the correct answer (A, B, C, or D): ").upper()

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(question.strip() + "\n")
        f.write(opt_a.strip() + "\n")
        f.write(opt_b.strip() + "\n")
        f.write(opt_c.strip() + "\n")
        f.write(opt_d.strip() + "\n")
        f.write(correct.strip() + "\n")

    another = input("Add another question? (yes/no): ").lower()
    if another != 'yes':
        break

print("QUIZ START !!!")

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

quiz_data = []
i = 0
while i + 5 < len(lines):
    question = lines[i]
    opt_a = lines[i+1]
    opt_b = lines[i+2]
    opt_c = lines[i+3]
    opt_d = lines[i+4]
    correct = lines[i+5]
    quiz_data.append((
        question,
        [f"A. {opt_a}", f"B. {opt_b}", f"C. {opt_c}", f"D. {opt_d}"],
        correct
    ))
    i += 6

random.shuffle(quiz_data)

score = 0

for question, options, correct in quiz_data:
    print("_________________")
    print(question)
    for opt in options:
        print(opt)

    guess = input("Enter your choice of answer (A, B, C, or D): ").upper()

    if guess == correct:
        score += 1
        print("Koreque! UwU")
    else:
        print("INCORRECT >:c ")
        print(f"{correct} is the correct answer.")

print("__________")
print("     RESULTS     ")
print("______________")
print(f"Your score is: {score}/{len(quiz_data)}")
