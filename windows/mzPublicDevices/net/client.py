#!/usr/bin/env python
# coding: utf-8
try:
	import twisted  
except ImportError:  
	print ("This examples requires the Twisted framework. Download it from http://twistedmatrix.com")  
	raise SystemExit
from twisted.internet.protocol import Protocol, Factory,ClientFactory,DatagramProtocol
from twisted.internet import reactor
from datetime import datetime
import json
import threading
import time
import socket

class MzUdp():
	"""docstring for MzUdp"""
	def __init__(self,addr='127.0.0.1',port=9999,mzcallback=False):
		self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.s.bind((addr,port))
		self.mzcallback=mzcallback
		tm=threading.Thread(target=self.start)
		tm.start()
	def start(self):
		while True:
			data,addr=self.s.recvfrom(1024)
			if(self.mzcallback):
				self.mzcallback(data.strip())
			print(data)			
		
		
#udp协议
class Echo(DatagramProtocol):
	def __init__(self,mzcallback=False):
		self.mzcallback=mzcallback
	def datagramReceived(self, data, addr):

		# print "received %r from %s:%d" % (data, host, port)

		# self.transport.write(data, (host, port))
		# self.transport.write(data, (host, port))
		if self.mzcallback:
			data = data.strip()
			self.mzcallback(data)


class TimerProtocol(Protocol):
	"""docstring for TimerProtocol"""
	def __init__(self):
		self.timeout = 20
		self.interval = 0.001
	def connectionLost(self, reason):
		Protocol.connectionLost(self, reason)
		self.stop()
		print ("locst connection:",reason)
		self.factory.number_of_connections -= 1
		print ("number_of_connections:",self.factory.number_of_connections)
	def connectionMade(self):  
		#如果服务器连接数超过最大连接数，拒绝新链接建立  
		if self.factory.number_of_connections >= self.factory.max_connections:  
			self.transport.write('Too many connections, try again later')  
			self.transport.loseConnection()  
			return  
		# print self.transport
		print ('\n'.join(['%s:%s' % item for item in self.transport.__dict__.items()])) 
		#总连接数+1  
		# help(self.transport)
		self.transport.write(self.factory.registinfo.encode("utf-8"))
		# self.factory.number_of_connections += 1
		# self.start()  
		# self.timeout_deferred = reactor.callLater(self.timeout, self.transport.loseConnection) 
	def dataReceived(self, data):  
		#去除server收到client数据两端的空格  
		data = data.strip()
		# print data
		# self.factory.mznet.device.clientmove(data)
		# print data  
		#如果收到的是'start'命令  
		if data == 'start':  
			# start sending a date object that contains the current time  
			if not self.started:  
				self.start()  
		elif data == 'stop':  
			self.stop()  
		#每次执行完客户端请求后重置timeout，重新开始计算无操作时间。  
		
	def start(self):  
		self.started = True  
		self.sendTime()  
	def stop(self):  
		self.started = False  
	def sendTime(self):  
		if self.started:  
			#往缓存流里写入信息，用编码器进行amf编码  
			# self.encoder.writeElement(datetime.now())  
			#返回给客户端编码后的信息  
			# if self.factory.mzcall:
			# 	sendmsg=self.factory.mzcall()
			# 	if sendmsg:
			# 		print self.transport.client
			# 		self.transport.write(sendmsg)
			#重置缓存流  
			# self.stream.truncate()  
			#每隔self.interval的时间再发送一次amf信息  
			# if self.timeout_deferred:  
			# 	self.timeout_deferred.cancel()  
			# 	self.timeout_deferred = reactor.callLater(TimerProtocol.timeout, self.transport.loseConnection)
			reactor.callLater(self.interval, self.sendTime)

class TimerFactory(ClientFactory):  
	protocol = TimerProtocol  
	#最大链接数  
	max_connections = 1000  
	def __init__(self,dename,mznet=False):  
		self.number_of_connections = 0
		self.mznet=mznet
		self.registinfo=json.dumps({"name":dename,"width":1364,"height":766,"port":9999,"ip":"192.168.0.96"})
class Client(object):
	"""docstring for Server"""
	def __init__(self,config,mznet=False):
		self.host=config("client","server")
		self.appPort=int(config("client","port"))
		self.mznet=mznet
		self.name=config("client","name")
	def run(self):
		print ("Running Socket AMF gateway on %s:%s" % (self.host, self.appPort))    
		reactor.connectTCP(self.host,int(self.appPort), TimerFactory(self.name,self.mznet))
		# MzUdp(addr='192.168.0.96',mzcallback=self.mznet.device.clientmove) 
		reactor.listenUDP(9999, Echo(self.mznet.device.clientmove)) 
		reactor.run()
if __name__ == '__main__':  
	#设置域名，端口。  
	host = 'localhost'  
	appPort = 8080
	print ("Running Socket AMF gateway on %s:%s" % (host, appPort))    
	reactor.connectTCP(host,int(appPort), TimerFactory("p1"))  
	reactor.listenUDP(9999, Echo())
	reactor.run()  