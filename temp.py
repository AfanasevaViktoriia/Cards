import pandas as pd
import os

path_to_project = '/home/pavel/mercurialprojects/cdi-all/'
sheet_name = 'ADDRESS'


def read_xlss(path):
    xls = pd.ExcelFile(path)
    if sheet_name in xls.sheet_names:
        book = pd.read_excel(xls, sheet_name=sheet_name)
        return book
    return pd.DataFrame()


def read_csvs(path):
    return pd.read_csv(path)


if __name__ == "__main__":
    addr = pd.DataFrame()
    xlss = []
    csvs = []

    for root, dirs, files in os.walk(path_to_project):
        xlss += [os.path.join(root, name) for name in files if
                 not root.__contains__('.hg') and root.__contains__('cdi-mats') and name.lower().__contains__('.xls')]

    with open('xlss', 'w') as f:
        for i in xlss:
            f.write("%s\n" % i)

    for root, dirs, files in os.walk(path_to_project):
        csvs += [os.path.join(root, name) for name in files if
                 name.lower() == 'address.csv' and root.__contains__('cdi-mats')]

    with open('csvs', 'w') as f:
        for i in csvs:
            f.write("%s\n" % i)

    for name in csvs:
        df = read_csvs(name)
        for col in df.columns:
            if col not in addr.columns:
                addr[col] = ""
        addr = pd.concat([addr, df], ignore_index=True, sort=False)

    for name in xlss:
        df = read_xlss(name)
        for col in df.columns:
            if col not in addr.columns:
                addr[col] = ""

        with open('debug', 'w') as d:
            d.write(name)

        addr = pd.concat([addr, df], ignore_index=True, sort=False)

    addr = addr.drop_duplicates()
    addr.to_csv('addresses.csv', sep=';')
