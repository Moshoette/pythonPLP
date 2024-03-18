def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

n = int(input("Enter the value of n: "))

fib_sequence = fibonacci_sequence(n)

print("Fibonacci sequence up to term", n, ":", fib_sequence)
