#!/usr/bin/env python
# coding: utf-8
'''
Project 3 03/2022
@Witch_Sec
https://github.com/miss-anthrope
-
Class: https://www.udemy.com/course/python-for-pentesters (Credit to Cristi Zot https://www.udemy.com/user/cristivlad2/)
-
import wx
import os
import ftplib


w=wx.App()
screen=wx.ScreenDC()
size=screen.GetSize()
bmap=wx.Bitmap(size[0],size[1])
memo=wx.MemoryDC(bmap)
memo.Blit(0,0,size[0],size[1],screen,0,0)

del memo
bmap.SaveFile("screengrabbed.png",wx.BITMAP_TYPE_PNG)
#Come back to this. The wx library poses some challenges all on its own. Deserves more study.
#All the references to wx from this apply to Python2...
-
Update 05/2022 - Trying this with Selenium
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenie.png")
driver.quit()
print("end...")
