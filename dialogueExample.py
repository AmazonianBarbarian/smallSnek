# Dialogue tree example script.

encounter1 = ["Hello I like pizza!", "Hey there friend!"]

diagChoice = input("Select dialogue[Options: 1, 2]: ")
i = 0 # Variable to keep dialogue encounter in a loop till a valid option is selected.
while i == 0:
    if diagChoice == "1": # Processing the number as a string so non numerical text won't produce an error.
        print(encounter1[0])
        i = 1 # This is to break out of the loop once a valid option is selected.
    elif diagChoice == "2":
        print(encounter1[1])
        i = 1
    else:
        print("Please select a valid option")
        diagChoice = input("Select dialogue[Options: 1, 2]: ")
