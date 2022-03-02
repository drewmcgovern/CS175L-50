def main():
    score1 = float(input("Enter score 1: "))
    while score1 > 100 or score1 < 0:
        score1 = float(input("Outside range, enter score 1: "))
    letter1 = determine_grade(score1)
    
    score2 = float(input("Enter score 2: "))
    while score2 > 100 or score2 < 0:
        score2 = float(input("Outside range, enter score 2: "))
    letter2 = determine_grade(score2)

    score3 = float(input("Enter score 3: "))
    while score3 > 100 or score3 < 0:
        score3 = float(input("Outside range, enter score 3: "))
    letter3 = determine_grade(score3)

    score4 = float(input("Enter score 4: "))
    while score4 > 100 or score4 < 0:
        score4 = float(input("Outside range, enter score 4: "))
    letter4 = determine_grade(score4)

    score5 = float(input("Enter score 5: "))
    while score5 > 100 or score5 < 0:
        score5 = float(input("Outside range, enter score 5: "))
    letter5 = determine_grade(score5)
    
    average = calc_average(score1, score2, score3, score4, score5)
    avg_letter = determine_grade(average)

    print("")
    print("Score\t\tNumeric Grade\tLetter Grade")
    print("------------------------------------------------")
    print(f"Score 1:\t{score1:^13}\t{letter1:^12}")
    print(f"Score 2:\t{score2:^13}\t{letter2:^12}")
    print(f"Score 3:\t{score3:^13}\t{letter3:^12}")
    print(f"Score 4:\t{score4:^13}\t{letter4:^12}")
    print(f"Score 5:\t{score5:^13}\t{letter5:^12}")
    print(f"Average score:\t{average:^13}\t{avg_letter:^12}")
    
    repeatYN = input("\nEnter 'yes' if you would "+
                     "like to do another calculation: ")
    if repeatYN.lower() == "yes" or repeatYN.lower() == "y":
        repeatTF = True
    else:
        repeatTF = False
    repeat(repeatTF)

def determine_grade(num):
    letter = "F"
    if num >= 90:
        letter = "A"
    elif num >= 80:
        letter = "B"
    elif num >= 70:
        letter = "C"
    elif num >= 60:
        letter = "D"
    else:
        pass
    return letter

def calc_average(num1,num2,num3,num4,num5):
    total = num1+num2+num3+num4+num5
    average = total / 5
    return average

def repeat(boolean):
    if boolean == True:
        main()
    else:
        print("Goodbye!")

#Running the program for the first time
main()
