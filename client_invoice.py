# Q7: Daily Transaction Processor

# A shop records transaction amounts one by one during the day.

# Exact requirements
# Start these values at 0:
# Repeatedly ask the user to enter a transaction amount.
# When the user enters -1:
# stop taking transactions;
# do not add -1 to any count or total.
# When the entered amount is 0 or less than 0—except -1:
# print Invalid transaction;
# skip the remaining processing for that amount.
# When the amount is greater than 5000:
# print Transaction sent for manual approval;
# increase rejected_transactions by 1;
# do not add it to total_sales.
# For every amount from 1 to 5000:
# add it to total_sales;
# increase successful_transactions by 1;
# print Transaction completed.
# After the user enters -1, print:
# Total sales:
# Successful transactions:
# Rejected transactions:
# Average successful transaction:
# Calculate the average only when at least one transaction was successful. Otherwise, print:
# Average successful transaction: 0

total_sales = 0
successful_transactions = 0
rejected_transactions = 0

while True:
    shop_record = int(input("Enter transaction amounts one by one during the day:"))

    if shop_record == -1:
        print("Total sales:",total_sales)
        print("Successful transactions:",successful_transactions)
        print("Rejected transactions:",rejected_transactions)
        if successful_transactions >= 1:
            average_successful_transaction = total_sales / successful_transactions
            print("Avrage Successful Transactions:",average_successful_transaction)
        else:
            avrage_successful_transactions = 0
            print("Avrage Successful Transactions:",avrage_successful_transactions)
        break

    elif shop_record <= 0:
        print("Invalid transaction")
        continue
    
    elif shop_record > 5000:
        print("Transaction sent for manual approval")
        rejected_transactions += 1
    
    else:
        total_sales = total_sales + shop_record
        successful_transactions += 1
        print("Transaction completed.")
