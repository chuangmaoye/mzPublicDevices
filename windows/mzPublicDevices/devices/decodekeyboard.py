#!/usr/bin/env python
# coding: utf-8
class Decodekeyboard():
	"""docstring for ClassName"""
	def __init__(self):
		self.linuxkeys={"Control_L":162,"Shift_L":160,"Caps_Lock":"CAPITAL",
		"Tab":9,"BackSpace":8,"Super_L":91,"Alt_L":164,"Alt_R":165,"Super_R":92,
		"Control_R":163,"Shift_R":161,"Menu":93,"Up":38,"Down":40,"Left":37,"Right":39,
		"Return":13,"Delete":46,"End":35,"Next":34,"Page_Up":33,"Home":36,"Insert":45,"KP_0":96,
		"KP_1":97,"KP_2":98,"KP_3":99,"KP_4":100,"KP_5":101,"KP_6":102,"KP_7":103,"KP_8":104,"KP_9":105,"KP_Decimal":110,"KP_Add":107
		,"KP_Subtract":109,"KP_Multiply":106,"KP_Divide":111,"L1":122,"L2":123,None:13
		}
	def linuxTOwin(self,keystr):
		if keystr in self.linuxkeys:
			return self.linuxkeys[keystr]
		else:
			return keystr
