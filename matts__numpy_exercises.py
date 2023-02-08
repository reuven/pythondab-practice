# Exercise 1

a = np.random.randint(0, 100, 10)

a.mean()

a.std()

b = random.randint(0, 100, 10)

c = (a+b)/2

d = random.rand(10) *100

d.mean()

d.std()

d.min()

d.max()


# Exercise 2

a = random.randint(0,100,20)
a[a%2==0].max()

a[a%2==1].mean()

b = np.array([a[a%2==1][0], a[a%2==1][-1]])

c = np.random.rand(20)
c[c<c.mean()]

c[c<c.std()]



# Exercise 3

a = np.random.randint(0,100,20)
a[(a%2==0) & (a>a.mean())].min()

a[(a<a.mean()-a.std()) | (a>a.mean()+a.std())]

a[((a%2==1) & (a<a.mean())) | ((a%2==0) & (a>a.mean()))]



# Exercise 4

a = np.random.randint(0,100,40)
print(f'Mean = {a.mean()}, std = {a.std()}')
a[(a>=a.mean()-a.std()) & (a<=a.mean()+a.std())] = a.mean()
print(f'Mean = {a.mean()}, std = {a.std()}')

b = np.random.randint(0,100,10)
b[np.arange(0,10,2)] = b[np.arange(1,10,2)]



# Exercise 5

a = np.random.randint(0, 100, 10)
a.mean()

b = random.rand(a.mean().astype(np.int64))
b[(b<b.mean()-b.std()) | (b>b.mean()+b.std())] = b.mean()
b

a = np.random.rand(20) * 100
a[a.astype(np.int64)%2 == 0] = a.mean()
a


# Exercise 6

a = np.random.randint(0, 1000, 30)
a = a.astype(float64)
a[(a<a.mean()-a.std()) | (a>a.mean()+a.std())] = np.nan
a[np.isnan(a)] = a[~np.isnan(a)].mean()
a