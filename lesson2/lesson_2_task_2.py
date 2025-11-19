def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


chosen_year = 1998

result = is_year_leap(chosen_year)

print(f"год {chosen_year}:{result}")
