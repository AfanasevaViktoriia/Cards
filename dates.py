import pandas as pd
from datetime import datetime

xls = '/home/pavel/export.xls'

df1 = pd.read_excel(xls, sheet_name='CDI_PAVELE_OPEN.MERGED')
df2 = pd.read_excel(xls, sheet_name='CDI_PAVELE_OPEN.PHYSICAL_PARTY')
df3 = pd.read_excel(xls, sheet_name='CDI_PAVELE_OPEN.DUPLICATE')


def convert(col):
    for i in range(col.values.shape[0]):
        row = col.values[i]
        format = "%d-%b-%y %H.%M.%S.%f000 %p"
        if str(row) != 'nan':
            col.values[i] = datetime.strptime(str(row), format).strftime("%Y-%m-%d %H:%M:%S")
            pass


convert(df1.CREATED)
convert(df2.STARTDATE)
convert(df2.ENDDATE)
convert(df2.ACTUALITY_DATE)
convert(df3.STARTDATE)
convert(df3.ENDDATE)

ew = pd.ExcelWriter('out.xls')

df1.to_excel(ew,sheet_name='CDI_PAVELE_OPEN.MERGED')
df2.to_excel(ew,sheet_name='CDI_PAVELE_OPEN.PHYSICAL_PARTY')
df3.to_excel(ew,sheet_name='CDI_PAVELE_OPEN.DUPLICATE')

ew.save()