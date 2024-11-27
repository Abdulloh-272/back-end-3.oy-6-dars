import math

def cube_number(x):
    return math.pow(x, 3)

result = cube_number(3)
print(result)

import random

def shuffle_list(nums):
    random.shuffle(nums)
    return nums

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = shuffle_list(numbers)
print(result)

import datetime

def time_to_iterate():
    start_time = datetime.datetime.now()
    
    for i in range(1, 10001):
        pass 
    
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    return elapsed_time.total_seconds()

result = time_to_iterate()
print(f"Vaqt: {result} s")

import calendar

def print_month_calendar(month_num):
    month_name = calendar.month_name[month_num]
    print(f"\n{month_name}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    month_days = calendar.monthcalendar(2024, month_num) 
    for week in month_days:
        print(" ".join(f"{day if day != 0 else ' ' :2}" for day in week))

month_input = int(input("1-12 gacha bo'lgan sonni kiriting: "))
print_month_calendar(month_input)
