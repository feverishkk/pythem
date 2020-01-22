#!/usr/bin/env python2.7

import os
import ssl
import socket


def Scan_SSL(hostname):
    print ("SSL Certificate Information : ")

    ctx = ssl.create_default_context()  # ctx means create_default_context and initialised in ctx
    s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    try:
        try:
            s.connect((hostname, 443))
            info = s.getpeercert()
            subject = dict(x[0] for x in info['subject'])
            issuer = dict(y[0] for y in info['issuer'])
        except:
            ctx = ssl._create_unverified_context()
            s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
            s.connect((hostname, 443))
            info = s.getpeercert(True)
            info = ssl.get_server_certificate((hostname, 443))
            f = open('{}.pem'.format(hostname), 'w')
            f.write(info)
            f.close()
            cert_dict = ssl._ssl._test_decode_cert('{}.pem'.format(hostname))
            subject = dict(x[0] for x in cert_dict['subject'])
            issuer = dict(y[0] for y in cert_dict['issuer'])
            info = cert_dict
            os.remove('{}.pem'.format(hostname))
        try:
            for k, v in subject.items():
                print("{} : ".format(str(k)), str(v))
            for k, v in issuer.items():
                print(" {} : ".format(str(k)), str(v))
            print("Version : ", str(info['version']))
            print("Serial Number : ", str(info['serialNumber']))
            print("OCSP : ", str(info['OCSP']))
            print("subject Alt Name : ", str(info['subjectAltName']))
            print("CA Issuers : ", str(info['caIssuers']))
            print("CRL Distribution Points : ", str(info['crlDistributionPoints']))
        except KeyError:
            pass

    except:
        print ("SSL is not Present on Target URL...This vulnerable web site")


if __name__ == '__main__':
    value = raw_input("target url: ")
    Scan_SSL(value)