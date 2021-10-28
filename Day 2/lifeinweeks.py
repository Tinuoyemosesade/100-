current_age = int(input("what is your current age"))
goal = 90
remaining_year = goal - current_age
weeks = round(remaining_year * 52, 2)
days = round(remaining_year * 365, 2)

print(f" you have {remaining_year} year, {weeks} weeks and {days} days left")

