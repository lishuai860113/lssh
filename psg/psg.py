#!/bin/env python
#use sar data create jpg
#write by lishuai

import cgi, os
import sys, re
import time
import commands
import random
import cgitb; cgitb.enable()

#status, output = commands.getstatusoutput("")


def psg():
    'create a jpg file for sar use gnuplot'
    
    status, output = commands.getstatusoutput("LANG=C;sar -f /var/log/sa/sa27 |grep -P '\d\d:\d\d:\d\d' |grep -v '%' |awk '{print $1,$8}'>tmp/test.sar")












if __name__ == "__main__":
    psg()

