#! /usr/bin/env python
# -*- coding=utf-8 -*-
import time, serial, urllib, urllib2
# pyserial is required. 
# http://pyserial.sourceforge.net/
print 'start\n'
try:
    ser = serial.Serial(2)    # open COM3
    ser.baudrate = 9600
    for x in xrange(1,10000):
        print str(x) + ':  ' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ': '
        line = ser.readline().replace('\r\n', '').split(',')
        data = {
            'device_index': 13726247339,
            'longitude': 113.540718,
            'latitude': 22.256467,
            'temperature': line[1],
            'humidity': line[2],
            'particulate_matter': line[0]
        }
        print data
        url = 'http://monitor.ourjnu.com/submit.php?'+urllib.urlencode(data)
        try:
            response = urllib2.urlopen(url).read()
            print response + '\n\n'
            #time.sleep(60)    #sleep 60 seconds
        except:
            print 'Network error.\n\n'
        ser.flushOutput()
    ser.close()
except:
    print 'Could not open port COM3.'
#raw_input()