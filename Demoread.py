import xlrd
# workbook=None
# sheet=None
# rr=0
# r=0
# def open_excel(srcfile):
#     global workbook,sheet,r,rr
#     xlrd.Book.encoding='utf-8'
#     workbook=xlrd.open_workbook(filename=srcfile)
#     sheet=workbook.sheet_by_index(0)
#     r=sheet.nrows
#     rr=2
#     return
# def readline():
#     global sheet,rr,r
#     row=None
#     if(rr<r):
#         row=sheet.row_values(rr)
#         rr=rr+1
#     return row
# if __name__=='__main__':
#     open_excel('F:/code/OCMTEST/Loginfo/test.xlsx')
#     for i in range(0,r):
#         print(readline())


