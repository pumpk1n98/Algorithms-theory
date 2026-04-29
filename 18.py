def is_subsequence(S, S_prime):
    i = 0  # указатель по S
    j = 0  # указатель по S'

    while i < len(S) and j < len(S_prime):
        if S[i] == S_prime[j]:
            j += 1
        i += 1

    return j == len(S_prime)


# пример
S = ["Amazon", "Yahoo", "eBay", "Yahoo", "Yahoo", "Oracle"]
S_prime = ["Yahoo", "eBay", "Yahoo", "Oracle"]

print(is_subsequence(S, S_prime))  # True