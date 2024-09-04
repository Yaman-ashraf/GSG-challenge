def fibonacci(n):
    seq = [0, 1]
    
    while len(seq) < n:
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)
    
    return seq

print("Fibonacci sequence:", fibonacci(11))
