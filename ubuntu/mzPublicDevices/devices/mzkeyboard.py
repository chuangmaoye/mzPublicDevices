#!/usr/bin/env python
# coding: utf-8
from pykeyboard import PyKeyboardEvent
def callfun(self):
	pass
class Mzkeybodard(PyKeyboardEvent):
	"""docstring for Mzkeybodard"""
	def __init__(self,callback=callfun):
		# super(Mzkeybodard, self).__init__()
		PyKeyboardEvent.__init__(self)
		self.callback=callback
	# def handler(self, reply):
	# 	print reply
	# def escape(self,event):
	# 	print event
	def tap(self, keycode, character, press):
		# print "keycode:%s,character:%s,press:%s" % (keycode, character, press)
		retevent={}
		retevent={"type":"keyboard","keycode":keycode,"character":character,"press":press}
		print retevent
		self.callback(retevent)
	def escape(self,event):
		pass
	def run(self):
		PyKeyboardEvent.run(self)
		print "end"

if __name__ == '__main__':
	mzkey=Mzkeybodard()
	mzkey.run()