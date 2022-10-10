from weather import *

menu = "     *** TUFFY TITAN WEATHER LOGGER MAIN MENU \n\n"
menu += "1. Set data filename\n"
menu += "2. Add weather data\n"
menu += "3. Print daily report\n"
menu += "4. Print historical report\n"
menu += "9. Exit the program\n\n"

chose = 0
while(True):
    print(menu)
    chose = input("Enter menu choice: ")
    print("\n")

    #select #1
    if(chose == '1'):
        f_name = input("Enter data filename: ")
        weather = read_data(f_name)
        print("\n")

    #select #2
    elif(chose == '2'):
        date = input("Enter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        tem = input("Enter temperature: ")
        hum = input("Enter humidity: ")
        rain = input("Enter rainfall: ")
        id= str(date) + str(time)
        weather[date+time] = {"t": int(tem), "h": int(hum), "r": float(rain)}
        write_data(weather , f_name)
        print("\n")


    #select #3
    elif(chose == '3'):
        date = input("Enter date (YYYYMMDD): ")
        report = report_daily(weather, date)
        print(report)
        print("\n")

    #select #4
    elif(chose == '4'):
        report = report_historical(weather)
        print(report)
        print("\n")

    #select #9
    elif(chose == '9'):
        break
