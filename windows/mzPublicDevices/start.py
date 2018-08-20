#!/usr/bin/env python
# coding: utf-8
from mzbase import *
from devices import *
from net import *

mzde=Mzdevice()
mznet=Mznet(mzde)
mznet.run()