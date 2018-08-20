#!/usr/bin/env python
# coding: utf-8
from pymouse import PyMouseEvent
def callfun(self):
	pass
class Mzmouse(PyMouseEvent):
	"""docstring for Mzmouse"""
	def __init__(self,callback=callfun):
		super(Mzmouse, self).__init__()
		self.callback=callback
	def click(self, x, y, button, press):
		# print "click x:%s,y:%s,button:%s,press:%s" % (x, y, button, press)
		retevent={}
		retevent={"type":"click","x":x,"y":y,"button":button,"press":press}
		self.callback(retevent)
	def move(self,x,y):
		# print "move x:%s,y:%s" % (x,y)
		retevent={}
		retevent={"type":"move","x":x,"y":y}
		self.callback(retevent)
	def scroll(self, x, y, vertical, horizontal):
		# print "scroll x:%s,y:%s,vertical:%s,horizontal:%s" % (x, y, vertical, horizontal)
		retevent={}
		retevent={"type":"scroll","x":x,"y":y,"vertical":vertical,"horizontal":horizontal}
		self.callback(retevent)
	
if __name__ == '__main__':
	mzmou=Mzmouse()
	mzmou.run()