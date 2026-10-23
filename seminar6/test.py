def functions(*args):

functions(1, 2, 3, 'ssd')

def functions(**kwargs):


functions(a = 'a', b = 'b', c = 1)


sum = lambda x, y: x + y

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))

def even_fn(x):
    return x % 2 == 0
print(list(filter(even_fn, numbers)))

print(list(filter(lambda x: x % 2 == 0, numbers)))