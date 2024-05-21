# My Prime Number Checker
# =======================
#
# This script checks if a given number is prime.

# It uses a simple calculation to check

#Author: Ibrahim Yisau
# Date: 21-May-2024

def is_prime(n):  # Define a function to check if a number is prime
# Check if the number is less than or equal to 1
if n <= 1:
return False  # It's not prime

# Check if the number is less than or equal to 3
elif n <= 3:
	return True  # It's prime (2 and 3 are the only primes less than 4)

# Check if the number is divisible by 2 or 3
elif n % 2 == 0 or n % 3 == 0:
	return False  # It's not prime

# Start checking from 5
i = 5

# Loop until i squared is less than or equal to n
while i * i <= n:
	# Check if the number is divisible by i or i+2
	if n % i == 0 or n % (i + 2) == 0:
		return False  # It's not prime
	
	# Increment i by 6 (since all primes are of the form 6k +- 1)
	i += 6

# If the number passes all checks, it's prime
return True

#Ask the user for a number
prime_input = int(input("Enter a number: "))

#Check if the input number is prime
if is_prime(prime_input):
# If it's prime, print a message
print("The input is a prime number")
else:
# If it's not prime, print a different message
print("The input is not a prime number")
