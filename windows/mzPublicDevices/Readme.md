安装之前需要先安装
sudo apt-get install python-xlib

https://blog.csdn.net/aggressive_snail/article/details/50789066 
http://qixinbo.info/2017/12/06/pyqt4-sophisticated/
pyqt4剪贴板内容类型参考

[python3.5][PyUserInput]模拟鼠标和键盘模拟
2016年11月05日 16:21:43
阅读数：13853
一、PyUserInput安装
python3.5的PyMouse和PyKeyboard模块都集成到了PyUserInput模块中。在python3.5中，直接安装PyUserInput模块即可

PyUserInput模块安装前需要安装pywin32和pyHook模块
1
2
3
4
pywin32模块默认已安装

pyHook模块可从这里下载 
http://www.lfd.uci.edu/~gohlke/pythonlibs/ 
//在python官网找了很多个pyHook都不适用于python3.5版本

PyUserInput模块 
https://github.com/PyUserInput/PyUserInput

二、使用方法
//导入模块

import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
1
2
3
//分别定义一个实例 
m = PyMouse() 
k = PyKeyboard()

鼠标操作： 
m.click(x,y,button,n) –鼠标点击 
x,y –是坐标位置 
buttong –1表示左键，2表示点击右键 
n –点击次数，默认是1次，2表示双击

m.move(x,y) –鼠标移动到坐标(x,y)

x_dim, y_dim = m.screen_size() –获得屏幕尺寸

键盘操作：

k.type_string(‘Hello, World!’) –模拟键盘输入字符串 
k.press_key(‘H’) –模拟键盘按H键 
k.release_key(‘H’) –模拟键盘松开H键 
k.tap_key(“H”) –模拟点击H键 
k.tap_key(‘H’,n=2,interval=5) –模拟点击H键，2次，每次间隔5秒 
k.tap_key(k.function_keys[5]) –点击功能键F5 
k.tap_key(k.numpad_keys[5],3) –点击小键盘5,3次

联合按键模拟 
例如同时按alt+tab键盘 
k.press_key(k.alt_key) –按住alt键 
k.tap_key(k.tab_key) –点击tab键 
k.release_key(k.alt_key) –松开alt键

版权声明：本文为博主原创文章，未经博主允许不得转载。  https://blog.csdn.net/shij19/article/details/53046048