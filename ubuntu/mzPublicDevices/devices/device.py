#!/usr/bin/env python
# coding: utf-8
from mzkeyboard import *
from mzmouse import *
from pymouse import PyMouse
import threading

class Mzdevice(object):
	"""docstring for Mzdevice"""
	def __init__(self,callwrite=False,mousecallback=False):
		super(Mzdevice, self).__init__()
		self.events=[]
		self.callwrite=callwrite
		self.mousecallback=mousecallback
		self.isnet=False
		self.mzkey={}
		self.mzmou={}
		self.mouse=PyMouse()
	def addevents(self,event):
		if event['type']=="move" and self.mousecallback:
			self.mousecallback(event["x"],event["y"])
		if self.isnet:
			self.events.append(event)
		# print self.events
		if self.callwrite:
			# self.callwrite(event)
			tkey = threading.Thread(target=self.callwrite,args=[event,])
			# tkey.setDaemon(True)
			tkey.start()
	def run(self):
		self.mzkey=Mzkeybodard(self.addevents)
		tkey = threading.Thread(target=self.mzkey.run)
		# tkey.setDaemon(True)
		tkey.start()
		self.mzmou=Mzmouse(self.addevents)
		tmou = threading.Thread(target=self.mzmou.run)
		# tmou.setDaemon(True)
		tmou.start()
if __name__ == '__main__':
	mzde=Mzdevice()
	mzde.run()

