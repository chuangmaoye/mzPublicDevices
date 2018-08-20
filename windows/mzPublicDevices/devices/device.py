#!/usr/bin/env python
# coding: utf-8
from .mzkeyboard import *
from .mzmouse import *

import threading
import time
import json
# import zlib
class Mzdevice(object):
	"""docstring for Mzdevice"""
	def __init__(self):
		super(Mzdevice, self).__init__()
		self.events=[]
		self.mzmou=Mzmouse(self.addevents)
		self.mzkey=Mzkeybodard(self.addevents)
	def addevents(self,event):
		self.events.append(event)
		# print self.events
	def run(self):
		
		tkey = threading.Thread(target=self.mzkey.run)
		tkey.setDaemon(True)
		tkey.start()
		
		tmou = threading.Thread(target=self.mzmou.run)
		tmou.setDaemon(True)
		tmou.start()
	def clientmove(self,event):

		if self.mzmou:
			# event = zlib.decompress(event)  
			# print eventcho
			# tm=threading.Thread(target=self.mzmou.clientmove,args=[event,])
			# tm.start()
			# print(event.decode("utf-8"))
			event=event.decode("utf-8")
			# event=event.strip("\n")
			revents=event.split("\n")
			print (revents)
			for ev in revents:
				jret=json.loads(ev)
				if jret['type']!='keyboard':
					self.mzmou.mouseevent.append(jret)
				else:
					self.mzkey.mzkeybodardevent.append(jret)
			# starttime=time.clock()
			# tk=threading.Thread(target=self.mzkey.clientkeyboard,args=[event,])
			# tk.setDaemon(True)
			# tk.start()
			# endtime=time.clock()
			# print str(endtime-starttime)
			# self.mzmou.clientmove(event)
if __name__ == '__main__':
	mzde=Mzdevice()
	mzde.run()