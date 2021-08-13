prompt_msg = "Enter any number: "
number = input(prompt_msg)

while not number.isdigit():
    print("Please enter valid positive number")
    number = input(prompt_msg)

result = int(number) + int(number * 2) + int(number * 3)
print(f"{number} + {number * 2} + {number * 3} = {result}")
