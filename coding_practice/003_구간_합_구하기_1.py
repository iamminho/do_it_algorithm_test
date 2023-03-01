def make_sum_numbers(input_numbers):
    temp = 0
    prefix_sum = [0]
    for num in input_numbers:
        temp += num
        prefix_sum.append(temp)
    return prefix_sum

input_number, quiz_number = map(int, input("N과 M을 입력해 주세요.\n").split())
numbers = list(map(int, input("배열을 입력해 주세요.\n").split()))
sumNumbers = make_sum_numbers(numbers)

for i in range(quiz_number):
    start, end = map(int, input("합을 구할 인덱스의 숫자를 입력해 주세요> \n").split())
    print(sumNumbers[end] - sumNumbers[start - 1])







