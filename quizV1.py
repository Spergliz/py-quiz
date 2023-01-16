
#score
score = 0

#title
print("welcome to my quiz")
#Q1
Question1 = input("why do people use linux: ")
if Question1.lower() == "tux":
    print("correct")
    score = score + 1
else: 
    print("wrong")
    
#Q2 
Question2 = input("what is 3+2: ")
if Question2.lower() == 5 or "five": 
    print ("Correct")
    score = score + 1
else:
     print("wrong")

#Q3
Question3 = input("what is the first name of the Father of Linux: ")
if Question3.lower() == "linus":
    print("correct")
    score = score + 1
else:
    print("wrong")

#Q4
Question4 = input(" : ")
if Question4.lower() == "":
    print("correct")
    score = score + 1
else:
    print("wrong")
