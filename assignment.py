
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Your age is:", age)


fruits = ["Apple", "Berries", "appricot", "lychee", "Grape"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())



# --- Part (i): Student Marks ---
students = {
    "Alice": 85,
    "Bob": 96,
    "Charlie": 12,
    "Diana": 67,
    "Ethan": 80
}

for name, mark in students.items():
    print(name, mark)

highest_mark = 0
top_student = ""
for name, mark in students.items():
    if mark > highest_mark:
        highest_mark = mark
        top_student = name

print("Top student:", top_student)
print("Highest mark:", highest_mark)
print()

# --- Part (ii): Book Class ---
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("To Kill a Mockingbird", "Harper Lee", 14.99)
book2 = Book("1984", "George Orwell", 12.50)

book1.display_details()
book2.display_details()


# ============================================================
# Question 4: Peak Usage
# ============================================================
from datetime import datetime


def find_peak_usage(logs):
    counts = [0] * 24

    for log in logs:
        dt = datetime.fromisoformat(log)
        hour = dt.hour
        counts[hour] = counts[hour] + 1

    max_logins = max(counts)
    return counts.index(max_logins)


logs = [
    "2026-08-04T08:15:20",
    "2026-08-04T09:30:11",
    "2026-08-04T13:05:44",
    "2026-08-04T13:21:18",
    "2026-08-04T13:55:01",
    "2026-08-04T14:10:00"
]

print(find_peak_usage(logs))
