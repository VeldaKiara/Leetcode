'''
0 and 1 are not primes
number in itself 
array of primes for, index number will rep values of numbers
sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2.


'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        prime_numbers = [1]*n
        prime_numbers[0] = 0
        prime_numbers[1] = 0
        
        #start at number 2
        i = 2
        while i < n:
            temporary = i
            #check multiples, if marked as true
            if prime_numbers[i]:
                temporary += i
                while temporary < n:
                    prime_numbers[temporary] = 0
                    temporary += i
                    
            i += 1
        return sum(prime_numbers)
            
                
        
        
        