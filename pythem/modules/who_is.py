#!/usr/bin/env python2.7
# coding=UTF-8


# Copyright (c) 2016-2018 Angelo Moura
#
# This file is part of the program pythem


# sudo pip install python-whois or sudo apt-get install -y python-whois or
# Pycharm will help to install it.
# Help to user find out information
# It assists that showing single domain or various domain look up
# And help to user display banner

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA


import os
import socket
import whois


class BannerAndWhoIs():

    def __init__(self):
        print("Welcome!")
        print("This is Whois look up function!")
        print("Please select 1 to 5!")

    def Banner_Grabbing(self, Target_host, Target_port=80):

        self.Target_host = Target_host
        self.paraTarget_portm5 = Target_port

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # TCP

        sock.connect((Target_host, Target_port))
        sock.send("GET HTTP/1.1 \r\n Host:target_host\r\n\r\n")

        response = sock.recv(4096)

        print(response)

    def Get_Multiple_Whois(self, location):

        self.location = location

        if location is not None:
            myfile = open(location, 'r')

        ALL = myfile.readlines()

        for _line in ALL:
            domain = whois.query(_line)
            print(domain.name)
            print(domain.registrar)
            print(domain.last_updated)
            print(domain.expiration_date)
            print(domain.creation_date)
            print("**********************")

        myfile.close()

    def Get_Single_WhoIs(self, param1):

        self.param1 = param1

        domain = whois.query(param1)
        print(domain.name)
        print(domain.registrar)
        print(domain.last_updated)
        print(domain.expiration_date)
        print(domain.creation_date)


if __name__ == "__main__":

   Total = BannerAndWhoIs()  # Initialised Class of BannerAndWhoIs to Total.

   _Choice = (raw_input
       (
       "1. Whois Single fuction.\n"
       "2. Whois Multiple function.\n"
       "3. Banner Grabbering.\n"
       "4. All of them(1 + 3).\n"
       "5. Exit\n"
   )
   )

   while True:

       if _Choice == "1":  # Single WhoIS
           _Mydata = raw_input("enter: ")
           Results1 = Total.Get_Single_WhoIs(_Mydata)
           print(Results1)
           break

       elif _Choice == "2":  # Multiple WhoIS
           print("Please select your .txt file")
           print("ex) /home/unknown/test.txt")
           _Myfile = raw_input("")
           Results2 = Total.Get_Multiple_Whois(_Myfile)
           print(Results2)
           break

       elif _Choice == "3":  # Banner Grabbing
           Host = raw_input("Please enter your Target_host: ")
           Port = input("Please enter your Target_port: ")
           Results3 = Total.Banner_Grabbing(Host, Port)
           print(Results3)
           break

       elif _Choice == "4":  # Above of 1 + 3
           _Mydata = raw_input("enter: ")
           Results4 = Total.Get_Single_WhoIs(_Mydata)
           print(Results4)  # From Single WhoIs Function to show results

           print("*******************************************")

           Host2 = raw_input("Please enter your Target_host: ")
           Port2 = input("Please enter your Target_port: ")
           Results5 = Total.Banner_Grabbing(Host2, Port2)
           print(Results5)  # From Banner_Grabbing Function to show results
           break

       elif _Choice == "5":  # Exit
           print("Good Bye!")
           os.system('clear')
           break