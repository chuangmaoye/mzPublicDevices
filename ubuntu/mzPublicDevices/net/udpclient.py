#!/usr/bin/env python
# coding: utf-8
from twisted.internet.protocol import DatagramProtocol

from twisted.internet import reactor
import threading
import time
class Helloer(DatagramProtocol):


	def startProtocol(self):

		self.transport.connect("127.0.0.1", 9999)
		# self.transport.write("hello")
		tkey = threading.Thread(target=self.startsend,args=[self.transport,])
		tkey.setDaemon(True)
		tkey.start()
		# print "we can only send to %s now" % str((host, port))

		
	# def makeConnection(self,transport):
	# 	# self.transport.write("hello") # no need for address
	# 	# tkey = threading.Thread(target=self.startsend,args=[self.transport,])
	# 	# tkey.setDaemon(True)
	# 	# tkey.start()
	# 	print "connect"
	# 	self.transport.connect("127.0.0.1", 9999)
	def startsend(self,transport):
		while True:
			try:
				transport.write("ts")
				time.sleep(0.01)
			except:
				reactor.listenUDP(0, Helloer())
				break
				# self.transport.connect("127.0.0.1", 9999)

	def datagramReceived(self, data, (host, port)):

		print "received %r from %s:%d" % (data, host, port)



	# Possibly invoked if there is no server listening on the

	# address to which we are sending.

	def connectionRefused(self):

		print "No one listening"

 

# 0 means any port, we don't care in this case

reactor.listenUDP(0, Helloer())

reactor.run()