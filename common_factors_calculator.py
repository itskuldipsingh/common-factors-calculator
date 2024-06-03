import math

def find_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors

def find_common_factors(numbers):
    common_factors = find_factors(numbers[0]
    for number in numbers[1:]:
        common_factors &= find_factors(number)
    return sorted(common_factors)

b_values = []

for a in range(1, 999):
    b = a * 1001
    b_values.append(b)

# Print all b values separated by tabs
print('\t'.join(f"{b:06d}" for b in b_values))

common_factors = find_common_factors(b_values)
print("Common factors:", common_factors)

