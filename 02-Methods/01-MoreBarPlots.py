dict = {'values':[10,20], 'names':['A','B']}
df = pd.DataFrame(dict)

p = Bar(df, 'names', values='values', title="test chart")
