# Readable Version of FizzBuzz

def fizzbuzz(num):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    return output or num

for num in range(1, 101):
    print(fizzbuzz(num))
