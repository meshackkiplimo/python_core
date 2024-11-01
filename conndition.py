temp = float(input("enter temp"))
if temp > 30:
    print("It's a hot day! Stay cool!")
else :
    print("It's a cold day! Stay hydrated!")
    


# logical operators
has_high_income =  True

has_good_credit = False
if has_high_income and has_good_credit:
    print("You are eligible for the loan")
else:
    print("You are not eligible for the loan")

# logical or
has_high_income =  False

has_good_credit = False

if has_high_income or has_good_credit:
    print("You are eligible for the loan")
else:
        print("You are not eligible for the loan")


# logical not
has_high_income =  False

has_criminal_record = True

if has_high_income and not has_criminal_record:
     print("You are eligible for the loan")
     
else:
     print("You are not eligible for the loan")     
     



