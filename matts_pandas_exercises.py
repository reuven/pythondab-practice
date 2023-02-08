# Exercise 1

np.random.seed(1)
s = Series(np.random.randint(0,100,10),
          index=list('abcdefghij'))
s.loc['b']

s.loc[['c','d','f']]

s.loc[['a','e','g','h']].mean()

s.iloc[np.arange(0,len(s))%2==0].mean()

s[s%2==0].mean()

s1 = s.loc['a':'e']
s2 = s.loc['f':'j']
s2.index=list('abcde')

s1

s1+s2