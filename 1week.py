# print('hello')

# hash diye commend korlam

# student = "maisha"
# age = 16
# isPresent = False
# result = 65.45

# print(f"{student} is good student and she is {age} years old")

# if result >= 80 :
#    print("he got A+")
# elif result >=70 :
#    print('she got A-')
# elif result >= 60 : 
#    print("she got B")
# else : 
#    print("She failed")


# for i in range(1,5):
#    print(i)


# def function (peremeter):
#    print(peremeter)


# function("peremeter pass korlam")

# def pluse (onePerameter, twoperameter):
#    equall = onePerameter + twoperameter
#    return equall

# print(pluse(5,7))

# arithmetic operators
# a = 39
# b = 53

# print("addition", a + b)
# print("division", a / b)
# print("floor division", a // b)
# print("module", a % b)
# print("power", a ** b)
# print("equal", a == b)
# print("greater than", a > b)


# furits = ["apple","banana","orange"]
# furits.append("mango")
# print(furits[0])

# colors = ("red","green","yellow")
# print(colors[1])

# dictionary
#student = {
#  "name": "Tanvir",
#   "age": "22",
#   "dpt": "Math"
    
#}

#print(student)

# for loop
# for i in range(3):
#     print("count",i)

# count = 0
# while count < 5 :
#     print("while loop count", count)
#     count += 1

# import datetime

# # Track a habit
# def track_habit():
#     habit = input("Enter the habit you want to track: ").strip()
#     status = input("Did you complete the habit today? (y/n): ").strip().lower()

#     done = "done" if status == 'y' else "not done"
#     today = datetime.date.today().isoformat()

#     with open("habit_tracker.txt", "a") as file:
#         file.write(f"{today} : {habit} : {done}\n")
#         print("Tracking completed successfully!")


# # View habit summary
# def view_habit():
#     try:
#         with open("habit_tracker.txt", "r") as file:
#             print("\nHabit Tracking Data (Last 30 Entries):\n")

#             lines = file.readlines()
#             recent = lines[-30:]  # last 30 entries

#             habit_summary = {}
#             for line in recent:
#                 parts = line.strip().split(":")
#                 if len(parts) != 3:
#                     continue
#                 date = parts[0].strip()
#                 habit = parts[1].strip()
#                 status = parts[2].strip()

#                 if habit not in habit_summary:
#                     habit_summary[habit] = {"done": 0, "not done": 0}
                
#                 if status in habit_summary[habit]:
#                     habit_summary[habit][status] += 1

#             for habit, summary in habit_summary.items():
#                 print(f"{habit}: Done {summary['done']} times, Not Done {summary['not done']} times\n")

#     except FileNotFoundError:
#         print("No habit tracking data found.")


# # Main menu function
# def habit_tracker():
#     print("\nHabit Tracker")
#     print("1. Track a habit")
#     print("2. View habit summary")
#     print("3. Exit")

#     choice = input("Enter your choice (1/2/3): ").strip()

#     if choice == '1':
#         track_habit()
#     elif choice == '2':
#         view_habit()
#     elif choice == '3':
#         print("Exiting Habit Tracker.")
#         return False
#     else:
#         print("Invalid choice, please try again.")
    
#     return True


# # Run the tracker in a loop
# while True:
#     if not habit_tracker():
#         break
#     again = input("Do you want to continue? (y/n): ").strip().lower()
#     if again != "y":
#         print("Thank you for using the Habit Tracker!")
#         break



import time;

test_sentence = "Practice makes a men perfect"

print("Typing speed test started...")
print("\n Type this sentence")
print(test_sentence)
print("\n Press enter to start....")


start_time = time.time()

typed = input("Start typing :")

end_time = time.time()

time_taken = end_time - start_time

words = typed.split()
wpm = (len(words) / time_taken) * 60

correct_charts = 0
for i in range(min(len(test_sentence), len(typed))):
    if test_sentence[i] == typed[i]:
        correct_charts += 1

accuracy = (correct_charts / len(test_sentence)) * 100

print("\n ----Result----")
print(f"Time taken: {round(time_taken, 2)} seconds")
print(f"Your typing speed is {round(wpm, 2)} words per minute")
print(f"You accurately typed {correct_charts} charaters out of { len(test_sentence)}")



