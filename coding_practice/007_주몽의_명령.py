n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
left_idx = 0
right_idx = n - 1

while left_idx < right_idx:
    if arr[left_idx] + arr[right_idx] < m:
        left_idx += 1
    elif arr[left_idx] + arr[right_idx] == m:
        count += 1
        left_idx += 1
        right_idx -= 1
    else:
        right_idx -= 1

print(count)