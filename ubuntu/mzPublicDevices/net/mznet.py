#!/usr/bin/env python
# coding: utf-8
from mzbase import *
from server import *
from client import *
import json
import time
import threading
import zlib
class Mznet(object):
	"""docstring for Mznet"""
	def __init__(self,device=False,screenmanage=False):
		super(Mznet, self).__init__()
		self.net=None
		self.device=device
		self.screenmanage=screenmanage
		self.transport=False
		self.moves=[]
		self.movsstr=""
		self.device.mousecallback=self.mouserpostion;
		self.cureen=self.screenmanage.Curren
		self.udp=False
	def run(self):
		netype=config("setting","terminal")
		print netype
		if netype == 'server':
			self.net=Server(config,self.mzwrite,self.register)
			width,height=self.device.mouse.screen_size()
			print self.device.mouse.screen_size()
			servername=config("server","name")
			self.screenmanage.setscreen(servername,True,width-2,height-2)
			self.screenmanage.setcurrenscreen(servername)
		else:
			self.net=Client(config,self.callback)
		self.device.run()
		self.net.run()
	def register(self,clientinfo,rettype=True):
		if rettype:
			clientinfo=json.loads(clientinfo)
			self.screenmanage.setscreen(clientinfo["name"],False,clientinfo["width"],clientinfo["height"],{"port":clientinfo["port"],"ip":clientinfo["ip"]})
		else:
			self.screenmanage.setcurrenstop(clientinfo)
	def mouserpostion(self,x,y):
		oldcureen=self.screenmanage.switchscrenn(x,y)
		if oldcureen!=self.cureen:
			self.cureen=oldcureen
			print(oldcureen)
			if self.cureen.own:
				self.device.isnet=False
				if self.udp:
					self.udp.isthre=False
			else:
				if self.udp:
					self.udp.isthre=True
				self.net.updto(oldcureen.addr["ip"],oldcureen.addr["port"])
	def mzwrite(self,transport=False,event=False,udp=False):
		self.udp=udp
		self.device.isnet=True
		# print self.transport.client
		# print event
		
		# if event["type"]=="move":
		# 	self.moves.append(event)
		# 	if len(self.moves)>1:
		# 		for i in range(len(self.moves)):
		# 			self.movsstr+=json.dumps(self.moves.pop(0))+"\n"
		# 			print self.movsstr
		# 		self.transport.write(self.movsstr)
		# 		self.movsstr=""
		# else:
		# while True:
		sendms=""
		if len(self.device.events)>0:
			for k in self.device.events:
				sendms+=json.dumps(self.device.events.pop(0))+"\n"
		if sendms!="":
			# print len(sendms)
			# sendms=zlib.compress(sendms, zlib.Z_BEST_COMPRESSION)
			# print len(sendms)
			transport.write(sendms)
		# starttime=time.clock()
		# self.transport.write(json.dumps(event)+"\n")
		# endtime=time.clock()
		# print str(endtime-starttime)

	def callback(self,transport):
		# if len(self.device.events)>0:
		# 	return json.dumps(self.device.events.pop(0))+"\n"
		# else:
		# 	return False
		if transport:
			self.transport=transport

			tkey = threading.Thread(target=self.mzwrite,args=[False,])
			# tkey.setDaemon(True)
			tkey.start()
			self.device.isnet=True
			# self.device.callwrite=self.mzwrite
		