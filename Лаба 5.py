import timeit
from itertools import product
def algorithmic_method(K):
    result = ['']     
    for _ in range(K):  
        result = [num + d for num in result for d in '1357']
    return result
        
def python_method(K):
    return [''.join(p) for p in product('1357', repeat=K)]

K = 3 
print("Алгоритмический метод:", algorithmic_method(K)[:10])  
print("Метод с itertools:", python_method(K)[:10])

print("\nСравнение скорости:")
print("Алгоритмический:", timeit.timeit(lambda: algorithmic_method(K), number=1000), " itertools:", timeit.timeit(lambda: python_method(K), number=1000))

def optimized_method(K, max_sum):
    nums = [(''.join(p), sum(int(d) for d in p)) for p in product('17', repeat=K) if sum(int(d) for d in p) <= max_sum]
    print(nums)
    return max(nums, key=lambda x: x[1]) if nums else None


K, max_sum = 3, 12
optimal = optimized_method(K, max_sum)

print(f"\nОптимальное: {optimal[0]} (сумма: {optimal[1]})" if optimal else "Нет чисел")

