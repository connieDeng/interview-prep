def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """

    isPrimeArr = [True for x in range(n)]
    print(isPrimeArr)
    
    for i in range(2, (i * i)):
        if(isPrimeArr):
            for j in range(i, (j*i)):
                isPrimeArr[i*j] = False

    primeCount = 0
    for k in range(len(isPrimeArr)):
        if isPrimeArr[k]:
            primeCount += 1
    
    return primeCount

#   following solutions gave a runtime error
#     numPrime = 0
#     for i in range(2, n):
#         if (isPrime(i)):
#             numPrime += 1

#     return numPrime

# def isPrime(n):
#     if n == 2 or n == 3:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         digArr = []
#         tempN = n
#         sumOfDig = 0
#         while tempN > 0:
#             digArr.append(tempN % 10)
#             tempN = int(tempN/10)
#         for i in range(len(digArr)):
#             sumOfDig += digArr[i]
        
#         if sumOfDig % 3 == 0:
#             return False

#         for j in range(2, n):
#             if n % j == 0:
#                 return False
            
#         return True
    
num = 123
print(countPrimes(num))

""" 
comments
I'll be using this place to type out thought process...

- anything ending in 0,2,4,7 not prime
- numbers whose digits add up /3 not prime
	- ex: 123: digits = 6 % 3 == 0 NOT PRIME

SCRAP
- initialize boolean where all is true
- according to leetCode 0 & 1 are NOT PRIME
	- meaning 2 is the first prime num
- ANY non-prime number will always have a factor that <=
its square root
	- ex: 36
	- factors:  1*36, 2*18, 3*12, 4*9, 6*6
	- all have a num/factor <= 6
	- we can eliminate the non-prime numbers up to n
	- current int squared is less than the value of n
	- Intuition behind solution: Initially consider
 all numbers as prime. Continuously
 iterate through numbers 2 - n and if the
 current number is prime, iterate through
 all numbers from the current number, i,
 up to i * i marking multiples of that numbers
 as not prime. Once the outer loop terminates,
 count the number of remaining true values in the
 array as though are the number of prime numbers
 """