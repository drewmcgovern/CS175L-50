#Andrew McGovern
#CS 175L 50
#Restaurant Selector

#Declare the boolean values for each dietary restriction
vegetarian = False
vegan = False
glutenFree = False

#Make a string variable for the yes or no inputs for each question,
VEGETARIAN_YN = input("Is anyone in your party a vegetarian?: ")
#Then check if the string equals any variation of saying Yes
if VEGETARIAN_YN == "yes" or VEGETARIAN_YN == "Yes" or VEGETARIAN_YN == "Y":
    #If so, set the boolean variable for that diet restriction to True
    vegetarian = True

#Do the same process for the other two conditions
VEGAN_YN = input("Is anyone in your party a vegan?: ")
if VEGAN_YN == "yes" or VEGAN_YN == "Yes" or VEGAN_YN == "Y":
    vegan = True
    
GLUTEN_FREE_YN = input("Is anyone in your party gluten-free?: ")
if GLUTEN_FREE_YN == "yes" or GLUTEN_FREE_YN == "Yes" or GLUTEN_FREE_YN == "Y":
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
