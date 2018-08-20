#!/usr/bin/env python
# coding: utf-8
from pymouse import PyMouseEvent,PyMouse
import json
import traceback
import threading
def callfun(self):
	pass
class Mzmouse(PyMouseEvent):
	"""docstring for Mzmouse"""
	def __init__(self,callback=callfun):
		super(Mzmouse, self).__init__()
		self.callback=callback
		self.mzpymouse=PyMouse()
		self.mouseevent=[]
		tm1=threading.Thread(target=self.clientmove)
		tm1.setDaemon(True)
		tm1.start()
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
	def clientmove(self,event=False):
		# print event
		# event=event.strip("\n")
		# revents=event.split("\n")
		# print len(revents)
		# print revents
		while True:
			try:
			
				if len(self.mouseevent)>0:
					tm1=threading.Thread(target=self.mousemoveactive,args=[self.mouseevent.pop(0),])
					tm1.setDaemon(True)
					tm1.start()
			# for e in range(0,len(revents),6):
			# 	# print e
			# 	eventobj=json.loads(revents[e])
			# 	# self.mousemoveactive(eventobj)
			# 	tm1=threading.Thread(target=self.mousemoveactive,args=[eventobj,])
			# 	tm1.setDaemon(True)
			# 	tm1.start()
			# 	if  e+1<len(revents):
			# 		# self.mousemoveactive(json.loads(revents[e+1]))
			# 		tm2=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
			# 		tm2.setDaemon(True)
			# 		tm2.start()
			# 	if e+1<len(revents):
			# 		# self.mousemoveactive(json.loads(revents[e+1]))
			# 		tm3=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
			# 		tm3.setDaemon(True)
			# 		tm3.start()
			# 	if  e+1<len(revents):
			# 		# self.mousemoveactive(json.loads(revents[e+1]))
			# 		tm4=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
			# 		tm4.setDaemon(True)
			# 		tm4.start()
			# 	if  e+1<len(revents):
			# 		# self.mousemoveactive(json.loads(revents[e+1]))
			# 		tm5=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
			# 		tm5.setDaemon(True)
			# 		tm5.start()
			# 	if  e+1<len(revents):
			# 		# self.mousemoveactive(json.loads(revents[e+1]))
			# 		tm6=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
			# 		tm6.setDaemon(True)
			# 		tm6.start()
				# if  e+1<len(revents):
				# 	# self.mousemoveactive(json.loads(revents[e+1]))
				# 	tm7=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
				# 	tm7.setDaemon(True)
				# 	tm7.start()
				# if  e+1<len(revents):
				# 	# self.mousemoveactive(json.loads(revents[e+1]))
				# 	tm8=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
				# 	tm8.setDaemon(True)
				# 	tm8.start()
				# if  e+1<len(revents):
				# 	# self.mousemoveactive(json.loads(revents[e+1]))
				# 	tm9=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
				# 	tm9.setDaemon(True)
				# 	tm9.start()
				# if  e+1<len(revents):
				# 	# self.mousemoveactive(json.loads(revents[e+1]))
				# 	tm10=threading.Thread(target=self.mousemoveactive,args=[json.loads(revents[e+1]),])
				# 	tm10.setDaemon(True)
				# 	tm10.start()

				# print eventobj
				# if eventobj['type']=='move':
				# 	# print eventobj
				# 	tm=threading.Thread(target=self.mzpymouse.move,args=[int(eventobj['x']),int(eventobj['y'])])
				# 	tm.start()
				# 	# self.mzpymouse.move(int(eventobj['x']),int(eventobj['y']))
				# elif eventobj['type']=='click':
				# 	if eventobj['press']:
				# 		self.mzpymouse.press(int(eventobj['x']),int(eventobj['y']),int(eventobj['button']))
				# 	else:
				# 		self.mzpymouse.release(int(eventobj['x']),int(eventobj['y']),int(eventobj['button']))
				# elif eventobj['type']=='scroll':
				# 	self.mzpymouse.scroll( vertical=eventobj['vertical'], horizontal=eventobj['horizontal'])
			except:
				print (event)
				print (traceback.format_exc())
		# if eventobj['type']=='move':
		# 	self.mzpymouse.move(int(eventobj['x']),int(eventobj['y']))
	def mousemoveactive(self,eventobj):
		if eventobj['type']=='move':
			# print eventobj
			tm=threading.Thread(target=self.mzpymouse.move,args=[int(eventobj['x']),int(eventobj['y'])])
			tm.start()
			# self.mzpymouse.move(int(eventobj['x']),int(eventobj['y']))
		elif eventobj['type']=='click':
			if eventobj['press']:
				self.mzpymouse.press(int(eventobj['x']),int(eventobj['y']),int(eventobj['button']))
			else:
				self.mzpymouse.release(int(eventobj['x']),int(eventobj['y']),int(eventobj['button']))
		elif eventobj['type']=='scroll':
			self.mzpymouse.scroll( vertical=eventobj['vertical'], horizontal=eventobj['horizontal'])

if __name__ == '__main__':
	mzmou=Mzmouse()
	mzmou.run()

# {"y": 955, "x": 704, "button": 1, "type": "click", "press": true}
# {"y": 955, "x": 704, "button": 1, "type": "click", "press": false}