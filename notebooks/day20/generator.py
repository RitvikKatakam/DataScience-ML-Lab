#Generators: A generator is an easier way to create iterators using yield.
#Instead of returning all values at once, it produces them one by one (lazy evaluation)

def count(n):
    i =1
    while i<=n:
        yield i
        i+=1
gen = count(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#prints all the numbera upto 10
