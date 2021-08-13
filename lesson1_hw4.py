prompt_msg = "Please enter any whole positive number: "
num = input(prompt_msg)

while not num.isdigit():
    print("Incorrect value")
    num = input(prompt_msg)

num = int(num)
a = 0

while num > 0:
    n = num % 10
    if n > a:
        a = n
        if a == 9:
            break
    num = num // 10

print(f"The greatest digit is {a}")
