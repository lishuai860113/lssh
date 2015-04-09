#!/usr/bin/env python
"USAGE: %s <port>"
from SocketServer import DatagramRequestHandler, UDPServer
from sys import argv
from dnslib import *
import re
import time
 
class EchoHandler(DatagramRequestHandler):
    def handle(self):
       print "Client connected:", self.client_address
       message = self.rfile.read()
       d = DNSRecord.parse(message)
       s = str(d.q)
       #print s
       domain = s.split(" ")[0].lstrip(";")
       d_arr = domain.split(".")
       print d_arr
       if d_arr[1] == "ttl" and d_arr[0].isdigit():
             t = int(d_arr[0])
             dida = int(time.time())/t
             cn = str(dida)+".ttl.lisux.me"
       else:
             cn = "nofound.ttl.lisux.me"
             t = 600
       print cn
       rd = DNSRecord(DNSHeader(id=d.header.id,qr=1,aa=1,ra=1),q=DNSQuestion(domain),a=RR(domain,rtype=QTYPE.CNAME,ttl=t,rdata=CNAME(cn)))
       rm = rd.pack()
       self.wfile.write(str(rm))
 
if len(argv) != 2:
    print __doc__ % argv[0]
else:
    UDPServer(('',int(argv[1])), EchoHandler).serve_forever()
