import os
import xlrd
from xlutils3.copy import copy
workbook=None
wb=None
sheet=None
df=None
def copy_open(srcfile,dstfile):
    global workbook
    global wb
    global sheet
    global df
    if not os.path.isfile(srcfile):
        print(srcfile+'not exist')
        return
    if os.path.isfile(dstfile):
        print('warning'+dstfile+'file already exist')
        df=dstfile
        workbook=xlrd.open_workbook(filename=srcfile,formatting_info=True)
        wb=copy(workbook)
        sheet=wb.get_sheet('Sheet1')
        return
def write(r,c,value):
    global workbook
    global sheet
    def _getCell(sheet,r,c):
        row=sheet._Worksheet__rows.get(r)
        if not row:return None
        cell=row._Row__cells.get(c)
        return cell
    cell=_getCell(sheet,r,c)
    sheet.write(r,c,value)
    if cell:
        ncell=_getCell(sheet,r,c)
        if ncell:
            ncell.xf_idx=cell.xf_idx
    return
def save_close():
    global wb
    global df
    wb.save(df)
    return
if __name__=='__main__':
    copy_open('')
    write(3,7,'PASS')
    save_close()