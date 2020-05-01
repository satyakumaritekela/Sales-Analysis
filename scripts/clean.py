from csv import writer
from csv import reader
import re

# open the input_file in read mode and output_file in write mode
with open('file.csv', 'r') as read_obj, \
        open('file_1.csv', 'wb') as write_obj:
    isFirstRow = False
    csv_reader = reader(read_obj)  # creating a csv.reader object from the input file object
    csv_writer = writer(write_obj)  # Creating a csv.writer object from the output file object

    # Read each row of the input csv file as list
    for row in csv_reader:
        if not isFirstRow:  # append the default text in the row / list
            isFirstRow = True
            row.append('ADDRESSLINE')  # append the newly created column
        else:
            row.append(re.sub(r'[^a-zA-Z0-9\s\.]+', '', ' '.join([row[14], row[15]]))) # merging columns address line 1 & address line 2 and also cleaning address line at the same time
        del (row[15], row[14])  # deleting address line 2 an 1
        csv_writer.writerow(row)  # writing the updated row / list to the output file
print("File created")
