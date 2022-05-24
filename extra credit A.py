def main():
    year = int(input("Enter the year"))
    if(year < 2022):
        print("Sorry the year have to be at least 2022")

    else:
         dayspassedeachyear = (year - 2022) * 365
         month = int(input("Please enter the number of month"))
         if(month > 12):
             print("Wrong input.Please there is only 12 months in the year")
         elif(month == 1):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 2):
             days = int(input("Please enter the number of days"))
             if (days > 28):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 3):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 4):
             days = int(input("Please enter the number of days"))
             if (days > 30):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 5):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 6):
             days = int(input("Please enter the number of days"))
             if (days > 30):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 7):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 30
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 8):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 30 + 31
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 9):
             days = int(input("Please enter the number of days"))
             if (days > 30):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 10):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 31 + 31 + 30 + 30
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 11):
             days = int(input("Please enter the number of days"))
             if (days > 30):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
                 print("We are done. Here is the number of days that have passed.", dayss)
         elif(month == 12):
             days = int(input("Please enter the number of days"))
             if (days > 31):
                 print("Please the maximum of days in a month is 31 days")
             else:
                 dayss = dayspassedeachyear + days + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
                 print("We are done. Here is the number of days that have passed.", dayss)
                 

                 
         

main()    


# for i in set for month selection
# 30s = {4,6,9,11}
