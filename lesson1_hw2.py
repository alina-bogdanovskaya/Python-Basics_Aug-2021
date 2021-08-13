prompt_msg = "Enter time in seconds: "
sec_input = input(prompt_msg)

while not sec_input.isdigit():
    print("Please enter valid positive numeric value")
    sec_input = input(prompt_msg)

sec_input = int(sec_input)

seconds = sec_input % 60
minutes = sec_input // 60
hours = minutes // 60
minutes = (sec_input // 60) - (minutes // 60 * 60)

if hours >= 24:
    days = hours // 24
    hours = hours % 24
    if days == 1:
        print (f"{days} day {hours:02}:{minutes:02}:{seconds:02}")
    else:
        print(f"{days} days {hours:02}:{minutes:02}:{seconds:02}")
else:
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
