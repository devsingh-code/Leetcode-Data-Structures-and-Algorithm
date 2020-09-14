'''
204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for multiples_of_i in range(i*i,n,i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)