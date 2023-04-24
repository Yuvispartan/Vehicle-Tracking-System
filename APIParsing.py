# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:25:27 2022
@author: senthil
"""
import threading
import requests
import json
from os.path import exists
from time import time, sleep
from multiprocessing import Process
from threading import Thread
import _thread
import mysql.connector
import urllib
import urllib.request
import urllib.error
import datetime

connection = mysql.connector.connect(host='localhost',
                                     database='vehicle',
                                     user='root',
                                     password='')
pasttense = "will reach"
mydate = datetime.datetime.now()
date = str(mydate)
mon = mydate.strftime("%B")
dat = "{}-{} {}".format(date[8:10],mon[0:3],date[11:16])

user = "senthil" # Your authentication key.

key = "cb4af5fca3XX" # Your authentication key.

url = "http://103.233.79.246/submitsms.jsp?" # API URL

def vehicle1():
    if response.status_code == 200:
        # print(response.json())
        response_lst = response.json()

        response_str1 = str(response_lst[0])
        vhstatus1 = response_str1[171:174]
        coords_1 = ['lat', 'long']
        count1 = 1

        while vhstatus1 != "ON" and count1 < 50:
            sleep(10 - time() % 10)
            lat_str1 = response_str1[13:31]
            long_str1 = response_str1[46:63]
            coords_1[0] = float(lat_str1[0:9]) + count1 / 10000
            coords_1[1] = float(long_str1[0:9]) + count1 / 100000
            if count1 == 1:
                sql_select_query1 = "Select * from vehicle1"
                cursor = connection.cursor()
                cursor.execute(sql_select_query1)
                records1 = cursor.fetchall()
                vhnum1 = []
                regno1 = []
                sname1 = []
                bpoint1 = []
                pname1 = []
                cno1 = []
                for row in records1:
                    vhnum1.append(row[0])
                    regno1.append(row[1])
                    sname1.append(row[2])
                    bpoint1.append(row[3])
                    pname1.append(row[4])
                    cno1.append(row[5])
                print(cno1)
                for i in range(len(sname1)):
                    message1 = "Your venicle {} {} {} at {}\nThanks\nIsight Solutions".format(vhnum1[i], pasttense,
                                                                                              bpoint1[i],
                                                                                              dat)  # Your message to send.
                    mobile1 = cno1[i]  # Multiple mobiles numbers separated by comma.

                    senderid = "ISTSOL"  # Sender ID,While using route4 sender id should be 6 characters long.
                    accusage = 1  # Define route

                    # Prepare you post parameters
                    values1 = {
                        'user': user,
                        'key': key,
                        'mobile': mobile1,
                        'message': message1,
                        'senderid': senderid,
                        'accusage': accusage
                    }

                    postdata1 = urllib.parse.urlencode(values1)  # URL encoding the data here.

                    postdata1 = postdata1.encode('utf-8')  # encoding the string values into bytes

                    req1 = urllib.request.Request(url, postdata1)

                    response1 = urllib.request.urlopen(req1)

                    output1 = response1.read()  # Get Response

                    print(output1)

            count1 += 1
            print(coords_1)

            # Data to be written
            json1 = {
                "latitude1": coords_1[0],
                "longitude1": coords_1[1],
            }

            # Serializing json
            json1_object = json.dumps(json1, indent=4)

            # Writing to sample.json
            with open("vh1.json", "w") as outfile:
                outfile.write(json1_object)

def vehicle2():
    if response.status_code == 200:
        # print(response.json())
        response_lst = response.json()

        response_str2 = str(response_lst[1])
        vhstatus2 = response_str2[171:174]
        coords_2 = ['lat', 'long']
        count2 = 1

        while vhstatus2 != "ON" and count2 < 50:
            sleep(10 - time() % 10)
            lat_str2 = response_str2[13:31]
            long_str2 = response_str2[46:63]
            coords_2[0] = float(lat_str2[0:9]) + count2 / 10000
            coords_2[1] = float(long_str2[0:9]) + count2 / 100000
            if count2 == 1:
                sql_select_query2 = "Select * from vehicle2"
                cursor = connection.cursor()
                cursor.execute(sql_select_query2)
                records2 = cursor.fetchall()
                vhnum2 = []
                regno2 = []
                sname2 = []
                bpoint2 = []
                pname2 = []
                cno2 = []
                for row in records2:
                    vhnum2.append(row[0])
                    regno2.append(row[1])
                    sname2.append(row[2])
                    bpoint2.append(row[3])
                    pname2.append(row[4])
                    cno2.append(row[5])
                print(cno2)
                for i in range(len(sname2)):
                    message2 = "Your venicle {} {} {} at {}\nThanks\nIsight Solutions".format(vhnum2[i], pasttense,
                                                                                              bpoint2[i],
                                                                                              dat)  # Your message to send.
                    mobile2 = cno2[i]  # Multiple mobiles numbers separated by comma.

                    senderid = "ISTSOL"  # Sender ID,While using route4 sender id should be 6 characters long.
                    accusage = 1  # Define route

                    values2 = {
                        'user': user,
                        'key': key,
                        'mobile': mobile2,
                        'message': message2,
                        'senderid': senderid,
                        'accusage': accusage
                    }

                    postdata2 = urllib.parse.urlencode(values2)  # URL encoding the data here.

                    postdata2 = postdata2.encode('utf-8')  # encoding the string values into bytes

                    req2 = urllib.request.Request(url, postdata2)

                    response2 = urllib.request.urlopen(req2)

                    output2 = response2.read()

                    print(output2)

            count2 += 1
            print(coords_2)

            # Data to be written
            json2 = {
                "latitude2": coords_2[0],
                "longitude2": coords_2[1],
            }

            # Serializing json
            json2_object = json.dumps(json2, indent=4)

            # Writing to sample.json
            with open("vh2.json", "w") as outfile:
                outfile.write(json2_object)

def vehicle3():
    if response.status_code == 200:
        # print(response.json())
        response_lst = response.json()

        response_str3 = str(response_lst[2])
        vhstatus3 = response_str3[171:174]
        coords_3 = ['lat', 'long']
        count3 = 1

        while vhstatus3 != "ON" and count3 < 50:
            sleep(10 - time() % 10)
            lat_str3 = response_str3[13:31]
            long_str3 = response_str3[46:63]
            coords_3[0] = float(lat_str3[0:9]) + count3 / 10000
            coords_3[1] = float(long_str3[0:9]) + count3 / 100000
            if count3 == 1:
                sql_select_query3 = "Select * from vehicle3"
                cursor = connection.cursor()
                cursor.execute(sql_select_query3)
                records3 = cursor.fetchall()
                vhnum3 = []
                regno3 = []
                sname3 = []
                bpoint3 = []
                pname3 = []
                cno3 = []
                for row in records3:
                    vhnum3.append(row[0])
                    regno3.append(row[1])
                    sname3.append(row[2])
                    bpoint3.append(row[3])
                    pname3.append(row[4])
                    cno3.append(row[5])
                print(cno3)

                for i in range(len(sname3)):
                    message3 = "Your venicle {} {} {} at {}\nThanks\nIsight Solutions".format(vhnum3[i], pasttense,
                                                                                              bpoint3[i],
                                                                                              dat)  # Your message to send.
                    mobile3 = cno3[i]  # Multiple mobiles numbers separated by comma.

                    senderid = "ISTSOL"  # Sender ID,While using route4 sender id should be 6 characters long.
                    accusage = 1  # Define route

                    values3 = {
                        'user': user,
                        'key': key,
                        'mobile': mobile3,
                        'message': message3,
                        'senderid': senderid,
                        'accusage': accusage
                    }

                    postdata3 = urllib.parse.urlencode(values3)  # URL encoding the data here.

                    postdata3 = postdata3.encode('utf-8')  # encoding the string values into bytes

                    req3 = urllib.request.Request(url, postdata3)

                    response3 = urllib.request.urlopen(req3)

                    output3 = response3.read()

                    print(output3)
            count3 += 1
            print(coords_3)

            # Data to be written
            json3 = {
                "latitude3": coords_3[0],
                "longitude3": coords_3[1],
            }

            # Serializing json
            json3_object = json.dumps(json3, indent=4)

            # Writing to sample.json
            with open("vh3.json", "w") as outfile:
                outfile.write(json3_object)

if __name__ == '__main__':

    api_url = "https://app.fleettrack.co.in/api/get_vehicles?token=infoisight_DuNc65uQtF4CmXdDtzGzSEaKvd92b7BZ&email=infoisight@gmail.com"
    response = requests.get(api_url)

    print("the response code", response.status_code)

    if response.status_code == 200:
        # print(response.json())
        response_lst = response.json()

        threading.Thread(target=vehicle1).start()
        threading.Thread(target=vehicle2).start()
        threading.Thread(target=vehicle3).start()














