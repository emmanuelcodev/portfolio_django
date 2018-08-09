def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
y = []
for x in range(1,100):
    y.append(x)

for x in chunks(y, 2):
    print(x[0])
rand_list = []
print('last try')
for i in range(1, 7, 2):
    rand_list.append(i)
print(rand_list)
