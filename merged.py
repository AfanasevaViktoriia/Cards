import pandas as pd
import os
from operator import methodcaller

path_to_project = '/home/pavel/mercurialprojects/cdi-all/'
sheet_name = 'MERGED'


def check_trans(xls):
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # map(methodcaller("upper"), df.columns)
    df.columns = map(methodcaller("upper"), df.columns)
    if df.shape[0] > 0 \
            and 'TRANSITIONAL' in df.columns \
            and not df[df['TRANSITIONAL'] == 1].empty:
        return True
    else:
        return False


if __name__ == "__main__":
    xlss = []

    with open('merged_xlss_tr', 'w') as f:
        for root, dirs, files in os.walk(path_to_project):
            for name in files:
                if not root.__contains__('.hg') \
                        and name.lower().__contains__('dbstart.xls') \
                        and not name.lower().__contains__('lock'):
                    path = os.path.join(root, name)
                    xls = pd.ExcelFile(path)
                    # has merged
                    if sheet_name in xls.sheet_names:
                        if check_trans(xls):
                            xlss.append(path)
                            f.write("%s\n" % path)


            # and 'HID_DIRECT_SCION' in df.columns \
            # and 'HID_FINAL_SCION' in df.columns \
            # and df[df['HID_DIRECT_SCION'] == df['HID_FINAL_SCION']].empty: