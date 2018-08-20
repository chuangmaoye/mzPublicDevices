#!/usr/bin/env python
# coding: utf-8
from mzbase import *
from devices import *
from net import *
from screen import *
mznet=Mznet(Mzdevice(),ScreenManage())
mznet.run()