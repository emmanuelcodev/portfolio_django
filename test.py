'''def chunks(l, n):
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
'''
class Car:
    number_wheels = 4
    _color = 'Black'
    __yearOfManufature = 2017

class Car2:
    def __init__(self):
        self.number_wheels = 4
        self._color = 'Black'
        self.__yearOfManufature = 2017


car1 = Car2()
print(car1.number_wheels)
print(car1._color)
print(car1._Car2__yearOfManufature)
print(car1.__yearOfManufature)

class BMW(Car):
    pass
