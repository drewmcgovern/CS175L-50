#Andrew McGovern
#CS 175L 50
#AverageFromInput with exceptions

def main():
    #Try to open and read the file
    try:
        #Open the numbers.txt for reading
        num_file = open('numbers.txt','r')
        
        x = 0 #Line number
        total = 0 #Initializing total counter for average
        
        #Read the lines from the file
        for line in num_file:
            #Add to the line counter
            x = x+1
            #Convert line to a float
            amount = float(line)
            #Add amount to the total for the average
            total = total + amount
            #Print out console output
            print(f"I read in {x} number(s)     "
                  f"Current number is: {amount:.1f}     "
                  f"Total is: {total:.1f}")
        #Close the file
        num_file.close()

        #Calculate and print the final average
        average = total / x
        print(f"Average: {average:.1f}")
        
    #If the file cannot be found        
    except IOError:
        print("ERROR: File could not be found.")

    #If the file does not have valid numbers
    except ValueError:
        print("ERROR: Detected a non-valid number.")
        
    
#Call the main function
if __name__ == '__main__':
    main()
