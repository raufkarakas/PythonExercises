__author__ = 'rkarakas'

import ntplib
from time import ctime

def correctTimeFromInternet():
    client = ntplib.NTPClient()
    response = client.request("pool.ntp.org")
    print(ctime(response.tx_time))

correctTimeFromInternet()
