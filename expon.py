def raise_power(base,power):
    result= 1
    for i in range(power):
        result=result*base
    return result
  

print(raise_power(3,2))  # Output: 8

        