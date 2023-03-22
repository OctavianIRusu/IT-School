# Remove all the items from months dict with value greater then 6.

def remove_month(d):
    for key, value in dict(d).items():
        if value > 6:
            del d[key]
    return d

months = { "January": 1, "February": 2, "March": 3, "April": 4,
          "May": 5, "June": 6, "July": 7, "August": 8, "September": 9,
          "October": 10, "November": 11, "December": 12}

remove_month(months)
print(months)
