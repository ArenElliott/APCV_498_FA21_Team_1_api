#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    findHalf = re.compile("AM|PM")
    findTime = re.compile("\\d{2}:\\d{2}:\\d{2}")

    time = findTime.search(s)
    times = time.group().split(':')

    hour = int(times[0])

    half = findHalf.search(s)

    if (hour == 12):
        if (half.group() == "AM"):
            hour -= 12
    else:
        if (half.group() == "PM"):
            hour += 12

    return f"{hour:02}:{times[1]}:{times[2]}"


timeConversion("12:45:54AM")
