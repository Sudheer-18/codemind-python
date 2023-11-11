n = int(input())
arr = list(map(int, input().split()))

el = []

from collections import Counter
count_dict = Counter(arr)
for key, value in count_dict.items():
    if key == value:
        el.append(key)

if len(el) == 0:
    print(-1)
else:
    print(*el)
