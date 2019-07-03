import pandas as pd
import os
import re

path_to_project = '/home/pavel/mercurialprojects/cdi-all/'
sheet_name = 'ADDRESS'
rubbish = "(^_)|[ #/\|?!+-]|(_$)"

regex = re.compile(rubbish, re.IGNORECASE)


def read_xlss(path):
    xls = pd.ExcelFile(path)
    if sheet_name in xls.sheet_names:
        book = pd.read_excel(xls, sheet_name=sheet_name)
        return book
    return pd.DataFrame()


def read_csvs(path):
    return pd.read_csv(path)


def clean_rubbish(word):
    while(not word == regex.sub('', word).upper()):
        word = regex.sub('', word).upper()
    return word


if __name__ == "__main__":
    addr = pd.DataFrame()
    xlss = []
    csvs = []

    for root, dirs, files in os.walk(path_to_project):
        xlss += [os.path.join(root, name) for name in files if
                 not root.__contains__('.hg') and root.__contains__('cdi-mats') and name.lower().__contains__(
                     '.xls') and not name.lower().__contains__('lock')]

    for root, dirs, files in os.walk(path_to_project):
        csvs += [os.path.join(root, name) for name in files if
                 name.lower() == 'address.csv' and root.__contains__('cdi-mats')]

    with open('xlss', 'w') as f:
        for i in xlss:
            f.write("%s\n" % i)

    with open('csvs', 'w') as f:
        for i in csvs:
            f.write("%s\n" % i)

    for name in csvs:
        df = read_csvs(name)
        for col in df.columns:
            col_cleaned = clean_rubbish(col)
            if col_cleaned not in addr.columns:
                addr[col_cleaned] = ""
        addr = pd.concat([addr, df], ignore_index=True, sort=False)

    for name in xlss:
        df = read_xlss(name)
        for col in df.columns:
            col = clean_rubbish(col)
            if col not in addr.columns:
                addr[col] = ""

        addr = pd.concat([addr, df], ignore_index=True, sort=False)

    addr = addr.drop_duplicates()
    addr.to_csv('addresses.csv', sep=';')
