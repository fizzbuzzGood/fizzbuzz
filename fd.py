# print "Fizz" if multiples of 3

def fizzbuzz(n):
	if n % 3 == 0 and n % 5 == 0:
		return "FizzBuzz"
	elif n % 3 == 0:
		return "Fizz"
	elif n % 5 == 0:
		return "Buzz"
	else:
		return str(n)

for i in range(1, 31):
	print(fizzbuzz(i))
