# (x ∈ Q) → (((x ∈ P) ≡ (x ∈ Q)) ∨ (¬(x ∈ P) → (x ∈ A))
def k(x, A):
    Q = list(range(77, 115))
    P = list(range(69, 92))
    return (x in Q) <= (((x in P) == (x in Q)) or (x not in P) <= (x in A))
lst = []
for A in range(1000):
    if all(k(x, list(range(A))) for x in range(1000)):
        lst.append(A)

print(lst)