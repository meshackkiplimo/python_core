def is_leap(year):
    leap=False
    if year % 4 == 0:
        if year % 100 == 0:
          if year % 400 == 0:
            return True
       
            
        else:
            return True
    return  leap


year = int(input("Enter a year: "))
print(is_leap(year))