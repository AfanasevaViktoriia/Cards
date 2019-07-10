import pandas as pd

geoid = pd.read_csv('BY_gaz.txt', sep='\t', header=None)
postal = pd.read_csv('BY_coord.txt', sep='\t', header=None)
altern = pd.read_csv('altern.txt', sep='\t', header=None)

# alter = pd.read_csv('alternateNames.txt', sep='\t', header=None)
# df = alter[alter[1].isin(geoid[0])]
# df.to_csv('altern.txt', sep='\t', header=None)

if __name__ == '__main__':
    geoid = geoid.iloc[:, [0, 1, 3, 4, 5, 14]]
    geoid.columns = ['id', 'name', 'names', 'lat', 'lon', 'pop']
    geoid = geoid[geoid['pop'] != 0]

    altern = altern.iloc[:, [2, 4]]
    altern.columns = ['gid', 'altname']

    postal = postal.iloc[:, [1, 2, 9, 10]]
    postal.columns = ['postal', 'nname', 'latt', 'long']
    postal.postal = postal.postal.astype(str)
    ser = postal.groupby(['nname', 'latt', 'long']).agg({'postal': lambda x: ', '.join(x)})
#    print(ser)

    df = pd.merge(left=geoid, right=altern, how='left', left_on='id', right_on='gid')
    df = df.drop_duplicates()
    print(df)

    final = pd.merge(left=df, right=ser, how='inner', left_on='name', right_on='nname')
    final = final.sort_values('pop', ascending=False)

    print(final.head(50))
    final = final.loc[:, ['id', 'nname', 'name', 'postal', 'latt', 'long', 'pop']]
    print(final.head(50))

#    print(final.head(20).values)
