import tkinter as tk
import random

file_path = r"C:\\OOP\\simple-number-programs\\quiz_maker\\confidential_quiz_bank.txt"

questions = []
options = []
answers = []

while True:
    print("Welcome to quiz maker! The quiz will start after...")
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

print("Opening quiz...")

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

quiz_data = []
i = 0
while i + 5 < len(lines):
    quiz_data.append((
        lines[i],
        [lines[i+1], lines[i+2], lines[i+3], lines[i+4]],
        lines[i+5]
    ))
    i += 6

random.shuffle(quiz_data)

root = tk.Tk()
root.title("Quiz Game")
root.geometry("800x600")
root.configure(bg="black")

question_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 20), wraplength=700)
question_label.pack(pady=50)

buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", font=("Arial", 16), width=30)
    btn.pack(pady=10)
    buttons.append(btn)

score = 0
current = 0

def next_question():
    global current
    if current >= len(quiz_data):
        question_label.config(text=f"Quiz Over! Score: {score}/{len(quiz_data)}")
        for btn in buttons:
            btn.pack_forget()
        return
    q, opts, _ = quiz_data[current]
    question_label.config(text=q)
    for idx, btn in enumerate(buttons):
        btn.config(text=opts[idx], command=lambda opt=chr(65+idx): check_answer(opt))
    root.configure(bg="black")

def check_answer(choice):
    global score, current
    correct = quiz_data[current][2]
    if choice == correct:
        root.configure(bg="green")
        score += 1
    else:
        root.configure(bg="red")
    current += 1
    root.after(1000, next_question)

next_question()
root.mainloop()

