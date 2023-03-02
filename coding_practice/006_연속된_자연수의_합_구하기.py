n = int(input())
sum = 1
count = 1
start_idx = 1
end_idx = 1

while end_idx != n:
    if sum > n:
        sum -= start_idx
        start_idx += 1
    elif sum == n:
        print(start_idx, end_idx)
        count += 1
        end_idx += 1
        sum += end_idx
    else:
        end_idx += 1
        sum += end_idx

print(count)

