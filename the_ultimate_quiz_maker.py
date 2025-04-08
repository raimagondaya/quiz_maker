# quiz maker men

questions = ("Makakapasa kaya ems??",)

options = (("A. YEZZIR", "B. SYEMPRE", "C. OMSIM", "D. OO IKINAMADA"),)

answers = ("A",)

guesses = []

score = 0

question_num = 0

for question in questions:
    print("_________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your choice of answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Koreque! UwU")
    else:
        print("INCORRECT >:c ")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("__________")
print("     RESULTS     ")
print("______________")
print(f"Your score is: {score}/{len(questions)}")
