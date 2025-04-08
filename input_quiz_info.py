questions = []
options = []
answers = []

while True:
    print("Add a New Question")
    question = input("Enter your question: ")
    questions.append(question)

    print("Enter the choices:")
    opt_a = input("A. ")
    opt_b = input("B. ")
    opt_c = input("C. ")
    opt_d = input("D. ")
    options.append([f"A. {opt_a}", f"B. {opt_b}", f"C. {opt_c}", f"D. {opt_d}"])

    correct = input("Enter the correct answer (A, B, C, or D): ").upper()
    while correct not in ['A', 'B', 'C', 'D']:
        print("Invalid choice. Please choose A, B, C, or D only.")
        correct = input("Enter the correct answer (A, B, C, or D): ").upper()
    answers.append(correct)

    another = input("Add another question? (yes/no): ").lower()
    if another != 'yes':
        break

print("QUIZ START !!!")

score = 0
guesses = []

for i in range(len(questions)):
    print("_________________")
    print(questions[i])
    for option in options[i]:
        print(option)

    guess = input("Enter your choice of answer (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        score += 1
        print("Koreque! UwU")
    else:
        print("INCORRECT >:c ")
        print(f"{answers[i]} is the correct answer.")

print("__________")
print("     RESULTS     ")
print("______________")
print(f"Your score is: {score}/{len(questions)}")
