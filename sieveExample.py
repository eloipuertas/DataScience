
# coding: utf-8

# ##Sieve of Eratosthenes

# In[1]:

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) / 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) / si)
    return [2] + [el for el in sieve if el]


# In[2]:

print sieveOfEratosthenes(1000)


# In[ ]:



