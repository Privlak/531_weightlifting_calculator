# Modules for writing the output and displaying the "Data saved successfully!" message.
import time
import os

# Username prompt
while True:
    username = input("Enter your name: ")
    
    if not isinstance(username, str) or not username.strip() or not username.isalpha():
        print("Input must be a string!")
        continue
    else:
        username_capitalized = username.capitalize()
        break

# Creating a list of exercises
print("----------------------------------------------------------------------------------------")
print("Enter the exercises you want to calculate your training max for, one per line!" + "\n")
print('Enter "back" (without the quotes) to go back and rewrite the exercise.' + "\n")
print('Enter "done" (without the quotes) to end the list.')
print("----------------------------------------------------------------------------------------")

exercises = []
current_index = 0 

while True:
    e = input(f"Exercise {current_index + 1}: ")
    
    if e.lower() == "done":
        break
        
    elif e.lower() == "back":
        if current_index > 0:
            current_index -= 1
            print(f"Returning to Exercise {current_index + 1}")
            del exercises[current_index]
            continue
        else:
            print("You need to enter an exercise!")
            continue
            
    elif e == "":
        print("You need to enter an exercise!")
        continue
        
    elif not e.isalpha():
        print("Input must be a string!")
        continue
        
    exercises.append(e)
    current_index += 1

# Capitalize the exercises 
for c in range(len(exercises)):
    exercises[c] = exercises[c].title()

# Printing out the exercises
print("----------------------------------------------------------------------------------------")
exercise_number = 1
for e in exercises:
    print(f"{exercise_number}) - {e}")
    exercise_number += 1

# Creating a list of training max values
print("----------------------------------------------------------------------------------------")
print("Enter your training max, one per line!" + "\n")
print('If you dont know your training max, enter "tm" (without the quotes).' + "\n")
print('Enter "back" (without the quotes) to go back and rewrite the training max.' + "\n")
print('Enter "done" (without the quotes) to end the list.')
print("----------------------------------------------------------------------------------------")

training_max = []
i = 0

while i < current_index:
    tm = input(f"Training max for {exercises[i]}: ")

    if tm.lower() == "done":
        break

    elif tm.lower() == "back":
        if i > 0:
            i -= 1
            del training_max[i]
            print(f"Returning to training max for {exercises[i]}")
            continue
        else:
            print("You need to enter a training max!")
            continue

    if tm == "tm":
        while True:
            weight_lifted = input(f'What is the highest weight you successfully lifted for {exercises[i]}? (Type "back" to go back): ')

            if weight_lifted == "":
                print("You need to enter a training max!")
                continue

            elif weight_lifted.lower() == "back":
                break

            elif not weight_lifted.replace(".", "").isdigit():
                print("Input must be a number (delimiter must be a dot ('.')!")
                continue

            while True:
                n_reps = input('How many times did you lift it in a single set? (Type "back" to go back): ')

                if n_reps == "":
                    print("You need to enter a number of repetitions!")
                    continue

                elif n_reps.lower() == "back":
                    break

                elif not n_reps.isdigit():
                    print("Input must be an integer!")
                    continue

                weight_lifted = float(weight_lifted)
                n_reps = int(n_reps)

                tm = round((n_reps * weight_lifted * 0.0333 + weight_lifted) * 0.9 / 2.5) * 2.5 # Currently using 90%! ; Calculates increments of 2.5!
                training_max.append(tm)
                print(f"Calculated training max added to exercise {exercises[i]}!")
                i += 1

                break 
            break
        continue

    elif tm == "":
        print(f'You need to enter a training max! If you do not know your training max, enter "tm" (without the quotes).')
        continue

    elif not tm.replace(".", "").isnumeric():
        print("Input must be a number (delimiter must be a dot ('.')!")
        continue

    tm = round(float(tm) * 0.9 / 2.5) * 2.5 # Currently using 90%! Calculates increments of 2.5!
    training_max.append(tm)
    i += 1

# Create a directory and write the monthly program to "{username_capitalized}_531.txt"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
gym_path = os.path.join(desktop_path, "Gym")

if not os.path.exists(gym_path):
    os.mkdir(gym_path)
    
file_path = os.path.join(gym_path, f"{username_capitalized}_531.txt")
    
with open(file_path, "w") as f:
    f.write("[Training maxes]" + "\n")
    f.write("--------------------------------------" + "\n")
    
    for e, tm in zip(exercises, training_max):
        f.write(e + " - " + str(tm) + "kg" + "\n")
 
    for e, tm in zip(exercises, training_max):
        f.write("--------------------------------------" + "\n")
        f.write(f"[{e}]" + "\n")
        f.write("Week 1 -" + " " + str(round(0.65 * float(tm) / 2.5) * 2.5) + "x5, " + str(round(0.75 * float(tm) / 2.5) * 2.5) + "x5, " + str(round(0.85 * float(tm) / 2.5) * 2.5) + "x5+" + "\n")
        f.write("Week 2 -" + " " + str(round(0.70 * float(tm) / 2.5) * 2.5) + "x3, " + str(round(0.80 * float(tm) / 2.5) * 2.5) + "x3, " + str(round(0.90 * float(tm) / 2.5) * 2.5) + "x3+" + "\n")
        f.write("Week 3 -" + " " + str(round(0.75 * float(tm) / 2.5) * 2.5) + "x5, " + str(round(0.85 * float(tm) / 2.5) * 2.5) + "x3, " + str(round(0.95 * float(tm) / 2.5) * 2.5) + "x1+" + "\n")
        f.write("Deload -" + " " + str(round(0.40 * float(tm) / 2.5) * 2.5) + "x5, " + str(round(0.50 * float(tm) / 2.5) * 2.5) + "x5, " + str(round(0.60 * float(tm) / 2.5) * 2.5) + "x5" + "\n")
        # Outputs increments of 2.5!

# The output message and how long it stays on
print("\nData saved successfully!")
time.sleep(3)
