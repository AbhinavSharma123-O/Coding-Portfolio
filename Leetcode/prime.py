def sieve_of_eratosthenes(n):
    # 1. vector<bool> isPrime(n+1, True);
    # In Python, we create a list of booleans.
    is_prime = [True] * (n + 1)
    
    # 2. Manually setting 0 and 1 to False
    is_prime[0] = False
    is_prime[1] = False
    
    # 3. for (int i = 2; i <= n; i++)
    # Python's range is exclusive at the end, so we use n + 1
    for i in range(2, n + 1):
        
        # 4. if (isPrime[i] == True)
        if is_prime[i]:
            
            # 5. The Inner Loop (The circled part in your image)
            # C++: for (int j = 2; i * j <= n; j++)
            # Python: We use range with a 'step'. 
            # We start at i*2, go up to n, stepping by i.
            for multiple in range(i * 2, n + 1, i):
                is_prime[multiple] = False
                
    return is_prime

# Example usage:
n = 30000
primes = sieve_of_eratosthenes(n)

# Printing the primes
for num, prime_status in enumerate(primes):
    if prime_status:
        print(num, end=" ")
