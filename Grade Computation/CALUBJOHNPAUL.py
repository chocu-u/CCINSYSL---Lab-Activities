def get_score(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

act1 = get_score("Input activity 1 score (0-30): ", 0, 30)
act2 = get_score("Input activity 2 score (0-20): ", 0, 20)
act3 = get_score("Input activity 3 score (0-10): ", 0, 10)

as1 = get_score("Input assignment 1 score (0-50): ", 0, 50)
as2 = get_score("Input assignment 2 score (0-50): ", 0, 50)
as3 = get_score("Input assignment 3 score (0-50): ", 0, 50)

longExam = get_score("Input long exam score (0-50): ", 0, 50)
finalProj = get_score("Input final project score (0-50): ", 0, 50)

tScore = act1 + act2 + act3 + as1 + as2 + as3
tItems = 210

csGrade = tScore / tItems * 100
csGradePerc = csGrade * 0.4

longExamGrade = longExam / 50 * 100
longExamGradePerc = longExamGrade * 0.4

finalProjGrade = finalProj / 50 * 100
finalProjGradePerc = finalProjGrade * 0.2

finalGrade = csGradePerc + longExamGradePerc + finalProjGradePerc

status = "Congratulations! You have passed!" if finalGrade >= 60 else "Unfortunately, you have failed."

print("\n{:14} {:>7} {:>7}".format("", "Score", "Items"))
print("{:14} {:>7} {:>7}".format("Activity 1", act1, 30))
print("{:14} {:>7} {:>7}".format("Activity 2", act2, 20))
print("{:14} {:>7} {:>7}".format("Activity 3", act3, 10))
print("{:14} {:>7} {:>7}".format("Assignment 1", as1, 50))
print("{:14} {:>7} {:>7}".format("Assignment 2", as2, 50))
print("{:14} {:>7} {:>7}".format("Assignment 3", as3, 50))
print("{:14} {:>7} {:>7}".format("Long Exam", longExam, 50))
print("{:14} {:>7} {:>7}".format("Final Project", finalProj, 50))
print ("")
print("{:14} {:>7.2f}".format("Final Grade", finalGrade))
print ("")
print("{:14} {:>7}".format(status, ""))