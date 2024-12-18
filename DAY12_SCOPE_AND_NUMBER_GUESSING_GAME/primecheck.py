def is_prime(num):
      if num <= 1:
        prime = False
      for i in range(2, int(num**.5) +1):
          if num % i == 0:
              prime = False
      prime = True
      return(prime)
      """
      if (num % 1 == 0) and (num % num == 0):
          for range(2, int(num**.5) +1)
              prime = False
          else:
               prime = True
      else:
          prime = False
      return prime
     """
print(is_prime(75))