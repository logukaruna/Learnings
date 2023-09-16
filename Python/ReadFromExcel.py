import xlrd

loc =("D:\\Programming\\Python\\NewBook.xlsx")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0,1))