n = int(input())
A = [0] * n

for i in range(n):
    A[i] = int(input())

currentNum = 1
stack = []
answer = ""
result = True

for i in range(n):
    target = A[i]
    if target >= currentNum:
        while target >= currentNum:
            stack.append(currentNum)
            currentNum += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        num = stack.pop()
        if num > target:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)