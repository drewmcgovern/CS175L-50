#Andrew McGovern
#CS 175L 50
#expensesPieChart

# This program displays a pie chart of expenses.
import matplotlib.pyplot as plt

def main():
    # Open the file with the expenses and categories
    expense_file = open("expenses.txt","r")
    # Declare the lists for the categories and amounts
    categories_list = []
    amounts_list = []
    
    # Write a for loop that breaks up each line in a file
    # and then separates the categories and amounts into lists
    for line in expense_file:
        line_list = line.split("\t")
        categories_list.append(line_list[0])
        amounts_list.append(line_list[1])
        
    # Close the file
    expense_file.close()
    
    # Build the line graph.
    plt.pie(amounts_list, labels=categories_list,
            colors=('r','y','g','c','b','m'))
    # Add a title.
    plt.title('Expenses Last Month')

    # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()
