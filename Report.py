import mysql.connector
import requests
import datetime

connection = mysql.connector.connect(host='localhost',
                                     database='report',
                                     user='root',
                                     password='')

cursor = connection.cursor()
api_url = "https://app.fleettrack.co.in/api/get_vehicles?token=infoisight_DuNc65uQtF4CmXdDtzGzSEaKvd92b7BZ&email=infoisight@gmail.com"
response = requests.get(api_url)
response_lst = response.json()

def repvh1():
    response_str1 = str(response_lst[0])
    vhstatus1 = response_str1[171:174]

    while vhstatus1 == "ONN":
        date = datetime.datetime.now()
        date = str(date)
        start_time = date[11:16]
    while vhstatus1 == "OFF":
        date = datetime.datetime.now()
        date = str(date)
        end_time = date[11:16]

    st = datetime.strptime(start_time, "%H:%M:%S")
    et = datetime.strptime(end_time, "%H:%M:%S")

    travel_dur = et - st

    insert_stmt = (
       "INSERT INTO vehicle1(dn, sp, ep, nos, st, et, td)"
       "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = ('Driver1', 'Neelambur', 'Vadavalli', 43, start_time, end_time, travel_dur)
    cursor.execute(insert_stmt, data)


def repvh2():
    response_str2 = str(response_lst[0])
    vhstatus2 = response_str2[171:174]

    while vhstatus2 == "ONN":
        date = datetime.datetime.now()
        date = str(date)
        start_time = date[11:16]
    while vhstatus2 == "OFF":
        date = datetime.datetime.now()
        date = str(date)
        end_time = date[11:16]

    st = datetime.strptime(start_time, "%H:%M:%S")
    et = datetime.strptime(end_time, "%H:%M:%S")

    travel_dur = et - st

    insert_stmt = (
        "INSERT INTO vehicle2(dn, sp, ep, nos, st, et, td)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = ('Driver2', 'Neelambur', 'Singanallur', 34, start_time, end_time, travel_dur)
    cursor.execute(insert_stmt, data)


def repvh3():
    response_str3 = str(response_lst[0])
    vhstatus3 = response_str3[171:174]

    while vhstatus3 == "ONN":
        date = datetime.datetime.now()
        date = str(date)
        start_time = date[11:16]
    while vhstatus3 == "OFF":
        date = datetime.datetime.now()
        date = str(date)
        end_time = date[11:16]

    st = datetime.strptime(start_time, "%H:%M:%S")
    et = datetime.strptime(end_time, "%H:%M:%S")

    travel_dur = et - st

    insert_stmt = (
        "INSERT INTO vehicle3(dn, sp, ep, nos, st, et, td)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = ('Driver3', 'Neelambur', 'Gandhipuram', 46, start_time, end_time, travel_dur)
    cursor.execute(insert_stmt, data)


