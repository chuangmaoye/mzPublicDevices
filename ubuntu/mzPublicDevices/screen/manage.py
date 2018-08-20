#!/usr/bin/env python
# coding: utf-8
from mzbase import *
import json
class Screen(object):
	"""docstring for Screen"""
	def __init__(self,name=False,screentype=False,height=0,width=0,isconnect=False):
		self._name=name;
		self._screentype=screentype
		self._height=height
		self._width=width
		self._isconnect=isconnect
		self._x=0
		self._y=0
		self._left=False
		self._right=False
		self._top=False
		self._bootom=False
		self._addr={}
		self._own=False
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name=value

	@property
	def own(self):
		return self._own
	@own.setter
	def own(self, value):
		self._own=value
	@property
	def addr(self):
		return self._addr
	@addr.setter
	def addr(self, value):
		self._addr=value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		self._height=value

	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		self._width=value
	
	@property
	def isconnect(self):
		return self._isconnect
	@isconnect.setter
	def isconnect(self, value):
		self._isconnect=value

	@property
	def x(self):
		return self._x
	@x.setter
	def x(self, value):
		self._x=value
	
	@property
	def y(self):
		return self._y
	@y.setter
	def y(self, value):
		self._y=value

	@property
	def screentype(self):
		return self._screentype
	@screentype.setter
	def screentype(self, value):
		self._screentype=value
	@property
	def left(self):
		return self._left
	@left.setter
	def left(self, value):
		self._left=value
	@property
	def right(self):
		return self._right
	@right.setter
	def right(self, value):
		self._right=value
	@property
	def top(self):
		return self._top
	@top.setter
	def top(self, value):
		self._top=value
	@property
	def bootom(self):
		return self._bootom
	@bootom.setter
	def bootom(self, value):
		self._bootom=value

class ScreenManage(object):
	"""docstring for ScreenManage"""
	def __init__(self):
		self.me=config("server","name")
		self.curren={}#当前屏幕
		self.screens={}
		self.screensetting={}
		self.screenpath=config("server","screenpath")
		print self.screenpath
		with open(self.screenpath, 'r') as f:
			self.screensetting=json.loads(f.read())
		self.initscreen()
	def switchscrenn(self,x,y):#自动切换屏幕
		if(x>=self.curren.width and self.curren.right.isconnect):
			
			self.curren=self.curren.right
			print self.curren.addr
			print 1
		elif(x<=0 and self.curren.left.isconnect):
			self.curren=self.curren.left
			print 2
		elif(y>=self.curren.height and self.curren.bootom.isconnect):
			self.curren=self.curren.bootom
			print 3
		elif(y<=0 and self.curren.top.isconnect):
			self.curren=self.curren.top
			print 4
		self.curren.x=x
		self.curren.y=y
		# print self.curren.name
		return self.curren
	def initscreen(self):#初始化所屏幕
		# print self.screensetting
		for v in self.screensetting["screens"]:
			# print v
			screenleft=Screen()
			screenright=Screen()
			screentop=Screen()
			screenbootom=Screen()
			me=Screen()
			if v["name"] in self.screens:
				me=self.screens[v["name"]]
			else:
				me.name=v["name"]
				self.screens[v["name"]]=me
			if v["left"] in self.screens:
				me.left=self.screens[v["left"]]
			else:
				self.screens[v["left"]]=screenleft
				me.left=screenleft
			if v["right"] in self.screens:
				me.right=self.screens[v["right"]]
			else:
				self.screens[v["right"]]=screenright
				me.right=screenright
			if v["top"] in self.screens:
				me.top=self.screens[v["top"]]
			else:
				self.screens[v["top"]]=screentop
				me.top=screentop
			if v["bootom"] in self.screens:
				me.bootom=self.screens[v["bootom"]]
			else:
				self.screens[v["bootom"]]=screenbootom
				me.bootom=screenbootom
		# print(self.screens)
		# print ("\n")
		# print(self.screens['s1'].left)
		# print ("\n")
		# print(self.screens['p2'].right)
	def setscreen(self,name,own,width,height,addr=False,isconnect=True):#上线屏幕的设置
		if name in self.screens:
			self.screens[name].name=name
			self.screens[name].own=own
			self.screens[name].height=height
			self.screens[name].width=width
			self.screens[name].isconnect=isconnect
			self.screens[name].addr=addr
	def setcurrenscreen(self,name):#设置当前屏幕
		if name in self.screens:
			print name
			print self.screens[name]
			self.curren=self.screens[name]
			print self.curren.name
	def setcurrenstop(self,name):#停止当前屏幕
		if name in self.screens:
			self.screens[name].isconnect=False
	@property
	def Curren(self):
		return self.curren
