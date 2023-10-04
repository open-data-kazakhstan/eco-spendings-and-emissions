import xlrd
import csv

# Specify the path to your XLS file "C:\Users\USER\Downloads\eco.xls"
xls_file_path = r"C:\Users\USER\Downloads\eco.xls"
# Specify the path where you want to save the CSV file
csv_file_path = r'C:\Users\USER\Desktop\Data\practice\eco.csv'

# Open the XLS file for reading
workbook = xlrd.open_workbook(xls_file_path)

# Select the first sheet in the workbook
sheet = workbook.sheet_by_index(0)

# Extract the header row (third row in the sheet)
header = sheet.row_values(2)

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the extracted header row to the CSV file
    csv_writer.writerow(header)
    
    # Iterate through rows in the sheet starting from the fourth row (index 3)
    for row_idx in range(3, sheet.nrows):
        csv_writer.writerow(sheet.row_values(row_idx))