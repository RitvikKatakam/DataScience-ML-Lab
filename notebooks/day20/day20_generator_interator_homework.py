"""Even Numbers Iterator
Create an iterator that:
Returns only even numbers up to a given limit
"""
class Even_Numbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current < self.limit:
            return self.current
        else:
            raise StopIteration

even_no = Even_Numbers(10)
for i in even_no:
    print(i)

print("\n new question now:")
"""
Fibonacci Generator
Create a generator that:
Yields Fibonacci numbers up to N terms
"""

def fibo(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1

for i in fibo(10):
    print(i)