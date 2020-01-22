#!/usr/bin/env python2.7

import shodan
import requests

class MyShodan():

    def Setting_Shodan_API(self):

        print("Setting function!!")
        print("If you don't have Shodan API")
        print("Cannot run.")
        print("Please visit shodan.io")

        global api, MyAPI
        MyAPI = raw_input("Input your Shodan API key: ")
        api = shodan.Shodan(MyAPI)
        #MyShodan.Setting_Target()

    def Setting_Target(self):

        target = raw_input("Input your target url: ")

        dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' \
                     + target + '&key=' + MyAPI
                    # Make a URL

        try:
            # First we need to resolve our targets domain to an IP
            resolved = requests.get(dnsResolve)
            hostIP = resolved.json()[target]

            # Then we need to do a Shodan search on that IP
            host = api.host(hostIP)
            print "IP: %s" % host['ip_str']
            print "Organization: %s" % host.get('org', 'n/a')
            print "Operating System: %s" % host.get('os', 'n/a')

            # Print all banners
            for item in host['data']:
                print "Port: %s" % item['port']
                print "Banner: %s" % item['data']

            # Print vulnerability information
            for item in host['vulns']:
                CVE = item.replace('!','')
                print 'Vulns: %s' % item
                exploits = api.exploits.search(CVE)
                for item in exploits['matches']:
                    if item.get('cve')[0] == CVE:
                        print item.get('description')
        except:
            'An error occured'