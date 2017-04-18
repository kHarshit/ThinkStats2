import nsfg

df = nsfg.ReadFemPreg()
print(df.columns)
print(df.columns[1])
print(df['pregordr'])  # pandas series
print(df.outcome.value_counts(sort=False))  # sort=False doesn’t sort the Series by values, so them appear in order.
