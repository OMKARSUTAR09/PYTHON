from datetime import datetime

def calculate_age(birthdate, today):
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

today_str = input("Enter today's date (YYYY-MM-DD): ")
today = datetime.strptime(today_str, "%Y-%m-%d")

birthdate_str = input("Enter your birth date (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

age = calculate_age(birthdate, today)

print(f"You are {age} years old.")
