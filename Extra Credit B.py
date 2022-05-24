def main():
    days = int(input("Please enter the number of days"))
    if(days < 0):
        print("I am sorry, there is no result for that number")
    elif(days < 31):
        print("01/", days, "/2022")
    elif(31 < days < 59):
        print("02/",days - 31,"/2022")
    elif(59 < days < 90):
        print("03/",days - 59,"/2022")
    elif(90 < days < 120):
        print("04/",days - 90,"/2022")
    elif(120 < days < 151):
        print("05/",days - 120,"/2022")
    elif(151 < days < 181):
        print("06/",days - 151,"/2022")
    elif(181 < days < 212):
        print("07/",days - 181,"/2022")
    elif(212 < days < 243):
        print("08/",days - 212,"/2022")
    elif(243 < days < 273):
        print("09/",days - 243,"/2022")
    elif(273 < days < 304):
        print("10/",days - 273 ,"/2022")
    elif(304 < days < 334):
        print("11/",days - 304,"/2022")
    elif(334 < days < 365):
        print("12/",days - 334,"/2022")
    elif(days > 365):
        sets = days // 365
        year = 2022 + sets
        dayys = days % 365
        if(dayys < 31):
            print("01/", dayys,"/",year)
        if(31 < dayys < 59):
            print("02/",dayys - 31,"/",year)
        if(59 < dayys < 90):
            print("03/",dayys - 59,"/",year)
        if(90 < dayys < 120):
           print("04/",dayys - 90,"/",year)
        if(120 < dayys < 151):
            print("05/",dayys - 120,"/",year)
        if(151 < dayys < 181):
            print("06/",dayys - 151,"/",year)
        if(181 < dayys < 212):
            print("07/",dayys - 181,"/",year)
        if(212 < dayys < 243):
            print("08/",dayys - 212,"/",year)
        if(243 < dayys < 273):
            print("09/",dayys - 243,"/",year)
        if(273 < dayys < 304):
            print("10/",dayys - 273,"/",year)
        if(304 < dayys < 334):
            print("11/",dayys - 304,"/",year)
        if(334 < dayys < 365):
            print("12/",dayys - 334,"/",year)
      
        
main()
