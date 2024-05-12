print("Welcome to Treasure Island 🏴‍☠️")
print("Your mission is to find the treasure.💰💰💰")
print("You are at a cross road.🏝️🏝️🏝️")
step1 = input("Where do you want to go? Type 'Left' or 'Right'.\n=>")

if step1 == "Left":
    print("You came to a lake.")
    print("There is an island in the middle of the lake.")
    step2 = input("What will you do? Type 'Wait' or 'Swim'.\n=>")

    if step2 == "Wait":
        print("You arrived at the island other side unharmed.")
        print("Now you have found three cave.🌌🌌🌌")
        step3 = input("Which cave which you follow.Type 'Left','Middle', 'Right'.\n=>")
        if step3 == "left" or step3 == "Right":
            print("You are trap in the cave forever.💀💀💀")
            print("--- Game over ---")
        else:
            print("You have found the treasure.💰💰💰")
    else:
        print("💀💀💀")
        print("Got attack by the snakes.")
        print("--- Game over ---")
else:
    print("💀💀💀")
    print("Got attack by the trolls.")
    print("--- Game over ---")