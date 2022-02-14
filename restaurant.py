#Andrew McGovern
#CS 175L 50
#Restaurant Selector V2

#Declare the boolean values for each dietary restriction
repeat = True

#V2: Repeat entire restaurant search if they answer yes to repeating at end
while repeat == True:

    #Set the variables to false for each loop
    vegetarian = False
    vegan = False
    glutenFree = False
    
    #Make a string variable for the yes or no inputs for each question,
    VEGETARIAN_YN = input("\nIs anyone in your party a vegetarian?: ")
    #Then check if the string equals any variation of saying Yes
    if VEGETARIAN_YN.lower() == "yes" or VEGETARIAN_YN.lower() == "y":
        #If so, set the boolean variable for that diet restriction to True
        vegetarian = True

    #Do the same process for the other two conditions
    VEGAN_YN = input("Is anyone in your party a vegan?: ")
    if VEGAN_YN.lower() == "yes" or VEGAN_YN.lower() == "y":
        vegan = True

    GLUTEN_FREE_YN = input("Is anyone in your party gluten-free?: ")
    if GLUTEN_FREE_YN.lower() == "yes" or GLUTEN_FREE_YN.lower() == "y":
        glutenFree = True

    #Print out the restaurant list
    print("\nHere are your restaurant choices:")

    #Joe's accomodates to no restrictions
    #Only an option if all conditions are no
    if (not vegetarian) and (not vegan) and (not glutenFree):
        print("Joe's Gourmet Burgers")

    #Mama's accomodates to only vegetarian
    #Only an option if vegan and gluten-free are no
    if (not vegan) and (not glutenFree):
        print("Mama's Fine Italian")

    #Main Street accomodates to only vegetarian and gluten-free
    #Only an option if vegan is no
    if (not vegan):
        print("Main Street Pizza Company")

    #These accomodate to all options, whether the party has needs or not
    #So they fit on every list, no if statement needed
    print("Corner Cafe")
    print("The Chef's Kitchen")

    #Version 2: Ask if the user wants to do another search
    REPEAT_YN = input("\nWould you like to do another restaurant search?: ")
    if REPEAT_YN.lower() == "yes" or REPEAT_YN.lower() == "y":
        repeat = True
    else:
        repeat = False
        print("Thank you for using this program.")
