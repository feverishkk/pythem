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
import pythonwhois


class BannerAndWhoIs():

    def __init__(self):
        print("This is Whois look up function!")

    def Banner_Grabbing(self, Target_host, Target_port = 80):

        self.Target_host = Target_host
        self.paraTarget_portm5 = Target_port

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # TCP

        sock.connect((Target_host,Target_port))
        sock.send("GET HTTP/1.1 \r\nHost:target_host\r\n\r\n")

        response = sock.recv(4096)

        print(response)

    def Get_WhoIs(self, param1):

        self.param1 = param1

        domain = pythonwhois.get_whois(param1)

        for i, j in domain.items():
            print("{} ".format(str(i)), str(j))

