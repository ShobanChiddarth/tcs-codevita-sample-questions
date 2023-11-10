# Square Free Numbers

def full_factors(number: int) -> list[int]:
    if not isinstance(number, int):
        raise TypeError("number must be int")
    factors=[]
    for n in range(1, int(number/2)+1):
        if number%n==0:
            factors.append(n)
    factors.append(number)
    return factors


def prime_factors(number: int) -> list[int]:
    """Returns a list of prime factors of `number` without 1

Source: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/"""
    if not isinstance(number, int):
        raise TypeError("number must be int")
    prime_factors=[]

    number_copy=number
    while number_copy%2==0:
        prime_factors.append(2)
        number_copy = int(number_copy/2)
    
    for ii in range(3, int(number_copy**(1/2))+1, 2):

        while number_copy%ii == 0:
            prime_factors.append(ii)
            number_copy = int(number_copy/ii)
    
    if number_copy>2:
        prime_factors.append(number_copy)
    
    return prime_factors


def frequence_counter(l: list)-> dict:
    """Source: https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/"""
    freq = {}
    for item in l:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def square_free(number: int) -> int:
    "Returns how many square free numbers divide the given `number"
    if isinstance(number, int):
        raise TypeError("number must be int")
    
    factors = full_factors(number)
    while 1 in factors:
        factors.remove(1)

    l_prime_fs = []
    for item in factors:
        l_prime_fs.append(prime_factors(item))
    

    repeated_count = 0
    for thing in l_prime_fs:
        
        frequency_count = frequence_counter(thing)
        for key in frequency_count:
            if frequency_count[key]>1:
                repeated_count+=1
                break

    return len(l_prime_fs)-repeated_count

print(square_free(72))
