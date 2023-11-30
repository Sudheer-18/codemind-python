n = input()
rev = ''
wrds = n.split(' ')
for i in range(len(wrds)-1, -1, -1):
    for j in range(len(wrds[i])-1, -1, -1):  # Fix the range
        rev += wrds[i][j]  # Access characters using wrds[i][j]
    print(rev, end=' ')
    rev = ''  # Reset rev for each word
