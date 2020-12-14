#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import json
import io
import datetime


TEMPERATURE = 20.0
HUMIDITY = 60
TXT = \
    '{{"dat":"{dat}","temperature": "{temperature}","humidity": "{humidity}" , "Alert" : "{Alert}"   }}'
filename = 'temp_log.json'


def run():


    try:

        while True:

            # Build the message with simulated telemetry values.

            for t in range(0, 2):
                temperature = TEMPERATURE + random.random() * 15
                humidity = HUMIDITY + random.random() * 20
                dat = (datetime.datetime.now())
                if temperature > 30 and humidity > 70.0:
                    Alert = ('Please Stay at Home!!')
                else:
                    Alert = ('Enjoy your Ride!!')

                msg = TXT.format(dat=dat, temperature=temperature,
                                 humidity=humidity, Alert=Alert)

                # msg = Message(msg_txt)

                json = open(filename, 'a+')

                # data = json.read(10)
                # if len(data) > 0:

                json.write('\n')
                json.write(msg)
                json.close()

                # Send the message.
                # print ('Message successfully sent')
                time.sleep(5)
    except KeyboardInterrupt:
        print ('data provider stopped')

def current(num):

    msgs=[]
    try:

        while True:

            # Build the message with simulated telemetry values.

            for t in range(num):
                temperature = TEMPERATURE + random.random() * 15
                humidity = HUMIDITY + random.random() * 20
                dat = (datetime.datetime.now())
                if temperature > 30 and humidity > 70.0:
                    Alert = ('Please Stay at Home!!')
                else:
                    Alert = ('Enjoy your Ride!!')

                msg = TXT.format(dat=dat, temperature=temperature,
                                 humidity=humidity, Alert=Alert)
                msgs.append(msg)
    except KeyboardInterrupt:
        print ('data provider stopped')
    return msgs

if __name__ == '__main__':
    run()
