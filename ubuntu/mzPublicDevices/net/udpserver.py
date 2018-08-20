#!/usr/bin/env python
# coding: utf-8
from twisted.internet.protocol import DatagramProtocol

from twisted.internet import reactor
import threading
import time
class Echo(DatagramProtocol):
	def datagramReceived(self, data, (host, port)):

		print "received %r from %s:%d" % (data, host, port)

		self.transport.write(data, (host, port))
		self.transport.write(data, (host, port))
		
		# tkey = threading.Thread(target=self.startsend,args=[self.transport,])
		# tkey.setDaemon(True)
		# tkey.start()

	def startsend(self,transport):
		while True:
			transport.write("ts")
			time.sleep(1)


reactor.listenUDP(9999, Echo())

reactor.run()