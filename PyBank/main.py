#import necassery libraries

import os
import csv 

#Define variables 
total_months = 0
total_net = 0
#initialize empty list for store the data
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
#Define the file Path
file_path = r"PyBank\Resources\budget_data.csv"

#Open and read the CVS file
with open(file_path, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter= ',')
     #skip the header row
     header = next(csvreader)

     first_row = next(csvreader)
     total_months += 1
     total_net += int(first_row[1])
     prev_net = int(first_row[1])

     for row in csvreader:
         total_months +=1
         total_net += int(row[1])

         net_change = int(row[1]) - prev_net
         prev_net = int(row[1])
         net_change_list += [net_change]
         month_of_change+=[row[0]]

         if net_change > greatest_increase[1]:
             greatest_increase[1] = net_change
             greatest_increase[0] = row[0]

         if net_change < greatest_decrease[1]:
             greatest_decrease[1] = net_change
             greatest_decrease[0] = row[0]          

net_monthly_avg = sum(net_change_list) / len(net_change_list)


print (
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Avarage Change: {net_monthly_avg:.2f}\n"
    f"Greatest increased in Profits: {greatest_increase}\n"
    f"Greatest Decreased in Profits: {greatest_decrease}\n"
)


# Define the output directory and file path
output_dir = os.path.join("PyBank", "Analysis_Bank")
output_file = os.path.join(output_dir, "results.txt")

# Ensure the directory exists
if not os.path.isdir(output_dir):
    print(f"'{output_dir}' is not a directory or does not exist. Creating it now.")
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")
else:
    print(f"'{output_dir}' is a directory.")

# Write results to the text file
try:
    with open(output_file, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total_net}\n")
        file.write(f"Average Change: ${net_monthly_avg:.2f}\n")
        file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
        print(f"Results have been written to: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
