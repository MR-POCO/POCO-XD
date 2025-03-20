#coding=utf-8
import os, sys
os.system('git pull')
try:
    __import__("POCO").runner('mrpoco')
except Exception as e:
    exit(str(e))
 