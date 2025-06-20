def power(base, exponent=2):
    result = base**exponent
    return result

# Call the function with only a base (exponent defaults to 2)
result1 = power(5)

print(f"5 raised to the power of 2 (default exponent) is:{result1}")

# Call the function with both base and exponent
result2 = power(2,4)
print (f"2 raised to the power of 4 (default exponent) is:{result2}")

result3 = power(10,3)
print (f"10 raised to the power of 3 (default exponent) is:{result3}")

