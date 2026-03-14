#Error Handling in python#single error handing
print("\tsingle error handling:")
try:
    x = 2
    y = x * 5

    if y <= 25:
        print("The number is less than or equal to 25")

except Exception as e:
    print("Error: A character cannot be multiplied")

print()

"""
1. syntax error
2. value error 
3. indentation error
4. 
"""

# realtime example
print("\treal-time error handling:")
class Invalidsalary(Exception):
    pass


class Employee:
    def __init__(self, first, age, salary):
        self.first = first
        self.age = age

        if salary < 0:   # custom error condition
            raise Invalidsalary("Salary cannot be negative")

        self.salary = salary

    def display(self):
        print(self.first)
        print(self.age)
        print(self.salary)


try:
    details = {
        "name": "ram",
        "age": 21,
        "salary": -1000
    }

    emp = Employee(details["name"], details["age"], details["salary"])
    emp.display()

except Invalidsalary as e:
    print("Error:", e)

print()

print("\tmultiple error handling:")
try:
    x= int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    res = x / y
except Exception as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)

except TypeError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)

else:
    print(res)

finally:
    print("I am done for today..")
