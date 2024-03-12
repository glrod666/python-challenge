import csv
import os

# Define the path to the dataset
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
prev_month_profit_loss = None # Initialize as None for the first iteration check
month_of_change = []
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) # Skip the header

    for row in csvreader:
# Count the total months
        total_months += 1
# Calculate the total profit/loss
        total_profit_loss += int(row[1])

# Calculate the monthly change in profit/loss
    if prev_month_profit_loss is not None:
        monthly_change = int(row[1]) - prev_month_profit_loss
        profit_loss_changes.append(monthly_change)
        month_of_change.append(row[0])

# Calculate the greatest increase
        if monthly_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
        greatest_increase[1] = monthly_change

# Calculate the greatest decrease
        if monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
        greatest_decrease[1] = monthly_change

        prev_month_profit_loss = int(row[1])

# Calculate the average change in Profit/Losses over the entire period
if len(profit_loss_changes) > 0:
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
else:
    average_change = 0

# Generate output summary
output = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit_loss}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to the terminal
print(output)

# Export the results to a text file
output_file = os.path.join('analysis', 'financial_analysis.txt')
with open(output_file, "w") as txt_file:
    txt_file.write(output)