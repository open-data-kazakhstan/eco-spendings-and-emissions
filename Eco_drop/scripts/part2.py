import xlrd
import csv


xls_file_path = r"C:\Users\USER\Downloads\part2.xls"

csv_file_path = r'C:\Users\USER\Desktop\project 1_part2\part2.csv'


workbook = xlrd.open_workbook(xls_file_path)


sheet = workbook.sheet_by_index(0)

header = sheet.row_values(2)

with open(csv_file_path, 'w', newline='',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    
    csv_writer.writerow(header)
    
    for row_idx in range(3, sheet.nrows):
        csv_writer.writerow(sheet.row_values(row_idx))