from datetime import datetime
from csv import writer
from csv import reader

with open('sales_data_sample.csv', 'r') as read_obj,\
        open('file.csv', 'wb') as write_obj:
    isFirstRow = False
    csv_reader = reader(read_obj) # creating a csv.reader object from the input file object
    csv_writer = writer(write_obj) # Creating a csv.writer object from the output file object
# Read each row of the input csv file as a list
    for row in csv_reader:
        if not isFirstRow:  # append the default text in the row / list
            isFirstRow = True
            row.append('ORDERDATE')		# appending the header row
        else:
            row.append((datetime.strptime(row[5], '%m/%d/%Y %H:%M')).strftime('%m/%d/%Y'))  # appending new date values
        del [row[5]]  # deleting the old date column
        csv_writer.writerow(row)  # writing the rest of the rows in output file
print("Completed")