#!/usr/bin/env python2.7
# coding=UTF-8


# Copyright (c) 2016-2018 Angelo Moura
#
# This file is part of the program pythem


# Pycharm will help to install about pythonwhois
# Help to user find out information
# It assists that showing single domain or various domain look up
# And help to user display banner


import os
import socket
import pythonwhois


class BannerAndWhoIs():

    def __init__(self):
        print("This is Whois look up function!")

    def Banner_Grabbing(self, Target_host, Target_port=80):

        self.Target_host = Target_host
        self.paraTarget_portm5 = Target_port

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # TCP

        sock.connect((Target_host,Target_port))
        sock.send("GET HTTP/1.1 \r\nHost:target_host\r\n\r\n")

        response = sock.recv(4096)

        print(response)

    def Get_Single_WhoIs(self, param1):

        self.param1 = param1

        domain = pythonwhois.get_whois(param1)

        for i, j in domain.items():
            print("{} ".format(str(i)), str(j))

if __name__ == "__main__":
    """
    Total = BannerAndWhoIs()  # Initialised Class of BannerAndWhoIs to Total.

    _Choice = (raw_input
        (
            "1. Whois Single fuction.\n"
            "2. Banner Grabbering.\n"
            "3. All of them(1 + 3).\n"
            "4. Exit\n"
        )
    )

    while True:

        if _Choice == "1":      # Single WhoIS
            _Mydata = raw_input("enter: ")
            Results1 = Total.Get_Single_WhoIs(_Mydata)
            print(Results1)
            break

        elif _Choice == "2":    # Banner Grabbing
            Host = raw_input("Please enter your Target_host: ")
            Port = input("Please enter your Target_port: ")
            Results3 = Total.Banner_Grabbing(Host, Port)
            print(Results3)
            break

        elif _Choice == "3":   # Above of 1 + 3
            _Mydata = raw_input("enter: ")
            Results4 = Total.Get_Single_WhoIs(_Mydata)
            print(Results4)    # From Single WhoIs Function to show results
            print("*******************************************")
            Host2 = raw_input("Please enter your Target_host: ")
            Port2 = input("Please enter your Target_port: ")
            Results5 = Total.Banner_Grabbing(Host2, Port2)
            print(Results5)    # From Banner_Grabbing Function to show results
            break

        elif _Choice == "4":   # Exit
            print("Good Bye!")
            os.system('clear')
            break


"""
