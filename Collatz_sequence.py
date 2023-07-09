def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
        else:  
            n = 3 * n + 1
        sequence.append(n) 
    return sequence
num = int(input("Enter a number: "))
result = collatz_sequence(num)
print(' '.join(map(str, result)))