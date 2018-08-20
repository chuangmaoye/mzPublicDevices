#!/usr/bin/env python
# coding: utf-8
from mzbase import *
from .server import *
from .client import *
import json
class Mznet(object):
	"""docstring for Mznet"""
	def __init__(self,device=False):
		super(Mznet, self).__init__()
		self.net=None
		self.device=device
	def run(self):
		netype=config("setting","terminal")
		print (netype)
		if netype == 'server':
			self.net=Server(config,self.callback)
			self.device.run()
		else:
			self.net=Client(config,self)
		self.net.run()
	def callback(self):
		if len(self.device.events)>0:
			return json.dumps(self.device.events.pop(0))
		else:
			return False
		