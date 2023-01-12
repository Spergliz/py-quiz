
# score
score = 0

# title
print("welcome to my quiz")
# Q1
Question1 = input("why do people use linux: ")
if Question1.lower() == "tux":
    print("correct")
    score = score + 1
else:
    print("wrong")

# Q2
Question2 = input("what is 3+2: ")
if Question2.lower() == "5" or Question2.lower() == "five":
    print("Correct")
    score = score + 1
else:
    print("wrong")

# Q3
Question3 = input("what is the first name of the Father of Linux: ")
if Question3.lower() == "linus":
    print("correct")
    score = score + 1
else:
    print("wrong")

# Q4
Question4 = input("what genre is the duo BLACK DRESES:  ")
if Question4.lower() == "eletro industrial" or Question4.lower() == "industrial":
    print("correct")
    score = score + 1
else:
    print("wrong")

# finish
print("your score is " + str(score)+"/4.")
if score == 4:
    print("100% well done")
elif score == 3:
    print("75% study a bit more")
elif score == 2:
    print("50%  study more")
else:
    print("0% study")
