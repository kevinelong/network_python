import re


# 25) Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)


dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ", dt1)
print("New date in DD-MM-YYYY Format: ", change_date_format(dt1))
