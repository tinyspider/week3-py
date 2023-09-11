import csv

pybank_path = '.\Resources\\budget_data.csv'
output_path = '.\\analysis\output.txt'

#open csv file
with open(pybank_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    month_count = 0
    month_previous = ''
    month_current = ''
    i = 0
    total = 0.0
    profit_list = []
    month_list = []
    for row in csv_reader:
        #skip header
        if i > 0 :
            #find total $
            total = total + float(row[1])
            #find total month
            month_current = row[0]
            if (month_current != month_previous):
                month_count = month_count +1
            #create lists for data processing
            month_list.append(row[0])
            profit_list.append(float(row[1]))
        i = i + 1
    # get change_list from raw monthly data
    change_list = []   
    for j in range(1,len(profit_list)):
        change_list.append((profit_list[j]-profit_list[j-1]))
    #get max change
    change_max = max(change_list)
    # raw month i = change_i + 1
    change_max_i = change_list.index(change_max)+1
    change_max_month = month_list[change_max_i]
    #get min change
    change_min = min(change_list)
    # raw month i = change_i + 1
    change_min_i = change_list.index(change_min)+1
    change_min_month = month_list[change_min_i]
    total_change = sum(change_list)
    change_average = round((total_change / len(change_list)),2)
    #output to file
    with open(output_path, 'w') as f:
        #format string for output
        output = f'''Financial Analysis \n
---------------------------- \n
Total Months: {month_count}
Total : {total}
Average Change: $ {change_average}
Greatest Increase in Profits: {change_max_month} (${change_max})
Greatest Decrease in Profits: {change_min_month} (${change_min})
                 '''
        print(output)
        f.write(output)


        


