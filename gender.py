age=int(input("enter the age"))
gender=input("enter the gender")
ms=input("enter the ms")
if gender=="f":
        print("she will work on urban area")
elif gender=="m":
    if age>20 and age<40 and ms=="y":
        print("he may work in anywhere")
    elif age>=40 and age<60 and ms=="y":
        print("he will work only in urban area")
    else:
        print("error")    