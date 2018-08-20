#!/usr/bin/env python
# coding: utf-8
from pykeyboard import PyKeyboardEvent,PyKeyboard
import traceback
import threading
import json
from .decodekeyboard import *
def callfun(self):
	pass
class Mzkeybodard(PyKeyboardEvent):
	"""docstring for Mzkeybodard"""
	def __init__(self,callback=callfun):
		# super(Mzkeybodard, self).__init__()
		PyKeyboardEvent.__init__(self)
		self.callback=callback
		self.mzkeybo=PyKeyboard()
		self.decodekey=Decodekeyboard()
		self.mzkeybodardevent=[]
		tm1=threading.Thread(target=self.clientkeyboard)
		tm1.setDaemon(True)
		tm1.start()
	# def handler(self, reply):
	# 	print reply
	# def escape(self,event):
	# 	print event
	def tap(self, keycode, character, press):
		# print "keycode:%s,character:%s,press:%s" % (keycode, character, press)
		retevent={}
		retevent={"type":"keyboard","keycode":keycode,"character":character,"press":press}
		print (retevent)
		print (character)
		self.callback(retevent)
	def clientkeyboard(self,event=False):
		# revents=event.split("\n")
		while True:
			try:
			
				if len(self.mzkeybodardevent)>0:
					eventobj=self.mzkeybodardevent.pop(0)
					if eventobj['type']=='keyboard':
						mzcharacter=self.decodekey.linuxTOwin(eventobj['character'])
						# print mzcharacter
						if eventobj['press']:
							self.mzkeybo.press_key(mzcharacter)
						else:
							self.mzkeybo.release_key(mzcharacter)
			# for e in revents:
			# 	# print e
			# 	eventobj=json.loads(e)
			# 	# print eventobj
				
			# 	if eventobj['type']=='keyboard':
			# 		mzcharacter=self.decodekey.linuxTOwin(eventobj['character'])
			# 		# print mzcharacter
			# 		if eventobj['press']:
			# 			self.mzkeybo.press_key(mzcharacter)
			# 		else:
			# 			self.mzkeybo.release_key(mzcharacter)
				
			except:
				print (event)
				print (traceback.format_exc())

if __name__ == '__main__':
	mzkey=Mzkeybodard()
	mzkey.run()