# FizzBuzz с list comprehensions
fizzbuzz = ['fizzbuzz'
            if v%3 == 0 and v%5 == 0
            else 'fizz' if v % 3 == 0
else 'buzz' if v % 5 == 0
else v for v in range(1, 51)]
print(fizzbuzz)