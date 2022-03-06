import myrand

def main():

    print("")
    print("Score\t\tNumeric Grade\tLetter Grade")
    print("------------------------------------------------")

    calc_average()
    repeat()

def calc_average():
    total = 0
    
    for x in range(1,5+1):
        score = myrand.my_random(1,100)
        letter = determine_grade(score)
        total = total + score
        print(f"Score {x}:\t{score:^13}\t{letter:^12}")
        
    average = total / 5
    avg_letter = determine_grade(average)
    print(f"Average score:\t{average:^13}\t{avg_letter:^12}")

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


def repeat():
    repeatYN = input("\nEnter 'yes' if you would "+
                     "like to do another calculation: ")
    if repeatYN.lower() == "yes" or repeatYN.lower() == "y":
        main()
    else:
        print("Goodbye!")

#Running the program for the first time
main()
