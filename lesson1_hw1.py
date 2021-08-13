correct_answer = "Right, off you go!"
incorrect_answer = "You are cast into the Gorge of Eternal Peril!"

name = input("What is your name? ")
quest = input(f"What is your quest {name.title()}? ")

if "Arthur" in name.title():
    swallow_speed = float(input("What is the air-speed velocity of an unladen swallow? "))
    print(swallow_speed)
    print ("You have to know these things when you're a king")
elif "Robin" in name.title():
    capital = input("What is the capital of Assyria? ")
    if capital.title() == "Assur":
        print(correct_answer)
    else:
        print(incorrect_answer)
else:
    color = input("What is your favorite color? ")
    if color.title() == "Blue":
        print(correct_answer)
    else:
        print(incorrect_answer)
