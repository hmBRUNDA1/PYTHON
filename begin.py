from collections import Counter

# 1. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

# 2. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 3. Find the most frequent element in a list
def most_frequent(lst):
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]

# Example usage
print(are_anagrams("listen", "silent"))   # True
print(is_prime(29))                        # True
print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  # 3
