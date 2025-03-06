# If...else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# If...elif...else statement
score = int(input("Enter your test score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Simulating switch-case using a dictionary
def get_day_name(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switch.get(day, "Invalid day")

day_num = int(input("Enter a day number (1-7): "))
print("Day:", get_day_name(day_num))

# While loop
counter = 5
while counter > 0:
    print("Countdown:", counter)
    counter -= 1

# Simulated do-while loop
while True:
    num = int(input("Enter a positive number (negative to exit): "))
    if num < 0:
        break
    print("You entered:", num)

print("Program ended.")

