#Iterator :An iterator is an object that lets you loop through data one item at a time.
#iterator must implement two special methods: _iter() and __next_().

my_list = [2,4,6,8,10]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("\n")
print("new example :")

class Count:
    def __init__(self, max):
        self.max = max
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.max:
            val = self.count
            self.count += 1
            return val
        else:
            raise StopIteration

for i in Count(3):
    print(i)