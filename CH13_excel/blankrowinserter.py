import openpyxl
import sys

def main():
    if len(sys.argv) < 4:
        sys.exit("Incorrect number of command line arguments")
    row_to_start = int(sys.argv[1])
    num_rows_to_insert = int(sys.argv[2])

    wb_name = sys.argv[3]
    print(row_to_start, num_rows_to_insert, wb_name, sep = '\n')
    wb = openpyxl.load_workbook(wb_name)
    sheet = wb.active
    for i in range(num_rows_to_insert):
        sheet.insert_rows(row_to_start + i)
    wb.save(wb_name)

main()