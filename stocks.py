#CS175L-50
#Andrew McGovern
#Stocks

#Ask the user to input the amount of shares they bought,
#the commission rate for the broker,
#the price they bought the shares at,
#and the price they sold the shares at
COMMISSION_RATE = float(input("What was the commission rate?: "))
SHARES = int(input("How many shares did you purchase?: "))
PURCHASE_PRICE = float(input("What price did you purchase the shares for?: $"))
SELLING_PRICE = float(input("What price did you sell the shares for?: $"))

#Calculate the total amount to purchase the stocks
totalPurchasePrice = SHARES * PURCHASE_PRICE
#Calculate the total amount of commission on the purchase
totalCommishAtBuy = totalPurchasePrice * COMMISSION_RATE
#Calculate the total amount on selling the stocks
totalSellingPrice = SHARES * SELLING_PRICE
#Calculate the total amount of commission on the sale
totalCommishAtSell = totalSellingPrice * COMMISSION_RATE
#Calculate the total commission paid for purchase and sale
totalCommishPaid = totalCommishAtBuy + totalCommishAtSell
#Calculate the total profit
totalProfit = (totalSellingPrice - totalPurchasePrice) - totalCommishPaid

#Output amount paid, amount sold for, commission paid on purchase and on sale,
#total commission paid, and profit
print(f'Amount paid for stocks: ${totalPurchasePrice:,.2f}')
print(f'Commission paid on the purchase: ${totalCommishAtBuy:,.2f}')
print(f'Amount the stocks sold for: ${totalSellingPrice:,.2f}')
print(f'Commission paid on the sale: ${totalCommishAtSell:,.2f}')
print(f'Total commission paid: ${totalCommishPaid:,.2f}')
print(f'Profit (or loss if negative): ${totalProfit:,.2f}')
