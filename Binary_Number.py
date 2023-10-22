n = int(input())# Length of the binary strings

for i in range(2**n):
    binary_str = bin(i)[2:].zfill(n)  # Convert to binary and zero-fill
    print(binary_str)
