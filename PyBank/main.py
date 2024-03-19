import os
import csv

output_path = os.path.join('Resources','budget_data.csv')
net_change_list = []
greatest_inc = ["",0]
greatest_dec = ["", 99999999999999]

with open(output_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    first_row = next(csv_reader)

    #print(f"CSV Header: {csv_header}")
    #print(type(csv_header))

    prev_net = int(first_row[1])

    counter = 1
    val = int(first_row[1])

    for row in csv_reader:
        counter = counter + 1
        val = val + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change

        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

    print('Financial Analysis')
    print('----------------------------')
# 1. total number of months included in dataset
    print(f'Total Months: {counter}')
# 2. net total amount of profit/losses over the entire period
    print(f'Total: ${val}')
# 3. changes in profit/losses over the entire period, and then the average of those changes
    print(f'Average Change: ${round(sum(net_change_list)/(counter-1),2)}')
# 4. greatest increase in profits (date and amount) over the entire period
    print(f'Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})')
# 5. greatest decrease in profits (date and amount) over the entire period
    print(f'Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})')
# 6. file export
output_path = os.path.join('analysis','financial analysis.txt')
with open(output_path,'w') as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(f'Total Months: {counter}')
    f.write('\n')
    f.write(f'Total: ${val}')
    f.write('\n')
    f.write(f'Average Change: ${round(sum(net_change_list)/(counter-1),2)}')
    f.write('\n')
    f.write(f'Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})')
    f.write('\n')
    f.write(f'Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})')
    f.close()