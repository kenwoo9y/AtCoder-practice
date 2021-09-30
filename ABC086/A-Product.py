input_numbers = list(map(int, input().split()))
product = input_numbers[0] * input_numbers[1]

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
