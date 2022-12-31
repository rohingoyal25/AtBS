import openpyxl

def main():
    PRICE_UPDATE = {"Celery": 1.19,
                    "Garlic": 3.07,
                    "Lemon": 1.27}

    wb = openpyxl.load_workbook('produceSales.xlsx')
    sheet = wb['Sheet']

    for row in range(2, sheet.max_row + 1):
        produce = sheet['A' + str(row)].value
        if produce in PRICE_UPDATE:
            sheet['B' + str(row)] = PRICE_UPDATE[produce]

    wb.save('produceSales_copy.xlsx')

main()