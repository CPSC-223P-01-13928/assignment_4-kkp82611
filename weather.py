import json
import calendar

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_data(data,filename):
    with open(filename , 'w') as f:
        json.dump(data,f)

def max_temperature(data,date):
    max_temp = 0
    for i in data:
        if date == i[0:8]:
            if data[i]["t"] > max_temp:
                max_temp = data[i]["t"]
    return max_temp


def min_temperature(data,date):
    min_temp = 9999
    for i in data:
        if date == i[0:8]:
            if data[i]["t"] < min_temp:
                min_temp = data[i]["t"]
    return min_temp


def max_humidity(data,date):
    max_hum = 0
    for i in data:
        if date == i[0:8]:
            if data[i]["h"] > max_hum:
                max_hum = data[i]["h"]
    return max_hum

def min_humidity(data,date):
    min_hum = 999999
    for i in data:
        if date == i[0:8]:
            if data[i]["h"] < min_hum:
                min_hum = data[i]["h"]
    return min_hum

def tot_rain(data,date):
    rain = 0
    for i in data:
        if date == i[0:8]:
            rain = rain + data[i]["r"]
    return rain


def report_daily(data,date):
    daily_report = "========================= DAILY REPORT ========================\n"
    daily_report += "Date                      Time  Temperature  Humidity  Rainfall\n"
    daily_report += "====================  ========  ===========  ========  ========\n"
    for i in data:
        if date == i[0:8]:
            m = calendar.month_name[int(i[4:6])] + " " + str(int(i[6:8])) + ", " + str(int(i[0:4]))
            tm = str(i[8:10]) + ":" + i[10:12] + ":" + str(i[12:14])
            t = data[i]["t"]
            h = data[i]["h"]
            r = data[i]["r"]
            daily_report += f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}' + "\n"

    
   # print(daily_report)
    return daily_report

def report_historical(data):
    historical_report = "============================== HISTORICAL REPORT ===========================\n"
    historical_report += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    historical_report += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    historical_report += "====================  ===========  ===========  ========  ========  ========\n"
    h = ''

    for i in data:
        if h == i[0:8]:
            continue
        else:
            h = i[0:8]
            m = calendar.month_name[int(i[4:6])] + " " + str(int(i[6:8])) + ", " + str(int(i[0:4]))
        
        min_tem = min_temperature(data,h)
        max_tem = max_temperature(data,h)
        min_hum = min_humidity(data, h)
        max_hum = max_humidity(data, h)
        t_rain = tot_rain(data, h)
        historical_report += f'{m:20}{min_tem:13}{max_tem:13}{min_hum:10}{max_hum:10}{t_rain:10.2f}' + "\n"

    return historical_report


